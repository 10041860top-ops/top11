import os
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Bump demo.html cache buster
            new_content = re.sub(r'demo\.html\?v=\d+', 'demo.html?v=10', content)
            # Also bump css to v=10 to be absolutely sure
            new_content = re.sub(r'css/standard\.css\?v=\d+', 'css/standard.css?v=10', new_content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Bumped iframe and css to v10.")
