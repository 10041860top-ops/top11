import os

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"
target = b'src="slider/demo/demo.html"'
replacement = b'src="slider/demo/demo.html?v=5"'

for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'rb') as f:
                content = f.read()
            
            if target in content:
                new_content = content.replace(target, replacement)
                with open(filepath, 'wb') as f:
                    f.write(new_content)

print("Safe cache buster applied!")
