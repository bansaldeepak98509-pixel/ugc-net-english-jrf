import json
W="/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/work/"
C="/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/"
g={}
for f in ["u9p_a.py","u9p_b.py","u9p_drop.py","u9p_c.py","u9p_d.py"]:
    exec(open(W+f).read(), g)
drop=set(x.strip() for x in g["DROP"])
works=[w for w in g["works"] if w["work"] not in drop]
d={"id":9,"pyq_focus":g["pyq_focus"],"easy":g["easy"],"works":works,"quotes":g["quotes"],"people":g["people"],"mcqs":g["mcqs"]}
json.dump(d,open(C+"unit9_plus.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
