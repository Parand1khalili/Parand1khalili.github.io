"""Create genuine alpha assets from the supplied logos; Pillow is development-only."""
from pathlib import Path
from collections import deque
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.local-tools'))
from PIL import Image

for filename in ('aut.png', 'emrc.jpg', 'yaas.jpg', 'quera.jpg', 'sematec.jpg', 'toefl.png'):
    source = ROOT / 'assets/logos' / filename
    im = Image.open(source).convert('RGBA')
    pixels = im.load()
    w, h = im.size
    background = set()
    def white(x, y):
        r, g, b, _ = pixels[x, y]
        return min(r, g, b) > 228 and max(r, g, b)-min(r, g, b) < 22
    if filename == 'sematec.jpg':
        # Preserve the white lettering inside the blue disc.
        queue = deque((x, y) for x in range(w) for y in (0, h-1))
        queue.extend((x, y) for y in range(h) for x in (0, w-1))
        while queue:
            x, y = queue.popleft()
            if (x, y) in background or not white(x, y):
                continue
            background.add((x, y))
            queue.extend((a, b) for a, b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)) if 0 <= a < w and 0 <= b < h)
    else:
        background = {(x,y) for y in range(h) for x in range(w) if white(x,y)}
    for x,y in background:
        r,g,b,_ = pixels[x,y]
        pixels[x,y] = (r,g,b,0)
    assert all(pixels[x,y][3] == 0 for x,y in ((0,0),(w-1,0),(0,h-1),(w-1,h-1)))
    im.save(source.with_name(source.stem+'-transparent.png'), optimize=True)
    print(filename, 'transparent background pixels:', len(background))
