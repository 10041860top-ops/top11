filepath = 'C:/Users/Admin/.gemini/antigravity/scratch/top11/css/standard.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the header menu image size
old_img_css = """    .header_menu table td img {
        height: 60px !important; /* Scale down menu images */
        width: auto !important;
        object-fit: contain;
    }"""
    
new_img_css = """    .header_menu table td {
        display: block !important;
        flex: 1 1 45%;
        max-width: 50%;
        text-align: center;
    }
    .header_menu table td img {
        width: 100% !important;
        height: auto !important;
        max-width: 160px !important;
        object-fit: contain;
    }"""

if old_img_css in content:
    content = content.replace(old_img_css, new_img_css)
else:
    print("Could not find old image CSS!")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu images resized.")
