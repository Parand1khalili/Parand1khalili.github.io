"""Regenerate social preview and PNG favicons. Pillow is needed only for this step."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
FONTS = Path('C:/Windows/Fonts')


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


card = Image.new('RGB', (1200, 630), '#FAF9F3')
draw = ImageDraw.Draw(card)
draw.rectangle((64, 85, 409, 124), fill='#F3F5A1')
draw.text((78, 92), 'COMPUTER ENGINEERING / DATA & AI', fill='#252525', font=font('consola.ttf', 16))
draw.text((64, 168), 'Parand Khalili', fill='#252525', font=font('segoeuib.ttf', 66))
draw.text((67, 280), 'Computer Engineering · Data Analytics', fill='#252525', font=font('segoeui.ttf', 26))
draw.text((67, 326), 'AI & Graph Machine Learning', fill='#61615B', font=font('segoeui.ttf', 26))
draw.text((67, 421), 'Amirkabir University of Technology', fill='#61615B', font=font('segoeui.ttf', 22))
draw.text((67, 527), 'parand1khalili.github.io', fill='#344F68', font=font('consola.ttf', 20))
portrait = Image.open(ASSETS / 'portrait/parand-khalili-768.jpg').convert('RGB')
portrait.thumbnail((300, 375), Image.Resampling.LANCZOS)
draw.rectangle((825, 102, 1143, 495), fill='#F3F5A1')
card.paste(portrait, (834, 111))
card.save(ASSETS / 'social-preview.png', optimize=True)

for size, filename in [(32, 'favicon-32.png'), (180, 'apple-touch-icon.png')]:
    scale = 4
    icon = Image.new('RGB', (size * scale, size * scale), '#F3F5A1')
    pen = ImageDraw.Draw(icon)
    pen.text((size * .15 * scale, size * .14 * scale), 'pk', fill='#252525', font=font('segoeuib.ttf', int(size * .58 * scale)))
    icon.resize((size, size), Image.Resampling.LANCZOS).save(ASSETS / filename, optimize=True)

print('Generated lemon/ivory social card and favicons using the actual portrait.')
