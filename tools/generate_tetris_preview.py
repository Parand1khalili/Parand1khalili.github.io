"""Replay the public saved genome with its Board implementation, without the GUI.

Pass the public Fundamentals-of-AI checkout as the sole argument.
The adapter loads exact Board/legal_x AST nodes to avoid package-level Pygame imports.
"""
import ast
from pathlib import Path
import sys
root=Path(sys.argv[1])/'06-Tetris-Genetic-Algorithm'
constants=ast.parse((root/'tetris_evolution/tetris/constants.py').read_text())
shapes=next(ast.literal_eval(n.value) for n in constants.body if isinstance(n,ast.AnnAssign) and n.target.id=='SHAPES')
seq=(root/'tetris_evolution/data/shape_sequence.txt').read_text().split()
placements=[tuple(map(int,line.split(','))) for line in (root/'best_agent.txt').read_text().splitlines() if line.strip()]
assert len(seq)==len(placements)
game=ast.parse((root/'tetris_evolution/tetris/game.py').read_text())
namespace={}
exec('from typing import List, Tuple, Set, Optional',namespace)
namespace.update(SHAPES=shapes,COLS=10,ROWS=15,SHAPE_SEQUENCE=seq)
exec(compile(ast.Module(body=[n for n in game.body if isinstance(n,(ast.ClassDef,ast.FunctionDef))],type_ignores=[]),'<original Board>','exec'),namespace)
board=namespace['Board']()
parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480"><title>Replay of the repository’s saved Tetris placements</title><rect width="800" height="480" fill="#FFFCF4"/><g font-family="Arial,sans-serif" fill="#26231D"><text x="30" y="38" font-size="24">A placement genome in action</text>']
stages=[]
for i,((rotation,x),shape) in enumerate(zip(placements,seq),1):
    board.drop(shape,rotation%len(shapes[shape]),x)
    if i in (8,16,24):
        stages.append((i,set(board.filled)))
    if board.game_over:
        break
assert len(stages)==3
for panel,(moves,filled) in enumerate(stages):
    ox=65+panel*255; oy=95; cell=19
    parts.append(f'<text x="{ox}" y="78" font-size="18">After {moves} placements</text>')
    for y in range(15):
        for x in range(10):
            color='#B77C36' if (x,y) in filled else '#F1E7D3'
            parts.append(f'<rect x="{ox+x*cell}" y="{oy+y*cell}" width="17" height="17" rx="2" fill="{color}"/>')
parts.append('<text x="30" y="426" font-size="17">Actual Board.drop replay of best_agent.txt and the fixed shape sequence.</text><text x="30" y="455" font-size="15">Rendered board states, not a Pygame screenshot or a new training run.</text></g></svg>')
out=Path(__file__).resolve().parents[1]/'assets/projects/tetris-replay.svg'
out.write_text(''.join(parts),encoding='utf-8')
print('PASS: replayed original Board.drop; captured placements 8, 16, 24')
