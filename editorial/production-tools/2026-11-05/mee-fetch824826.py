from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import runpy

source=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-11-05/mee-fetch821823.py').read_text()
prefix=source[:source.index('jobs=')]
functions=source[source.index('def fetch('):source.index('with ThreadPoolExecutor')]
namespace={}
exec(prefix+functions,namespace)
jobs=[
 ('E2.6.14','safety-planning.html','https://www.1800respect.org.au/help-and-support/safety-planning'),
 ('E2.6.15','granovetter1973.pdf','https://cpi.stanford.edu/_media/pdf/Reference%20Media/Granovetter_1973_Social%20Networks.pdf'),
 ('E2.6.15','putnam-excerpt2020.html','https://www.simonandschuster.com/books/Bowling-Alone-Revised-and-Updated/Robert-D-Putnam/9781982130848'),
 ('E1.7.01','who-mental-health2026.html','https://www.who.int/news-room/fact-sheets/detail/mental-health-strengthening-our-response'),
 ('E1.7.01','who-report2022-overview.html','https://www.who.int/publications/i/item/9789240049338'),
 ('E1.7.01','nimh-caring-mental-health.html','https://www.nimh.nih.gov/health/topics/caring-for-your-mental-health'),
]
with ThreadPoolExecutor(max_workers=4) as ex:
 for result in ex.map(namespace['fetch'],jobs):
  print(namespace['json'].dumps(result,ensure_ascii=False),flush=True)
