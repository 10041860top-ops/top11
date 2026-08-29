filepath = 'C:/Users/Admin/.gemini/antigravity/scratch/top11/slider/demo/demo.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("$(function() {\n        $('#slider').nivoSlider();\n    });", "$(window).load(function() {\n        $('#slider').nivoSlider();\n    });")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Nivo slider fixed.")
