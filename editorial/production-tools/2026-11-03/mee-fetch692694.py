from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.5.02', 'woodruff2001.pdf', 'https://chriswoodruff.qeh.ox.ac.uk/wp-content/uploads/2019/10/de-soto-JEL.pdf'), ('E6.5.02', 'galiani2010-fresh.pdf', 'https://repositorio.utdt.edu/bitstreams/23a81ac5-61b1-4950-a517-ef1c2c05d73b/download'), ('E6.5.02', 'ild-current.html', 'https://www.ild.org.pe/about-us/history/success-stories'), ('E6.5.03', 'ilo-trends2026.html', 'https://www.ilo.org/publications/flagship-reports/employment-and-social-trends-2026'), ('E6.5.03', 'laporta-shleifer2014.pdf', 'https://www.nber.org/system/files/working_papers/w20205/w20205.pdf'), ('E6.5.03', 'bready-faq2026.html', 'https://www.worldbank.org/en/businessready/about-us/faq'), ('E6.5.04', 'microcredit-six2015.pdf', 'https://economics.mit.edu/sites/default/files/publications/Six%20Randomized%20Evaluations%20of%20Microcredit.pdf'), ('E6.5.04', 'nobel2006.html', 'https://www.nobelprize.org/prizes/peace/2006/summary/')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
