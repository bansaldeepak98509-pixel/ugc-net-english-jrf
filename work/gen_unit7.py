import json
T=[]
def t(title,*pts): T.append({"title":title,"points":list(pts)})
t("Background: From Arnold and Leavis to Cultural Studies",
 "Matthew Arnold, Culture and Anarchy (1869): culture is 'the best which has been thought and said in the world' (sweetness and light vs Philistines, Barbarians, Populace).",
 "F. R. Leavis, Mass Civilisation and Minority Culture (1930): culture is kept alive by a small minority; mass culture means 'levelling down'.",
 "Q. D. Leavis, Fiction and the Reading Public (1932): attack on popular fiction and best-sellers.",
 "F. R. Leavis and Denys Thompson, Culture and Environment (1933): training critical awareness against advertising and mass media; nostalgia for the 'organic community'.",
 "This 'Culture and Civilisation' tradition (Leavisism) saw mass culture as a threat; Cultural Studies began by both learning from and rejecting it.",
 "Cultural Studies treats culture as 'a whole way of life' (Williams), not only high art; studies everyday practices, media, youth, class, race and gender.",
 "Founding texts (often called 'culturalism'): Hoggart's The Uses of Literacy (1957), Williams's Culture and Society 1780-1950 (1958) and The Long Revolution (1961), E. P. Thompson's The Making of the English Working Class (1963).",
 "Stuart Hall, 'Cultural Studies: Two Paradigms' (1980) divides the field into culturalism (Hoggart, Williams, Thompson) and structuralism (Levi-Strauss, Barthes, Althusser).",
 "Popular textbook: John Storey, Cultural Theory and Popular Culture: An Introduction (first ed. 1993) gives six definitions of popular culture.")
t("Birmingham CCCS (Centre for Contemporary Cultural Studies)",
 "Founded in 1964 at the University of Birmingham by Richard Hoggart, its first director.",
 "Stuart Hall joined in 1964, became acting director in 1968 and director (1972-1979); then moved to the Open University (1979).",
 "Later directors: Richard Johnson (1979-), Jorge Lorrain; the department was closed by the university in 2002.",
 "Method: interdisciplinary, Marxist (Gramsci, Althusser), semiotic and ethnographic; 'Working Papers in Cultural Studies' (from 1971).",
 "Resistance Through Rituals: Youth Subcultures in Post-War Britain (1975), ed. Stuart Hall and Tony Jefferson.",
 "Policing the Crisis: Mugging, the State, and Law and Order (1978), Hall et al.: moral panic over 'mugging' and race.",
 "Women Take Issue (1978) by the CCCS Women's Studies Group: feminist intervention into the Centre.",
 "The Empire Strikes Back: Race and Racism in 70s Britain (1982), CCCS collective incl. Paul Gilroy.",
 "Paul Willis, Learning to Labour: How Working Class Kids Get Working Class Jobs (1977): ethnography of 'the lads'.",
 "David Morley, The 'Nationwide' Audience (1980, with Charlotte Brunsdon): audience study testing Hall's encoding/decoding.")
t("Richard Hoggart and E. P. Thompson",
 "Richard Hoggart (1918-2014), The Uses of Literacy: Aspects of Working-Class Life with Special Reference to Publications and Entertainments (1957).",
 "Part one: the older 'full rich life' of working-class Leeds (Hunslet); part two: 'Yielding Place to New' - criticises Americanised mass entertainment.",
 "Famous phrases: 'candy-floss world', 'juke-box boys', 'shiny barbarism'; the anxious 'scholarship boy' uprooted by education.",
 "Hoggart was a defence witness in the Lady Chatterley's Lover obscenity trial (1960).",
 "E. P. Thompson (1924-1993), The Making of the English Working Class (1963): 'history from below'.",
 "Opening claim: 'The working class did not rise like the sun at an appointed time. It was present at its own making.'",
 "Quote: 'I am seeking to rescue the poor stockinger, the Luddite cropper, the obsolete hand-loom weaver ... from the enormous condescension of posterity.'",
 "Class for Thompson is a 'historical relationship' and 'happening', not a static thing or category.",
 "Other works: William Morris: Romantic to Revolutionary (1955), Whigs and Hunters (1975), The Poverty of Theory (1978, attack on Althusser's structuralism), Customs in Common (1991, 'moral economy').")
t("Raymond Williams and Cultural Materialism",
 "Raymond Williams (1921-1988), Welsh critic; 'Culture is Ordinary' (essay, 1958).",
 "Culture and Society 1780-1950 (1958): traces 'culture' through Burke, Coleridge, Arnold, Carlyle, Eliot, Leavis; five keywords: industry, democracy, class, art, culture.",
 "The Long Revolution (1961): three definitions of culture - ideal, documentary, social ('a particular way of life').",
 "'Structure of feeling': lived experience of a period (first in Preface to Film, 1954; developed in The Long Revolution).",
 "Marxism and Literature (1977): dominant, residual and emergent cultures; rethinks base and superstructure; coins 'cultural materialism'.",
 "Keywords: A Vocabulary of Culture and Society (1976): 'Culture is one of the two or three most complicated words in the English language.'",
 "The Country and the City (1973): critique of pastoral myths of a lost 'organic' rural England.",
 "Television: Technology and Cultural Form (1974): concept of 'flow' in TV programming.",
 "Other works: Drama from Ibsen to Brecht (1968), Modern Tragedy (1966), Problems in Materialism and Culture (1980), Culture (1981); novel Border Country (1960).",
 "'Cultural materialism' was later used by Jonathan Dollimore and Alan Sinfield in Political Shakespeare (1985); its US cousin is New Historicism (Greenblatt).")
t("Stuart Hall",
 "Stuart Hall (1932-2014), born in Kingston, Jamaica; Rhodes Scholar at Oxford; founding editor of New Left Review (1960).",
 "'Encoding and Decoding in the Television Discourse' (CCCS paper, 1973; revised as 'Encoding/Decoding', 1980).",
 "Three reading positions: dominant-hegemonic (preferred), negotiated, and oppositional.",
 "Meaning is not fixed in the text: the moments of encoding and decoding are 'relatively autonomous'.",
 "'Cultural Studies: Two Paradigms' (1980): culturalism vs structuralism.",
 "'Notes on Deconstructing the Popular' (1981): popular culture is a site of struggle for and against the culture of the powerful.",
 "'The Great Moving Right Show' (1979) and The Hard Road to Renewal (1988): Thatcherism as 'authoritarian populism'.",
 "'Cultural Identity and Diaspora' (1990): identity is 'a production which is never complete'; identity as 'being' and as 'becoming'.",
 "'New Ethnicities' (1988): end of the 'innocent notion of the essential black subject'.",
 "Representation: Cultural Representations and Signifying Practices (1997): reflective, intentional and constructionist approaches; theory of 'articulation'; 'the West and the Rest' (1992).")
t("Youth Subcultures, Style and Moral Panics",
 "Stanley Cohen, Folk Devils and Moral Panics (1972): Mods and Rockers clashes (Clacton, 1964); coined the sociological use of 'moral panic'.",
 "Dick Hebdige, Subculture: The Meaning of Style (1979): punk, skinheads, Rastafarians; style as 'intentional communication'.",
 "Hebdige borrows 'bricolage' from Claude Levi-Strauss (The Savage Mind, 1962): objects re-used to make new meanings (e.g. punk safety pin).",
 "Hebdige: subcultures are 'incorporated' by two forms - the commodity form and the ideological form.",
 "Hebdige also uses 'homology' (Willis) and semiotic guerrilla warfare (Umberto Eco).",
 "Phil Cohen (1972): subcultures 'magically resolve' contradictions of the parent working-class culture.",
 "Angela McRobbie: 'Jackie: An Ideology of Adolescent Femininity' (1978); with Jenny Garber 'Girls and Subcultures' (1975).",
 "Post-subcultural theory (1990s-2000s): 'neo-tribes' (Michel Maffesoli), club cultures and 'subcultural capital' (Sarah Thornton, 1995).")
t("Frankfurt School and the Culture Industry",
 "Institute for Social Research founded in Frankfurt in 1923; Max Horkheimer became director in 1930; exiled to New York during Nazism.",
 "Members: Max Horkheimer, Theodor W. Adorno, Herbert Marcuse, Walter Benjamin (associate), Leo Lowenthal, Erich Fromm; second generation: Jurgen Habermas.",
 "Horkheimer, 'Traditional and Critical Theory' (1937) defines 'critical theory'.",
 "Adorno and Horkheimer, Dialectic of Enlightenment (1944 as Philosophical Fragments; 1947 Amsterdam).",
 "Key chapter: 'The Culture Industry: Enlightenment as Mass Deception' - culture produced like factory goods.",
 "Features of the culture industry: standardisation, pseudo-individuality, repetition, passive consumers, amusement as 'prolongation of work'.",
 "Adorno, 'On Popular Music' (1941): standardised hit songs; 'Culture Industry Reconsidered' (1963): 'the masses are not primary but secondary'.",
 "Adorno: 'To write poetry after Auschwitz is barbaric' ('Cultural Criticism and Society', 1949/1951); other works Minima Moralia (1951), Negative Dialectics (1966), Aesthetic Theory (1970).",
 "Herbert Marcuse, One-Dimensional Man (1964): 'repressive desublimation', false needs; Eros and Civilization (1955).",
 "Jurgen Habermas, The Structural Transformation of the Public Sphere (1962): bourgeois 'public sphere' of coffee houses and salons.")
t("Walter Benjamin",
 "Walter Benjamin (1892-1940), German-Jewish critic; died at Portbou on the French-Spanish border fleeing the Nazis.",
 "'The Work of Art in the Age of Mechanical Reproduction' (1935 draft; published 1936).",
 "Mechanical reproduction (photography, film) destroys the 'aura' of the original - its 'here and now', unique existence.",
 "Shift from 'cult value' to 'exhibition value'; art's basis shifts from ritual to politics.",
 "Conclusion: fascism 'aestheticizes politics'; communism responds by 'politicizing art'.",
 "'Theses on the Philosophy of History' (1940): angel of history (Paul Klee's Angelus Novus) faces the past as 'one single catastrophe'.",
 "Quote: 'There is no document of civilization which is not at the same time a document of barbarism.'",
 "The Arcades Project (Passagen-Werk, unfinished, 1927-1940): Paris arcades, the flaneur (from Baudelaire).",
 "Other essays: 'The Task of the Translator' (1923), 'The Author as Producer' (1934), 'The Storyteller' (1936); book The Origin of German Tragic Drama (1928, Trauerspiel).",
 "Unlike Adorno, Benjamin saw democratic potential in film and mass reproduction.")
t("Antonio Gramsci and Hegemony",
 "Antonio Gramsci (1891-1937), Italian Marxist, co-founder of the Italian Communist Party; imprisoned by Mussolini in 1926.",
 "Prison Notebooks (Quaderni del carcere), written 1929-1935; selections in English 1971 (Hoare and Nowell-Smith).",
 "Hegemony: rule by the dominant class through consent ('spontaneous consent' of the masses) backed by coercion.",
 "Civil society (church, schools, media - consent) vs political society/State (army, police, courts - coercion).",
 "Organic intellectuals (arise from a class and organise it) vs traditional intellectuals (clergy, professors who see themselves as autonomous).",
 "Quote: 'All men are intellectuals, but not all men have in society the function of intellectuals.'",
 "War of position (cultural trench warfare in civil society) vs war of manoeuvre (frontal attack on the state).",
 "Other terms: historic bloc, common sense vs good sense, passive revolution, counter-hegemony.",
 "Gramsci used 'subaltern' for subordinated groups (peasants of southern Italy) - later taken up by Subaltern Studies.",
 "The 'turn to Gramsci' at CCCS in the 1970s: popular culture seen as a site of negotiation between resistance and incorporation.")
t("Louis Althusser and Ideological State Apparatuses",
 "Louis Althusser (1918-1990), French structuralist Marxist.",
 "'Ideology and Ideological State Apparatuses (Notes towards an Investigation)' (written 1969, published 1970; in Lenin and Philosophy, 1971).",
 "Repressive State Apparatus (RSA): government, army, police, courts, prisons - functions 'by violence'.",
 "Ideological State Apparatuses (ISAs): religious, educational, family, legal, political, trade-union, communications, cultural - function 'by ideology'.",
 "In mature capitalism the educational ISA (school) is the dominant ISA, replacing the Church.",
 "Definition: 'Ideology represents the imaginary relationship of individuals to their real conditions of existence.'",
 "'Ideology has a material existence' and 'Ideology has no history'.",
 "Interpellation (hailing): 'Hey, you there!' - ideology interpellates individuals as subjects.",
 "Other works: For Marx (1965), Reading Capital (1965, with Balibar and others).",
 "Key concepts: epistemological break (young vs mature Marx), overdetermination, problematic, symptomatic reading, relative autonomy of the superstructure; influenced Pierre Macherey, A Theory of Literary Production (1966).")
t("Roland Barthes: Mythologies and Semiology",
 "Roland Barthes (1915-1980), French semiotician; Mythologies (1957; English selection 1972, trans. Annette Lavers).",
 "Short essays on everyday French culture: 'The World of Wrestling', 'Wine and Milk', 'Steak and Chips', 'Soap-powders and Detergents', 'The Face of Garbo', 'The New Citroen', 'Einstein's Brain', 'Toys', 'The Great Family of Man'.",
 "Theoretical essay 'Myth Today': myth is a 'type of speech' and a 'second-order semiological system'.",
 "First order: signifier + signified = sign; in myth this sign becomes the 'form', joined to a 'concept' to give 'signification'.",
 "Example: Paris-Match cover of a young Black soldier in French uniform saluting the tricolour - myth of French imperiality.",
 "Myth 'transforms history into nature'; myth is 'depoliticized speech'; it serves bourgeois ideology ('ex-nomination' of the bourgeoisie).",
 "Elements of Semiology (1964): denotation and connotation (borrowed from Hjelmslev).",
 "'The Death of the Author' (1967): 'the birth of the reader must be at the cost of the death of the Author'.",
 "S/Z (1970): readerly (lisible) vs writerly (scriptible) texts; five codes (hermeneutic, proairetic, semic, symbolic, cultural).",
 "The Pleasure of the Text (1973): plaisir vs jouissance; Camera Lucida (1980): studium vs punctum; Empire of Signs (1970) on Japan.")
t("Baudrillard, Simulation and Postmodern Media Theory",
 "Jean Baudrillard (1929-2007), French theorist; Simulacra and Simulation (1981; English 1994).",
 "Hyperreality: 'the generation by models of a real without origin or reality'; the map precedes the territory ('precession of simulacra').",
 "Four phases of the image: reflects a basic reality; masks and perverts reality; masks the absence of reality; bears no relation to any reality - its own pure simulacrum.",
 "Three orders of simulacra (Symbolic Exchange and Death, 1976): counterfeit (Renaissance), production (industrial), simulation (code-governed present).",
 "Disneyland is presented as imaginary 'in order to make us believe that the rest is real'.",
 "The Gulf War Did Not Take Place (1991): war as media spectacle; other works The System of Objects (1968), The Consumer Society (1970), For a Critique of the Political Economy of the Sign (1972).",
 "Guy Debord, The Society of the Spectacle (1967): 'All that once was directly lived has become mere representation.'",
 "Marshall McLuhan: 'the medium is the message' (Understanding Media, 1964); 'global village' (The Gutenberg Galaxy, 1962); hot vs cool media.",
 "Fredric Jameson, Postmodernism, or, the Cultural Logic of Late Capitalism (1991; essay 1984): pastiche, depthlessness, 'waning of affect'.",
 "Jean-Francois Lyotard, The Postmodern Condition: A Report on Knowledge (1979): 'incredulity toward metanarratives'.")
t("Pierre Bourdieu: Taste, Capital and Field",
 "Pierre Bourdieu (1930-2002), French sociologist.",
 "Distinction: A Social Critique of the Judgement of Taste (1979; English 1984): taste is socially produced and marks class.",
 "Quote: 'Taste classifies, and it classifies the classifier.'",
 "Forms of capital ('The Forms of Capital', 1986): economic, cultural, social, and symbolic capital.",
 "Cultural capital has three states: embodied, objectified, institutionalised (degrees).",
 "Habitus: durable, internalised dispositions shaping how people perceive and act (Outline of a Theory of Practice, 1972/1977).",
 "Field (champ): a structured social arena of struggle, e.g. The Field of Cultural Production (1993), The Rules of Art (1992).",
 "Symbolic violence: domination accepted as natural by the dominated; Reproduction in Education, Society and Culture (1970, with Jean-Claude Passeron).",
 "Taste types in Distinction: legitimate (high), middle-brow, popular; 'pure gaze' vs 'popular aesthetic'.")
t("John Fiske and Popular Culture Studies",
 "John Fiske (1939-2021): Reading Television (1978, with John Hartley), Television Culture (1987), Understanding Popular Culture (1989), Reading the Popular (1989).",
 "Fiske: popular culture is made by the people from the products of the culture industry, 'not imposed upon them'.",
 "Key ideas: polysemy of TV texts, 'semiotic democracy', 'producerly text' (between Barthes's readerly and writerly).",
 "Two economies of TV: financial economy (wealth) and cultural economy (meanings and pleasures).",
 "Michel de Certeau, The Practice of Everyday Life (1980; English 1984): strategies (of the powerful) vs tactics (of the weak); reading as 'poaching'.",
 "Henry Jenkins, Textual Poachers: Television Fans and Participatory Culture (1992); Convergence Culture (2006).",
 "Janice Radway, Reading the Romance (1984): ethnography of women romance readers in 'Smithton'.",
 "Ien Ang, Watching Dallas (1982; English 1985): 'ideology of mass culture' and viewers' pleasure.",
 "Mass-culture critics: Dwight Macdonald, 'A Theory of Mass Culture' (1953) - masscult and midcult; Clement Greenberg, 'Avant-Garde and Kitsch' (1939).",
 "Leslie Fiedler, 'Cross the Border - Close the Gap' (1969) urged closing the gap between high and popular culture.")
t("Subaltern Studies",
 "Term 'subaltern' taken from Gramsci; Subaltern Studies collective founded by Ranajit Guha; first volume 1982 (Oxford University Press, Delhi).",
 "Guha's manifesto 'On Some Aspects of the Historiography of Colonial India' (1982) attacks colonialist and bourgeois-nationalist elitism.",
 "Guha: Elementary Aspects of Peasant Insurgency in Colonial India (1983); Dominance without Hegemony (1997).",
 "Members: Partha Chatterjee, Dipesh Chakrabarty, Shahid Amin, Gyanendra Pandey, David Hardiman, David Arnold, Gautam Bhadra.",
 "Shahid Amin, 'Gandhi as Mahatma' (1984); Event, Metaphor, Memory: Chauri Chaura 1922-1992 (1995).",
 "Partha Chatterjee: Nationalist Thought and the Colonial World: A Derivative Discourse? (1986); The Nation and Its Fragments (1993) - inner/spiritual vs outer/material domain.",
 "Dipesh Chakrabarty, Provincializing Europe (2000): Europe as 'hyperreal' and the 'waiting room of history'.",
 "Gayatri Chakravorty Spivak, 'Can the Subaltern Speak?' (1983 lecture; published 1988 in Marxism and the Interpretation of Culture): sati debate; 'White men are saving brown women from brown men'; answer: 'the subaltern cannot speak'.",
 "Spivak's 'strategic essentialism' ('Subaltern Studies: Deconstructing Historiography', 1985); Selected Subaltern Studies (1988), ed. Guha and Spivak, foreword by Edward Said.")
t("Gender, Sexuality and Queer Theory in Cultural Studies",
 "Laura Mulvey, 'Visual Pleasure and Narrative Cinema' (Screen, 1975): the 'male gaze', scopophilia; woman as 'to-be-looked-at-ness'.",
 "bell hooks, 'The Oppositional Gaze: Black Female Spectators' (1992).",
 "Michel Foucault, The History of Sexuality, Vol. 1 (1976): rejects the 'repressive hypothesis'; sexuality produced by discourse.",
 "Adrienne Rich, 'Compulsory Heterosexuality and Lesbian Existence' (1980): 'lesbian continuum'.",
 "Monique Wittig, 'One Is Not Born a Woman' (1981) and The Straight Mind (1992).",
 "Teresa de Lauretis coined 'queer theory' (1990 conference; 'Queer Theory: Lesbian and Gay Sexualities', differences, 1991).",
 "Judith Butler, Gender Trouble (1990): gender is 'performative' - 'a stylized repetition of acts'; Bodies That Matter (1993).",
 "Eve Kosofsky Sedgwick: Between Men (1985) - 'male homosocial desire'; Epistemology of the Closet (1990).",
 "Michael Warner popularised 'heteronormativity' (Fear of a Queer Planet, 1993); Lee Edelman, No Future (2004) - 'reproductive futurism'.",
 "Donna Haraway, 'A Cyborg Manifesto' (1985): 'I would rather be a cyborg than a goddess.'")
t("Ecocriticism",
 "Term 'ecocriticism' coined by William Rueckert in 'Literature and Ecology: An Experiment in Ecocriticism' (1978).",
 "Cheryll Glotfelty and Harold Fromm (eds.), The Ecocriticism Reader (1996): 'ecocriticism is the study of the relationship between literature and the physical environment' (Glotfelty).",
 "ASLE (Association for the Study of Literature and Environment) founded in 1992; journal ISLE from 1993.",
 "Lawrence Buell, The Environmental Imagination (1995) on Thoreau; The Future of Environmental Criticism (2005) - 'first wave' and 'second wave'.",
 "British 'green studies': Jonathan Bate, Romantic Ecology (1991) and The Song of the Earth (2000); Greg Garrard, Ecocriticism (2004, New Critical Idiom).",
 "Rachel Carson, Silent Spring (1962); Leo Marx, The Machine in the Garden (1964); Arne Naess coined 'deep ecology' (1973).",
 "Francoise d'Eaubonne coined 'ecofeminism' (1974); Vandana Shiva, Staying Alive (1988).",
 "Ramachandra Guha and Joan Martinez-Alier, Varieties of Environmentalism (1997): 'environmentalism of the poor'.",
 "Rob Nixon, Slow Violence and the Environmentalism of the Poor (2011); Amitav Ghosh, The Great Derangement (2016) on climate change and the novel.",
 "Timothy Morton: Ecology without Nature (2007), Hyperobjects (2013); Anthropocene term popularised by Paul Crutzen (2000).")
t("Digital Culture, New Media and Indian Cultural Studies",
 "Ted Nelson coined 'hypertext' (1965); George Landow, Hypertext (1992); Espen Aarseth, Cybertext (1997) - 'ergodic literature'.",
 "William Gibson coined 'cyberspace' ('Burning Chrome', 1982; Neuromancer, 1984); Richard Dawkins coined 'meme' (The Selfish Gene, 1976).",
 "Lev Manovich, The Language of New Media (2001); Bolter and Grusin, Remediation (1999); Manuel Castells, The Rise of the Network Society (1996).",
 "N. Katherine Hayles, How We Became Posthuman (1999); Sherry Turkle, Alone Together (2011); Shoshana Zuboff, The Age of Surveillance Capitalism (2019).",
 "Arjun Appadurai, Modernity at Large (1996): five 'scapes' - ethnoscapes, mediascapes, technoscapes, financescapes, ideoscapes.",
 "Homi K. Bhabha, The Location of Culture (1994): hybridity, mimicry ('almost the same, but not quite'), ambivalence, Third Space.",
 "Ashis Nandy, The Intimate Enemy: Loss and Recovery of Self under Colonialism (1983).",
 "Tejaswini Niranjana, Siting Translation (1992); Susie Tharu and K. Lalita (eds.), Women Writing in India (1991-93); G. N. Devy, After Amnesia (1992).",
 "Kancha Ilaiah, Why I Am Not a Hindu (1996); A. K. Ramanujan, 'Three Hundred Ramayanas' (1991); Arvind Rajagopal, Politics after Television (2001) on the TV Ramayan.",
 "Centre for the Study of Culture and Society (CSCS), Bangalore, founded 1996; Ashish Rajadhyaksha, 'The Bollywoodization of the Indian Cinema' (2003).")

TM=[]
def m(term,pron,hindi,net): TM.append({"term":term,"pron":pron,"hindi":hindi,"net":net})
m("Cultural Studies","कल्चरल स्टडीज़ (KUL-chuh-rul STUH-deez)","संस्कृति, मीडिया और रोज़मर्रा की ज़िंदगी में सत्ता का अध्ययन","An interdisciplinary field, institutionalised at the Birmingham CCCS (1964), that studies culture as 'a whole way of life' and as a site of power, ideology and resistance.")
m("Culturalism","कल्चरलिज़्म (KUL-chuh-ruh-liz-um)","आम लोगों के जीवित अनुभव को संस्कृति का केंद्र मानना","Stuart Hall's term (1980) for the humanist, experience-centred paradigm of Hoggart, Williams and Thompson, opposed to structuralism.")
m("Structure of Feeling","स्ट्रक्चर ऑफ़ फ़ीलिंग (STRUK-chur uv FEE-ling)","किसी दौर की साझा भावना या जिया गया अनुभव","Raymond Williams's term (Preface to Film, 1954; The Long Revolution, 1961) for the lived, felt sense of life of a particular generation or period.")
m("Cultural Materialism","कल्चरल मटीरियलिज़्म (KUL-chur-ul muh-TEER-ee-uh-liz-um)","संस्कृति को भौतिक-आर्थिक हालात से जोड़कर पढ़ना","Williams's term (Marxism and Literature, 1977) for analysing culture as material production; later applied to Renaissance texts by Dollimore and Sinfield (Political Shakespeare, 1985).")
m("Dominant, Residual, Emergent","डॉमिनेंट, रेज़िड्युअल, इमर्जेंट (DOM-i-nunt, ri-ZID-yoo-ul, i-MUR-junt)","हावी, पुरानी बची हुई, और नई उभरती संस्कृति","Williams's threefold model (Marxism and Literature, 1977) of cultural elements in any period: the ruling, the survivals of the past, and new meanings and practices.")
m("Culture Industry","कल्चर इंडस्ट्री (KUL-chur IN-dus-tree)","फ़ैक्ट्री की तरह बनाई-बेची जाने वाली मनोरंजन संस्कृति","Adorno and Horkheimer's term in Dialectic of Enlightenment (1947) for the standardised, mass-produced culture of capitalism that produces passive conformity.")
m("Pseudo-individuality","स्यूडो-इंडिविजुअलिटी (SOO-doh in-di-vi-joo-AL-i-tee)","नकली अनोखापन, असल में सब एक जैसा","Adorno's term ('On Popular Music', 1941) for the superficial differences that disguise the standardisation of mass-cultural products.")
m("Aura","ऑरा (AW-ruh)","मूल कलाकृति की अनोखी, पवित्र चमक","Walter Benjamin's term ('The Work of Art in the Age of Mechanical Reproduction', 1936) for the unique presence in time and space of the original work, which mechanical reproduction destroys.")
m("Flaneur","फ़्लानर (flah-NUR)","शहर की गलियों में बेमक़सद घूमने-देखने वाला","The idle urban stroller-observer of modern Paris, from Baudelaire, theorised by Walter Benjamin in The Arcades Project.")
m("Hegemony","हेजेमनी (hi-JEM-uh-nee)","ज़बरदस्ती से नहीं, सहमति से चलने वाला वर्चस्व","Gramsci's concept (Prison Notebooks, 1929-35) of the leadership of a dominant class secured chiefly through the consent of subordinate groups, backed by coercion.")
m("Organic Intellectual","ऑर्गैनिक इंटेलेक्चुअल (or-GAN-ik in-tuh-LEK-choo-ul)","अपने वर्ग से निकला और उसी के लिए सोचने वाला बुद्धिजीवी","Gramsci's term for intellectuals who emerge from and articulate the interests of a social class, as against 'traditional intellectuals'.")
m("War of Position","वॉर ऑफ़ पोज़ीशन (WOR uv puh-ZI-shun)","संस्कृति और समाज में धीरे-धीरे लड़ी जाने वाली लड़ाई","Gramsci's term for long-term cultural and ideological struggle within civil society, contrasted with the 'war of manoeuvre' (direct assault on the state).")
m("Historic Bloc","हिस्टॉरिक ब्लॉक (his-TOR-ik BLOK)","अलग-अलग वर्गों का सत्ता के लिए बना गठजोड़","Gramsci's term for the alliance of social forces and the unity of base and superstructure through which hegemony is exercised.")
m("Ideological State Apparatus","आइडियोलॉजिकल स्टेट एपरेटस (eye-dee-uh-LOJ-i-kul STAYT ap-uh-RAY-tus)","स्कूल, परिवार, धर्म, मीडिया जैसी संस्थाएँ जो विचारधारा फैलाती हैं","Althusser's term ('Ideology and Ideological State Apparatuses', 1970) for institutions that function 'by ideology' (school, church, family, media), as against the Repressive State Apparatus.")
m("Repressive State Apparatus","रिप्रेसिव स्टेट एपरेटस (ri-PRES-iv STAYT ap-uh-RAY-tus)","पुलिस, सेना, अदालत जैसी दबाने वाली ताक़तें","Althusser's term for the government, army, police, courts and prisons, which function predominantly 'by violence'.")
m("Interpellation","इंटरपेलेशन (in-tur-puh-LAY-shun)","विचारधारा का हमें 'ऐ, तुम!' कहकर पुकारना और हमें 'subject' बनाना","Althusser's term for the process by which ideology 'hails' ('Hey, you there!') concrete individuals and constitutes them as subjects.")
m("Overdetermination","ओवरडिटर्मिनेशन (oh-vur-di-tur-mi-NAY-shun)","एक घटना के पीछे कई कारण एक साथ होना","Althusser's term (For Marx, 1965), from Freud, for the multiple, interacting causes of any social contradiction, rejecting simple economic determinism.")
m("Symptomatic Reading","सिम्प्टोमैटिक रीडिंग (simp-tuh-MAT-ik REE-ding)","पाठ की चुप्पियों और कमियों को पढ़ना","Althusser's method (Reading Capital, 1965) of reading a text for its absences, silences and gaps, which reveal its hidden problematic.")
m("Myth","मिथ (MITH)","ऐसा अर्थ जो इतिहास को 'स्वाभाविक' बताकर पेश करे","For Barthes ('Myth Today', Mythologies, 1957) a second-order semiological system and 'depoliticized speech' that turns history into nature.")
m("Connotation","कनोटेशन (kon-uh-TAY-shun)","शब्द या चित्र का छिपा, सांस्कृतिक अर्थ","The secondary, culturally coded meaning of a sign beyond its literal denotation; developed by Barthes (Elements of Semiology, 1964) from Hjelmslev.")
m("Punctum","पंक्टम (PUNK-tum)","फ़ोटो की वो बारीक चीज़ जो दिल को चुभ जाए","Barthes's term (Camera Lucida, 1980) for the poignant, personal detail in a photograph that 'pricks' the viewer, as against the studium (general cultural interest).")
m("Jouissance","ज़ुइसाँस (zhwee-SAHNS)","चरम, तोड़-फोड़ करने वाला आनंद","Barthes's term (The Pleasure of the Text, 1973) for disruptive bliss in reading, as opposed to comfortable 'plaisir'.")
m("Simulacrum","सिम्युलेक्रम (sim-yoo-LAY-krum)","असली के बिना बनी नकल","For Baudrillard (Simulacra and Simulation, 1981) a copy without an original; in the final phase the image 'bears no relation to any reality'.")
m("Hyperreality","हाइपररियलिटी (hy-pur-ree-AL-i-tee)","नकल जो असली से भी ज़्यादा असली लगे","Baudrillard's term for 'the generation by models of a real without origin or reality', where simulation replaces the real (e.g. Disneyland).")
m("Spectacle","स्पेक्टेकल (SPEK-tuh-kul)","तस्वीरों के ज़रिए बना सामाजिक रिश्ता, दिखावे का समाज","Guy Debord's term (The Society of the Spectacle, 1967) for 'a social relation among people, mediated by images'.")
m("Cultural Capital","कल्चरल कैपिटल (KUL-chur-ul KAP-i-tul)","शिक्षा, रुचि, ज्ञान जैसी सांस्कृतिक पूँजी","Bourdieu's term (Distinction, 1979; 'The Forms of Capital', 1986) for non-economic assets (education, tastes, credentials) existing in embodied, objectified and institutionalised states.")
m("Habitus","हैबिटस (HAB-i-tus)","समाज से सीखी आदतें और सोचने का ढंग","Bourdieu's term for a system of durable, internalised dispositions that generate perceptions and practices (Outline of a Theory of Practice, 1972).")
m("Symbolic Violence","सिम्बॉलिक वायलेंस (sim-BOL-ik VY-uh-luns)","ऐसा दबदबा जिसे दबे हुए लोग भी स्वाभाविक मान लें","Bourdieu's term for domination exercised through culture and accepted as legitimate by those subjected to it.")
m("Encoding/Decoding","एनकोडिंग/डीकोडिंग (en-KOH-ding / dee-KOH-ding)","संदेश बनाना और दर्शक का उसे अपने ढंग से समझना","Stuart Hall's model (1973/1980) of mass communication in which audiences may decode a text in dominant-hegemonic, negotiated or oppositional ways.")
m("Preferred Reading","प्रेफ़र्ड रीडिंग (pri-FURD REE-ding)","वो अर्थ जो बनाने वाला चाहता है कि दर्शक समझे","In Hall's encoding/decoding model, the dominant meaning inscribed in a media text, which audiences may accept, negotiate or oppose.")
m("Articulation","आर्टिक्युलेशन (ar-tik-yoo-LAY-shun)","अलग-अलग चीज़ों का किसी समय विशेष पर जुड़ जाना","Hall's (from Laclau) concept of a contingent, non-necessary linkage between different elements that forms a unity under specific conditions.")
m("Moral Panic","मॉरल पैनिक (MOR-ul PAN-ik)","किसी समूह को समाज के लिए ख़तरा बताकर फैलाया गया डर","Stanley Cohen's term (Folk Devils and Moral Panics, 1972) for the media-amplified reaction defining a group (e.g. Mods and Rockers) as a threat to social values.")
m("Subculture","सबकल्चर (SUB-kul-chur)","मुख्य संस्कृति के भीतर अलग पहचान वाला छोटा समूह","A group within a larger culture marked by distinctive style and values; theorised at CCCS (Resistance Through Rituals, 1975) and by Hebdige (1979) as symbolic resistance.")
m("Bricolage","ब्रिकोलाज़ (bree-koh-LAHZH)","पुरानी चीज़ों को जोड़कर नया अर्थ बनाना","Levi-Strauss's term (The Savage Mind, 1962), used by Hebdige (Subculture, 1979) for subcultures' re-use of objects to create new, oppositional meanings.")
m("Semiotic Democracy","सेमियोटिक डेमोक्रेसी (sem-ee-OT-ik di-MOK-ruh-see)","दर्शकों को टीवी के अर्थ ख़ुद बनाने की आज़ादी","John Fiske's term (Television Culture, 1987) for audiences' freedom to make their own meanings from polysemic television texts.")
m("Producerly Text","प्रोड्यूसरली टेक्स्ट (pruh-DOO-sur-lee TEKST)","आसान पर कई अर्थ देने वाला लोकप्रिय पाठ","Fiske's term for a popular text that is accessible like Barthes's readerly text yet open, like the writerly, to the reader's own meanings.")
m("Tactics","टैक्टिक्स (TAK-tiks)","कमज़ोर लोगों की रोज़ की चालाक जुगत","Michel de Certeau's term (The Practice of Everyday Life, 1980) for the improvised practices of the weak, as against the 'strategies' of institutions.")
m("Subaltern","सबाल्टर्न (suh-BAWL-turn)","समाज के हाशिए पर पड़े, दबे हुए लोग","Gramsci's term for subordinated social groups, adopted by Ranajit Guha's Subaltern Studies (1982-) and problematised in Spivak's 'Can the Subaltern Speak?' (1988).")
m("Strategic Essentialism","स्ट्रैटेजिक एसेंशियलिज़्म (struh-TEE-jik i-SEN-shuh-liz-um)","राजनीतिक मक़सद के लिए अस्थायी रूप से एक साझा पहचान अपनाना","Spivak's term (1985) for the provisional, tactical use of a shared group identity by marginalised groups for political ends.")
m("Epistemic Violence","एपिस्टेमिक वायलेंस (ep-i-STEE-mik VY-uh-luns)","ज्ञान के नाम पर दूसरों की आवाज़ मिटा देना","Spivak's term ('Can the Subaltern Speak?') for the violence done by colonial and Western knowledge systems in constituting and silencing the colonised Other.")
m("Male Gaze","मेल गेज़ (MAYL GAYZ)","फ़िल्म में औरत को मर्द की नज़र से भोग की वस्तु दिखाना","Laura Mulvey's term ('Visual Pleasure and Narrative Cinema', 1975) for the way classical cinema positions woman as image and man as bearer of the look.")
m("Scopophilia","स्कोपोफ़िलिया (skoh-puh-FIL-ee-uh)","देखने से मिलने वाला सुख","Freud's term for pleasure in looking, used by Mulvey (1975) to analyse cinematic spectatorship.")
m("Performativity","परफ़ॉर्मेटिविटी (pur-for-muh-TIV-i-tee)","जेंडर का बार-बार दोहराए गए व्यवहार से बनना","Judith Butler's concept (Gender Trouble, 1990) that gender is produced through 'the repeated stylization of the body', not an inner essence.")
m("Heteronormativity","हेटरोनॉर्मेटिविटी (het-uh-roh-nor-muh-TIV-i-tee)","विषमलैंगिकता को ही 'सामान्य' मान लेना","Michael Warner's term (Fear of a Queer Planet, 1993) for the institutions and assumptions that make heterosexuality seem natural and normative.")
m("Homosocial Desire","होमोसोशल डिज़ायर (hoh-moh-SOH-shul di-ZY-ur)","पुरुषों के आपसी सामाजिक बंधन जिनमें छिपी चाह हो","Eve Kosofsky Sedgwick's term (Between Men, 1985) for the continuum of male bonds, often triangulated through a woman.")
m("Queer Theory","क्वीयर थ्योरी (KWEER THEE-uh-ree)","लैंगिक और यौन पहचानों की तयशुदा श्रेणियों पर सवाल","A theory, so named by Teresa de Lauretis (1990-91), that deconstructs fixed categories of sex, gender and sexuality; key figures Butler and Sedgwick.")
m("Ecocriticism","इकोक्रिटिसिज़्म (EE-koh-KRIT-i-siz-um)","साहित्य और पर्यावरण के रिश्ते का अध्ययन","Term coined by William Rueckert (1978); defined by Cheryll Glotfelty (1996) as 'the study of the relationship between literature and the physical environment'.")
m("Deep Ecology","डीप इकोलॉजी (DEEP ee-KOL-uh-jee)","प्रकृति का अपना मूल्य मानने वाली पर्यावरण सोच","Arne Naess's term (1973) for a biocentric philosophy asserting the intrinsic value of all life, against 'shallow', human-centred environmentalism.")
m("Ecofeminism","इकोफ़ेमिनिज़्म (ee-koh-FEM-i-niz-um)","औरत और प्रकृति के शोषण को जोड़कर देखने वाला नारीवाद","Term coined by Francoise d'Eaubonne (1974) linking the domination of women and of nature; Indian voice Vandana Shiva (Staying Alive, 1988).")
m("Slow Violence","स्लो वायलेंस (SLOH VY-uh-luns)","धीरे-धीरे, बिना दिखे होने वाली पर्यावरणीय तबाही","Rob Nixon's term (2011) for gradual, often invisible environmental harm that falls mostly on the poor.")
m("Hyperobject","हाइपरऑब्जेक्ट (HY-pur-OB-jikt)","इतना बड़ा फैला चीज़ जिसे पूरा देखा न जा सके, जैसे जलवायु परिवर्तन","Timothy Morton's term (Hyperobjects, 2013) for entities massively distributed in time and space, such as global warming.")
m("Hybridity","हाइब्रिडिटी (hy-BRID-i-tee)","दो संस्कृतियों के मिलने से बनी नई मिश्रित पहचान","Homi Bhabha's term (The Location of Culture, 1994) for new transcultural forms produced in the 'Third Space' of colonial encounter.")
m("Mediascape","मीडियास्केप (MEE-dee-uh-skayp)","दुनिया भर में फैले मीडिया चित्रों का जाल","One of Arjun Appadurai's five 'scapes' of global cultural flow (Modernity at Large, 1996), with ethnoscapes, technoscapes, financescapes and ideoscapes.")
m("Remediation","रिमीडिएशन (ree-mee-dee-AY-shun)","एक माध्यम का दूसरे माध्यम को अपने भीतर दोहराना","Bolter and Grusin's term (Remediation, 1999) for the representation of one medium in another, through immediacy and hypermediacy.")
m("Ergodic Literature","अर्गोडिक लिटरेचर (ur-GOD-ik LIT-ruh-chur)","ऐसा पाठ जिसे पढ़ने में पाठक को मेहनत से रास्ता चुनना पड़े","Espen Aarseth's term (Cybertext, 1997) for texts requiring 'non-trivial effort' by the reader to traverse, e.g. hypertext fiction and games.")

Q=[]
def q(qq,opts,a,e): Q.append({"q":qq,"options":opts,"answer":a,"exp":e})
q("Who founded the Centre for Contemporary Cultural Studies at Birmingham in 1964?",["Stuart Hall","Raymond Williams","Richard Hoggart","E. P. Thompson"],2,"Richard Hoggart founded CCCS in 1964 and was its first director.")
q("Arrange in chronological order: (a) The Uses of Literacy (b) The Making of the English Working Class (c) Culture and Society 1780-1950 (d) Keywords",["a, c, b, d","c, a, b, d","a, b, c, d","c, b, a, d"],0,"1957, 1958, 1963, 1976.")
q("'Structure of feeling' is a concept associated with:",["Richard Hoggart","Raymond Williams","Terry Eagleton","Louis Althusser"],1,"Williams developed it in Preface to Film (1954) and The Long Revolution (1961).")
q("Match the List I with List II:\nI. Dominant, residual, emergent  II. Interpellation  III. Aura  IV. Hegemony\n1. Benjamin  2. Gramsci  3. Williams  4. Althusser",["I-3, II-4, III-1, IV-2","I-4, II-3, III-2, IV-1","I-3, II-1, III-4, IV-2","I-2, II-4, III-1, IV-3"],0,"Williams-dominant/residual/emergent; Althusser-interpellation; Benjamin-aura; Gramsci-hegemony.")
q("In Stuart Hall's 'Encoding/Decoding', which is NOT one of the three decoding positions?",["Dominant-hegemonic","Negotiated","Oppositional","Aberrant-hermeneutic"],3,"Hall names dominant-hegemonic, negotiated and oppositional readings.")
q("'The Culture Industry: Enlightenment as Mass Deception' is a chapter of:",["One-Dimensional Man","Minima Moralia","Dialectic of Enlightenment","The Society of the Spectacle"],2,"It appears in Adorno and Horkheimer's Dialectic of Enlightenment (1947).")
q("Assertion (A): Benjamin argues that mechanical reproduction withers the aura of a work of art.\nReason (R): Reproduction substitutes a plurality of copies for a unique existence.",["Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true"],0,"Benjamin explicitly links loss of aura to replacing unique existence with mass copies.")
q("Who said 'There is no document of civilization which is not at the same time a document of barbarism'?",["Theodor Adorno","Walter Benjamin","Herbert Marcuse","Antonio Gramsci"],1,"From Benjamin's 'Theses on the Philosophy of History' (1940).")
q("According to Althusser, the dominant Ideological State Apparatus in mature capitalist societies is the:",["Religious ISA","Family ISA","Educational ISA","Communications ISA"],2,"Althusser says the school replaced the Church as the dominant ISA.")
q("Which of the following belongs to the Repressive State Apparatus in Althusser's scheme?",["The family","The trade unions","The courts and prisons","The press"],2,"The RSA includes government, army, police, courts and prisons.")
q("'Ideology represents the imaginary relationship of individuals to their real conditions of existence.' This definition is given by:",["Karl Marx","Louis Althusser","Antonio Gramsci","Pierre Macherey"],1,"From Althusser's 'Ideology and Ideological State Apparatuses' (1970).")
q("Gramsci's distinction between 'war of position' and 'war of manoeuvre' appears in:",["Prison Notebooks","For Marx","The German Ideology","History and Class Consciousness"],0,"These concepts belong to Gramsci's Prison Notebooks (1929-35).")
q("In Barthes's 'Myth Today', the photograph of a young Black soldier saluting the French flag appears on the cover of:",["Le Monde","Paris-Match","Elle","Les Temps Modernes"],1,"Barthes's famous example is the Paris-Match cover.")
q("Which essay is NOT part of Barthes's Mythologies?",["The World of Wrestling","Wine and Milk","The Death of the Author","The Face of Garbo"],2,"'The Death of the Author' is a separate essay of 1967.")
q("Barthes describes myth as:",["A first-order linguistic system","A second-order semiological system","A purely denotative sign","An archetypal pattern of the collective unconscious"],1,"In 'Myth Today' myth is a second-order semiological system.")
q("Baudrillard's essays claiming that a certain war 'did not take place' concern:",["The Vietnam War","The Falklands War","The Gulf War","The Second World War"],2,"The Gulf War Did Not Take Place (1991).")
q("Arrange Baudrillard's phases of the image in correct order:\n(a) It masks the absence of a basic reality (b) It is the reflection of a basic reality (c) It bears no relation to any reality (d) It masks and perverts a basic reality",["b, d, a, c","b, a, d, c","d, b, a, c","a, b, d, c"],0,"Reflection, perversion, masking absence, pure simulacrum.")
q("'Taste classifies, and it classifies the classifier' is from:",["Bourdieu's Distinction","Fiske's Understanding Popular Culture","Williams's Keywords","Hebdige's Subculture"],0,"Bourdieu, Distinction (1979).")
q("Which is NOT one of the three states of cultural capital in Bourdieu?",["Embodied","Objectified","Institutionalised","Commodified"],3,"Bourdieu lists embodied, objectified and institutionalised states.")
q("The concept of 'semiotic democracy' is associated with:",["John Fiske","Dwight Macdonald","F. R. Leavis","Jurgen Habermas"],0,"Fiske, Television Culture (1987).")
q("Match the authors with their works:\nI. Dick Hebdige  II. Stanley Cohen  III. Paul Willis  IV. Janice Radway\n1. Learning to Labour  2. Reading the Romance  3. Subculture: The Meaning of Style  4. Folk Devils and Moral Panics",["I-3, II-4, III-1, IV-2","I-4, II-3, III-2, IV-1","I-3, II-1, III-4, IV-2","I-1, II-4, III-3, IV-2"],0,"Hebdige 1979, Cohen 1972, Willis 1977, Radway 1984.")
q("Hebdige borrowed the term 'bricolage' from:",["Roland Barthes","Claude Levi-Strauss","Jacques Derrida","Umberto Eco"],1,"Levi-Strauss used it in The Savage Mind (1962).")
q("The first volume of Subaltern Studies was published in 1982 under the editorship of:",["Partha Chatterjee","Dipesh Chakrabarty","Ranajit Guha","Gayatri Spivak"],2,"Ranajit Guha founded and edited the series.")
q("'White men are saving brown women from brown men' is a sentence analysed in:",["Orientalism","Can the Subaltern Speak?","The Location of Culture","Provincializing Europe"],1,"Spivak uses it to discuss the British abolition of sati.")
q("Who coined the term 'ecocriticism'?",["Cheryll Glotfelty","Lawrence Buell","William Rueckert","Jonathan Bate"],2,"Rueckert, 'Literature and Ecology: An Experiment in Ecocriticism' (1978).")
q("Assertion (A): Laura Mulvey argues that classical Hollywood cinema is structured by a male gaze.\nReason (R): In it, woman is displayed as spectacle, connoting 'to-be-looked-at-ness'.",["Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true"],0,"Mulvey's 1975 essay links the male gaze to woman as passive spectacle.")
q("Gender as 'performative' is a key idea in:",["Sedgwick's Between Men","Butler's Gender Trouble","Rich's 'Compulsory Heterosexuality'","Foucault's The History of Sexuality"],1,"Butler, Gender Trouble (1990).")
q("Which is NOT one of Arjun Appadurai's five 'scapes'?",["Ethnoscapes","Ideoscapes","Financescapes","Landscapes"],3,"The five are ethnoscapes, mediascapes, technoscapes, financescapes and ideoscapes.")
q("'The medium is the message' was said by:",["Jean Baudrillard","Marshall McLuhan","Guy Debord","Raymond Williams"],1,"McLuhan, Understanding Media (1964).")
q("Arrange chronologically: (a) Dialectic of Enlightenment (b) Mythologies (c) Simulacra and Simulation (d) Distinction",["a, b, d, c","b, a, d, c","a, b, c, d","a, d, b, c"],0,"1947, 1957, 1979, 1981.")

d={"id":7,"title":"Cultural Studies",
 "overview":"Is unit me Birmingham CCCS (Hoggart, Williams, Hall, Thompson), Frankfurt School, Benjamin, Gramsci, Althusser, Barthes, Baudrillard, Bourdieu, Fiske se lekar subaltern, gender-queer, ecocriticism, digital aur Indian cultural studies tak sab aata hai. NET mostly author-work matching, coined terms, famous quotes, chronology aur assertion-reason pooch ta hai.",
 "topics":T,"terms":TM,"mcqs":Q}
p="/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/unit7.json"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(T),len(TM),len(Q),[len(x["points"]) for x in T])
