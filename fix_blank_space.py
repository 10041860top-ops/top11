import os
import re

local_dir = "C:/Users/Admin/.gemini/antigravity/scratch/top11"

# We want to hide broken images across the site
# We can do this in css/standard.css
css_path = os.path.join(local_dir, 'css', 'standard.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.link_img { display: none !important; }' not in css_content:
    css_content += '\n/* Hide broken link images */\n.link_img { display: none !important; }\n'
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# We want to remove the <div class="soild"> block from all non-index HTML files
# because it contains the slider iframe which creates a huge blank space on subpages.
soild_regex = re.compile(r'<div class="soild">.*?</div><!-- soild -->\s*', re.DOTALL)

for root, _, files in os.walk(local_dir):
    if ".git" in root: continue
    for file in files:
        if file.endswith('.html'):
            if file.startswith('index'):
                # keep slider in index.html and its subpages
                pass
            else:
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it has soild
                if '<div class="soild">' in content:
                    new_content = soild_regex.sub('', content)
                    # if the regex fails for some reason, just replace the exact iframe line
                    if new_content == content:
                         new_content = re.sub(r'<div class="soild">.*?</iframe>.*?</div>', '', content, flags=re.DOTALL)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Removed slider from {file}")

print("Done fixing blank space and broken images.")
