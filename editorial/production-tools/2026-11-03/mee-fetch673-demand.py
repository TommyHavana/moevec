from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.3.13', 'medetel-job-ad.html', 'https://www.cubisima.com/empleos/ofertas/cerro-la-habana/39011%211'), ('E6.3.13', 'onei-channel-current.html', 'https://t.me/s/CubaONEI'), ('E6.3.13', 'gaceta-2026-es11-current.pdf', 'https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-es11.pdf')]
with ThreadPoolExecutor(max_workers=3)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
