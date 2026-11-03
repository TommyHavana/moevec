from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.4.06', 'oecd-resilience2025.html', 'https://www.oecd.org/en/publications/2025/06/oecd-supply-chain-resilience-review_9930d256.html'), ('E6.4.06', 'oecd-resilience2025.pdf', 'https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/oecd-supply-chain-resilience-review_9930d256/94e3a8ea-en.pdf'), ('E6.4.06', 'imf-diversification2025.html', 'https://www.imf.org/en/publications/wp/issues/2025/05/23/supply-chain-diversification-and-resilience-567065'), ('E6.4.06', 'imf-bottlenecks2022.pdf', 'https://www.imf.org/-/media/files/publications/wp/2022/english/wpiea2022031-print-pdf.pdf'), ('E6.4.07', 'ine-2025-1t2026.html', 'https://www.ine.es/dyngs/Prensa/ETICCE20251T2026.htm')]
with ThreadPoolExecutor(max_workers=5)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
