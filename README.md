Here’s a clean, professional `README.md` for your **Root SEO Broken Link Scanner** project.

---

# 📄 README.md

````md
# 🔍 SEO Broken Link Scanner (Python)

A simple Python tool that scans your website source code and detects broken links at the **root file level**, similar to SEO crawlers like Screaming Frog.

It shows:
- ❌ Broken URLs
- 📄 Exact file where the link exists
- 📍 Line number
- ⚠️ HTTP status code
- 📊 Export to TXT and CSV reports

---

## 🚀 Features

- Scans entire project directory recursively
- Supports `.php`, `.html`, `.js`, `.css`
- Detects external + internal broken links
- Shows exact location (file + line number)
- Generates:
  - `broken_links.txt`
  - `broken_links.csv`

---

## 📦 Requirements

Install dependencies using:

```bash
pip install requests
````

---

## ⚙️ Usage

1. Clone or copy the script into your server:

```bash
nano broken_link_finder.py
```

2. Set your project root path:

```python
ROOT_DIR = "/var/www/your-site"
```

3. Run the script:

```bash
python3 broken_link_finder.py
```

---

## 📁 Output Files

After execution, you will get:

### 🧾 broken_links.txt

Human-readable report:

```
URL: https://example.com/broken
FILE: /var/www/site/page.php
LINE: 45
STATUS: 404
```

### 📊 broken_links.csv

Structured format for Excel / Google Sheets:

| url | file | line | status |
| --- | ---- | ---- | ------ |
| ... | ...  | ...  | 404    |

---

## 🧠 How It Works

1. Scans all files in the root directory
2. Extracts URLs using regex
3. Sends HTTP HEAD request to check status
4. Logs broken URLs with exact source location
5. Exports results to files

---

## ⚠️ Notes

* Large websites may take time due to HTTP checks
* Some servers may block HEAD requests
* Use responsibly on your own server only

---

## 🚀 Future Improvements

* Async / multithreaded scanning (faster performance)
* Sitemap-based crawling
* Orphan page detection
* Auto redirect (.htaccess / nginx rules generator)
* Duplicate URL detection (www vs non-www)

---

## 👨‍💻 Author

Built for SEO debugging and website maintenance automation.

---

## 📜 License

Free to use for personal and educational purposes.

```

---

If you want next upgrade, I can turn this into a **real SEO toolkit package**:

- CLI command (`seo-scan`)
- progress bar
- multi-thread speed boost
- full website audit report (like Ahrefs lite)

Just tell me 👍
```
