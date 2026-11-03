from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,shutil
helper=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-10-31/mee-fetch649651.py').read_text();exec(helper[:helper.index('with ThreadPoolExecutor')])
jobs=[
('E4.12.11','thunderbird-home.html','https://www.thunderbird.net/en-GB/'),
('E4.12.11','doctorow2023.html','https://pluralistic.net/2023/01/21/potemkin-ai/'),
('E4.12.11','incibe-backups.pdf','https://www.incibe.es/sites/default/files/contenidos/guias/guia-copias-de-seguridad.pdf'),
('E4.12.12','itu2026-mobile-ownership.html','https://www.itu.int/itu-d/reports/statistics/2026/10/13/ff26-mobile-phone-ownership/'),
('E4.12.12','itu2026-release.html','https://www.itu.int/en/mediacentre/Pages/PR-2026-11-03-Facts-and-Figures.aspx'),
('E4.12.12','itu2026-subscriptions.html','https://www.itu.int/itu-d/reports/statistics/2026/10/13/ff26-subscriptions/'),
('E4.12.13','incibe-seven-keys.pdf','https://www.incibe.es/sites/default/files/2025-11/7clavesPracticasFortalecerSeguridadDigitalPYME_.pdf'),
('E4.12.13','enisa-smes.html','https://www.enisa.europa.eu/topics/awareness-and-cyber-hygiene/smes-cybersecurity'),
('E4.12.13','enisa-guide2021.pdf','https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Cybersecurity%20guide%20for%20SMEs-online-single_page.pdf'),
('E4.12.13','incibe-ransomware.pdf','https://www.incibe.es/sites/default/files/contenidos/guias/doc/guia_ransomware.pdf')]
with ThreadPoolExecutor(max_workers=4)as pool:
 for x in pool.map(fetch,jobs):print(x,flush=True)
for src,name,dst,newname in [('E4.12.04','libre-free.html','E4.12.11','libreoffice-free.html'),('E4.12.08','findex2025-report-page.html','E4.12.12','findex2025-report-page.html')]:
 source=r/src/'sources'/name;dest=r/dst/'sources'/newname;assert not dest.exists();shutil.copy2(source,dest);h=hashlib.sha256(source.read_bytes()).hexdigest();assert hashlib.sha256(dest.read_bytes()).hexdigest()==h;dest.with_name(newname+'.copy-record.json').write_text(json.dumps(dict(source=str(source),sha256=h,note='Copia exacta; lectura parcial documentada por separado.'),ensure_ascii=False,indent=2)+'\n');print('copied',dst,newname,flush=True)
