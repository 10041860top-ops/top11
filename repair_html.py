import os
import urllib.request
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"
base_url = "https://www.ydacc.com.tw/home2/"

def get_original_url(filename):
    if filename == "index.html" or filename == "index.php.html" or filename == "index_inId_400.html":
        return base_url + "index.php"
    if filename == "demo.html":
        return base_url + "slider/demo/demo.html"
    
    name = filename[:-5]
    if "_MCid_" in name or "_Cid_" in name or "_inId_" in name or "_id_" in name:
        parts = name.split('_')
        base_page = parts[0] + ".php"
        query = []
        i = 1
        while i < len(parts):
            if parts[i] in ["MCid", "Cid", "inId", "id"] and i + 1 < len(parts):
                query.append(f"{parts[i]}={parts[i+1]}")
                i += 2
            else:
                base_page += "_" + parts[i]
                i += 1
        if "news_info" in name:
            base_page = "news_info.php"
        return base_url + base_page + "?" + "&".join(query)
    else:
        return base_url + name + ".php"

def apply_fixes(content_str):
    # Viewport
    if '<meta name="viewport"' not in content_str:
        content_str = content_str.replace('<head>', '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    
    # CSS cache buster
    content_str = content_str.replace('href="css/standard.css"', 'href="css/standard.css?v=7"')
    content_str = re.sub(r'href="css/standard\.css\?v=\d+"', 'href="css/standard.css?v=7"', content_str)
    
    # Iframe cache buster
    content_str = content_str.replace('src="slider/demo/demo.html"', 'src="slider/demo/demo.html?v=7"')
    content_str = re.sub(r'src="slider/demo/demo\.html\?v=\d+"', 'src="slider/demo/demo.html?v=7"', content_str)
    
    # Link mapping
    def repl_link(m):
        url = m.group(1)
        if not url.endswith('.php') and '.php?' not in url:
            return m.group(0)
        if '?' in url:
            path, qs = url.split('?', 1)
            new_name = path.replace('.php', '')
            for kv in qs.split('&'):
                if '=' in kv:
                    k, v = kv.split('=', 1)
                    new_name += f"_{k}_{v}"
            new_name += ".html"
            return 'href="' + new_name + '"'
        else:
            return 'href="' + url.replace('.php', '.html') + '"'
            
    content_str = re.sub(r'href="([^"]+)"', repl_link, content_str)
    
    # Script issues in demo.html
    content_str = content_str.replace('$(window).load(function() {', '$(function() {')
    content_str = content_str.replace('src="scripts/jquery-1.7.1.min.js"', 'src="scripts/jquery-1.7.1.min.js?v=5"')
    content_str = content_str.replace('src="../jquery.nivo.slider.pack.js"', 'src="../jquery.nivo.slider.pack.js?v=5"')
    content_str = content_str.replace('scripts/jquery-1.7.1.min.js.mjs', 'scripts/jquery-1.7.1.min.js?v=5')
    content_str = content_str.replace('../jquery.nivo.slider.pack.js.mjs', '../jquery.nivo.slider.pack.js?v=5')

    return content_str

count = 0
for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            url = get_original_url(file)
            
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                resp = urllib.request.urlopen(req)
                raw_bytes = resp.read()
                
                # The site is UTF-8!
                text = raw_bytes.decode('utf-8', errors='ignore')
                
                fixed_text = apply_fixes(text)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_text)
                count += 1
            except Exception as e:
                pass

print(f"Successfully repaired {count} files with UTF-8 encoding.")
