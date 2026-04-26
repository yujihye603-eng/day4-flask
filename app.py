import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import psycopg2
import psycopg2.extras

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "board.db")

PG = bool(DATABASE_URL)
PH = "%s" if PG else "?"


def get_db():
    if PG:
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        conn.autocommit = False
        return conn
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    if PG:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT (NOW() AT TIME ZONE 'Asia/Seoul')
            )
        """)
    else:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at DATETIME DEFAULT (datetime('now', 'localtime'))
            )
        """)
    conn.commit()
    conn.close()


def query_all(conn, sql, params=()):
    if PG:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql, params)
        return [dict(r) for r in cur.fetchall()]
    cur = conn.execute(sql, params)
    return cur.fetchall()


def query_one(conn, sql, params=()):
    if PG:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(sql, params)
        row = cur.fetchone()
        return dict(row) if row else None
    return conn.execute(sql, params).fetchone()


def execute(conn, sql, params=()):
    conn.execute(sql, params)


# ── Routes ──────────────────────────────────────────────────────────

PER_PAGE = 10

SORT_MAP = {
    "latest": "created_at DESC",
    "oldest": "created_at ASC",
    "title": "title ASC",
}


@app.route("/")
def post_list():
    page = request.args.get("page", 1, type=int)
    query = request.args.get("q", "").strip()
    sort = request.args.get("sort", "latest")
    order_by = SORT_MAP.get(sort, "created_at DESC")
    conn = get_db()

    if query:
        like = f"%{query}%"
        if PG:
            cnt_sql = f"SELECT COUNT(*) as cnt FROM posts WHERE title ILIKE {PH} OR content ILIKE {PH}"
        else:
            cnt_sql = f"SELECT COUNT(*) as cnt FROM posts WHERE title LIKE {PH} OR content LIKE {PH}"
        total = query_one(conn, cnt_sql, (like, like))["cnt"]
    else:
        total = query_one(conn, "SELECT COUNT(*) as cnt FROM posts")["cnt"]

    total_pages = max(1, (total + PER_PAGE - 1) // PER_PAGE)
    page = max(1, min(page, total_pages))
    offset = (page - 1) * PER_PAGE

    if query:
        like = f"%{query}%"
        if PG:
            sql = f"SELECT * FROM posts WHERE title ILIKE {PH} OR content ILIKE {PH} ORDER BY {order_by} LIMIT {PH} OFFSET {PH}"
        else:
            sql = f"SELECT * FROM posts WHERE title LIKE {PH} OR content LIKE {PH} ORDER BY {order_by} LIMIT {PH} OFFSET {PH}"
        posts = query_all(conn, sql, (like, like, PER_PAGE, offset))
    else:
        sql = f"SELECT * FROM posts ORDER BY {order_by} LIMIT {PH} OFFSET {PH}"
        posts = query_all(conn, sql, (PER_PAGE, offset))

    conn.close()
    return render_template(
        "blog_list.html",
        posts=posts,
        page=page,
        total_pages=total_pages,
        query=query,
        sort=sort,
    )


@app.route("/write", methods=["GET", "POST"])
def write_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if title and content:
            conn = get_db()
            execute(conn, f"INSERT INTO posts (title, content) VALUES ({PH}, {PH})", (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for("post_list"))
    return render_template("write_post.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    conn = get_db()
    post = query_one(conn, f"SELECT * FROM posts WHERE id = {PH}", (post_id,))
    conn.close()
    if post is None:
        return redirect(url_for("post_list"))
    return render_template("post_detail.html", post=post)


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    conn = get_db()
    post = query_one(conn, f"SELECT * FROM posts WHERE id = {PH}", (post_id,))
    conn.close()
    if post is None:
        return redirect(url_for("post_list"))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if title and content:
            conn = get_db()
            execute(conn, f"UPDATE posts SET title = {PH}, content = {PH} WHERE id = {PH}", (title, content, post_id))
            conn.commit()
            conn.close()
            return redirect(url_for("post_detail", post_id=post_id))
    return render_template("write_post.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    conn = get_db()
    execute(conn, f"DELETE FROM posts WHERE id = {PH}", (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("post_list"))


# ── Init ────────────────────────────────────────────────────────────

with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
