from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[
('E4.12.08','gaceta2026-o69-official.pdf','https://www.gacetaoficial.gob.cu/sites/default/files/goc-2026-o69_0.pdf'),
('E4.12.08','unctad-b2c2020.pdf','https://unctad.org/system/files/official-document/tn_unctad_ict4d17_en.pdf'),
('E4.12.08','gaceta2026-o69-mirror.html','https://www.cibercuba.com/s/gacetaoficial/decreto-167-de-2026-de-consejo-de-ministros'),
('E4.12.09','autor2015-aea.html','https://www.aeaweb.org/articles?id=10.1257/jep.29.3.3'),
('E4.12.09','autor2015-mit.pdf','https://economics.mit.edu/sites/default/files/publications/why%20are%20there%20still%20jobs%202014.pdf'),
('E4.12.09','autor2024-new-frontiers.pdf','https://economics.mit.edu/sites/default/files/2026-04/New-Frontiers-QJE-v139%283%29-p1399-1465-Aug-2024.pdf'),
('E4.12.10','oecd2024-career-mobility.html','https://www.oecd.org/en/publications/promoting-better-career-choices-for-longer-working-lives_1ef9a0d0-en.html')]
with ThreadPoolExecutor(max_workers=4)as pool:
 for result in pool.map(fetch,jobs):print(result,flush=True)
copies=[('E4.9.01','findex-report-page.html','E4.12.08','findex2025-report-page.html'),('E4.9.01','findex-report2025.pdf','E4.12.08','findex2025.pdf'),('E4.12.05','acemoglu2019.html','E4.12.09','acemoglu2019-aea.html'),('E4.12.03','oecd-piaac2024-insights.pdf','E4.12.10','oecd-piaac2024-insights.pdf')]
for src,name,dst,newname in copies:
 source=r/src/'sources'/name;dest=r/dst/'sources'/newname;assert not dest.exists();shutil.copy2(source,dest);digest=hashlib.sha256(source.read_bytes()).hexdigest();assert hashlib.sha256(dest.read_bytes()).hexdigest()==digest;dest.with_name(newname+'.copy-record.json').write_text(json.dumps(dict(source=str(source),sha256=digest,note='Copia exacta de una fuente primaria ya archivada, sin nueva lectura íntegra afirmada.'),ensure_ascii=False,indent=2)+'\n');print('copied',dst,newname,dest.stat().st_size,flush=True)
