import os

filepath = "C:/Users/Admin/.gemini/antigravity/scratch/top11/css/standard.css"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add root tokens at the beginning
tokens = """
/*====================*/
/*=== Design Tokens ===*/
/*====================*/
:root {
  --color-primary: #00A0E9;
  --color-primary-dark: #007BB5;
  --color-brand: #AACD06;
  --color-brand-dark: #8DB305;
  --color-text-main: #333333;
  --color-text-muted: #666666;
  --color-bg-body: #FFFFFF;
  --color-bg-card: #FFFFFF;
  --color-border: #E5E7EB;
  
  --font-family-primary: "微軟正黑體", "Microsoft JhengHei", Arial, sans-serif;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem; /* 16px */
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
  
  --radius-md: 0.5rem;
  --transition-fast: 150ms ease;
  --transition-normal: 300ms ease;
}

"""

if ":root {" not in content:
    content = content.replace("html,body{", tokens + "html,body{")

# 2. Find the /* Responsive Styles */ marker and replace everything after it
responsive_marker = "/* Responsive Styles */"
if responsive_marker in content:
    desktop_part = content.split(responsive_marker)[0]
else:
    desktop_part = content

new_responsive = """
/*====================*/
/*= Responsive Styles =*/
/*====================*/
img {
    max-width: 100%;
    height: auto;
}

/* Touch target accessibility for ALL links */
@media (max-width: 1024px) {
    a {
        transition: color var(--transition-fast);
    }
    
    /* Global Containers */
    .all, .header, .content, .footer {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden;
    }
    .soild {
        width: 100% !important;
        margin-right: 0 !important;
        margin-left: 0 !important;
        height: auto !important;
    }
    
    /* Header & Logo */
    .header {
        height: auto !important;
        padding-bottom: var(--space-4);
    }
    .logo {
        float: none !important;
        margin: var(--space-4) auto !important;
        display: flex;
        justify-content: center;
        background-position: center !important;
        background-repeat: no-repeat !important;
        width: 100% !important;
    }
    
    /* Header Menu (Table to Flexbox) */
    .header_menu {
        float: none !important;
        width: 100% !important;
        height: auto !important;
    }
    .header_menu table {
        width: 100% !important;
        display: block;
    }
    .header_menu table tbody {
        display: block;
        width: 100%;
    }
    .header_menu table tr {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: var(--space-2);
        padding: 0 var(--space-2);
    }
    .header_menu table td {
        display: block !important;
        flex: 0 1 auto;
    }
    .header_menu table td a {
        display: block;
        padding: var(--space-2);
        border-radius: var(--radius-md);
        transition: transform var(--transition-fast);
    }
    .header_menu table td a:hover,
    .header_menu table td a:focus {
        transform: translateY(-2px);
    }
    .header_menu table td img {
        height: 60px !important; /* Scale down menu images */
        width: auto !important;
        object-fit: contain;
    }
    
    /* Main Content Layout */
    .left_menu, .right_contat {
        width: 100% !important;
        float: none !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        border-left: none !important;
        box-sizing: border-box;
    }
    
    .right_contat {
        margin-top: var(--space-6) !important;
        padding: 0 var(--space-4);
    }
    
    /* Cards UI for Sidebar */
    .left_upmenu {
        width: calc(100% - var(--space-8)) !important;
        margin: 0 auto var(--space-4) auto !important;
        float: none !important;
        display: flex;
        align-items: center;
        padding: var(--space-3) var(--space-4);
        background: var(--color-bg-card);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-sm);
        border-bottom: 3px solid var(--color-primary) !important;
    }
    
    .left_li {
        width: calc(100% - var(--space-8)) !important;
        margin: 0 auto var(--space-6) auto !important;
        float: none !important;
        background: var(--color-bg-card);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-sm);
        padding: var(--space-2) 0;
    }
    
    /* Touch Target Optimization */
    .left_li li {
        width: 100% !important;
        border-bottom: 1px solid var(--color-border) !important;
        line-height: normal !important;
    }
    .left_li li:last-child {
        border-bottom: none !important;
    }
    .left_li li a {
        display: block;
        padding: 12px 16px; /* Min 44px height */
        min-height: 44px;
        box-sizing: border-box;
        color: var(--color-text-main);
        font-size: var(--font-size-base);
        text-decoration: none;
    }
    .left_li li a:hover, .left_li li a:focus {
        background-color: rgba(0, 160, 233, 0.05);
        color: var(--color-primary);
        padding-left: 20px;
    }
    
    .left_li ol {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        border-bottom: 1px solid var(--color-border) !important;
    }
    .left_li ol a {
        display: block;
        padding: 12px 16px 12px 32px; /* Indent child links */
        min-height: 44px;
        box-sizing: border-box;
        font-size: var(--font-size-sm);
        color: var(--color-text-muted);
    }
    .left_li ol a:hover {
        background-color: rgba(0, 160, 233, 0.05);
        color: var(--color-primary);
    }
    
    /* Left Services Block */
    .left_service {
        width: calc(100% - var(--space-8)) !important;
        margin: 0 auto var(--space-6) auto !important;
        float: none !important;
        background: var(--color-bg-card);
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-md);
        border: 1px solid var(--color-brand) !important;
        overflow: hidden;
    }
    .left_service_title {
        width: 100% !important;
        margin: 0 !important;
        border-bottom: none !important;
        padding: var(--space-3) var(--space-4);
        background: rgba(170, 205, 6, 0.1);
        display: flex;
        align-items: center;
        box-sizing: border-box;
    }
    
    .left_cont1 {
        width: 100% !important;
        margin: 0 !important;
        padding: var(--space-2) 0;
    }
    .left_con_title {
        width: 100% !important;
        margin: 0 !important;
        height: auto !important;
    }
    .left_con_title a {
        display: block;
        padding: 12px 16px;
        min-height: 44px;
        box-sizing: border-box;
        font-size: var(--font-size-base);
        line-height: 1.4 !important;
        color: var(--color-text-main);
    }
    
    /* Inner Content (Right Content) */
    .right_upmenu {
        width: 100% !important;
        margin-left: 0 !important;
        padding: var(--space-2) 0;
        display: flex;
        align-items: center;
    }
    
    .right_li, .right_co, .right_co1, .right_co2 {
        width: 100% !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        line-height: 1.6 !important;
        font-size: var(--font-size-base) !important;
    }
    
    /* Footer */
    .footer {
        text-align: center !important;
        padding: var(--space-6) 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--space-4);
    }
    .footer_logo {
        float: none !important;
        margin: 0 auto !important;
    }
    .footer_icon {
        display: none !important;
    }
    .footer_cont {
        width: 100% !important;
        margin-top: 0 !important;
        padding: 0 var(--space-4);
        box-sizing: border-box;
        line-height: 2 !important;
    }
    .footer_ac {
        float: none !important;
        width: 100% !important;
        text-align: center !important;
        margin-top: 0 !important;
        padding: 0 var(--space-4) var(--space-6) var(--space-4);
        box-sizing: border-box;
    }
}
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(desktop_part + "\n" + new_responsive)
