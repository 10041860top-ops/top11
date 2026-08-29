import re
content = open('C:/Users/Admin/.gemini/antigravity/scratch/top11/service.html', 'r', encoding='utf-8').read()
links = re.findall(r'href=[\"\'](.*?)[\"\']', content)
for l in links[:30]:
    print(l)
