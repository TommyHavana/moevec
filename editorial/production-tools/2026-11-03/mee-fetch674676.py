from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.3.15', 'boe-ley18-1982-consolidado.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-1982-13818'), ('E6.3.15', 'boe-ley18-1982-consolidado.pdf', 'https://www.boe.es/buscar/pdf/1982/BOE-A-1982-13818-consolidado.pdf'), ('E6.4.01', 'markowitz1952.pdf', 'https://traders.berkeley.edu/papers/Markowitz.pdf'), ('E6.4.01', 'longin-solnik2001.pdf', 'https://solnik.people.ust.hk/Articles/A6-JoFLongin.pdf'), ('E6.4.01', 'nobel1990-press.html', 'https://www.nobelprize.org/prizes/economic-sciences/1990/press-release/')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
