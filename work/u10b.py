import json
# Unit 10 plus B: 70 MCQs. Non-AR items written with correct option first (answer 0); rebalanced at dump.
Q = []
def d(q, opts, exp, ans=0, fixed=False):
    Q.append({"q": q, "options": opts, "answer": ans, "exp": exp, "_fixed": fixed})

# ---- Chunk 1: direct (1-20) ----
d("In an MLA 9 works-cited entry, which form of the publisher's name is correct?",
  ["Oxford UP", "Oxford University Press, Inc.", "Oxford Univ. Pr.", "OUP Ltd."],
  "MLA 9 drops business words such as Inc. and Ltd. and, in the works-cited list, abbreviates University Press as UP (Oxford UP).")
d("According to MLA 9, the city of publication in a works-cited entry for a book is:",
  ["Normally omitted, except in special cases such as books published before 1900",
   "Always given before the publisher's name",
   "Given only when the publisher is a university press",
   "Given in place of the publication date"],
  "Since MLA 8, the city is usually left out. MLA 9 allows it for books published before 1900 or when a publisher issues different versions in different countries.")
d("When two or more lines of poetry are quoted in the running text, MLA shows each line break with:",
  ["A forward slash with a space on each side ( / )", "A vertical bar ( | )", "A double slash ( // )", "An em dash ( — )"],
  "MLA uses a slash with a space on each side for a line break in a run-in verse quotation.")
d("In a run-in quotation of poetry, MLA marks a stanza break with:",
  ["A double slash ( // )", "A single slash ( / )", "An ellipsis in square brackets", "A pilcrow (¶)"],
  "A double slash shows a stanza break; a single slash shows a line break.")
d("In MLA style, a quotation of verse is set off as a block quotation when it runs to more than:",
  ["Three lines", "Two lines", "Four lines", "Ten lines"],
  "Verse of more than three lines is set off as a block; for prose the limit is more than four lines.")
d("Which is the correct MLA in-text citation of page 45 of a work by Sandra M. Gilbert and Susan Gubar?",
  ["(Gilbert and Gubar 45)", "(Gilbert & Gubar, 45)", "(Gilbert et al. 45)", "(Gilbert, Gubar, p. 45)"],
  "For two authors, give both surnames joined by 'and', with no comma or 'p.' before the page number.")
d("When two works by Toni Morrison are cited, the MLA in-text citation of page 45 of Beloved is:",
  ["(Morrison, Beloved 45)", "(Morrison Beloved, 45)", "(Beloved, Morrison 45)", "(Morrison 45, Beloved)"],
  "With more than one work by an author, add a short title after the name and a comma: (Morrison, Beloved 45). The title is italicised.")
d("When you quote a writer whose words you found in someone else's book (an indirect source), MLA puts which phrase before the source you consulted?",
  ["qtd. in", "cited in", "ibid.", "cf."],
  "MLA uses 'qtd. in' (quoted in) before the indirect source, for example (qtd. in Boswell 2: 450).")
d("Which is the MLA-style citation for Act 3, Scene 1, lines 56-58 of Shakespeare's Hamlet?",
  ["(Ham. 3.1.56-58)", "(Hamlet III.i.56-58)", "(Ham., act 3, sc. 1, p. 56)", "(Shakespeare 56-58)"],
  "MLA cites verse plays by act, scene and line in Arabic numerals separated by periods, and may abbreviate the title (Ham.).")
d("In MLA 9, when an organisation is both the author and the publisher of a work, the entry:",
  ["Begins with the title and names the organisation only as publisher",
   "Lists the organisation twice, as author and as publisher",
   "Begins with 'Anonymous'",
   "Omits the organisation altogether"],
  "To avoid repetition, MLA starts with the title and gives the organisation only in the publisher slot, e.g. MLA Handbook. 9th ed., Modern Language Association of America, 2021.")
d("In an MLA works-cited list, the author's name in the second and later entries by the same author is replaced by:",
  ["Three hyphens followed by a period", "Ibid.", "Id.", "An em dash followed by a comma"],
  "Give the name in the first entry only; in later entries use three hyphens and a period, with entries alphabetised by title.")
d("In MLA, how is a work with no named author entered in the works-cited list?",
  ["It begins with the title, and the in-text citation uses a shortened title",
   "It begins with 'Anonymous'",
   "It begins with 'Anon.'",
   "It begins with the publisher's name"],
  "MLA never uses 'Anonymous'. The entry starts with the title, and the in-text citation gives the title, shortened if it is long.")
d("In MLA style, the title of a single page on a website is:",
  ["Placed in quotation marks, while the website's name is italicised",
   "Italicised, while the website's name is in quotation marks",
   "Underlined",
   "Written in capitals with no other marking"],
  "A part of a larger whole (a web page) goes in quotation marks; the container (the website) is italicised.")
d("When a source has no title, MLA 9 asks the writer to describe it in the title slot. That description is:",
  ["In plain text, not italicised or in quotation marks, with only the first word and proper nouns capitalised",
   "Italicised",
   "Placed in quotation marks",
   "Enclosed in square brackets"],
  "A description of an untitled source is plain text, capitalised like a sentence (e.g. Advertisement for Upton Tea Imports).")
d("To cite a specific moment in a film or video, MLA gives a time stamp in the form:",
  ["Hours, minutes and seconds separated by colons (00:12:23-35)", "Minutes only, with 'min.'", "Seconds only", "The frame number"],
  "MLA cites time-based media with a time stamp of hours, minutes and seconds joined by colons.")
d("In MLA, the parenthetical citation for a block quotation is placed:",
  ["After the final punctuation mark of the quotation", "Before the final punctuation mark", "Above the quotation", "In a footnote only"],
  "In a block quotation the citation follows the closing punctuation; in a run-in quotation it comes before the period.")
d("In the 'other contributors' element of an MLA 9 entry, a translator is shown as:",
  ["Translated by Edith Grossman", "Trans. Edith Grossman", "Grossman, Edith, tr.", "tr. by Grossman"],
  "In the other-contributors slot, MLA 9 writes out the role: 'translated by', 'edited by'. A short form such as 'translator' is used only when the person is in the author slot.")
d("In MLA, entries in the works-cited list are formatted with:",
  ["A hanging indent of half an inch", "The first line indented one inch", "No indentation at all", "Numbers in square brackets"],
  "Works-cited entries are alphabetical, double-spaced and given a half-inch hanging indent.")
d("Where does the running head of an MLA research paper appear, and what does it contain?",
  ["In the upper right corner, half an inch from the top: the writer's surname and the page number",
   "In the upper left corner: the paper's title",
   "At the bottom centre: the page number only",
   "In the upper right corner: the instructor's name"],
  "MLA puts the writer's last name and the page number flush right, half an inch from the top of each page.")
d("Which of the following is NOT part of the heading at the top left of the first page of an MLA paper?",
  ["The student's roll or ID number", "The writer's name", "The instructor's name", "The course and the date"],
  "The MLA heading has four double-spaced lines: the writer's name, the instructor's name, the course, and the date. No separate title page is used unless one is asked for.")

# ---- Chunk 2: direct (21-40) ----
d("Which date format does MLA use in works-cited entries?",
  ["21 Apr. 2021", "April 21, 2021", "2021-04-21", "04/21/2021"],
  "MLA gives dates as day, month, year, abbreviating the month except May, June and July.")
d("Following MLA's rule for number ranges, pages 321 to 328 are written as:",
  ["pp. 321-28", "pp. 321-328", "p. 321-8", "pages 321-8"],
  "For numbers above ninety-nine, MLA gives only the last two digits of the second number unless more are needed (321-28, 96-101).")
d("Which of the following fills MLA's 'Version' core element?",
  ["2nd ed.", "vol. 3", "Penguin Books", "pp. 10-25"],
  "The Version element covers editions and versions such as 2nd ed., unabridged version, or King James Version.")
d("In the entry 'PMLA, vol. 136, no. 2, 2021, pp. 230-45', the words 'vol. 136, no. 2' fill which MLA core element?",
  ["Number", "Version", "Location", "Other contributors"],
  "Volume and issue numbers are the Number element; the page range is the Location element.")
d("A journal article read on JSTOR is cited with two containers. In MLA terms, JSTOR is:",
  ["The second container", "The first container", "The publisher", "The version"],
  "The journal is the first container; the database (JSTOR) is the second container, followed by its DOI or URL.")
d("Under the UGC Regulations 2018 on academic integrity, which of the following is NOT excluded from the similarity check?",
  ["The researcher's own analysis in the main chapters",
   "References and bibliography",
   "Acknowledgements and the table of contents",
   "Generic terms, laws, standard symbols and equations"],
  "The regulations exclude quoted work used with permission and attribution, references, bibliography, contents, preface, acknowledgements, and generic terms, laws, symbols and equations. The thesis's own text is checked.")
d("Under the UGC Regulations 2018, what penalty does a student face whose thesis falls in Level 2 (above 40% and up to 60% similarity)?",
  ["Barred from submitting a revised script for one year",
   "Asked to submit a revised script within six months",
   "Registration for the programme cancelled",
   "No penalty"],
  "Level 1 (10-40%): revise within six months. Level 2 (40-60%): barred from submitting a revised script for one year. Level 3 (above 60%): registration cancelled.")
d("In the study of research misconduct, the abbreviation FFP stands for:",
  ["Fabrication, Falsification, Plagiarism", "Funding, Fraud, Publication", "Falsification, Forgery, Piracy", "Fabrication, Fraud, Peer review"],
  "FFP (fabrication, falsification and plagiarism) is the standard core definition of research misconduct.")
d("The three basic ethical principles set out in the Belmont Report (1979) are:",
  ["Respect for persons, beneficence and justice",
   "Autonomy, confidentiality and honesty",
   "Consent, anonymity and integrity",
   "Objectivity, reliability and validity"],
  "The Belmont Report names three principles: respect for persons, beneficence and justice.")
d("Publishing one's own earlier work again as if it were new, without saying so, is called:",
  ["Self-plagiarism", "Ghost writing", "Fabrication", "Gift authorship"],
  "Reusing one's own published work without disclosure (duplicate or redundant publication) is self-plagiarism.")
d("In UGC-CARE, the UGC's initiative on quality journals, CARE stands for:",
  ["Consortium for Academic and Research Ethics",
   "Council for Academic Research and Evaluation",
   "Committee for Assessment of Research Excellence",
   "Centre for Academic Reference and Edition"],
  "UGC set up the Consortium for Academic and Research Ethics (UGC-CARE) in 2019.")
d("What is the INFLIBNET initiative that gives universities access to plagiarism-detection software?",
  ["ShodhShuddhi", "ShodhGangotri", "ShodhSindhu", "Vidwan"],
  "ShodhShuddhi gives universities access to plagiarism-detection software through INFLIBNET.")
d("ShodhGangotri, run by INFLIBNET, is a repository of:",
  ["Synopses of research proposals submitted for Ph.D. registration",
   "Full texts of completed Ph.D. theses",
   "E-journals subscribed to by universities",
   "Profiles of subject experts"],
  "ShodhGangotri holds synopses; ShodhGanga holds full theses; ShodhSindhu is the e-resources consortium; Vidwan is the expert database.")
d("Under the UGC Ph.D. Regulations, 2022, what are the minimum and maximum durations of a Ph.D.?",
  ["Minimum three years, maximum six years", "Minimum two years, maximum five years", "Minimum three years, maximum five years", "Minimum four years, maximum seven years"],
  "The 2022 regulations set a minimum of three years including coursework and a maximum of six years, with extra time allowed for re-registration, women and persons with disabilities.")
d("Grounded theory, a method of building theory from data, was developed by:",
  ["Barney Glaser and Anselm Strauss", "Kurt Lewin", "Clifford Geertz", "Norman Denzin"],
  "Glaser and Strauss set out grounded theory in The Discovery of Grounded Theory (1967).")
d("Reasoning that moves from particular observations to a general conclusion is called:",
  ["Inductive", "Deductive", "Hypothetico-deductive", "A priori"],
  "Induction goes from the particular to the general; deduction goes from the general to the particular.")
d("A Type II error in hypothesis testing means:",
  ["Failing to reject a null hypothesis that is false",
   "Rejecting a null hypothesis that is true",
   "Choosing the wrong sample size",
   "Using a non-random sample"],
  "Type I is rejecting a true null hypothesis; Type II is keeping (failing to reject) a false one.")
d("A researcher studying a hidden population asks each participant to refer others to the study. This is:",
  ["Snowball sampling", "Stratified sampling", "Systematic sampling", "Cluster sampling"],
  "In snowball (chain-referral) sampling, existing participants recruit new ones. It is a non-probability method.")
d("The extent to which a research tool measures what it claims to measure is its:",
  ["Validity", "Reliability", "Objectivity", "Generalisability"],
  "Validity is accuracy of measurement. Reliability is consistency: getting the same result when the tool is used again.")
d("The Art of Literary Research (1963) was written by:",
  ["Richard D. Altick", "Fredson Bowers", "George Watson", "Wayne C. Booth"],
  "Richard D. Altick wrote The Art of Literary Research (1963); later editions were revised with John J. Fenstermaker.")

# ---- Chunk 3: match (41-50), assertion-reason (51-58), chronology (59-60) ----
M = "Choose the correct answer from the options given below:"
d("Match List I (MLA core element) with List II (example):\nList I: a. Title of container  b. Version  c. Number  d. Location\nList II: i. vol. 47, no. 2  ii. pp. 112-30  iii. Unabridged ed.  iv. Victorian Studies\n" + M,
  ["a-iv, b-iii, c-i, d-ii", "a-iii, b-iv, c-ii, d-i", "a-iv, b-i, c-iii, d-ii", "a-ii, b-iii, c-i, d-iv"],
  "The journal title (Victorian Studies) is the container; an edition (Unabridged ed.) is the version; volume and issue are the number; the page range is the location.")
d("Match List I (abbreviation) with List II (meaning):\nList I: a. op. cit.  b. loc. cit.  c. et seq.  d. q.v.\nList II: i. and the following  ii. in the work cited  iii. in the place cited  iv. which see\n" + M,
  ["a-ii, b-iii, c-i, d-iv", "a-iii, b-ii, c-i, d-iv", "a-ii, b-iii, c-iv, d-i", "a-i, b-iii, c-ii, d-iv"],
  "op. cit. = opere citato (in the work cited); loc. cit. = loco citato (in the place cited); et seq. = et sequens (and the following); q.v. = quod vide (which see).")
d("Match List I (research misconduct) with List II (description):\nList I: a. Fabrication  b. Falsification  c. Salami slicing  d. Gift authorship\nList II: i. Splitting one study into several minimal publications  ii. Making up data or results  iii. Naming as author someone who did not contribute substantially  iv. Altering or manipulating data or results\n" + M,
  ["a-ii, b-iv, c-i, d-iii", "a-iv, b-ii, c-i, d-iii", "a-ii, b-iv, c-iii, d-i", "a-ii, b-i, c-iv, d-iii"],
  "Fabrication is inventing data; falsification is manipulating it; salami slicing splits one study into many papers; gift authorship credits someone who did not contribute.")
d("Match List I (book format) with List II (leaves per printed sheet):\nList I: a. Folio  b. Quarto  c. Octavo  d. Duodecimo\nList II: i. 12 leaves  ii. Sheet folded once, 2 leaves  iii. Sheet folded three times, 8 leaves  iv. Sheet folded twice, 4 leaves\n" + M,
  ["a-ii, b-iv, c-iii, d-i", "a-iv, b-ii, c-iii, d-i", "a-ii, b-iii, c-iv, d-i", "a-i, b-iv, c-iii, d-ii"],
  "Folio: folded once (2 leaves, 4 pages). Quarto: twice (4 leaves, 8 pages). Octavo: three times (8 leaves, 16 pages). Duodecimo: 12 leaves.")
d("Match List I (book) with List II (author):\nList I: a. The Craft of Research  b. Principles of Bibliographical Description  c. Graphs, Maps, Trees  d. The Literary Thesis: A Guide to Research\nList II: i. Fredson Bowers  ii. George Watson  iii. Wayne C. Booth, Gregory G. Colomb and Joseph M. Williams  iv. Franco Moretti\n" + M,
  ["a-iii, b-i, c-iv, d-ii", "a-iii, b-ii, c-iv, d-i", "a-iv, b-i, c-iii, d-ii", "a-i, b-iii, c-iv, d-ii"],
  "The Craft of Research (1995) is by Booth, Colomb and Williams; Principles of Bibliographical Description (1949) by Bowers; Graphs, Maps, Trees (2005) by Moretti; The Literary Thesis (1970) by Watson.")
d("Match List I (type of research) with List II (feature):\nList I: a. Historical research  b. Ex post facto research  c. Action research  d. Ethnography\nList II: i. Reconstructs the past from records and documents  ii. Studies causes after the effects have occurred, without manipulating variables  iii. Long-term participant observation of a culture  iv. A practitioner studies and solves an immediate problem in their own setting\n" + M,
  ["a-i, b-ii, c-iv, d-iii", "a-ii, b-i, c-iv, d-iii", "a-i, b-ii, c-iii, d-iv", "a-i, b-iv, c-ii, d-iii"],
  "Historical research uses records; ex post facto works backward from effects already present; action research is practitioner problem-solving; ethnography relies on participant observation.")
d("Match List I (INFLIBNET service) with List II (function):\nList I: a. ShodhGanga  b. ShodhGangotri  c. ShodhSindhu  d. Vidwan\nList II: i. Database of experts  ii. Repository of synopses  iii. Consortium for e-resources  iv. Repository of full-text theses\n" + M,
  ["a-iv, b-ii, c-iii, d-i", "a-ii, b-iv, c-iii, d-i", "a-iv, b-iii, c-ii, d-i", "a-iv, b-ii, c-i, d-iii"],
  "ShodhGanga holds theses, ShodhGangotri synopses, ShodhSindhu is the e-journal consortium, and Vidwan is the expert database.")
d("Match List I (textual criticism term) with List II (meaning):\nList I: a. Collation  b. Emendation  c. Stemma  d. Recension\nList II: i. Family tree showing how surviving manuscripts descend  ii. Comparing copies or witnesses to record variants  iii. An editor's correction of a corrupt reading  iv. Weighing all the witnesses to establish the most authoritative evidence for the text\n" + M,
  ["a-ii, b-iii, c-i, d-iv", "a-iii, b-ii, c-i, d-iv", "a-ii, b-i, c-iii, d-iv", "a-ii, b-iii, c-iv, d-i"],
  "Collation compares witnesses; emendation corrects errors; a stemma (stemma codicum) charts how manuscripts descend; recension is the critical sifting of witnesses (the first stage of Lachmann's method).")
d("Match List I (what is cited) with List II (MLA in-text form):\nList I: a. A prose novel, with chapter  b. A poem with numbered lines, first citation  c. The Bible  d. A verse play\nList II: i. (Ham. 1.5.30-35)  ii. (Austen 45; ch. 3)  iii. (New Jerusalem Bible, Gen. 1.1)  iv. (lines 11-14)\n" + M,
  ["a-ii, b-iv, c-iii, d-i", "a-iv, b-ii, c-iii, d-i", "a-ii, b-iv, c-i, d-iii", "a-ii, b-iii, c-iv, d-i"],
  "For prose fiction MLA adds the chapter after a semicolon; poems are cited by line ('lines' in the first citation); the Bible by edition, book, chapter and verse; verse plays by act, scene and line.")
d("Match List I (ethics document) with List II (year):\nList I: a. Nuremberg Code  b. Declaration of Helsinki  c. Belmont Report  d. UGC Regulations on academic integrity and plagiarism\nList II: i. 1979  ii. 2018  iii. 1947  iv. 1964\n" + M,
  ["a-iii, b-iv, c-i, d-ii", "a-iv, b-iii, c-i, d-ii", "a-iii, b-i, c-iv, d-ii", "a-iii, b-iv, c-ii, d-i"],
  "Nuremberg Code 1947; Declaration of Helsinki (World Medical Association) 1964; Belmont Report 1979; UGC Regulations 2018.")

AR = ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"]
H = "Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R).\n"
T = "\nIn the light of the above statements, choose the correct answer from the options given below:"
def ar(a, r, ans, exp):
    d(H + "Assertion (A): " + a + "\nReason (R): " + r + T, list(AR), exp, ans, True)
ar("MLA 9 normally leaves the city of publication out of a book's works-cited entry.",
   "Publishers today often have offices in several cities, so the city adds little useful information.", 0,
   "Both are true. The MLA explains that the city is usually left out because publishers often have offices in more than one city, which is the reason R gives.")
ar("In MLA style, the page number in a parenthetical citation is preceded by 'p.'.",
   "MLA keeps parenthetical citations as brief as possible.", 3,
   "A is false: MLA writes (Morrison 45) with no 'p.' or comma. R is true: brevity is the purpose of the author-page system.")
ar("An MLA block quotation is enclosed in quotation marks.",
   "An MLA block quotation is indented half an inch from the left margin.", 3,
   "A is false: the indentation itself marks the quotation, so no quotation marks are added. R is true.")
ar("Plagiarism can occur even when the writer did not intend to deceive.",
   "Plagiarism means presenting another's words or ideas as one's own without acknowledgement, whatever the intention.", 0,
   "Both are true, and R explains A: because plagiarism is defined by the act and not the intent, careless or unintentional borrowing still counts.")
ar("An encyclopaedia is a tertiary source.",
   "Tertiary sources are original creative works such as novels and poems.", 2,
   "A is true. R is false: novels and poems are primary sources; tertiary sources such as encyclopaedias and bibliographies compile and index other sources.")
ar("Hypothesis testing is central to quantitative research.",
   "Qualitative research often generates hypotheses rather than testing them.", 1,
   "Both statements are true, but a fact about qualitative research does not explain why quantitative research relies on hypothesis testing.")
ar("An MLA works-cited list includes only the sources cited in the text.",
   "A list that also includes works consulted but not cited may be titled 'Works Consulted'.", 1,
   "Both are true, but R describes a different kind of list and does not explain the rule in A.")
ar("Shakespeare's First Folio was published in 1623.",
   "Shakespeare compiled the First Folio himself shortly before his death.", 2,
   "A is true. R is false: Shakespeare died in 1616, and the Folio was compiled by his fellow actors John Heminges and Henry Condell.")

C = "Arrange the following in chronological order:\n"
d(C + "(i) MLA Handbook, 7th edition  (ii) MLA Handbook, 9th edition  (iii) MLA Handbook, 8th edition  (iv) MLA Handbook, 6th edition\n" + M,
  ["(iv), (i), (iii), (ii)", "(i), (iv), (iii), (ii)", "(iv), (iii), (i), (ii)", "(iv), (i), (ii), (iii)"],
  "6th edition 2003, 7th 2009, 8th 2016, 9th 2021.")
d(C + "(i) Belmont Report  (ii) Nuremberg Code  (iii) UGC Regulations on plagiarism  (iv) Declaration of Helsinki\n" + M,
  ["(ii), (iv), (i), (iii)", "(iv), (ii), (i), (iii)", "(ii), (i), (iv), (iii)", "(ii), (iv), (iii), (i)"],
  "Nuremberg Code 1947, Declaration of Helsinki 1964, Belmont Report 1979, UGC Regulations 2018.")

# ---- Chunk 4: chronology (61-65), correct statements (66-70) ----
d(C + "(i) Text Encoding Initiative (TEI) founded  (ii) Roberto Busa begins the Index Thomisticus  (iii) Michael Hart starts Project Gutenberg  (iv) Franco Moretti's Distant Reading published\n" + M,
  ["(ii), (iii), (i), (iv)", "(iii), (ii), (i), (iv)", "(ii), (i), (iii), (iv)", "(ii), (iii), (iv), (i)"],
  "Index Thomisticus 1949, Project Gutenberg 1971, TEI 1987, Distant Reading 2013.")
d("Arrange the following stages of the research process in their proper sequence:\n(i) Collection of data  (ii) Identification of the research problem  (iii) Formulation of hypothesis  (iv) Review of literature\n" + M,
  ["(ii), (iv), (iii), (i)", "(iv), (ii), (iii), (i)", "(ii), (iii), (iv), (i)", "(ii), (iv), (i), (iii)"],
  "The problem is identified first, the literature is reviewed, a hypothesis is framed from that review, and then data are collected.")
d("Arrange the following parts of a Ph.D. thesis in the order in which they appear:\n(i) Works Cited / Bibliography  (ii) Table of contents  (iii) Conclusion  (iv) Declaration and supervisor's certificate\n" + M,
  ["(iv), (ii), (iii), (i)", "(ii), (iv), (iii), (i)", "(iv), (ii), (i), (iii)", "(iv), (iii), (ii), (i)"],
  "Preliminary pages (declaration, certificate) come first, then the table of contents, then the chapters ending in the conclusion, then the works cited or bibliography.")
d(C + "(i) First edition of the APA Publication Manual  (ii) First edition of the Chicago Manual of Style  (iii) First edition of the MLA Handbook  (iv) The MLA Style Sheet\n" + M,
  ["(ii), (iv), (i), (iii)", "(ii), (i), (iv), (iii)", "(iv), (ii), (i), (iii)", "(ii), (iv), (iii), (i)"],
  "Chicago Manual 1906, MLA Style Sheet 1951, APA Publication Manual 1952, MLA Handbook 1977.")
d(C + "(i) Richard D. Altick, The Art of Literary Research  (ii) Fredson Bowers, Principles of Bibliographical Description  (iii) Booth, Colomb and Williams, The Craft of Research  (iv) Franco Moretti, Graphs, Maps, Trees\n" + M,
  ["(ii), (i), (iii), (iv)", "(i), (ii), (iii), (iv)", "(ii), (iii), (i), (iv)", "(ii), (i), (iv), (iii)"],
  "Bowers 1949, Altick 1963, Booth, Colomb and Williams 1995, Moretti 2005.")

S = "Choose the correct answer from the options given below:"
d("Which of the following statements about the MLA works-cited list are correct?\n(A) It is double-spaced throughout.\n(B) Its entries are numbered in order of citation.\n(C) Each entry has a half-inch hanging indent.\n(D) The heading 'Works Cited' is centred at the top of the page.\n" + S,
  ["(A), (C) and (D) only", "(A), (B) and (C) only", "(B) and (D) only", "(A) and (B) only"],
  "The list is alphabetical, not numbered. It is double-spaced, uses a hanging indent, and has a centred heading.")
d("Which of the following statements about the UGC Regulations 2018 on plagiarism are correct?\n(A) Similarity of up to 10% (Level 0) attracts no penalty.\n(B) References and the bibliography are excluded from the similarity check.\n(C) A student's Level 3 similarity (above 60%) leads to cancellation of registration.\n(D) A teacher's Level 1 similarity leads to denial of two annual increments.\n" + S,
  ["(A), (B) and (C) only", "(A), (B) and (D) only", "(B), (C) and (D) only", "(A) and (D) only"],
  "D is false: a teacher at Level 1 is asked to withdraw the manuscript. Denial of two increments applies at Level 3.")
d("Which of the following statements about sources in literary research are correct?\n(A) A writer's diary is a primary source.\n(B) A critical biography of a writer is a secondary source.\n(C) An annotated bibliography is a primary source.\n(D) A literary history is a primary source.\n" + S,
  ["(A) and (B) only", "(A), (B) and (C) only", "(B) and (D) only", "(A), (C) and (D) only"],
  "Diaries are primary; critical biographies and literary histories are secondary; bibliographies are tertiary.")
d("Which of the following statements about MLA in-text citation are correct?\n(A) No comma is placed between the author's name and the page number.\n(B) If the author is named in a signal phrase, only the page number is needed in parentheses.\n(C) 'et al.' is used for a source with three or more authors.\n(D) In a run-in quotation, the parenthetical citation comes before the sentence's final period.\n" + S,
  ["(A), (B), (C) and (D)", "(A), (B) and (C) only", "(B), (C) and (D) only", "(A) and (C) only"],
  "All four are MLA 9 rules: (Morrison 45); signal phrase plus page; et al. for three or more authors; citation before the period in run-in text.")
d("Which of the following statements about types of research are correct?\n(A) Fundamental research aims to extend knowledge rather than solve an immediate practical problem.\n(B) Action research is generally associated with Kurt Lewin.\n(C) Qualitative research relies chiefly on statistical analysis of large samples.\n(D) Grounded theory builds theory inductively from data.\n" + S,
  ["(A), (B) and (D) only", "(A), (B) and (C) only", "(B), (C) and (D) only", "(A) and (C) only"],
  "C describes quantitative research. Qualitative research relies on interpretation of non-numerical data, often from small samples.")

# ---- Rebalance answer positions (non-AR) and dump ----
if __name__ == "__main__":
    k = 0
    for m in Q:
        if not m["_fixed"]:
            t = k % 4; k += 1
            o = m["options"]; a = m["answer"]
            o[a], o[t] = o[t], o[a]
            m["answer"] = t
    out = [{"q": m["q"], "options": m["options"], "answer": m["answer"], "exp": m["exp"]} for m in Q]
    path = "/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/unit10_plus_b.json"
    json.dump({"mcqs": out}, open(path, "w"), ensure_ascii=False, indent=1)
