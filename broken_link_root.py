import os
import re
import requests
import csv

ROOT_DIR = "/var/www/enfp.xyz"

url_pattern = re.compile(r'https?://[^\s"\'<>]+')

broken_links = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

def check_url(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=10, headers=headers)
        return r.status_code
    except:
        return None

def scan_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            urls = url_pattern.findall(line)

            for url in urls:
                status = check_url(url)

                if status is None or status >= 400:
                    broken_links.append({
                        "file": file_path,
                        "line": i,
                        "url": url,
                        "status": status
                    })

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def scan_root():
    for folder, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith((".php", ".html", ".js", ".css")):
                scan_file(os.path.join(folder, file))

# RUN SCAN
scan_root()

print("\n===== BROKEN LINKS (ROOT SCAN) =====\n")

for b in broken_links:
    print(f"❌ {b['url']}")
    print(f"📄 File: {b['file']} (line {b['line']})")
    print(f"⚠️ Status: {b['status']}")
    print("-" * 60)

# -------------------------
# SAVE TO TXT FILE
# -------------------------
txt_file = "broken_links.txt"
with open(txt_file, "w", encoding="utf-8") as f:
    for b in broken_links:
        f.write(f"URL: {b['url']}\n")
        f.write(f"FILE: {b['file']}\n")
        f.write(f"LINE: {b['line']}\n")
        f.write(f"STATUS: {b['status']}\n")
        f.write("-" * 40 + "\n")

print(f"\nSaved TXT report → {txt_file}")

# -------------------------
# SAVE TO CSV FILE
# -------------------------
csv_file = "broken_links.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["url", "file", "line", "status"])
    writer.writeheader()

    for b in broken_links:
        writer.writerow(b)

print(f"Saved CSV report → {csv_file}")
