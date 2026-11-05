from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
source=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/production-tools/2026-11-05/mee-fetch821823.py').read_text()
ns={};exec(source[:source.index('jobs=')]+source[source.index('def fetch('):source.index('with ThreadPoolExecutor')],ns)
jobs=[
('E1.7.02','mani2013.pdf','https://shafir.scholar.princeton.edu/document/9'),
('E1.7.02','almeida2024.pdf','https://research.unl.pt/ws/portalfiles/portal/84162063/Financial_scarcity_and_cognitive_performance_A_meta-analysis.pdf'),
('E1.7.02','szecsi-szaszi2024.html','https://online.ucpress.edu/collabra/article/10/1/122943/203333/'),
('E1.7.02','scarcity2013-harvard.html','https://www.hks.harvard.edu/centers/cid/publications/books/scarcity-why-having-too-little-means-so-much'),
('E1.7.02','cfpb-emergency-fund.html','https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/'),
('E1.7.03','frankl2006.pdf','https://www.iccpp.org/wp-content/uploads/2020/09/Mans-Search-for-Meaning.pdf'),
('E1.7.03','frankl-biography.html','https://www.viktorfrankl.org/biographie.html'),
('E1.7.03','frankl-logotherapy.html','https://www.viktorfrankl.org/logotherapy.html'),
('E1.7.04','gallup2026-financial-worries.html','https://news.gallup.com/poll/708905/affordability-dominates-americans-financial-worries.aspx'),
('E1.7.04','gallup2026-methods.pdf','https://news.gallup.com/file/poll/708947/20260428PersonalFinancesInflation.pdf'),
('E1.7.04','nhs-money-worries.html','https://www.nhs.uk/every-mind-matters/lifes-challenges/money-worries-mental-health/'),
('E1.7.04','moneyhelper-debt.html','https://www.moneyhelper.org.uk/en/money-troubles/dealing-with-debt/help-if-youre-struggling-with-debt'),
]
with ThreadPoolExecutor(max_workers=4) as ex:
 for x in ex.map(ns['fetch'],jobs):print(ns['json'].dumps(x,ensure_ascii=False),flush=True)
