import os
import requests
import re

base_url = "https://www.ydacc.com.tw/home2/"
local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

to_download = [
    "service.php",
    "news.php",
    "links.php",
    "contact.php",
    "index.php",
    "service.php?MCid=765",
    "service.php?MCid=766",
    "service.php?MCid=767",
    "service.php?MCid=768",
    "service.php?MCid=779",
    "service.php?MCid=799",
    "service.php?MCid=806",
    "service.php?MCid=816",
    "service.php?MCid=821",
    "service.php?MCid=848",
    "service.php?MCid=951",
    "news_info.php?inId=938&bp=1",
    "news_info.php?inId=942&bp=1",
    "news_info.php?inId=943&bp=1",
    "news_info.php?inId=944&bp=1",
    "news_info.php?inId=961&bp=1"
]

def get_filename(url_path):
    name = url_path.replace('.php?', '_')
    name = name.replace('=', '_')
    name = name.replace('&amp;', '_')
    name = name.replace('&', '_')
    if '.php' in name and '_' not in name:
        name = name.replace('.php', '.html')
    elif '_' in name:
        name += '.html'
    return name

for page in to_download:
    url = base_url + page
    print(f"Downloading {url}")
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        r.encoding = 'utf-8'
        content = r.text
        
        # Check if it's a real page and not a 404
        if "404 Not Found" in content and "ErrorDocument" in content:
            print(f"FAILED (404 returned): {url}")
            continue
            
        html_name = get_filename(page)
        file_path = os.path.join(local_dir, html_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved {html_name}")
    except Exception as e:
        print(f"Failed to download {page}: {e}")

print("Done downloading.")
