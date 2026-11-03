from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[
('E6.3.02','ricardo-ch7.html','https://www.econlib.org/book-chapters/chapter-ch-7-on-foreign-trade/'),
('E6.3.02','krugman1996.html','https://web.mit.edu/krugman/www/ricardo.htm'),
('E6.3.03','product-space2007.pdf','https://barabasi.com/media/pub_imports/files/220.pdf'),
('E6.3.03','atlas-release2024.html','https://growthlab.hks.harvard.edu/news/atlas-economic-complexity-100-brings-new-data-and-product-space-design/'),
('E6.3.04','imbs-wacziarg2003.pdf','https://www.anderson.ucla.edu/faculty_pages/romain.wacziarg/downloads/2003_stages.pdf'),
('E6.3.04','imbs-wacziarg2003-aea.html','https://www.aeaweb.org/articles?id=10.1257/000282803321455160')]
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
