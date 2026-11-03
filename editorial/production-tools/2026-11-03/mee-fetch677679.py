from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.4.02', 'hbs-five-forces.html', 'https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-forces.aspx?content_language=English'), ('E6.4.03', 'opec-asb2026-launch.html', 'https://www.opec.org/pr-detail/1784601-29-april-2026.html'), ('E6.4.03', 'chile-fees.html', 'https://www.hacienda.cl/english/work-areas/international-finance/sovereign-wealth-funds/economic-and-social-stabilization-fund'), ('E6.4.04', 'rumelt-author.html', 'https://www.richardrumelt.com/strategy-structure'), ('E6.4.04', 'berkshire2025.pdf', 'https://www.berkshirehathaway.com/2025ar/2025ar.pdf')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
