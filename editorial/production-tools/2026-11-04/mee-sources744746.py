from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import urllib.request,json,hashlib
r=Path('/Users/nerea/Documents/Proyectos/MEE/mee-web/editorial/articles')
jobs=[('E2.1.09','black-devereux-salvanes2005.pdf',"https://researchonline.lse.ac.uk/id/eprint/19444/1/The_More_the_Merrier_The_Effect_of_Family_Size_and_Birth_Order_on_Children%27s_Education.pdf"),('E2.1.10','guevara-clacso.pdf','https://biblioteca.clacso.edu.ar/clacso/se/20191016042156/el_socialismo_y_el_hombre_en_cuba.pdf'),('E2.1.10','hayek-condensed-iea2001.pdf','https://iea.org.uk/wp-content/uploads/2016/07/upldbook43pdf.pdf'),('E2.1.11','vazquez-oso2025.html','https://revintsociologia.revistas.csic.es/index.php/revintsociologia/article/view/1502'),('E2.1.11','duany-redes-remesas-paladares.pdf','https://static.nuso.org/media/articles/downloads/2976_1.pdf')]
def get(t):
 ident,name,url=t;p=r/ident/'sources'/name
 if p.exists():return dict(file=str(p),already_exists=True)
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'MEE editorial research'}),timeout=35)as f:b=f.read();status=f.status
  assert not name.endswith('.pdf')or b.startswith(b'%PDF-');p.write_bytes(b);j=dict(url=url,status=status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),retrieved_on='2026-11-04');p.with_name(name+'.retrieval.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');return dict(file=str(p),**j)
 except Exception as e:
  j=dict(url=url,error=str(e),retrieved_on='2026-11-04',no_bypass=True);p.with_name(name+'.error.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n');return j
with ThreadPoolExecutor(max_workers=5)as ex:
 for f in as_completed([ex.submit(get,j)for j in jobs]):print(json.dumps(f.result(),ensure_ascii=False),flush=True)
