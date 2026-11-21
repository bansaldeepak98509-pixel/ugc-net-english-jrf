import json, itertools
MCQS = []
_pos = [0]
def nextpos():
    p = _pos[0] % 4; _pos[0] += 1; return p
def Q(q, correct, wrong, exp, pos=None):
    pos = nextpos() if pos is None else pos
    o = list(wrong); o.insert(pos, correct)
    MCQS.append({"q": q, "options": o, "answer": pos, "exp": exp})

# ---------- Chunk 1: direct, classical to neoclassical ----------
Q("According to Aristotle, tragedy effects the catharsis of which emotions?", "Pity and fear", ["Love and hate", "Joy and sorrow", "Anger and shame"], "Poetics ch. 6: tragedy, through pity (eleos) and fear (phobos), effects the catharsis of such emotions.")
Q("In Aristotle's Poetics, 'hamartia' refers to:", "An error or flaw of judgement in the tragic hero", ["The reversal of the situation", "The recognition of the truth", "The spectacle of suffering"], "Hamartia is the hero's error of judgement (Poetics ch. 13), not necessarily a moral vice.")
Q("Aristotle's term for 'a change from ignorance to knowledge' in the plot is:", "Anagnorisis", ["Peripeteia", "Hamartia", "Hubris"], "Poetics ch. 11 defines anagnorisis (recognition) as a change from ignorance to knowledge; peripeteia is reversal.")
Q("In the final chapter of the Poetics, which form does Aristotle judge superior?", "Tragedy, over epic", ["Epic, over tragedy", "Comedy, over tragedy", "Lyric, over epic"], "Poetics ch. 26 concludes that tragedy is superior to epic because it attains its end more vividly and in a more concentrated form.")
Q("Plato speaks of 'an ancient quarrel between philosophy and poetry' in which Book of the Republic?", "Book X", ["Book II", "Book VII", "Book V"], "The phrase occurs in Republic Book X (607b), where Plato returns to the expulsion of the poets.")
Q("Horace's Ars Poetica is written in the form of a verse epistle addressed to:", "The Pisos", ["Maecenas", "Augustus", "Virgil"], "The Ars Poetica is also called the Epistula ad Pisones, a letter to Piso and his sons.")
Q("How many acts does Horace prescribe for a play in the Ars Poetica?", "Five", ["Three", "Four", "Seven"], "Horace says a play should be neither shorter nor longer than five acts.")
Q("Longinus's treatise On the Sublime is addressed to:", "Postumius Terentianus", ["Caecilius of Calacte", "Dionysius of Halicarnassus", "Lucius Piso"], "The treatise is addressed to Postumius Terentianus; it answers an earlier treatise on the sublime by Caecilius.")
Q("Which two of Longinus's five sources of the sublime are largely innate?", "Grandeur of thought and vehement, inspired passion", ["Figures of speech and noble diction", "Noble diction and dignified composition", "Figures of speech and dignified composition"], "Longinus says the first two sources are mostly innate, while figures, noble diction and dignified composition come from art.")
Q("Which Platonic dialogue discusses rhetoric and writing and contains the myth of the soul as a charioteer?", "Phaedrus", ["Ion", "Symposium", "Timaeus"], "The Phaedrus treats rhetoric, love and writing, and gives the charioteer myth of the soul.")
Q("Aristotle's remark that tragedy tries to confine itself 'to a single revolution of the sun' later became the basis of the unity of:", "Time", ["Place", "Action", "Character"], "Poetics ch. 5; Renaissance critics hardened this observation into the unity of time.")
Q("Dante's De Vulgari Eloquentia is chiefly a defence of:", "Poetry in the vernacular", ["Latin as the only literary language", "Allegorical interpretation of scripture", "Classical tragedy"], "Written in Latin, De Vulgari Eloquentia argues for the dignity of the Italian vernacular as a literary language.")
Q("In An Apology for Poetry, Sidney calls the poet the ______ of all human sciences.", "Monarch", ["Servant", "Physician", "Architect"], "Sidney: 'Now therein of all sciences ... is our poet the monarch.'")
Q("Ben Jonson's critical notes and reflections were published under the title:", "Timber, or Discoveries", ["The Arte of English Poesie", "A Defence of Ryme", "Observations in the Art of English Poesie"], "Timber, or Discoveries was published posthumously (1640-41). The other titles belong to Puttenham, Daniel and Campion.")
Q("Dryden's An Essay of Dramatic Poesy (1668) is set on the day of:", "A naval battle between the English and the Dutch", ["The Great Fire of London", "The coronation of Charles II", "The reopening of the theatres in 1660"], "The four speakers talk on a barge on the Thames while the English and Dutch fleets fight in June 1665.")
Q("Who described Shakespeare as the man 'who of all modern, and perhaps ancient poets, had the largest and most comprehensive soul'?", "John Dryden", ["Samuel Johnson", "Ben Jonson", "Alexander Pope"], "Neander (Dryden) says this in An Essay of Dramatic Poesy.")
Q("Dryden's famous judgement on Chaucer, 'Here is God's plenty', occurs in:", "Preface to the Fables, Ancient and Modern", ["An Essay of Dramatic Poesy", "A Discourse concerning Satire", "Preface to All for Love"], "The remark appears in the Preface to Fables, Ancient and Modern (1700).")
Q("'Shakespeare is above all writers, at least above all modern writers, the poet of nature' is from:", "Johnson's Preface to Shakespeare", ["Dryden's An Essay of Dramatic Poesy", "Pope's Preface to Shakespeare", "Coleridge's Lectures on Shakespeare"], "Johnson's Preface to Shakespeare (1765) opens its praise with this claim.")
Q("In Johnson's Rasselas, who says that the poet does not 'number the streaks of the tulip'?", "Imlac", ["Rasselas", "Nekayah", "Pekuah"], "Imlac's dissertation on poetry (ch. 10) says the poet examines the species, not the individual.")
Q("Addison's essays on 'The Pleasures of the Imagination' appeared in:", "The Spectator", ["The Tatler", "The Rambler", "The Idler"], "Addison published the series in The Spectator in 1712 (Nos. 411-421).")
print("chunk1", len(MCQS))

# ---------- Chunk 2: direct, Romantic to New Critics + Indian ----------
Q("Wordsworth's Preface first appeared in which edition of Lyrical Ballads?", "1800", ["1798", "1802", "1815"], "The 1798 volume had only a short Advertisement. The Preface came in 1800 and was enlarged in 1802.")
Q("In the Preface to Lyrical Ballads, Wordsworth defines the poet as:", "A man speaking to men", ["An unacknowledged legislator", "A seer and a prophet", "A maker of verbal icons"], "Wordsworth: the poet 'is a man speaking to men', though gifted with more lively sensibility.")
Q("Coleridge's phrase 'that willing suspension of disbelief for the moment, which constitutes poetic faith' occurs in:", "Biographia Literaria, Chapter XIV", ["Biographia Literaria, Chapter XIII", "Table Talk", "Lectures on Shakespeare"], "Chapter XIV explains the plan of Lyrical Ballads and gives the phrase.")
Q("Coleridge coined which word for the unifying, shaping power of the imagination?", "Esemplastic", ["Synaesthetic", "Mimetic", "Organic"], "In Biographia Literaria (ch. X) Coleridge coins 'esemplastic', meaning 'to shape into one'.")
Q("Keats first defined 'Negative Capability' in a letter of December 1817 to:", "His brothers George and Tom", ["Benjamin Bailey", "John Hamilton Reynolds", "Fanny Brawne"], "The letter to George and Tom Keats defines Negative Capability as being 'capable of being in uncertainties, Mysteries, doubts, without any irritable reaching after fact and reason'.")
Q("Arnold's definition of criticism as 'a disinterested endeavour to learn and propagate the best that is known and thought in the world' is from:", "The Function of Criticism at the Present Time", ["The Study of Poetry", "Culture and Anarchy", "On Translating Homer"], "The definition closes 'The Function of Criticism at the Present Time' (1864).")
Q("In 'Tradition and the Individual Talent', Eliot compares the mind of the poet to:", "A shred of platinum acting as a catalyst", ["A lamp that projects light", "A mirror held up to nature", "An Aeolian harp"], "Eliot's analogy: the mind is a shred of platinum, a catalyst that stays unchanged while oxygen and sulphur dioxide combine.")
Q("Eliot introduced the phrase 'dissociation of sensibility' in:", "The Metaphysical Poets (1921)", ["Hamlet and His Problems (1919)", "The Function of Criticism (1923)", "Tradition and the Individual Talent (1919)"], "In 'The Metaphysical Poets' Eliot says a dissociation of sensibility set in during the seventeenth century.")
Q("I.A. Richards's Practical Criticism (1929) was based on:", "Responses ('protocols') written by Cambridge students to unsigned poems", ["A survey of Victorian periodical reviews", "Lectures on Shakespeare's tragedies", "A study of myths and archetypes"], "Richards gave his students poems without author or date and analysed the protocols they wrote.")
Q("Which work by William Empson, a pupil of I.A. Richards, appeared in 1930?", "Seven Types of Ambiguity", ["Some Versions of Pastoral", "The Structure of Complex Words", "Milton's God"], "Seven Types of Ambiguity (1930) was Empson's first book. The others came in 1935, 1951 and 1961.")
Q("'The Heresy of Paraphrase' is a chapter in:", "Cleanth Brooks's The Well Wrought Urn", ["John Crowe Ransom's The New Criticism", "W.K. Wimsatt's The Verbal Icon", "Allen Tate's Reason in Madness"], "Brooks argues in The Well Wrought Urn (1947) that a poem's meaning cannot be reduced to a prose paraphrase.")
Q("Allen Tate formed his critical term 'tension' by taking the prefixes off which two logical terms?", "Extension and intension", ["Intention and attention", "Extension and pretension", "Intension and dissension"], "In 'Tension in Poetry' (1938) Tate takes the prefixes off extension and intension.")
Q("Kavyalankara, the work that founded the alamkara school, was written by:", "Bhamaha", ["Dandin", "Udbhata", "Rudrata"], "Bhamaha's Kavyalankara (c. 7th century) treats alamkara as the central element of poetry.")
Q("Dandin's Kavyadarsha distinguishes which two margas (styles) of poetry?", "Vaidarbha and Gauda", ["Vaidarbhi and Panchali", "Gaudi and Lati", "Panchali and Lati"], "Dandin describes two margas, Vaidarbha and Gauda, and links ten gunas to the Vaidarbha.")
Q("Which of the following is NOT one of Anandavardhana's three kinds of dhvani?", "Riti-dhvani", ["Vastu-dhvani", "Alamkara-dhvani", "Rasa-dhvani"], "The Dhvanyaloka names three kinds of suggestion: of a fact (vastu), of a figure (alamkara) and of emotion (rasa).")
Q("Bhatta Nayaka's interpretation of the rasa sutra is known as:", "Bhuktivada", ["Utpattivada", "Anumitivada", "Abhivyaktivada"], "Bhatta Nayaka posits the powers of bhavakatva (generalisation) and bhojakatva (enjoyment) beyond abhidha. Hence his theory is called bhuktivada.")
Q("Who defined poetry as 'tad adoshau shabdarthau sagunav analankriti punah kvapi'?", "Mammata", ["Vishvanatha", "Jagannatha", "Rajashekhara"], "Mammata's Kavyaprakasha defines poetry as word and meaning free from faults, having gunas, and sometimes without evident ornament.")
Q("'Vakyam rasatmakam kavyam' (poetry is a sentence whose soul is rasa) is the definition given by:", "Vishvanatha in Sahityadarpana", ["Mammata in Kavyaprakasha", "Bharata in Natyashastra", "Kshemendra in Kavikanthabharana"], "Vishvanatha (14th century) gives this definition in the Sahityadarpana.")
Q("'Ramaniyartha-pratipadakah shabdah kavyam' is the definition of poetry given in:", "Rasagangadhara", ["Dhvanyaloka", "Kavyamimamsa", "Vakroktijivita"], "Jagannatha's Rasagangadhara (17th century) defines poetry as words that convey a charming meaning.")
Q("Shri Shankuka explained the realisation of rasa through the analogy of the 'chitraturaga nyaya' (picture of a horse). His theory is called:", "Anumitivada", ["Bhuktivada", "Utpattivada", "Abhivyaktivada"], "Shankuka held that rasa is inferred (anumiti) in the actor, as one takes a painted horse for a horse.")
print("chunk2", len(MCQS))

# ---------- Chunk 3: match-the-following (10) + assertion-reason (8) ----------
ROM = ["i", "ii", "iii", "iv"]
def fmt(key): return ", ".join(f"{l}-{r}" for l, r in zip("abcd", key))
def MATCH(intro, list1, list2, key, exp, seed=0):
    # key: list of roman numerals for a,b,c,d
    perms = [list(p) for p in itertools.permutations(ROM) if list(p) != key]
    # prefer distractors that keep one or two pairs right (plausible)
    perms.sort(key=lambda p: (-sum(x == y for x, y in zip(p, key)), "".join(p)))
    wrong = [perms[(seed) % 6], perms[(seed + 3) % 6 + 6], perms[(seed + 5) % 8 + 10]]
    q = (f"{intro} List I: " + " ".join(f"({l}) {t}" for l, t in zip("abcd", list1))
         + " List II: " + " ".join(f"({r}) {t}" for r, t in zip(ROM, list2)))
    Q(q, fmt(key), [fmt(w) for w in wrong], exp)

MATCH("Match List I (concept) with List II (critic):",
      ["Catharsis", "Decorum", "The sublime", "Poetry as imitation of an imitation"],
      ["Plato", "Longinus", "Aristotle", "Horace"],
      ["iii", "iv", "ii", "i"], "Catharsis comes from Aristotle, decorum from Horace, the sublime from Longinus, and the poet as copier of appearances from Plato.", 0)
MATCH("Match List I (work) with List II (author):",
      ["Biographia Literaria", "A Defence of Poetry", "Essays in Criticism", "Preface to Lyrical Ballads"],
      ["Wordsworth", "Arnold", "Coleridge", "Shelley"],
      ["iii", "iv", "ii", "i"], "Biographia Literaria is by Coleridge (1817), A Defence of Poetry by Shelley (1821), Essays in Criticism by Arnold, and the Preface by Wordsworth (1800).", 1)
MATCH("Match List I (book) with List II (critic):",
      ["The Well Wrought Urn", "The World's Body", "The Verbal Icon", "Principles of Literary Criticism"],
      ["I.A. Richards", "W.K. Wimsatt", "Cleanth Brooks", "John Crowe Ransom"],
      ["iii", "iv", "ii", "i"], "The Well Wrought Urn is by Brooks (1947), The World's Body by Ransom (1938), The Verbal Icon by Wimsatt (1954), and Principles of Literary Criticism by Richards (1924).", 2)
MATCH("Match List I (critical concept) with List II (critic):",
      ["Negative capability", "Touchstone method", "Dissociation of sensibility", "Heresy of paraphrase"],
      ["T.S. Eliot", "Cleanth Brooks", "John Keats", "Matthew Arnold"],
      ["iii", "iv", "i", "ii"], "Negative capability is Keats's, the touchstone method Arnold's, dissociation of sensibility Eliot's, and the heresy of paraphrase Brooks's.", 3)
MATCH("Match List I (text) with List II (author):",
      ["Natyashastra", "Kavyadarsha", "Kavyaprakasha", "Sahityadarpana"],
      ["Mammata", "Bharata", "Vishvanatha", "Dandin"],
      ["ii", "iv", "i", "iii"], "The Natyashastra is Bharata's, Kavyadarsha Dandin's, Kavyaprakasha Mammata's, and Sahityadarpana Vishvanatha's.", 4)
MATCH("Match List I (interpreter of the rasa sutra) with List II (theory):",
      ["Bhatta Lollata", "Shri Shankuka", "Bhatta Nayaka", "Abhinavagupta"],
      ["Anumitivada", "Abhivyaktivada", "Utpattivada", "Bhuktivada"],
      ["iii", "i", "iv", "ii"], "Lollata held utpattivada (production), Shankuka anumitivada (inference), Bhatta Nayaka bhuktivada (enjoyment), and Abhinavagupta abhivyaktivada (manifestation).", 5)
MATCH("Match List I (sthayibhava) with List II (rasa):",
      ["Rati", "Hasa", "Krodha", "Bhaya"],
      ["Raudra", "Bhayanaka", "Shringara", "Hasya"],
      ["iii", "iv", "i", "ii"], "Rati gives shringara, hasa gives hasya, krodha gives raudra, and bhaya gives bhayanaka (Natyashastra ch. 6).", 0)
MATCH("Match List I (quotation) with List II (author):",
      ["'Poetry is the breath and finer spirit of all knowledge'", "'Poetry is the record of the best and happiest moments of the happiest and best minds'", "'Poetry = the best words in the best order'", "'Poetry is not a turning loose of emotion, but an escape from emotion'"],
      ["Coleridge", "T.S. Eliot", "Wordsworth", "Shelley"],
      ["iii", "iv", "i", "ii"], "The first is from Wordsworth's Preface (1802), the second from Shelley's Defence, the third from Coleridge's Table Talk (1827), and the fourth from Eliot's 'Tradition and the Individual Talent'.", 1)
MATCH("Match List I (work) with List II (author):",
      ["Timber, or Discoveries", "An Essay on Criticism", "Lives of the Poets", "Of Dramatic Poesy: An Essay"],
      ["Dryden", "Johnson", "Ben Jonson", "Pope"],
      ["iii", "iv", "ii", "i"], "Timber is by Ben Jonson, An Essay on Criticism by Pope (1711), Lives of the Poets by Johnson (1779-81), and Of Dramatic Poesy by Dryden (1668).", 2)
MATCH("Match List I (essay) with List II (authors):",
      ["'The Intentional Fallacy'", "'Tension in Poetry'", "'Criticism, Inc.'", "'Hamlet and His Problems'"],
      ["T.S. Eliot", "Wimsatt and Beardsley", "Allen Tate", "John Crowe Ransom"],
      ["ii", "iii", "iv", "i"], "'The Intentional Fallacy' is by Wimsatt and Beardsley (1946), 'Tension in Poetry' by Tate (1938), 'Criticism, Inc.' by Ransom (1937), and 'Hamlet and His Problems' by Eliot (1919).", 3)

AR_OPTS = ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
           "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
           "(A) is true but (R) is false",
           "(A) is false but (R) is true"]
def AR(a, r, ans, exp):
    MCQS.append({"q": f"Given below are two statements, one labelled Assertion (A) and the other Reason (R). Assertion (A): {a} Reason (R): {r} In the light of the above statements, choose the correct answer from the options given below.",
                 "options": list(AR_OPTS), "answer": ans, "exp": exp})

AR("Plato would banish poets from his ideal republic.",
   "Poetry imitates appearances, which are themselves copies of the Ideas, and it feeds the irrational passions.", 0,
   "In Republic X Plato expels poets because poetry is at a third remove from truth and nourishes the passions. R gives his reason for A.")
AR("Horace holds that poetry should both delight and instruct.",
   "Horace insists that a play should have exactly three acts.", 2,
   "Horace's ideal is 'dulce et utile', but he prescribes five acts, not three. So R is false.")
AR("Eliot holds that poetry is the expression of the poet's personality.",
   "Eliot says that the progress of an artist is a continual self-sacrifice, a continual extinction of personality.", 3,
   "Eliot says that poetry 'is not the expression of personality, but an escape from personality'. So A is false and R is a true quotation.")
AR("Wordsworth rejected the poetic diction of the eighteenth-century poets.",
   "The Preface first appeared in the 1800 edition of Lyrical Ballads.", 1,
   "Both statements are true, but the date of the Preface does not explain why he rejected poetic diction. His reason was his wish to use 'the real language of men'.")
AR("Vamana regards alamkara as the soul of poetry.",
   "Vamana defines riti as a special arrangement of words (vishishta padaracana ritih).", 3,
   "Vamana says 'ritir atma kavyasya': riti, not alamkara, is the soul of poetry. So A is false. R is his own definition of riti.")
AR("Arnold calls Dryden and Pope 'classics of our prose' rather than of our poetry.",
   "Arnold believes their poetry is conceived and composed in their wits, whereas genuine poetry is conceived and composed in the soul.", 0,
   "Both are from 'The Study of Poetry', and R is Arnold's stated reason for A.")
AR("Johnson defends Shakespeare's disregard of the unities of time and place.",
   "Johnson is the author of Lives of the Poets.", 1,
   "Both are true. Johnson argues that the spectator always knows he is in a theatre, so time and place may change, but his authorship of Lives of the Poets does not explain this.")
AR("Kuntaka regards vakrokti as the life of poetry.",
   "Kuntaka holds that only the content of poetry matters and that its mode of expression is of no importance.", 2,
   "In the Vakroktijivita Kuntaka makes vakrokti, a striking and oblique mode of expression, the life (jivita) of poetry. So R misstates his view.")
print("chunk3", len(MCQS))

# ---------- Chunk 4: chronology (7) + correct-statement (5) ----------
def CHRONO(intro, items, order, exp, seed=0):
    f = lambda o: ", ".join(f"({x})" for x in o)
    perms = [list(p) for p in itertools.permutations("abcd") if list(p) != order]
    perms.sort(key=lambda p: (-sum(x == y for x, y in zip(p, order)), "".join(p)))
    wrong = [perms[seed % 5], perms[(seed + 2) % 6 + 6], perms[(seed + 4) % 8 + 12]]
    q = f"{intro} " + " ".join(f"({l}) {t}" for l, t in zip("abcd", items)) + " Choose the correct answer from the options given below."
    Q(q, f(order), [f(w) for w in wrong], exp)

CHRONO("Arrange the following in chronological order of composition:",
       ["Ars Poetica", "Poetics", "On the Sublime", "Republic"], list("dbac"),
       "Plato's Republic dates from c. 375 BC, Aristotle's Poetics c. 335 BC, Horace's Ars Poetica c. 19 BC, and Longinus's On the Sublime the 1st century AD.", 0)
CHRONO("Arrange the following in chronological order of publication:",
       ["Pope's An Essay on Criticism", "Johnson's Preface to Shakespeare", "Sidney's An Apology for Poetry", "Dryden's An Essay of Dramatic Poesy"], list("cdab"),
       "Sidney's Apology was published in 1595, Dryden's Essay in 1668, Pope's Essay on Criticism in 1711, and Johnson's Preface in 1765.", 1)
CHRONO("Arrange the following in chronological order:",
       ["Biographia Literaria", "The Function of Criticism at the Present Time", "Preface to Lyrical Ballads", "A Defence of Poetry (written)"], list("cadb"),
       "The Preface dates from 1800, Biographia Literaria from 1817, A Defence of Poetry was written in 1821, and Arnold's essay is from 1864.", 2)
CHRONO("Arrange the following in chronological order of publication:",
       ["The Well Wrought Urn", "Seven Types of Ambiguity", "Principles of Literary Criticism", "'Tradition and the Individual Talent'"], list("dcba"),
       "'Tradition and the Individual Talent' appeared in 1919, Principles of Literary Criticism in 1924, Seven Types of Ambiguity in 1930, and The Well Wrought Urn in 1947.", 3)
CHRONO("Arrange the following Indian theorists in chronological order:",
       ["Kuntaka", "Vishvanatha", "Vamana", "Anandavardhana"], list("cdab"),
       "Vamana is dated c. late 8th century, Anandavardhana the 9th century, Kuntaka the late 10th or early 11th century, and Vishvanatha the 14th century.", 4)
CHRONO("Arrange the following in chronological order of publication:",
       ["Ransom's The New Criticism", "Arnold's 'The Study of Poetry'", "Eliot's The Sacred Wood", "Pater's Studies in the History of the Renaissance"], list("dbca"),
       "Pater's Renaissance was published in 1873, 'The Study of Poetry' in 1880, The Sacred Wood in 1920, and The New Criticism in 1941.", 0)
CHRONO("Arrange the following Sanskrit theorists in chronological order:",
       ["Mammata", "Jagannatha", "Dandin", "Abhinavagupta"], list("cdab"),
       "Dandin is dated c. 7th century, Abhinavagupta c. 950-1016, Mammata the 11th century, and Jagannatha the 17th century.", 5)

def CS(intro, stmts, correct, wrong, exp):
    q = f"{intro} " + " ".join(f"({l}) {t}" for l, t in zip("abcd", stmts)) + " Choose the correct answer from the options given below."
    Q(q, correct, wrong, exp)

CS("Which of the following statements about Aristotle's Poetics are correct?",
   ["Tragedy is an imitation of an action that is serious, complete and of a certain magnitude.",
    "Plot is the first principle and, as it were, the soul of tragedy.",
    "Aristotle laid down the three unities of time, place and action as binding rules.",
    "Tragedy effects, through pity and fear, the catharsis of such emotions."],
   "(a), (b) and (d) only", ["(a) and (c) only", "(b), (c) and (d) only", "(a), (b), (c) and (d)"],
   "Aristotle insists only on unity of action. Later critics, notably Castelvetro, added the unity of place and made the unities rules.")
CS("Which of the following statements about the New Criticism are correct?",
   ["It treats the biographical and historical context as the key to a poem's meaning.",
    "Wimsatt and Beardsley reject the author's intention as a standard for judging a work.",
    "Cleanth Brooks wrote The Well Wrought Urn.",
    "John Crowe Ransom's The New Criticism (1941) gave the movement its name."],
   "(b), (c) and (d) only", ["(a), (b) and (c) only", "(a) and (d) only", "(a), (b), (c) and (d)"],
   "The New Critics practised close reading of the text itself and set aside biography and history. So (a) is false.")
CS("Which of the following statements are correct?",
   ["Anandavardhana wrote the Dhvanyaloka.",
    "Abhinavagupta wrote the Locana, a commentary on the Dhvanyaloka.",
    "Kuntaka wrote the Kavyadarsha.",
    "Bharata wrote the Dhvanyaloka."],
   "(a) and (b) only", ["(a), (b) and (c) only", "(b) and (d) only", "(c) and (d) only"],
   "Kavyadarsha is by Dandin, and Bharata wrote the Natyashastra. Abhinavagupta also wrote the Abhinavabharati on the Natyashastra.")
CS("Which of the following statements about Coleridge's Biographia Literaria are correct?",
   ["The primary imagination is 'the living Power and prime Agent of all human Perception'.",
    "The secondary imagination 'dissolves, diffuses, dissipates, in order to re-create'.",
    "Coleridge distinguishes between imagination and fancy.",
    "Coleridge holds fancy to be superior to imagination."],
   "(a), (b) and (c) only", ["(a), (c) and (d) only", "(b) and (d) only", "(a), (b), (c) and (d)"],
   "In Chapter XIII fancy is called a mode of memory that deals in 'fixities and definites', so it is lower than imagination.")
CS("Which of the following statements about On the Sublime are correct?",
   ["It names five sources of sublimity.",
    "It holds that the sublime's effect is transport (ekstasis) rather than persuasion.",
    "It was written in Latin.",
    "Boileau's French translation (1674) did much to spread its influence."],
   "(a), (b) and (d) only", ["(a) and (c) only", "(b), (c) and (d) only", "(c) and (d) only"],
   "The treatise is in Greek. Boileau's 1674 translation made it influential in neoclassical Europe.")

print("chunk4", len(MCQS))

if __name__ == "__main__":
    out = "/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/unit8_plus_b.json"
    json.dump({"mcqs": MCQS}, open(out, "w"), ensure_ascii=False, indent=1)
    d = json.load(open(out))["mcqs"]
    assert len(d) == 70, len(d)
    from collections import Counter
    for m in d:
        assert set(m) == {"q", "options", "answer", "exp"} and len(m["options"]) == 4 and 0 <= m["answer"] <= 3
        assert len(set(m["options"])) == 4, m["q"]
    print(len(d), Counter(m["answer"] for m in d))
