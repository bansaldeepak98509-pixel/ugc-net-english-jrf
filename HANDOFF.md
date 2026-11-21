# HANDOFF: UGC NET English JRF app (read this first)

Owner: Deepak Bansal. Exam: UGC NET Dec 2026, on 17 Dec 2026, morning shift. Reply to him in Hinglish (Roman Hindi).

## What the app is
Offline Android APK (WebView, package com.deepak.ugcnetenglish). All content is JSON in `content/`. `build_data.py` merges it into `android/app/src/main/assets/www/data.js`. Pushing to `main` makes GitHub Actions (`.github/workflows/build-apk.yml`) build the APK and publish a Release `v1.0.<run>` with the APK attached.

The app has a Paper 1/Paper 2 switch and these tabs for each unit:
- Aasaan (5-year-old style stories and tricks)
- Notes
- Terms (pronunciation, simple Hindi, NET wording, TTS)
- Kisne likha (author-work-year, chronological)
- Quotes
- Log (characters and thinkers)
- MCQ

It also has: Mock Test (Paper 2 is 100 Q, Paper 1 is 50 Q), Galtiyan dobara, Saved, Search, progress tracking, a countdown and a study plan.

## Content files
- `content/SCHEMA.md` is the base unit schema: topics, terms {term, pron, hindi, net}, and mcqs {q, options[4], answer 0-3, exp}.
- `content/SCHEMA_PLUS.md` is the extra schema: pyq_focus, easy {title, story, trick}, works, quotes, people, and 70 new mcqs.
- Paper 2: `unitN.json` (N = 1..10), plus `unitN_plus.json`, or `unitN_plus_a.json` with `unitN_plus_b.json` (MCQs only). The build merges every `unitN_plus*.json`.
- Paper 1: `p1unitN.json` and `p1unitN_plus.json`, with id 100+N. `build_data.py` tags them paper 1.
- `work/` holds the Python draft scripts used to generate the plus files.

## Status (Nov 21, 2026)
- Paper 2: all 10 units have base content (500 terms, 300 MCQs). The plus content was being finished for every unit; check `content/` to see which `unitN_plus*` files exist.
- Paper 1: Unit 1 (Teaching Aptitude) is complete. **Units 2-10 are NOT done.**

## Next steps
1. For each Paper 1 unit from 2 to 10, write `content/p1unitN.json` (base schema, id 100+N, 10-15 topics, 30-40 terms, 30 MCQs) and `content/p1unitN_plus.json` (plus schema, 70 new MCQs). The units are:
   - 2 Research Aptitude
   - 3 Comprehension (include passages)
   - 4 Communication
   - 5 Mathematical Reasoning
   - 6 Logical Reasoning (include Indian logic)
   - 7 Data Interpretation
   - 8 ICT
   - 9 People, Development and Environment
   - 10 Higher Education System (include NEP 2020)
2. Run `python3 build_data.py` and check that it reports `bad 0`.
3. Bump `versionCode` and `versionName` in `android/app/build.gradle`, then commit and push to `main`. Actions builds the Release.
4. Give Deepak the Release link: https://github.com/bansaldeepak98509-pixel/ugc-net-english-jrf/releases
