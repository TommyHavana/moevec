from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil,fitz
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
print(fetch(('E4.12.11','thunderbird-desktop.html','https://www.thunderbird.net/en-GB/desktop/')),flush=True)
for ident,name in [('E4.12.11','enisa-guide2021.pdf'),('E4.12.12','doctorow2023.html')]:
 src=r/('E4.12.13' if name.endswith('.pdf') else 'E4.12.11')/'sources'/name;dst=r/ident/'sources'/name;assert not dst.exists();shutil.copy2(src,dst);assert hashlib.sha256(src.read_bytes()).digest()==hashlib.sha256(dst.read_bytes()).digest()
 dst.with_name(name+'.copy-record.json').write_text(json.dumps(dict(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),note='Copia exacta; alcance parcial documentado por separado.'),ensure_ascii=False,indent=2)+'\n')
d=fitz.open(r/'E4.12.13/sources/enisa-guide2021.pdf')
for n in [5,8]:
 p=r/'E4.12.13/sources'/('enisa-guide2021-p'+str(n+1)+'.png');assert not p.exists();d[n].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(p)
(r/'E4.12.13/sources/enisa-guide2021-extracted.txt').write_text('\n'.join('PDF page '+str(i+1)+'\n'+p.get_text()for i,p in enumerate(d)))
