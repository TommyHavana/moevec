from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[
('E4.12.14','dunlosky2013.pdf','https://acs.ist.psu.edu/ist521/dunloskyRMNW13.pdf'),
('E4.12.15','oecd-smes-ai2026.html','https://www.oecd.org/en/publications/empowering-smes-in-the-age-of-ai_bf5a9816-en.html'),
('E4.12.15','pvps-trends2026.html','https://iea-pvps.org/trends_reports/trends-2026/'),
('E4.12.15','bloom-hybrid2024.html','https://www.nature.com/articles/s41586-024-07500-2'),
('E6.3.01','smith-book1.html','https://pages.uoregon.edu/rbear/wealth/wealth1.html'),
('E6.3.01','smith-book5.html','https://pages.uoregon.edu/rbear/wealth/wealth5.html')]
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
for src,name,dst,newname in [('E4.2.03','ericsson1993.pdf','E4.12.14','ericsson1993.pdf'),('E4.12.01','wef2025.pdf','E4.12.15','wef2025.pdf'),('E4.12.12','itu2026-release.html','E4.12.15','itu2026-release.html'),('E4.12.12','findex2025-report-page.html','E4.12.15','findex2025-report-page.html')]:
 source=r/src/'sources'/name;dest=r/dst/'sources'/newname;assert not dest.exists();shutil.copy2(source,dest);h=hashlib.sha256(source.read_bytes()).hexdigest();assert hashlib.sha256(dest.read_bytes()).hexdigest()==h;dest.with_name(newname+'.copy-record.json').write_text(json.dumps(dict(source=str(source),sha256=h,note='Copia exacta; lectura parcial documentada por separado.'),ensure_ascii=False,indent=2)+'\n');print('copied',dst,newname,flush=True)
