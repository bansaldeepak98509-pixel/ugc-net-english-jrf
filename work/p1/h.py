import json,random
OUT='/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/'
AR=["Both (A) and (R) are true and (R) is the correct explanation of (A)","Both (A) and (R) are true but (R) is NOT the correct explanation of (A)","(A) is true but (R) is false","(A) is false but (R) is true"]
def mk(items,seed):
    rnd=random.Random(seed);out=[]
    for it in items:
        if it[0]=='AR':
            _,a,r,ans,exp=it
            out.append({"q":"Assertion (A): "+a+" Reason (R): "+r,"options":AR[:],"answer":ans,"exp":exp})
        else:
            q,opts,exp=it
            assert len(opts)==4 and len(set(opts))==4,q
            c=opts[0];o=opts[:];rnd.shuffle(o)
            out.append({"q":q,"options":o,"answer":o.index(c),"exp":exp})
    return out
def T(rows): return [{"term":a,"pron":b,"hindi":c,"net":d} for a,b,c,d in rows]
def W(rows): return [{"author":a,"work":b,"year":c,"type":d,"note":e} for a,b,c,d,e in rows]
def Q(rows): return [{"quote":a,"by":b,"source":c} for a,b,c in rows]
def P(rows): return [{"name":a,"where":b,"note":c} for a,b,c in rows]
def save(n,title,overview,topics,terms,mcq30,pyq,easy,works,quotes,people,mcq70):
    base={"id":100+n,"title":title,"overview":overview,"topics":[{"title":t,"points":p} for t,p in topics],"terms":T(terms),"mcqs":mk(mcq30,n)}
    plus={"id":100+n,"pyq_focus":pyq,"easy":[{"title":topics[i][0],"story":s,"trick":k} for i,(s,k) in enumerate(easy)],"works":W(works),"quotes":Q(quotes),"people":P(people),"mcqs":mk(mcq70,n*7+3)}
    assert len(easy)==len(topics),(len(easy),len(topics))
    qs={m['q'] for m in base['mcqs']}
    dup=[m['q'] for m in plus['mcqs'] if m['q'] in qs]; assert not dup,dup
    for f,d in ((f'p1unit{n}.json',base),(f'p1unit{n}_plus.json',plus)):
        json.dump(d,open(OUT+f,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
        d2=json.load(open(OUT+f,encoding='utf-8'))
        print(f,{k:len(v) for k,v in d2.items() if isinstance(v,list)})
    from collections import Counter
    print(' ans spread base',Counter(m['answer'] for m in base['mcqs']),'plus',Counter(m['answer'] for m in plus['mcqs']))
    print(' topic bullets',[len(p) for _,p in topics])
