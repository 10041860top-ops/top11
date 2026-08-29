import os
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

def fix_links():
    count = 0
    for root, _, files in os.walk(local_dir):
        if ".git" in root: continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Fix amp; in links like href="service_MCid_765_amp;Cid_853.html"
                if "_amp;Cid_" in content or "_amp;" in content:
                    new_content = content.replace("_amp;Cid_", "_Cid_")
                    new_content = new_content.replace("_amp;", "_")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
    print(f"Fixed links in {count} files")

fix_links()
