import os
import sqlite3
from crawler import fetch_news

try:
    import psycopg2
except ImportError:
    psycopg2 = None

DATABASE_URL = os.environ.get("DATABASE_URL")
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "board.db")
PG = bool(DATABASE_URL)


def get_conn():
    if PG:
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        conn.autocommit = False
        return conn
    conn = sqlite3.connect(DB_PATH)
    return conn


def seed():
    articles = fetch_news(10)
    conn = get_conn()
    cur = conn.cursor()
    ph = "%s" if PG else "?"

    added = 0
    for a in articles:
        content = a["summary"]
        if a["link"]:
            content += f"\n\n{a['link']}" if content else a["link"]

        cur.execute(f"SELECT 1 FROM posts WHERE title = {ph}", (a["title"],))
        if cur.fetchone():
            continue

        cur.execute(
            f"INSERT INTO posts (title, content) VALUES ({ph}, {ph})",
            (a["title"], content),
        )
        added += 1

    conn.commit()
    conn.close()
    print(f"{added}건 추가됨 (중복 제외 {len(articles) - added}건)")


if __name__ == "__main__":
    seed()
