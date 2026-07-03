from pathlib import Path
import re
import textwrap

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text(encoding='utf-8')
image_paths = re.findall(r'<img[^>]+src="images/([^\"]+)"', html)
image_paths = sorted(set(image_paths))

images_dir = root / 'images'
images_dir.mkdir(exist_ok=True)

for rel_name in image_paths:
    target = images_dir / rel_name
    if target.exists():
        continue
    label = Path(rel_name).stem.replace('-', ' ').replace('_', ' ').title()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">
  <rect width="1200" height="800" fill="#0f172a"/>
  <rect x="40" y="40" width="1120" height="720" rx="28" fill="#111827" stroke="#38bdf8" stroke-width="6"/>
  <circle cx="300" cy="300" r="140" fill="#38bdf8" fill-opacity="0.22"/>
  <rect x="180" y="470" width="840" height="80" rx="20" fill="#f8fafc" fill-opacity="0.14"/>
  <rect x="180" y="575" width="660" height="40" rx="20" fill="#f8fafc" fill-opacity="0.12"/>
  <rect x="180" y="635" width="520" height="40" rx="20" fill="#f8fafc" fill-opacity="0.10"/>
  <text x="600" y="395" text-anchor="middle" font-family="Arial, sans-serif" font-size="56" font-weight="700" fill="#f8fafc">{label}</text>
  <text x="600" y="445" text-anchor="middle" font-family="Arial, sans-serif" font-size="26" fill="#cbd5e1">Portfolio Image Placeholder</text>
</svg>'''
    target.write_text(svg, encoding='utf-8')
    print(f'created {target.relative_to(root)}')

print(f'created {len(image_paths)} image placeholder(s)')
