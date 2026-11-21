import json
ns = {}
for f in ("u1p_a.py", "u1p_b.py", "u1p_c.py", "u1p_d.py"):
    exec(open(f, encoding="utf-8").read(), ns)
OUT = "../app/content/unit1_plus.json"
works_all = ns["W"] + ns["W2"]
# least important for NET, dropped to get works <= 160 (author, work)
DROP = {
 ("Aeschylus","The Persians"),("Aeschylus","Prometheus Bound"),("Sophocles","Oedipus at Colonus"),
 ("Euripides","Hippolytus"),("Euripides","The Trojan Women"),("Menander","Dyskolos (The Grouch)"),
 ("Horace","Ars Poetica"),("Anonymous","The Castle of Perseverance"),("Henry Medwall","Fulgens and Lucrece"),
 ("John Bale","King Johan"),("John Lyly","Campaspe"),("John Lyly","Endimion"),("George Peele","The Old Wives' Tale"),
 ("William Shakespeare","Titus Andronicus"),("William Shakespeare","A Midsummer Night's Dream"),
 ("William Shakespeare","The Merchant of Venice"),("William Shakespeare","Henry IV, Part 1"),
 ("William Shakespeare","Julius Caesar"),("William Shakespeare","As You Like It"),("William Shakespeare","The Winter's Tale"),
 ("Ben Jonson","The Masque of Blackness"),("Francis Beaumont","The Knight of the Burning Pestle"),
 ("Beaumont and Fletcher","Philaster"),("John Dryden","The Conquest of Granada"),("Thomas Otway","Venice Preserv'd"),
 ("William Congreve","The Mourning Bride"),("Joseph Addison","Cato"),("Henry Fielding","Tom Thumb"),
 ("R. B. Sheridan","The Critic"),("Lord Byron","Manfred"),("P. B. Shelley","Prometheus Unbound"),
 ("T. W. Robertson","Caste"),("Oscar Wilde","Salome"),("A. W. Pinero","The Second Mrs Tanqueray"),
 ("J. M. Barrie","Peter Pan"),("G. B. Shaw","Major Barbara"),("John Galsworthy","Strife"),
 ("T. S. Eliot","The Cocktail Party"),("Christopher Fry","The Lady's Not for Burning"),("Arnold Wesker","Roots"),
 ("Robert Bolt","A Man for All Seasons"),("Peter Shaffer","Equus"),("Harold Pinter","Betrayal"),
 ("W. B. Yeats","At the Hawk's Well"),("Samuel Beckett","Krapp's Last Tape"),("Samuel Beckett","Happy Days"),
 ("Brian Friel","Dancing at Lughnasa"),
 ("Susan Glaspell","Trifles"),("Elmer Rice","The Adding Machine"),("Eugene O'Neill","Mourning Becomes Electra"),
 ("Clifford Odets","Waiting for Lefty"),("Arthur Miller","All My Sons"),
 ("Ntozake Shange","for colored girls who have considered suicide / when the rainbow is enuf"),
 ("Sam Shepard","Buried Child"),("Eugene Ionesco","The Chairs"),("Anton Chekhov","The Seagull"),
 ("Friedrich Durrenmatt","The Visit"),("Wole Soyinka","The Lion and the Jewel"),
 ("Athol Fugard (with John Kani and Winston Ntshona)","Sizwe Bansi Is Dead"),("Derek Walcott","Dream on Monkey Mountain"),
 ("Ngugi wa Thiong'o and Micere Mugo","The Trial of Dedan Kimathi"),("Girish Karnad","Yayati"),
 ("Mahesh Dattani","Dance Like a Man"),("Mahesh Dattani","Final Solutions"),("Manjula Padmanabhan","Harvest"),
 ("Charles Lamb","On the Tragedies of Shakespeare"),("Thomas De Quincey","On the Knocking at the Gate in Macbeth"),
 ("Emile Zola","Naturalism in the Theatre"),("Raymond Williams","Modern Tragedy"),
}
keys = {(w[0], w[1]) for w in works_all}
assert DROP <= keys, DROP - keys
works = [w for w in works_all if (w[0], w[1]) not in DROP]
assert len(works) <= 160
d = {
 "id": 1,
 "pyq_focus": ns["pyq_focus"],
 "easy": [dict(zip(("title","story","trick"), e)) for e in ns["easy"]],
 "works": [dict(zip(("author","work","year","type","note"), w)) for w in works],
 "quotes": [dict(zip(("quote","by","source"), q)) for q in ns["Q"]],
 "people": [dict(zip(("name","where","note"), p)) for p in ns["P"]],
 "mcqs": [{"q": m[0], "options": list(m[1]), "answer": m[2], "exp": m[3]} for m in ns["M"]],
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print("wrote", OUT)
