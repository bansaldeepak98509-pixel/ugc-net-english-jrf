import json,glob,os,re
d=os.path.dirname(os.path.abspath(__file__))
C=d+'/content/'
units=[];bad=[]
def load(p):
    try: return json.load(open(p,encoding='utf-8'))
    except Exception as e: bad.append((p,str(e))); return None
files=sorted(glob.glob(C+'unit*.json'))+sorted(glob.glob(C+'p1unit*.json'))
for f in files:
    if '_plus' in os.path.basename(f): continue
    u=load(f)
    if not u: continue
    u['paper']=1 if os.path.basename(f).startswith('p1') else 2
    for plus in sorted(glob.glob(f[:-5]+'_plus*.json')):
        p=load(plus) or {}
        for k in ('pyq_focus','easy','works','quotes','people'):
            if p.get(k): u[k]=p[k]
        u['mcqs']=u.get('mcqs',[])+p.get('mcqs',[])
    ok=[]
    for q in u.get('mcqs',[]):
        if isinstance(q.get('options'),list) and len(q['options'])==4 and q.get('answer') in (0,1,2,3) and q.get('q'): ok.append(q)
        else: bad.append((f,'mcq '+str(q.get('q'))[:40]))
    u['mcqs']=ok
    units.append(u)
open(d+'/android/app/src/main/assets/www/data.js','w',encoding='utf-8').write('window.UNITS='+json.dumps(units,ensure_ascii=False)+';')
for P in (2,1):
    us=[u for u in units if u['paper']==P]
    print('Paper',P,len(us),'units', {k:sum(len(u.get(k,[])) for u in us) for k in ('topics','terms','mcqs','easy','works','quotes','people')})
print('bad',len(bad),bad[:10])
