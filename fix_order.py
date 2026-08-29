filepath = 'C:/Users/Admin/.gemini/antigravity/scratch/top11/css/standard.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will add flexbox order to the .content, .left_menu, and .right_contat
fix = """
    /* Main Content Area */
    .content {
        display: flex !important;
        flex-direction: column !important; /* Stack vertically */
    }
    .left_menu {
        width: 100% !important;
        float: none !important;
        margin-bottom: var(--space-4);
        order: 2 !important; /* Submenu at the bottom */
    }
    .right_contat {
        order: 1 !important; /* Content at the top */
        width: 100% !important;
        float: none !important;
    }
"""

if "/* Main Content Area */" in content:
    # Just append it inside the media query before the closing brace
    # I'll use regex to append it
    import re
    content = re.sub(r'\}$', fix + '\n}', content.strip())
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Order fixed.")
else:
    print("Main Content Area not found.")
