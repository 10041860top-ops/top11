import os
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

missing = set()
found_links = set()

for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
            for link in links:
                if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
                    continue
                link = link.split('#')[0]
                link = link.replace('./', '')
                if '/' in link: # Ignore cross directory stuff for now
                    continue
                found_links.add(link)
                
for link in found_links:
    path = os.path.join(local_dir, link)
    if not os.path.exists(path):
        missing.add(link)
        
print("Missing files:")
for m in missing:
    print(m)
