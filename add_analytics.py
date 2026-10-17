import os
from pathlib import Path

# Your Google Analytics Tag Snippet
GA_SNIPPET = """    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-MHNN1TP5FT"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-MHNN1TP5FT');
    </script>"""

def inject_analytics():
    root_dir = Path("C:/Users/brian/Downloads/professional-site")
    
    # Find all HTML files in root and subdirectories (like artifacts/)
    html_files = list(root_dir.glob("**/*.html"))
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    for file_path in html_files:
        content = file_path.read_text(encoding="utf-8")
        
        # Check if tracking tag is already present to avoid duplication
        if "G-MHNN1TP5FT" in content:
            print(f"Skipped (already has tag): {file_path.relative_to(root_dir)}")
            continue
            
        # Inject right before </head>
        if "</head>" in content:
            updated_content = content.replace("</head>", f"{GA_SNIPPET}\n</head>")
            file_path.write_text(updated_content, encoding="utf-8")
            print(f"Successfully updated: {file_path.relative_to(root_dir)}")
        else:
            print(f"Warning: No </head> tag found in {file_path.relative_to(root_dir)}")

if __name__ == "__main__":
    inject_analytics()