from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[
('E6.3.05','becker1964-training.pdf','https://www.nber.org/system/files/chapters/c3733/c3733.pdf'),
('E6.3.06','moore-author-book.html','https://geoffreyamoore.com/book/crossing-the-chasm'),
('E6.3.06','porter1980-abstract.html','https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1496175'),
('E6.3.07','ansoff1957.pdf','https://www.casrilanka.com/casl/images/stories/2017/2017_pdfs/sab_portal/course_material/strategies_for_diversification.pdf')]
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
for src,name,dst,newname in [('E4.12.14','ericsson1993.pdf','E6.3.05','ericsson1993.pdf'),('E6.3.03','product-space2007.pdf','E6.3.07','product-space2007.pdf')]:
 source=r/src/'sources'/name;dest=r/dst/'sources'/newname;assert not dest.exists();shutil.copy2(source,dest);h=hashlib.sha256(source.read_bytes()).hexdigest();assert hashlib.sha256(dest.read_bytes()).hexdigest()==h;dest.with_name(newname+'.copy-record.json').write_text(json.dumps(dict(source=str(source),sha256=h,note='Copia exacta; lectura parcial documentada por separado.'),ensure_ascii=False,indent=2)+'\n');print('copied',dst,newname,flush=True)
