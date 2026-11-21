import json,re,collections
ns={}
for f in ['u6p_a.py','u6p_b.py','u6p_c.py','u6p_d.py']: exec(open(f).read(),ns)
drop={11,21,24,25,31,35,36,37,38,45,47,51,52,54,55,56,60,65,66,67,68,70,71,73,75,77,78,79,90,100,101,103,107,108,109,110,111,112,
116,117,118,119,126,128,132,133,134,138,139,144,146,147,149,150,151,154,155,164,167,169,170,172,173,175,177,178,181,183,184,187,188,
189,193,194,198,202,203,206,207,208,211,212,215,218,221,223,224,225,226,228,229,230,232,234,235,239,240,241,248,249,251,252,253}
W=[w for i,w in enumerate(ns['W']) if i not in drop]
easy=ns['easy']
easy=[e if isinstance(e,dict) else {"title":e[0],"story":e[1],"trick":e[2]} for e in easy]
mcqs=ns['build']()
u=json.load(open('../app/content/unit6.json'))
old={re.sub(r'\W','',m['q'].lower()) for m in u['mcqs']}
assert not any(re.sub(r'\W','',m['q'].lower()) in old for m in mcqs)
d={"id":6,"pyq_focus":ns['pyq_focus'],"easy":easy,
 "works":[dict(zip(["author","work","year","type","note"],w)) for w in W],
 "quotes":[dict(zip(["quote","by","source"],q)) for q in ns['Q']],
 "people":[dict(zip(["name","where","note"],p)) for p in ns['P']],
 "mcqs":mcqs}
json.dump(d,open('../app/content/unit6_plus.json','w'),ensure_ascii=False,indent=1)
d=json.load(open('../app/content/unit6_plus.json'))
print({k:len(v) for k,v in d.items() if isinstance(v,list)})
print('titles match:',[e['title'] for e in d['easy']]==[t['title'] for t in u['topics']])
print('answers:',collections.Counter(m['answer'] for m in d['mcqs']))
print('opts4:',all(len(m['options'])==4 and len(set(m['options']))==4 for m in d['mcqs']))
print('dup works:',[k for k,c in collections.Counter((w['author'],w['work']) for w in d['works']).items() if c>1])
