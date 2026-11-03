from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.4.08', 'wto-services2026.html', 'https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm'), ('E6.4.08', 'icex-consultoria.html', 'https://www.icex.es/es/servicios/consultoria-estrategica'), ('E6.4.08', 'procolombia-exportar.html', 'https://www.procolombia.co/colombiatrade/exportador/exportar-desde-colombia'), ('E6.4.09', 'subscribed-publisher.html', 'https://www.penguinrandomhouse.com/books/574589/subscribed-by-tien-tzuo-with-gabe-weisert/'), ('E6.4.09', 'zuora-sei2025-release.html', 'https://www.zuora.com/press-release/zuora-subscription-economy-index-2025/')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
