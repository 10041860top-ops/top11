import re

filepath = 'C:/Users/Admin/.gemini/antigravity/scratch/top11/css/standard.css'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the entire .header_menu block inside the media query.
# Let's use regex to find it and replace it.

new_css = """
    /* --- World-Class Mobile Navigation Menu --- */
    .header_menu {
        float: none !important;
        width: 100% !important;
        height: auto !important;
        padding: 15px 20px;
        box-sizing: border-box;
    }
    .header_menu table, .header_menu tbody {
        width: 100% !important;
        display: block !important;
    }
    .header_menu table tr {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: space-between !important;
        gap: 12px;
    }
    .header_menu table td {
        display: block !important;
        flex: 1 1 calc(50% - 6px); /* 2 items per row with 12px gap */
        max-width: calc(50% - 6px);
        margin: 0 !important;
        padding: 0 !important;
    }
    /* Hide the old sliced images completely */
    .header_menu table td img {
        display: none !important;
    }
    
    /* Style the anchor tags as modern premium buttons */
    .header_menu table td a {
        display: flex !important;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 48px;
        background: linear-gradient(135deg, #aacd06 0%, #8ebd00 100%);
        border-radius: 12px;
        text-decoration: none !important;
        box-shadow: 0 4px 10px rgba(170, 205, 6, 0.3), inset 0 1px 0 rgba(255,255,255,0.4);
        position: relative;
        overflow: hidden;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .header_menu table td a:active {
        transform: scale(0.96);
        box-shadow: 0 2px 4px rgba(170, 205, 6, 0.2);
    }
    
    /* Typography inside the buttons using pseudo-elements */
    .header_menu table td a::after {
        color: #ffffff;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 1px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.15);
    }
    
    /* Map each link to its text */
    .header_menu table td a[href="index.html"]::after { content: "關於永登"; }
    .header_menu table td a[href="service.html"]::after { content: "服務項目"; }
    .header_menu table td a[href="news.html"]::after { content: "最新消息"; }
    .header_menu table td a[href="links.html"]::after { content: "相關連結"; }
    .header_menu table td a[href="contact.html"]::after { content: "稅務諮詢"; }
    
    /* Make the Contact button stand out more */
    .header_menu table td a[href="contact.html"] {
        flex: 1 1 100%;
        max-width: 100%;
        background: linear-gradient(135deg, #00A0E9 0%, #0088cc 100%);
        box-shadow: 0 4px 10px rgba(0, 160, 233, 0.3), inset 0 1px 0 rgba(255,255,255,0.4);
    }
"""

# Now replace the old CSS.
# The old CSS starts with `.header_menu {` inside the media query and ends right before `/* Main Content Layout */`
start_marker = ".header_menu {"
end_marker = "/* Main Content Layout */"

# find the media query start
mq_start = content.rfind("@media (max-width: 1024px) {")
if mq_start != -1:
    header_start = content.find(start_marker, mq_start)
    header_end = content.find(end_marker, mq_start)
    if header_start != -1 and header_end != -1:
        # Replace the chunk
        content = content[:header_start] + new_css + "\n      " + content[header_end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully injected world-class mobile menu CSS.")
    else:
        print("Could not find start or end markers.")
else:
    print("Media query not found.")
