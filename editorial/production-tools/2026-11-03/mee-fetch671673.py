from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.3.12', 'ries-author-principles.html', 'https://theleanstartup.com/principles'), ('E6.3.13', 'gaceta-2026-o62-current.pdf', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o62.pdf'), ('E6.3.13', 'gaceta-2026-es12-current.pdf', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-es12.pdf'), ('E6.3.13', 'gaceta-2026-o71-current.pdf', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o71_0.pdf')]
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
