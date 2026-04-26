import sqlite3
import os
from crawler import fetch_news

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "board.db")


def seed():
    articles = fetch_news(10)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    added = 0
    for a in articles:
        content = a["summary"]
        if a["link"]:
            content += f"\n\n{a['link']}" if content else a["link"]

        cur.execute("SELECT 1 FROM posts WHERE title = ?", (a["title"],))
        if cur.fetchone():
            continue

        cur.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (a["title"], content),
        )
        added += 1

    conn.commit()
    conn.close()
    print(f"✅ {added}건 추가됨 (중복 제외 {len(articles) - added}건)")


if __name__ == "__main__":
    seed()
