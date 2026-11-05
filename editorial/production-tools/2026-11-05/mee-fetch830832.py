from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
source=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-11-05/mee-fetch821823.py').read_text()
ns={};exec(source[:source.index('jobs=')]+source[source.index('def fetch('):source.index('with ThreadPoolExecutor')],ns)
jobs=[
('E1.7.05','holt-lunstad2010.html','https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316'),
('E1.7.05','who-social-connection2025.html','https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death'),
('E1.7.06','who-burnout.html','https://www.who.int/standards/classifications/frequently-asked-questions/burn-out-an-occupational-phenomenon'),
('E1.7.06','who-work2026.html','https://www.who.int/news-room/fact-sheets/detail/mental-health-at-work'),
('E1.7.07','odgers2024.pdf','https://internet.psych.wisc.edu/wp-content/uploads/532-Master/532-UnitPages/Unit-11/Odgers_Nature_2024.pdf'),
('E1.7.07','orben2019.pdf','https://zenodo.org/records/2648689/files/2019_orbenprzybylski_nhb.pdf?download=1'),
('E1.7.07','haidt-book2024.html','https://www.theanxiousgeneration.com/book'),
('E1.7.07','haidt-four-norms.html','https://www.theanxiousgeneration.com/resources/four-norms'),
('E1.7.07','australia-minimum-age2026.html','https://www.infrastructure.gov.au/media-communications/internet/online-safety/social-media-minimum-age'),
('E1.7.07','esafety-minimum-age.html','https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions'),
]
with ThreadPoolExecutor(max_workers=4) as ex:
 for x in ex.map(ns['fetch'],jobs):print(ns['json'].dumps(x,ensure_ascii=False),flush=True)
