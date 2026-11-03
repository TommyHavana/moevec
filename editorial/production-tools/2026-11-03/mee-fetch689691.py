from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.4.14', 'doj-hhi.html', 'https://www.justice.gov/atr/herfindahl-hirschman-index'), ('E6.5.01', 'ine-dirce2025.html', 'https://www.ine.es/dyngs/Prensa/DIRCE2025.htm'), ('E6.5.01', 'uruguay-miem2026.html', 'https://www.gub.uy/ministerio-industria-energia-mineria/comunicacion/noticias/su-dia-miem-reconoce-aporte-micro-pequenas-medianas-empresas-desarrollo-del'), ('E6.5.01', 'gem2025-2026.pdf', 'https://www.gemconsortium.org/file/open?fileId=51858'), ('E6.5.01', 'cepal-acerca.html', 'https://www.cepal.org/es/temas/micro-pequenas-medianas-empresas-mipyme/acerca-microempresas-pymes')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
