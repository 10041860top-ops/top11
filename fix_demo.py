filepath = 'C:/Users/Admin/.gemini/antigravity/scratch/top11/slider/demo/demo.html'
with open(filepath, 'rb') as f:
    content = f.read()

content = content.replace(b'$(window).load(function() {', b'$(function() {')
content = content.replace(b'src="scripts/jquery-1.7.1.min.js"', b'src="scripts/jquery-1.7.1.min.js?v=5"')
content = content.replace(b'src="../jquery.nivo.slider.pack.js"', b'src="../jquery.nivo.slider.pack.js?v=5"')

with open(filepath, 'wb') as f:
    f.write(content)
print("demo.html fixed")
