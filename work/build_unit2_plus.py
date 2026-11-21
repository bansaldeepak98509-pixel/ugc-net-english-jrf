import json, sys
sys.path.insert(0, "/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/work")
import u2p_a, u2p_b, u2p_c, u2p_d
ROOT = "/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/"
base = json.load(open(ROOT + "unit2.json"))
DROP = {2,3,9,14,20,23,24,31,34,38,41,43,45,52,53,57,63,64,67,72,77,80,83,86,91,92,97,100,101,104,106,108,109,110,117,122,124,125,127,128,131,135,139,140,143,146,148,149,152,154,158,159,162,165,167,171,173,174,176,181,183,185,188,190,191,193,194,197,199,201,204,207,208,213,214,216,217,221,223,226,228,231,233,236,243,245,246,247,248}
works = [{"author":a,"work":w,"year":y,"type":t,"note":n} for i,(a,w,y,t,n) in enumerate(u2p_b.W) if i not in DROP]
works = works[:160]
for x in works:
    assert len(x["note"].split()) <= 12, x
d = {"id": 2, "pyq_focus": u2p_a.pyq_focus, "easy": u2p_a.easy, "works": works,
     "quotes": u2p_c.quotes, "people": u2p_c.people, "mcqs": u2p_d.MCQS}
json.dump(d, open(ROOT + "unit2_plus.json", "w"), ensure_ascii=False, indent=1)
