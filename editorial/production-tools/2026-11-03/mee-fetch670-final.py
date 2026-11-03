from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[('E6.3.10', 'tim-brown2005.pdf', 'https://new-ideo-com.s3.amazonaws.com/assets/files/pdfs/news/FastCo-StrategyByDesignTimBrown.pdf')]
with ThreadPoolExecutor(max_workers=2)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
source=r/'E4.12.15/sources/wef2025.pdf';dest=r/'E6.3.10/sources/wef2025.pdf';assert not dest.exists();shutil.copy2(source,dest);dest.with_name('wef2025.pdf.copy-record.json').write_text(json.dumps({'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'reading_pending':True},indent=2)+'\n')
source=r/'E6.3.06/sources';print([str(x)for x in source.glob('*porter*')])
