"""Reproduce the descriptive comparison from the archived primary sources."""
from pathlib import Path
import csv, json, re, html, math, statistics
r=Path(__file__).parent
rs=list(csv.DictReader((r/'rsf2026.csv').read_text(encoding='cp1252').splitlines(),delimiter=';'))
assert len(rs)==180 and len({t['ISO'] for t in rs})==180
wb=json.loads((r/'wdi-gdp-2025.json').read_text())
assert wb[0]['pages']==1 and all(t['date']=='2025' for t in wb[1])
w={t['countryiso3code']:t for t in wb[1] if t['value'] is not None and t['value']>0}
fh=[]
for tr in re.findall('<tr.*?</tr>',(r/'fh-countries2026.html').read_text(),re.S):
 n=re.search('data-code="country_name"[^>]*>.*?<a[^>]*>(.*?)</a>',tr,re.S)
 f=re.search('data-code="fiw"[^>]*>.*?<span class="score">(-?\d+)</span>',tr,re.S)
 if n and f:fh.append((html.unescape(re.sub('<[^>]+>','',n[1])).strip(),int(f[1])))
national=[(n,v) for n,v in fh if not n.endswith('*')]
assert len(fh)==208 and len(national)==195
aliases={'Democratic Republic of the Congo':'COD','Republic of the Congo':'COG','Micronesia':'FSM','Nauru':'NRU','São Tomé and Príncipe':'STP','The Bahamas':'BHS','The Gambia':'GMB','Turkey':'TUR'}
lookup={p['Country_EN']:p['ISO'] for p in rs}
lookup.update({p['country']['value']:p['countryiso3code'] for p in wb[1]});lookup.update(aliases)
assert all(n in lookup for n,v in national)
pairsrs=[dict(iso=t['ISO'],name=t['Country_EN'],score=float(t['Score 2026'].replace(',','.')),gdp_ppp=w[t['ISO']]['value']) for t in rs if t['ISO'] in w]
pairsfh=[dict(iso=lookup[n],name=n,score=v,gdp_ppp=w[lookup[n]]['value']) for n,v in national if lookup[n] in w]
def corr(rows):
 x=[p['score'] for p in rows];y=[math.log(p['gdp_ppp']) for p in rows]
 a=statistics.mean(x);b=statistics.mean(y)
 return sum((u-a)*(v-b) for u,v in zip(x,y))/math.sqrt(sum((u-a)**2 for u in x)*sum((v-b)**2 for v in y))
result=dict(checked_on='2026-10-30',wb_lastupdated=wb[0]['lastupdated'],gdp_year=2025,gdp_indicator='NY.GDP.PCAP.PP.CD',units='Current international dollars per person;PPP,not USD or real growth',freedom_editions=2026,reference_period='2025;RSF permits updates before publication',method='Unweighted Pearson correlation of index score with natural logarithm of positive GDP per capita PPP2025;complete cases;FH excludes13 starred territories;no imputation,no causal claim,no growth regression',rsf=dict(n=len(pairsrs),pearson_log_gdp=corr(pairsrs),excluded=[t['ISO'] for t in rs if t['ISO'] not in w],pairs=pairsrs),fh=dict(n=len(pairsfh),pearson_log_gdp=corr(pairsfh),excluded=[dict(name=n,iso=lookup[n]) for n,v in national if lookup[n] not in w],pairs=pairsfh),explicit_name_aliases=aliases)
previous=json.loads((r/'descriptive-comparison.json').read_text())
assert result==previous,'The archived inputs must reproduce the saved comparison exactly.'
print(json.dumps({k:{'n':result[k]['n'],'r':result[k]['pearson_log_gdp']} for k in ['rsf','fh']}))
