import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://yourmindtype.com"
visited = set()
broken_links = []

headers = {
    "User-Agent": "Mozilla/5.0 (Broken Link Checker Bot)"
}

def is_internal(url):
    return url.startswith(BASE_URL)

def check_link(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=10, headers=headers)
        return r.status_code
    except:
        return None

def crawl(page_url):
    if page_url in visited:
        return

    visited.add(page_url)

    try:
        res = requests.get(page_url, timeout=10, headers=headers)
        if res.status_code >= 400:
            return

        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a", href=True):
            link = urljoin(page_url, a["href"])
            text = a.get_text(strip=True)

            # Skip useless links
            if link.startswith("mailto:") or link.startswith("tel:"):
                continue

            status = check_link(link)

            # If broken
            if status is None or status >= 400:
                broken_links.append({
                    "broken_url": link,
                    "found_on": page_url,
                    "anchor_text": text,
                    "status": status
                })

            # Crawl internal links only
            if is_internal(link):
                crawl(link)

        time.sleep(0.3)

    except Exception as e:
        print(f"Error crawling {page_url}: {e}")

# START CRAWL
crawl(BASE_URL)

# OUTPUT REPORT
print("\n\n===== BROKEN LINKS REPORT =====\n")

for i, b in enumerate(broken_links, 1):
    print(f"{i}. ❌ Broken URL: {b['broken_url']}")
    print(f"   📄 Found on: {b['found_on']}")
    print(f"   🔗 Anchor text: {b['anchor_text']}")
    print(f"   ⚠️ Status: {b['status']}")
    print("-" * 60)

# SAVE TO FILE
with open("broken_links_report.txt", "w") as f:
    for b in broken_links:
        f.write(f"BROKEN: {b['broken_url']}\n")
        f.write(f"FOUND ON: {b['found_on']}\n")
        f.write(f"TEXT: {b['anchor_text']}\n")
        f.write(f"STATUS: {b['status']}\n")
        f.write("-" * 40 + "\n")

print("\nSaved: broken_links_report.txt")
