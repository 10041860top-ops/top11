import os
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            # Read first
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix amp; links
            if "_amp;Cid_" in content or "_amp;" in content:
                content = content.replace("_amp;Cid_", "_Cid_")
                content = content.replace("_amp;", "_")
            
            # Bump cache buster to v=8
            content = re.sub(r'css/standard\.css\?v=\d+', 'css/standard.css?v=8', content)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Safe update applied to all HTML files.")
