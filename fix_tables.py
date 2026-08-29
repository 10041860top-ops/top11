filepath = 'C:/Users/Admin/.gemini/antigravity/scratch/top11/css/standard.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Append table fixes inside the media query
table_fix = """
    /* Fix legacy table widths overriding mobile viewport */
    table, tbody, tr, td, th {
        max-width: 100% !important;
        box-sizing: border-box;
    }
    
    /* Ensure content inside doesn't force width */
    .right_co, .right_co1, .right_co2, .right_li {
        word-wrap: break-word;
        overflow-wrap: break-word;
        width: 100% !important;
        box-sizing: border-box;
    }
}
"""
if "/* Fix legacy table widths" not in content:
    content = content.replace("}\n}\n", "}\n" + table_fix) # There is a closing brace for the media query

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS table fixes applied.")
