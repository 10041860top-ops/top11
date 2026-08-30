import os

files = ["index.html", "index.php.html", "index_inId_400.html", "index_inId_400.php.html"]
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace("demo.html?v=11", "demo.html?v=14")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
