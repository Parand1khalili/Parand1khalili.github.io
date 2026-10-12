"""Create web-sized editorial crops; leave the supplied original untouched.

Usage: python tools/prepare_portrait.py path/to/original.jpg
Requires Pillow for this development-only step.
"""
import argparse
import hashlib
from pathlib import Path
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('original', type=Path)
args = parser.parse_args()
before = hashlib.sha256(args.original.read_bytes()).hexdigest()
root = Path(__file__).resolve().parents[1]
folder = root / 'assets' / 'portrait'
folder.mkdir(exist_ok=True)

with Image.open(args.original) as source:
    original = ImageOps.exif_transpose(source).convert('RGB')
    # Reviewed crop for the supplied 2910×3000 photo; no retouching or segmentation.
    box = tuple(round(value * scale) for value, scale in zip(
        (720, 865, 2310, 2852),
        (original.width / 2910, original.height / 3000) * 2,
    ))
    crop = original.crop(box)
    for width in (480, 768):
        height = round(width * crop.height / crop.width)
        image = crop.resize((width, height), Image.Resampling.LANCZOS)
        image.save(folder / f'parand-khalili-{width}.webp', quality=86, method=6)
        if width == 768:
            image.save(folder / 'parand-khalili-768.jpg', quality=87, optimize=True)

assert hashlib.sha256(args.original.read_bytes()).hexdigest() == before
print('Portrait derivatives saved. Original unchanged; no generated or retouched pixels; EXIF omitted.')
