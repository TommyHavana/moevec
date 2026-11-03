from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.4.12', 'tgss-importass.html', 'https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/Trabajo%2BAutonomo/Guia'), ('E6.4.12', 'who-ilo-hours2021.html', 'https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke-who-ilo'), ('E6.4.12', 'boe-estatuto-trabajadores.html', 'https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430'), ('E6.4.13', 'bcc1022026-ficha.html', 'https://www.gacetaoficial.gob.cu/es/resolucion-102-de-2026-de-banco-central-de-cuba')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
