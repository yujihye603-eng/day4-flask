import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_PATH = os.path.join(app.root_path, "board.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
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


# ── Routes ──────────────────────────────────────────────────────────

@app.route("/")
def post_list():
    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return render_template("blog_list.html", posts=posts)


@app.route("/write", methods=["GET", "POST"])
def write_post():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        if title and content:
            conn = get_db()
            conn.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)",
                (title, content),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("post_list"))
    return render_template("write_post.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    conn = get_db()
    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
    conn.close()
    if post is None:
        return redirect(url_for("post_list"))
    return render_template("post_detail.html", post=post)


# ── Init ────────────────────────────────────────────────────────────

with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
