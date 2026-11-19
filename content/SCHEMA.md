Write ONE valid JSON file (UTF-8) with this exact shape:
{
 "id": <unit number>,
 "title": "<unit title as in UGC NET syllabus>",
 "overview": "<2-3 lines in simple Hinglish: what this unit covers and how NET asks it>",
 "topics": [ {"title":"<topic>", "points":["<to-the-point exam fact in English, optionally with a short Hindi hint in brackets>", ...]} ],
 "terms": [ {"term":"Hamartia",
             "pron":"हा-मार-टी-आ (haa-maar-TEE-uh)",
             "hindi":"<aam bolchal ki aasaan Hindi (Devanagari) meaning, 1 line>",
             "net":"<precise English definition in the wording UGC NET / standard glossaries (Abrams, Cuddon) use; name the coiner/source work if any>"} ],
 "mcqs": [ {"q":"<NET-style question, incl. match-the-following / assertion-reason / chronology styles>",
            "options":["A","B","C","D"], "answer":<0-3 index>, "exp":"<1-line reason>"} ]
}
Requirements: 12-18 topics, each 6-12 crisp bullets (authors, works with years, characters, famous quotes and who said them, movements, chronology - the facts NET repeatedly asks). 35-50 terms (every difficult word / literary term of the unit). 30 MCQs, modelled on actual UGC NET English Paper 2 PYQs (2012-2025). Facts must be accurate; dates as standard sources give them. No markdown inside strings. Validate with: python3 -c "import json;json.load(open('<path>'))" and fix until it loads.
