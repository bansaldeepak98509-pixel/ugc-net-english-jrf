PLUS file = extra depth for one unit, so a student needs NO outside book. Write ONE valid UTF-8 JSON file:
{
 "id": <unit number>,
 "pyq_focus": ["<6-10 lines in very simple Hinglish (Roman Hindi): what NET has asked most from this unit in 2012-2025 and how to prepare>"],
 "easy": [ {"title":"<EXACT topic title from the existing unit file, same order, one entry per topic>",
            "story":"<explain this topic like to a 5-year-old: very simple Hinglish (Roman Hindi), 4-7 short sentences, a desi everyday example/analogy, keep English names/titles in English>",
            "trick":"<one memory trick / mnemonic / funny hook in Hinglish to remember the key names-years of this topic>"} ],
 "works": [ {"author":"..","work":"..","year":"<as standard sources give, e.g. 1604 or 1925>","type":"<play/poem/novel/essay/book/theory text...>","note":"<max 12 words: why NET cares - famous character, first line, movement, award>"} ],
 "quotes": [ {"quote":"<famous line / definition / opening line NET asks>","by":"<author>","source":"<work and year>"} ],
 "people": [ {"name":"<character (units 1-4) or thinker/critic/linguist/scholar>","where":"<work/book it belongs to + author + year>","note":"<1 line: who/what, why remembered>"} ],
 "mcqs": [ {"q":"..","options":["A","B","C","D"],"answer":<0-3>,"exp":"<1 line, simple, can use Hinglish>"} ]
}
Counts: works 100-160 (cover EVERY author/work in the NET syllabus for that unit, incl. syllabus-listed texts); quotes 30-50; people 40-70; mcqs exactly 70, NEW (must not repeat the unit's existing 30 MCQs), real UGC NET Paper 2 English style: ~40 direct, ~10 match-the-following (put the lists inside q, options like "a-iii, b-i, c-iv, d-ii"), ~8 assertion-reason (options in standard NET wording), ~7 chronology (arrange in order), ~5 identify-the-statement-that-is-correct. Answer keys spread across 0-3.
Accuracy is critical: only well-established facts (Abrams, Cuddon, Oxford Companion, Norton). If unsure about a year, leave it out rather than guess. No markdown in strings. Escape quotes properly. Validate: python3 -c "import json;d=json.load(open(PATH));print({k:len(v) for k,v in d.items() if isinstance(v,list)})" and fix until it loads with the right counts.
