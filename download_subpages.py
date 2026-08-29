import os
import requests
import re

base_url = "https://www.ydacc.com.tw/home2/"
local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

# We will read all .html files we currently have, extract all .php links, and download them.
to_download = set([
    "service.php",
    "news.php",
    "links.php",
    "contact.php",
    "index.php"
])

# Read existing files to find more php links
for filename in os.listdir(local_dir):
    if filename.endswith(".html"):
        with open(os.path.join(local_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
            links = re.findall(r'href=["\']([^"\']+\.php)["\']', content)
            for link in links:
                if not link.startswith("http") and not link.startswith("/") and not link.startswith(".."):
                    link = link.replace("./", "")
                    to_download.add(link)

print(f"Found {len(to_download)} pages to download.")

downloaded_files = []

for page in to_download:
    url = base_url + page
    print(f"Downloading {url}")
    try:
        r = requests.get(url, verify=False, timeout=10)
        r.encoding = 'utf-8'
        content = r.text
        
        html_name = page.replace(".php", ".html")
        file_path = os.path.join(local_dir, html_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        downloaded_files.append(html_name)
    except Exception as e:
        print(f"Failed to download {page}: {e}")

# Now rewrite all links in all .html files
for filename in os.listdir(local_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(local_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Add viewport meta if missing
        if '<meta name="viewport"' not in content:
            content = content.replace('<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">')

        # Responsive iframe
        content = content.replace('height="340" width="960"', 'style="width: 100%; max-width: 960px; height: 340px;"')

        # Replace .php links to .html
        content = re.sub(r'href=["\'](\./)?([^"\']+\.php)["\']', lambda m: 'href="' + m.group(2).replace('.php', '.html') + '"', content)
        content = re.sub(r'src=["\'](\./)?([^"\']+\.php)["\']', lambda m: 'src="' + m.group(2).replace('.php', '.html') + '"', content)

        # Make sure stylesheet link has cache buster if it's standard.css
        content = content.replace('href="css/standard.css"', 'href="css/standard.css?v=2"')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Finished rewriting links.")
