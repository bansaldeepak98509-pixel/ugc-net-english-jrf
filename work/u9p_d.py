# Unit 9 plus: 70 new MCQs. D(...) = correct option listed first, placed later; AR(...) = fixed standard options.
AR_OPTS = ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
 "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
 "(A) is true but (R) is false",
 "(A) is false but (R) is true"]
D = []   # (q, [correct, d1, d2, d3], exp)
AR = []  # (q, answer, exp)
# ---- chunk 1: direct 1-20
D += [
("Writing Degree Zero (1953) was written by:",["Roland Barthes","Jacques Derrida","Michel Foucault","Jacques Lacan"],"Barthes ki pehli kitaab, 1953 - writing ki 'zero degree' style."),
("'The World of Wrestling' is the opening essay of:",["Mythologies","S/Z","Image-Music-Text","The Pleasure of the Text"],"Barthes ki Mythologies (1957) mein wrestling, wine, toys par essays hain."),
("Gerard Genette's Narrative Discourse is built mainly on a reading of:",["Proust's In Search of Lost Time","Joyce's Ulysses","Flaubert's Madame Bovary","Cervantes's Don Quixote"],"Genette ne order, duration, frequency, mood, voice Proust par samjhaaye."),
("In Genette's terms, a narrator who is also a character in the story he tells is:",["Homodiegetic","Heterodiegetic","Extradiegetic only","Metadiegetic"],"Homo = same: narrator kahani ke andar maujood hai."),
("How many functions does Vladimir Propp identify in Morphology of the Folktale?",["31","7","21","36"],"Propp: 31 functions aur 7 spheres of action."),
("In Of Grammatology Derrida develops the logic of the 'supplement' through a reading of:",["Rousseau","Plato","Hegel","Husserl"],"Rousseau writing ko speech ka 'dangerous supplement' kehte hain."),
("Derrida's essay 'Plato's Pharmacy' appears in:",["Dissemination","Writing and Difference","Margins of Philosophy","Positions"],"Dissemination (1972) mein pharmakon = dawa bhi, zeher bhi."),
("Allegories of Reading (1979) was written by:",["Paul de Man","J. Hillis Miller","Geoffrey Hartman","Harold Bloom"],"Paul de Man, Yale School ka deconstructionist."),
("The concept of the 'author function' is proposed in Foucault's:",["What Is an Author?","The Order of Things","The Archaeology of Knowledge","Madness and Civilization"],"'What Is an Author?' (1969) - author ek discourse ka function hai."),
("In The History of Sexuality, Volume 1, Foucault questions:",["The repressive hypothesis","The death drive","The mirror stage","The anxiety of influence"],"Foucault: Victorian daur mein sex dabaaya nahi, uske baare mein discourse badha."),
("Which of the following is NOT one of Harold Bloom's revisionary ratios?",["Catharsis","Clinamen","Tessera","Kenosis"],"Bloom ke 6 ratios: clinamen, tessera, kenosis, daemonization, askesis, apophrades. Catharsis Aristotle ka hai."),
("For Carl Jung, archetypes reside in the:",["Collective unconscious","Personal unconscious","Superego","Symbolic order"],"Jung: archetypes poori insaaniyat ke saanjhe collective unconscious mein."),
("Which of the following is NOT one of Lacan's three orders?",["The Semiotic","The Imaginary","The Symbolic","The Real"],"Semiotic Kristeva ka term hai; Lacan: Imaginary, Symbolic, Real."),
("Lacan's seminar, critiqued by Derrida in 'The Purveyor of Truth', reads:",["Poe's The Purloined Letter","Hoffmann's The Sandman","James's The Turn of the Screw","Poe's The Fall of the House of Usher"],"Lacan ka Seminar on 'The Purloined Letter'; Derrida ne jawab diya."),
("Freud's essay 'The Uncanny' (1919) discusses:",["Hoffmann's The Sandman","Shakespeare's Hamlet","Sophocles's Oedipus Rex","Jensen's Gradiva"],"Uncanny = jaana-pehchaana jo ajeeb lage; Sandman ki kahani."),
("Which of the following is a Repressive State Apparatus for Althusser?",["The police","The church","The school","The family"],"RSA force se chalta hai (police, army); church, school, family ISA hain."),
("The concept of 'structure of feeling' is associated with:",["Raymond Williams","Terry Eagleton","Georg Lukacs","Lucien Goldmann"],"Williams: ek daur ka jiya hua anubhav, structure of feeling."),
("The term 'culture industry' was introduced by:",["Adorno and Horkheimer","Benjamin and Brecht","Marcuse and Fromm","Habermas and Lukacs"],"Dialectic of Enlightenment mein 'The Culture Industry' chapter."),
("The decline of the 'aura' of the artwork is discussed by:",["Walter Benjamin","Theodor Adorno","Herbert Marcuse","Antonio Gramsci"],"Benjamin, 'The Work of Art in the Age of Mechanical Reproduction' (1936)."),
("Hegemony as rule by consent rather than force is a key concept of:",["Antonio Gramsci","Louis Althusser","Georg Lukacs","Pierre Macherey"],"Gramsci ki Prison Notebooks."),
]
# ---- chunk 2: direct 21-40
D += [
("Fredric Jameson describes postmodern pastiche as:",["Blank parody","Historiographic metafiction","A simulacrum of the third order","Carnival laughter"],"Jameson: pastiche = bina vyangya ki nakal, 'blank parody'."),
("Criticism and Ideology (1976) was written by:",["Terry Eagleton","Raymond Williams","Pierre Macherey","Fredric Jameson"],"Eagleton ki 1976 ki Marxist kitaab."),
("The idea that the reader fills 'gaps' or 'blanks' in the text is central to:",["Wolfgang Iser","Hans Robert Jauss","Stanley Fish","Norman Holland"],"Iser: The Implied Reader, The Act of Reading."),
("The concept of 'interpretive communities' belongs to:",["Stanley Fish","Wolfgang Iser","Hans Robert Jauss","Jonathan Culler"],"Fish: meaning reader ki community tay karti hai."),
("Iser and Jauss are associated with the:",["Konstanz School","Geneva School","Yale School","Chicago School"],"Dono Konstanz University (Germany) se - reception theory."),
("Norman Holland's psychoanalytic reader-response theory centres on the reader's:",["Identity theme","Horizon of expectations","Interpretive community","Implied reader"],"Holland, 5 Readers Reading (1975)."),
("In The Second Sex, Beauvoir argues that man is the Subject and woman is:",["The Other","The Abject","The subaltern","The Real"],"'He is the Subject, he is the Absolute - she is the Other.'"),
("Showalter coined 'gynocriticism' in the essay:",["Towards a Feminist Poetics","A Literature of Their Own","Sexual Politics","The Madwoman in the Attic"],"Towards a Feminist Poetics (1979): gynocritics = women as writers."),
("Which writer is NOT among those attacked in Kate Millett's Sexual Politics?",["Virginia Woolf","D. H. Lawrence","Henry Miller","Norman Mailer"],"Millett ne Lawrence, Miller, Mailer aur Genet ki aalochana ki."),
("The title The Madwoman in the Attic refers to a character from:",["Jane Eyre","Wuthering Heights","Middlemarch","Frankenstein"],"Bertha Mason, Rochester ki pagal patni, attic mein band."),
("Kristeva's distinction between the semiotic and the symbolic is developed in:",["Revolution in Poetic Language","Speculum of the Other Woman","Gender Trouble","The Newly Born Woman"],"Revolution in Poetic Language (1974)."),
("Bodies That Matter (1993) was written by:",["Judith Butler","Eve Kosofsky Sedgwick","Luce Irigaray","Monique Wittig"],"Butler ki Gender Trouble ke baad ki kitaab."),
("Said's notion of Orientalism as a discourse draws chiefly on:",["Michel Foucault","Jacques Derrida","Jacques Lacan","Roland Barthes"],"Said ne Foucault ka discourse aur Gramsci ka hegemony use kiya."),
("In Culture and Imperialism, Said reads the Antigua plantation in:",["Mansfield Park","Emma","Persuasion","Pride and Prejudice"],"Sir Thomas Bertram ki Antigua estate - contrapuntal reading."),
("Who translated Derrida's Of Grammatology into English (1976)?",["Gayatri Chakravorty Spivak","Homi K. Bhabha","Barbara Johnson","Alan Bass"],"Spivak ka lamba translator's preface mashhoor hai."),
("The concept of the 'Third Space' of enunciation belongs to:",["Homi K. Bhabha","Edward Said","Gayatri Spivak","Frantz Fanon"],"Bhabha, The Location of Culture (1994): hybridity, Third Space."),
("The preface to Fanon's The Wretched of the Earth was written by:",["Jean-Paul Sartre","Albert Camus","Aime Cesaire","Albert Memmi"],"Sartre ne 1961 mein preface likha."),
("In Decolonising the Mind, Ngugi announces he will write in:",["Gikuyu","Swahili","Yoruba","Igbo"],"Ngugi ne English chhodkar Gikuyu apnaayi."),
("Negritude is chiefly associated with:",["Aime Cesaire and Leopold Senghor","Frantz Fanon and Albert Memmi","Chinua Achebe and Wole Soyinka","Edward Said and Gayatri Spivak"],"Cesaire aur Senghor - Black identity ka French-language movement."),
("The term 'strategic essentialism' is associated with:",["Gayatri Spivak","Homi Bhabha","Judith Butler","Julia Kristeva"],"Spivak: political maqsad ke liye kuch der identity ko ek maan lena."),
]
# ---- chunk 3: 10 match + 8 assertion-reason
D += [
("Match the theorists with their terms: (a) Derrida (b) Foucault (c) Althusser (d) Bhabha -- (i) interpellation (ii) differance (iii) hybridity (iv) episteme",["a-ii, b-iv, c-i, d-iii","a-iv, b-ii, c-i, d-iii","a-ii, b-i, c-iv, d-iii","a-iii, b-iv, c-ii, d-i"],"Derrida-differance, Foucault-episteme, Althusser-interpellation, Bhabha-hybridity."),
("Match the works with their authors: (a) Simulacra and Simulation (b) The Postmodern Condition (c) A Poetics of Postmodernism (d) Postmodernism, or, The Cultural Logic of Late Capitalism -- (i) Lyotard (ii) Jameson (iii) Baudrillard (iv) Hutcheon",["a-iii, b-i, c-iv, d-ii","a-i, b-iii, c-iv, d-ii","a-iii, b-i, c-ii, d-iv","a-iv, b-i, c-iii, d-ii"],"Baudrillard 1981, Lyotard 1979, Hutcheon 1988, Jameson 1991."),
("Match the ecocritics with their works: (a) Cheryll Glotfelty (b) William Rueckert (c) Lawrence Buell (d) Greg Garrard -- (i) The Environmental Imagination (ii) Literature and Ecology: An Experiment in Ecocriticism (iii) Ecocriticism (New Critical Idiom) (iv) The Ecocriticism Reader (co-edited)",["a-iv, b-ii, c-i, d-iii","a-ii, b-iv, c-i, d-iii","a-iv, b-ii, c-iii, d-i","a-i, b-ii, c-iv, d-iii"],"Glotfelty-Reader 1996, Rueckert-1978 essay, Buell-1995, Garrard-2004."),
("Match the Bakhtin-circle texts with what they are known for: (a) Problems of Dostoevsky's Poetics (b) Rabelais and His World (c) The Dialogic Imagination (d) Marxism and the Philosophy of Language -- (i) heteroglossia (ii) published under V. N. Voloshinov's name (iii) polyphony (iv) carnival",["a-iii, b-iv, c-i, d-ii","a-iv, b-iii, c-i, d-ii","a-iii, b-iv, c-ii, d-i","a-i, b-iv, c-iii, d-ii"],"Dostoevsky-polyphony, Rabelais-carnival, Dialogic-heteroglossia, Voloshinov ke naam se Marxism and the Philosophy of Language."),
("Match the critics with their works or phrases: (a) Stephen Greenblatt (b) Louis Montrose (c) Jonathan Dollimore (d) Alan Sinfield -- (i) Radical Tragedy (ii) Renaissance Self-Fashioning (iii) Faultlines (iv) 'the textuality of history and the historicity of texts'",["a-ii, b-iv, c-i, d-iii","a-ii, b-i, c-iv, d-iii","a-iv, b-ii, c-i, d-iii","a-ii, b-iv, c-iii, d-i"],"Greenblatt 1980, Montrose ka mashhoor phrase, Dollimore 1984, Sinfield 1992."),
("Match the thinkers with their works: (a) Freud (b) Jung (c) Lacan (d) Bloom -- (i) Ecrits (ii) The Interpretation of Dreams (iii) The Anxiety of Influence (iv) The Archetypes and the Collective Unconscious",["a-ii, b-iv, c-i, d-iii","a-iv, b-ii, c-i, d-iii","a-ii, b-iv, c-iii, d-i","a-ii, b-i, c-iv, d-iii"],"Freud 1900, Jung archetypes, Lacan 1966, Bloom 1973."),
("Match the feminist critics with their works: (a) Toril Moi (b) Elaine Showalter (c) Kate Millett (d) Adrienne Rich -- (i) Sexual Politics (ii) Compulsory Heterosexuality and Lesbian Existence (iii) Sexual/Textual Politics (iv) A Literature of Their Own",["a-iii, b-iv, c-i, d-ii","a-i, b-iv, c-iii, d-ii","a-iii, b-ii, c-i, d-iv","a-iv, b-iii, c-i, d-ii"],"Moi 1985, Showalter 1977, Millett 1970, Rich 1980."),
("Match the narratologists with their concepts: (a) Genette (b) Greimas (c) Propp (d) Todorov -- (i) actantial model (ii) focalization (iii) coined 'narratology' (iv) functions of the folktale",["a-ii, b-i, c-iv, d-iii","a-i, b-ii, c-iv, d-iii","a-ii, b-i, c-iii, d-iv","a-iii, b-i, c-iv, d-ii"],"Genette-focalization, Greimas-actants, Propp-31 functions, Todorov-narratologie (1969)."),
("Match the queer theorists with their concepts: (a) Eve Kosofsky Sedgwick (b) Teresa de Lauretis (c) Michael Warner (d) Lee Edelman -- (i) heteronormativity (ii) homosocial desire (iii) reproductive futurism (iv) coined the term 'queer theory'",["a-ii, b-iv, c-i, d-iii","a-iv, b-ii, c-i, d-iii","a-ii, b-i, c-iv, d-iii","a-ii, b-iv, c-iii, d-i"],"Sedgwick-Between Men, de Lauretis-1990/91, Warner-heteronormativity, Edelman-No Future."),
("Match the Marxist critics with their works: (a) Georg Lukacs (b) Lucien Goldmann (c) Pierre Macherey (d) Walter Benjamin -- (i) The Hidden God (ii) The Historical Novel (iii) A Theory of Literary Production (iv) Illuminations",["a-ii, b-i, c-iii, d-iv","a-i, b-ii, c-iii, d-iv","a-ii, b-iii, c-i, d-iv","a-ii, b-i, c-iv, d-iii"],"Lukacs-Historical Novel, Goldmann-Hidden God, Macherey-Literary Production, Benjamin-Illuminations."),
]
AR += [
("Assertion (A): Saussure holds that the linguistic sign is arbitrary. Reason (R): There is no natural or necessary link between the signifier and the signified.",0,"R hi batata hai sign arbitrary kyon hai."),
("Assertion (A): Derrida's 'differance' combines the senses of 'to differ' and 'to defer'. Reason (R): Derrida holds that meaning is fully present in speech.",2,"A sahi; R galat - Derrida logocentrism aur presence ko hi challenge karte hain."),
("Assertion (A): Frantz Fanon wrote Black Skin, White Masks. Reason (R): Fanon was born in Martinique.",1,"Dono sach, par janm-sthaan kitaab likhne ki wajah nahi."),
("Assertion (A): Showalter's gynocriticism studies women as writers. Reason (R): Showalter's A Literature of Their Own was published in 1990.",2,"A sahi; A Literature of Their Own 1977 mein aayi."),
("Assertion (A): In Discipline and Punish, Foucault argues that power is held only by the sovereign. Reason (R): Foucault sees power as diffuse and productive, circulating through institutions.",3,"Foucault ke liye power har jagah failaa hua hai, sirf raja ke paas nahi."),
("Assertion (A): For Bhabha, colonial mimicry is ambivalent and can menace colonial authority. Reason (R): Mimicry produces a subject who is 'almost the same, but not quite'.",0,"'Not quite' wala farak hi mimicry ko khatarnaak banata hai."),
("Assertion (A): Cheryll Glotfelty coined the term 'ecocriticism' in 1996. Reason (R): Glotfelty co-edited The Ecocriticism Reader.",3,"Term William Rueckert ne 1978 mein diya; R sahi hai."),
("Assertion (A): Ngugi wa Thiong'o wrote Decolonising the Mind. Reason (R): Ngugi was born in Kenya.",1,"Dono sach, par R A ko explain nahi karta."),
]
# ---- chunk 4: 7 chronology + 5 correct-statement
D += [
("Arrange in chronological order: (i) S/Z (ii) Course in General Linguistics (iii) Structural Anthropology (iv) Morphology of the Folktale",["ii, iv, iii, i","iv, ii, iii, i","ii, iii, iv, i","ii, iv, i, iii"],"1916, 1928, 1958, 1970."),
("Arrange Foucault's works in chronological order: (i) Discipline and Punish (ii) The Order of Things (iii) The History of Sexuality, Vol. 1 (iv) Madness and Civilization",["iv, ii, i, iii","ii, iv, i, iii","iv, ii, iii, i","iv, i, ii, iii"],"1961, 1966, 1975, 1976."),
("Arrange in chronological order: (i) The Madwoman in the Attic (ii) A Room of One's Own (iii) Gender Trouble (iv) Sexual Politics",["ii, iv, i, iii","iv, ii, i, iii","ii, i, iv, iii","ii, iv, iii, i"],"1929, 1970, 1979, 1990."),
("Arrange in chronological order: (i) The Location of Culture (ii) Black Skin, White Masks (iii) Can the Subaltern Speak? (iv) Orientalism",["ii, iv, iii, i","iv, ii, iii, i","ii, iii, iv, i","ii, iv, i, iii"],"1952, 1978, 1988, 1994."),
("Arrange in chronological order: (i) A Poetics of Postmodernism (ii) Postmodernism, or, The Cultural Logic of Late Capitalism (iii) Simulacra and Simulation (iv) The Postmodern Condition",["iv, iii, i, ii","iii, iv, i, ii","iv, iii, ii, i","iv, i, iii, ii"],"1979, 1981, 1988, 1991."),
("Arrange in chronological order: (i) Ecrits (ii) Beyond the Pleasure Principle (iii) The Anxiety of Influence (iv) The Interpretation of Dreams",["iv, ii, i, iii","ii, iv, i, iii","iv, i, ii, iii","iv, ii, iii, i"],"1900, 1920, 1966, 1973."),
("Arrange in chronological order: (i) The Ecocriticism Reader (ii) Silent Spring (iii) The Environmental Imagination (iv) Rueckert's 'Literature and Ecology: An Experiment in Ecocriticism'",["ii, iv, iii, i","iv, ii, iii, i","ii, iv, i, iii","ii, iii, iv, i"],"1962, 1978, 1995, 1996."),
("Identify the correct statement:",["Jakobson links metaphor with the axis of selection and metonymy with the axis of combination.","Saussure's Course in General Linguistics was published in his lifetime.","Levi-Strauss coined the term 'narratology'.","Propp's Morphology analyses Greek tragedies."],"Course 1916 mein maut ke baad chhapi; narratology Todorov ka; Propp ne Russian folktales padhi."),
("Identify the correct statement:",["Raymond Williams used the term 'cultural materialism'.","Stephen Greenblatt coined 'cultural materialism'.","Political Shakespeare was edited by Greenblatt and Montrose.","New Historicism excludes non-literary texts."],"Political Shakespeare - Dollimore aur Sinfield; Greenblatt ne 'New Historicism' kaha."),
("Identify the correct statement:",["Spivak's 'Can the Subaltern Speak?' discusses the abolition of sati.","Said's Orientalism was published in 1968.","Bhabha wrote The Wretched of the Earth.","Ngugi's Decolonising the Mind argues for writing African literature in English."],"Orientalism 1978; Wretched - Fanon; Ngugi ne English chhodi."),
("Identify the correct statement:",["Cixous, Irigaray and Kristeva are commonly grouped as French feminists.","Irigaray wrote 'The Laugh of the Medusa'.","Kristeva wrote This Sex Which Is Not One.","Butler's Gender Trouble appeared in 1979."],"Medusa - Cixous; This Sex - Irigaray; Gender Trouble 1990."),
("Identify the correct statement:",["Bakhtin's 'chronotope' means the fusion of time and space in narrative.","Bakhtin coined the term 'intertextuality'.","Bakhtin took Tolstoy's novels as the model of polyphony.","Rabelais and His World is a study of the Romantic lyric."],"Intertextuality - Kristeva; polyphony - Dostoevsky; Rabelais - carnival."),
]
# ---- build
import random as _r
_T = [0,1,2,3]*16; _r.Random(9).shuffle(_T)  # 62 D items need targets
out = []
for idx, (q, opts, exp) in enumerate(D):
    t = _T[idx]
    o = list(opts)
    o[0], o[t] = o[t], o[0]
    out.append(dict(q=q, options=o, answer=t, exp=exp))
ar_items = [dict(q=q, options=list(AR_OPTS), answer=a, exp=e) for q, a, e in AR]
mcqs = out[:50] + ar_items + out[50:]
