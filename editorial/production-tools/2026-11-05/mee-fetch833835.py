from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import shutil
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web');source=(r/'editorial/production-tools/2026-11-05/mee-fetch821823.py').read_text()
ns={};exec(source[:source.index('jobs=')]+source[source.index('def fetch('):source.index('with ThreadPoolExecutor')],ns)
jobs=[
('E1.7.08','peters2017.pdf','https://discovery.ucl.ac.uk/id/eprint/1559140/1/Peters_Uncertainty_stress_causes_diseases.pdf'),
('E1.7.08','cepal-venezuela2019.pdf','https://repositorio.cepal.org/bitstream/handle/11362/44675/EEI2019_Venezuela_en.pdf'),
('E1.7.08','boe-uncertainty2026.html','https://www.bankofengland.co.uk/working-paper/2025/when-the-fog-clears-the-effect-of-reduced-inflation-uncertainty-on-households-financial-behaviour'),
('E1.7.08','unhcr-resilience.html','https://www.unhcr.org/handbooks/ih/mental-health/mental-health'),
('E1.7.08','who-migration2026.html','https://www.who.int/news-room/fact-sheets/detail/refugee-and-migrant-health'),
('E1.7.09','who-atlas2024.pdf','https://iris.who.int/bitstream/handle/10665/382452/9789240114487-eng.pdf'),
('E1.7.09','who-atlas2024-presentation.html','https://www.who.int/publications/i/item/9789240114487'),
('E1.7.09','oecd-health2025.pdf','https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/health-at-a-glance-2025_a894f72e/8f9e3f98-en.pdf'),
('E1.7.09','bag-swiss-insurance2026.html','https://www.bag.admin.ch/en/health-insurance-key-points-in-brief'),
('E1.7.09','dutch-insurance2025.html','https://www.government.nl/themes/family-health-and-care/health-insurance/standard-health-insurance/taking-out-compulsory-health-insurance'),
('E1.7.09','nza-waiting2025.html','https://www.nza.nl/actueel/nieuws/2025/07/22/toegang-tot-geestelijke-gezondheidszorg-verder-onder-druk'),
('E1.7.10','who-activity2026.html','https://www.who.int/news-room/fact-sheets/detail/physical-activity'),
('E1.7.10','who-activity2020-presentation.html','https://www.who.int/publications/i/item/9789240015128'),
('E1.7.10','who-activity2020.pdf','https://iris.who.int/server/api/core/bitstreams/faa83413-d89e-4be9-bb01-b24671aef7ca/content'),
('E1.7.10','cochrane-exercise2026.html','https://www.cochrane.org/evidence/CD004366_exercise-effective-treating-depression'),
]
for i in ['E1.7.08','E1.7.09','E1.7.10']:
 for f in (r/'editorial/articles/E1.7.05/sources').glob('nimh-caring-mental-health.html*'):
  p=r/'editorial/articles'/i/'sources'/f.name;assert not p.exists();shutil.copyfile(f,p)
with ThreadPoolExecutor(max_workers=4)as ex:
 for x in ex.map(ns['fetch'],jobs):print(ns['json'].dumps(x,ensure_ascii=False),flush=True)
