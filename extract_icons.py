#!/usr/bin/env python3
import subprocess
import os

icons_dir = "assets/icons"

# Font Awesome icons (usando a CDN)
fa_icons = {
    "whatsapp": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/svgs/brands/whatsapp.svg",
    "facebook": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/svgs/brands/facebook-square.svg",
    "instagram": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/svgs/brands/instagram.svg",
    "tiktok": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/svgs/brands/tiktok.svg",
    "money": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/svgs/solid/money-bill-1-wave.svg",
}

# Themify icons - vamos usar SVG simples para location-pin
themify_icons = {
    "location-pin": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
  <path d="M12 2C6.48 2 2 6.48 2 12c0 7 10 20 10 20s10-13 10-20c0-5.52-4.48-10-10-10zm0 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z"/>
</svg>"""
}

# Download Font Awesome icons
print("Baixando ícones Font Awesome...")
for name, url in fa_icons.items():
    try:
        cmd = f'curl -s "{url}" -o "{icons_dir}/fa-{name}.svg"'
        os.system(cmd)
        print(f"✅ {name}")
    except Exception as e:
        print(f"❌ {name}: {e}")

# Create Themify icons
print("\nCriando ícones Themify...")
for name, svg_content in themify_icons.items():
    try:
        with open(f"{icons_dir}/ti-{name}.svg", "w") as f:
            f.write(svg_content)
        print(f"✅ {name}")
    except Exception as e:
        print(f"❌ {name}: {e}")

print("\n✅ Ícones extraídos em assets/icons/")
