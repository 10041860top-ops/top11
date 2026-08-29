import os
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"
links = set()

for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            for m in re.findall(r'href=[\"\'](.*?)[\"\']', content):
                links.add(m)

broken = [l for l in links if 'amp;' in l]
print(f"Total unique links: {len(links)}")
print(f"Broken links with amp;: {broken}")
