import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import requests
from bs4 import BeautifulSoup
from datetime import datetime


RSS_URL = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"


def fetch_news(limit=10):
    resp = requests.get(RSS_URL, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, "xml")
    items = soup.find_all("item")[:limit]

    articles = []
    for item in items:
        title = item.find("title").text.strip() if item.find("title") else ""
        link = item.find("link").text.strip() if item.find("link") else ""
        pub_date = item.find("pubDate").text.strip() if item.find("pubDate") else ""
        summary = item.find("description").text.strip() if item.find("description") else ""

        # HTML 태그 제거
        if summary:
            desc_soup = BeautifulSoup(summary, "html.parser")
            summary = desc_soup.get_text().strip()

        # 날짜 포맷 정리
        if pub_date:
            try:
                dt = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S GMT")
                pub_date = dt.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                pass

        articles.append({
            "title": title,
            "summary": summary[:100] + ("..." if len(summary) > 100 else ""),
            "link": link,
            "pub_date": pub_date,
        })

    return articles


def print_articles(articles):
    print()
    print("=" * 70)
    print(f"  Google News 한국어 RSS - 최신 {len(articles)}건")
    print("=" * 70)

    for i, a in enumerate(articles, 1):
        print()
        print(f"  [{i}] {a['title']}")
        print(f"      {a['pub_date']}")
        if a["summary"]:
            print(f"      {a['summary']}")
        print(f"      {a['link']}")
        print(f"  {'-' * 66}")

    print()
    print("=" * 70)
    print()


if __name__ == "__main__":
    articles = fetch_news(10)
    print_articles(articles)
