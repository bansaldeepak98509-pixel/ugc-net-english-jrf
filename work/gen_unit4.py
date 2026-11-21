import json

T = []
def topic(title, *points): T.append({"title": title, "points": list(points)})

topic("The Essay: Origins and Francis Bacon",
 "Michel de Montaigne's Essais (1580) gave the form its name: 'essai' = attempt, trial (koshish). Montaigne: 'I am myself the matter of my book.'",
 "Francis Bacon (1561-1626) is called the father of the English essay; his essays are aphoristic, impersonal and didactic, unlike Montaigne's personal ones.",
 "Bacon's Essays: 1597 (10 essays), 1612 (38 essays), 1625 (58 essays, titled Essays or Counsels, Civil and Moral).",
 "Of Studies: 'Some books are to be tasted, others to be swallowed, and some few to be chewed and digested.' Also: 'Reading maketh a full man; conference a ready man; and writing an exact man.'",
 "Of Truth (opening essay of 1625): 'What is truth? said jesting Pilate, and would not stay for an answer.'",
 "Of Marriage and Single Life: 'He that hath wife and children hath given hostages to fortune.' Of Revenge: 'Revenge is a kind of wild justice.'",
 "Of Adversity: 'Prosperity is the blessing of the Old Testament; adversity is the blessing of the New.' Of Gardens: 'God Almighty first planted a garden.'",
 "Other Bacon prose: The Advancement of Learning (1605), Novum Organum (1620, Latin), History of the Reign of King Henry VII (1622), New Atlantis (1627, posthumous utopia; Salomon's House).",
 "In Novum Organum Bacon names four Idols (false notions): Idols of the Tribe, the Cave, the Market-place and the Theatre.",
 "Bacon's style is Senecan/curt (short, pointed sentences), opposed to the long Ciceronian period.")

topic("Seventeenth-Century Prose: Browne, Burton, Walton and Others",
 "Sir Thomas Browne (1605-1682), a Norwich physician: Religio Medici (pirated 1642, authorised 1643) - 'the religion of a doctor'.",
 "Browne's Pseudodoxia Epidemica (1646), also called Vulgar Errors, examines popular false beliefs.",
 "Browne's Hydriotaphia, Urn-Burial and The Garden of Cyrus appeared together in 1658; Christian Morals was posthumous (1716). His style is ornate, Latinate, baroque.",
 "Hydriotaphia: 'Man is a noble animal, splendid in ashes, and pompous in the grave.'",
 "Robert Burton, The Anatomy of Melancholy (1621), written under the pseudonym Democritus Junior.",
 "Izaak Walton, The Compleat Angler (1653), a dialogue on fishing (Piscator, Venator, Auceps); also Lives of Donne, Wotton, Hooker, Herbert and Sanderson.",
 "Thomas Hobbes, Leviathan (1651): life in the state of nature is 'solitary, poor, nasty, brutish, and short'.",
 "Jeremy Taylor, Holy Living (1650) and Holy Dying (1651); Thomas Fuller, The History of the Worthies of England (1662).",
 "Character writing (Theophrastan): Joseph Hall, Characters of Vertues and Vices (1608); Sir Thomas Overbury, Characters (1614); John Earle, Micro-cosmographie (1628).",
 "Bunyan's Grace Abounding to the Chief of Sinners (1666) is a spiritual autobiography; Pepys's Diary covers 1660-1669 (deciphered and published 1825).")

topic("Milton's Prose",
 "Milton called his prose the work of his 'left hand' (in The Reason of Church-Government, 1642, where he also announces his epic ambition).",
 "Anti-prelatical tracts: Of Reformation (1641), The Reason of Church-Government Urged against Prelaty (1642).",
 "Divorce tracts: The Doctrine and Discipline of Divorce (1643), Tetrachordon and Colasterion (1645).",
 "Of Education (1644), addressed to Samuel Hartlib.",
 "Areopagitica (November 1644): 'A Speech of Mr. John Milton for the Liberty of Unlicenc'd Printing, to the Parliament of England', against the Licensing Order of 1643; title from Isocrates' Areopagiticus.",
 "Areopagitica quote: 'Who kills a man kills a reasonable creature, God's image; but he who destroys a good book, kills reason itself.'",
 "Areopagitica quote: 'I cannot praise a fugitive and cloistered virtue, unexercised and unbreathed.'",
 "The Tenure of Kings and Magistrates (1649) defends the right to depose a tyrant; Eikonoklastes (1649) answers Eikon Basilike.",
 "Defensio pro Populo Anglicano (1651, Latin, against Salmasius) and Defensio Secunda (1654); The Ready and Easy Way to Establish a Free Commonwealth (1660).",
 "De Doctrina Christiana (Latin theological treatise) was discovered in 1823 and published in 1825.")

topic("The Periodical Essay: Addison and Steele",
 "Daniel Defoe's Review (1704-1713) is an early periodical; the periodical essay flowered in the Queen Anne (Augustan) age.",
 "The Tatler was started by Richard Steele on 12 April 1709 (ran till January 1711) under the persona Isaac Bickerstaff, a name borrowed from Swift.",
 "The Spectator (1 March 1711 - 6 December 1712, 555 numbers) by Joseph Addison and Steele; Addison revived it in 1714 (Nos. 556-635).",
 "The Spectator Club: Mr. Spectator (silent narrator), Sir Roger de Coverley (Tory country squire), Sir Andrew Freeport (Whig merchant), Captain Sentry, Will Honeycomb (ageing beau), the Templar and the Clergyman.",
 "Spectator No. 10 (Addison): aim 'to have brought philosophy out of closets and libraries, schools and colleges, to dwell in clubs and assemblies, at tea-tables and in coffee-houses.'",
 "Addison's 'Pleasures of the Imagination' series (Spectator Nos. 411-421, 1712) and his Saturday papers on Paradise Lost.",
 "Sir Roger de Coverley was created by Steele (Spectator No. 2) but developed mainly by Addison; Addison 'killed' him (No. 517).",
 "The Guardian (1713) followed; Addison wrote the tragedy Cato (1713), Steele the sentimental comedy The Conscious Lovers (1722).",
 "Johnson on Addison: 'Whoever wishes to attain an English style, familiar but not coarse, and elegant but not ostentatious, must give his days and nights to the volumes of Addison.'",
 "Swift wrote for The Examiner (Tory, 1710-11); Goldsmith's The Citizen of the World (1762, as book) presents Lien Chi Altangi, a Chinese philosopher in London.")

topic("Samuel Johnson and Boswell",
 "Johnson's periodicals: The Rambler (1750-1752, 208 numbers, almost all by Johnson), contributions to The Adventurer, and The Idler (1758-1760, in the Universal Chronicle).",
 "A Dictionary of the English Language (1755); the Letter to Lord Chesterfield (1755) rebukes a late patron: 'Is not a patron, my Lord, one who looks with unconcern on a man struggling for life in the water...'",
 "Life of Mr Richard Savage (1744); Rasselas, Prince of Abyssinia (1759), written to pay for his mother's funeral.",
 "Preface to Shakespeare (1765): Shakespeare is 'the poet of nature' who holds up 'a faithful mirrour of manners and of life'; defends mixing tragedy and comedy and rejects unities of time and place.",
 "A Journey to the Western Islands of Scotland (1775), from the 1773 tour with Boswell.",
 "Lives of the Poets (1779-1781): 52 lives; the term 'metaphysical poets' is fixed in the Life of Cowley ('heterogeneous ideas are yoked by violence together').",
 "Johnson: 'Language is the dress of thought'; 'Patriotism is the last refuge of a scoundrel' (reported by Boswell).",
 "James Boswell, The Life of Samuel Johnson, LL.D. (1791), often called the greatest English biography; The Journal of a Tour to the Hebrides (1785).",
 "The Club (Literary Club, 1764) included Johnson, Reynolds, Burke, Goldsmith, Garrick and later Boswell.",
 "'Johnsonese' = heavy, Latinate, balanced periodic style.")

topic("Charles Lamb (Elia)",
 "Charles Lamb (1775-1834), clerk at the East India House; the Elia essays appeared in the London Magazine from 1820.",
 "Essays of Elia (1823) and The Last Essays of Elia (1833). 'Elia' was the name of an Italian clerk at the South-Sea House.",
 "First Elia essay: 'The South-Sea House' (1820).",
 "'Dream-Children: A Reverie': Elia tells his imagined children Alice and John about grandmother Field and uncle John L.; ends 'We are not of Alice, nor of thee, nor are we children at all.'",
 "'A Dissertation upon Roast Pig': Ho-ti and his son Bo-bo in China discover roast pork by burning down a house (story from a Chinese manuscript, attributed to his friend Manning).",
 "Other Essays of Elia: 'Christ's Hospital Five and Thirty Years Ago', 'The Two Races of Men' (borrowers and lenders), 'Mrs. Battle's Opinions on Whist', 'Imperfect Sympathies', 'Mackery End, in Hertfordshire', 'New Year's Eve', 'The Praise of Chimney-Sweepers', 'A Chapter on Ears', 'Oxford in the Vacation', 'Witches and Other Night-Fears'.",
 "Last Essays of Elia: 'Old China', 'The Superannuated Man', 'Poor Relations', 'Detached Thoughts on Books and Reading', 'Sanity of True Genius'.",
 "Bridget Elia in the essays is his sister Mary Lamb; Tales from Shakespeare (1807) was written with Mary.",
 "Specimens of English Dramatic Poets (1808); 'On the Tragedies of Shakespeare' (1811) argues that King Lear cannot be acted on the stage.",
 "Lamb is the master of the familiar/personal essay: whimsical, nostalgic, archaic in diction (Browne and Burton are his models).")

topic("William Hazlitt and Leigh Hunt",
 "Hazlitt (1778-1830): An Essay on the Principles of Human Action (1805).",
 "The Round Table (1817, with Leigh Hunt) includes 'On Gusto'.",
 "Characters of Shakespear's Plays (1817); Lectures on the English Poets (1818); Lectures on the English Comic Writers (1819).",
 "Table-Talk (1821-22): 'On Going a Journey' ('One of the pleasantest things in the world is going a journey; but I like to go by myself'), 'On Familiar Style', 'On the Pleasure of Painting'.",
 "The Spirit of the Age (1825): portraits of contemporaries such as Bentham, Godwin, Coleridge, Wordsworth, Scott, Byron, Jeffrey, Lamb.",
 "The Plain Speaker (1826) includes 'On the Prose Style of Poets'; Liber Amoris (1823) records his passion for Sarah Walker.",
 "'My First Acquaintance with Poets' (1823, in The Liberal) recalls meeting Coleridge in 1798.",
 "Other essays: 'The Fight', 'On the Feeling of Immortality in Youth', 'On the Pleasure of Hating'; also The Life of Napoleon Buonaparte (1828-30).",
 "Leigh Hunt edited The Examiner (from 1808; jailed 1813-15 for libelling the Prince Regent); his Autobiography appeared in 1850. Blackwood's attacked Hunt, Keats and Hazlitt as the 'Cockney School'.")

topic("Thomas De Quincey",
 "Confessions of an English Opium-Eater: London Magazine 1821, book 1822, enlarged revision 1856.",
 "Sections: preliminary confessions (runaway youth, Ann of Oxford Street), 'The Pleasures of Opium', 'The Pains of Opium'.",
 "'On the Knocking at the Gate in Macbeth' (1823, London Magazine): the knocking marks the return of the human world after the murder.",
 "'On Murder Considered as One of the Fine Arts' (1827, Blackwood's; later postscripts).",
 "Suspiria de Profundis (1845, Blackwood's) includes 'Levana and Our Ladies of Sorrow': Mater Lachrymarum (Our Lady of Tears), Mater Suspiriorum (Our Lady of Sighs), Mater Tenebrarum (Our Lady of Darkness).",
 "The English Mail-Coach (1849) includes 'The Vision of Sudden Death' and 'Dream-Fugue'.",
 "Distinction between 'literature of knowledge' (to teach) and 'literature of power' (to move): in 'Letters to a Young Man' (1823) and the essay on Pope (1848).",
 "Recollections of the Lakes and the Lake Poets (Tait's Magazine, 1834-40) on Wordsworth, Coleridge and Southey.",
 "De Quincey's style is called 'impassioned prose' (prose-poetry with musical, ornate rhythms).")

topic("Thomas Carlyle",
 "Thomas Carlyle (1795-1881), Scottish 'Sage of Chelsea'.",
 "'Signs of the Times' (1829, Edinburgh Review) calls the age 'the Mechanical Age'; 'Characteristics' (1831).",
 "Sartor Resartus ('The Tailor Re-tailored'): Fraser's Magazine 1833-34, book USA 1836, UK 1838. Hero: Professor Diogenes Teufelsdrockh of Weissnichtwo, 'Professor of Things in General'; philosophy of clothes.",
 "Sartor's spiritual stages: 'The Everlasting No', 'Centre of Indifference', 'The Everlasting Yea'.",
 "The French Revolution: A History (1837); the first manuscript of vol. I was burnt by J. S. Mill's housemaid and rewritten.",
 "On Heroes, Hero-Worship and the Heroic in History (lectures 1840, book 1841): Hero as Divinity (Odin), Prophet (Mahomet), Poet (Dante, Shakespeare), Priest (Luther, Knox), Man of Letters (Johnson, Rousseau, Burns), King (Cromwell, Napoleon).",
 "'The history of the world is but the biography of great men' (On Heroes).",
 "Chartism (1839) raised the 'Condition-of-England question'; Past and Present (1843) contrasts Abbot Samson of medieval Bury St Edmunds with modern 'cash nexus' society.",
 "Latter-Day Pamphlets (1850); History of Frederick the Great (1858-65); he called economics 'the dismal science' (1849).",
 "'Carlylese': Germanic, capitalised, exclamatory, prophetic style; strongly influenced by Goethe and German idealism.")

topic("John Ruskin",
 "Modern Painters (5 vols, 1843-1860) began as a defence of J. M. W. Turner.",
 "'Pathetic fallacy' coined in Modern Painters vol. III (1856), chapter 'Of the Pathetic Fallacy'.",
 "The Seven Lamps of Architecture (1849): Sacrifice, Truth, Power, Beauty, Life, Memory, Obedience.",
 "The Stones of Venice (1851-53) contains the chapter 'The Nature of Gothic', reprinted by William Morris's Kelmscott Press (1892).",
 "Unto This Last (four essays in the Cornhill Magazine 1860, book 1862) attacks classical political economy; title from the parable of the labourers in the vineyard (Matthew 20). Key line: 'There is no wealth but life.'",
 "Gandhi read Unto This Last in 1904 and paraphrased it in Gujarati as Sarvodaya (1908).",
 "Sesame and Lilies (1865): 'Of Kings' Treasuries' (on reading) and 'Of Queens' Gardens' (on women's role); The Crown of Wild Olive (1866); Munera Pulveris (1862-63, book 1872).",
 "Fors Clavigera (1871-84): monthly letters 'to the workmen and labourers of Great Britain'; founded the Guild of St George.",
 "First Slade Professor of Fine Art at Oxford (1869); Whistler sued him for libel in 1878 over the phrase 'flinging a pot of paint in the public's face'.",
 "Praeterita (1885-89) is his unfinished autobiography.")

topic("Matthew Arnold's Prose Criticism",
 "Preface to Poems (1853) explains dropping Empedocles on Etna; On Translating Homer (1861): Homer is rapid, plain in thought and style, and noble.",
 "'The Function of Criticism at the Present Time' (1864): criticism is 'a disinterested endeavour to learn and propagate the best that is known and thought in the world.'",
 "Essays in Criticism, First Series (1865); Second Series (1888, posthumous) includes 'The Study of Poetry', 'Wordsworth', 'Byron', 'Shelley', 'Keats'.",
 "'The Study of Poetry' (1880): poetry is 'a criticism of life'; touchstone method; Chaucer lacks 'high seriousness'; Dryden and Pope are 'classics of our prose'.",
 "In 'Shelley' Arnold calls him 'a beautiful and ineffectual angel, beating in the void his luminous wings in vain'.",
 "Culture and Anarchy (1869): culture is 'the study of perfection'; 'sweetness and light' (phrase from Swift's The Battle of the Books).",
 "Culture and Anarchy divides society into Barbarians (aristocracy), Philistines (middle class) and Populace (working class); contrasts Hebraism (strictness of conscience) and Hellenism (spontaneity of consciousness).",
 "Other prose: On the Study of Celtic Literature (1867), Friendship's Garland (1871), Literature and Dogma (1873).",
 "Arnold was Oxford Professor of Poetry (1857-67) and an Inspector of Schools for 35 years.")

topic("Walter Pater, Aestheticism and Wilde",
 "Pater's Studies in the History of the Renaissance (1873), retitled The Renaissance: Studies in Art and Poetry (1877).",
 "Conclusion: 'To burn always with this hard, gem-like flame, to maintain this ecstasy, is success in life.' It was dropped from the 2nd edition (1877) and restored in 1888.",
 "'All art constantly aspires towards the condition of music' - from 'The School of Giorgione' (added 1877).",
 "The Leonardo essay's Mona Lisa passage: 'She is older than the rocks among which she sits'; Yeats printed it as free verse in the Oxford Book of Modern Verse (1936).",
 "Marius the Epicurean (1885); Imaginary Portraits (1887); Appreciations, with an Essay on Style (1889); Plato and Platonism (1893).",
 "Aestheticism slogan 'art for art's sake' (l'art pour l'art) goes back to Gautier's preface to Mademoiselle de Maupin (1835).",
 "Oscar Wilde's Intentions (1891): 'The Decay of Lying' ('Life imitates Art far more than Art imitates Life') and 'The Critic as Artist'; also 'The Soul of Man under Socialism' (1891) and De Profundis (1905, letter written in Reading Gaol).",
 "The Yellow Book (1894-97) was the quarterly of the Decadents, art editor Aubrey Beardsley.")

topic("Newman, Mill, Macaulay and Victorian Thought",
 "John Henry Newman led the Oxford (Tractarian) Movement through Tracts for the Times (1833-41); Keble's Assize Sermon (14 July 1833) began it; Tract 90 (1841) caused a storm.",
 "Newman converted to Roman Catholicism in 1845 and became a Cardinal in 1879; canonised in 2019.",
 "The Idea of a University (discourses 1852, final form 1873): knowledge is its own end; 'It is almost a definition of a gentleman to say he is one who never inflicts pain.'",
 "Apologia Pro Vita Sua (1864), a spiritual autobiography written in reply to Charles Kingsley's attack.",
 "Newman also wrote The Dream of Gerontius (1865), An Essay in Aid of a Grammar of Assent (1870) and the hymn 'Lead, Kindly Light' (1833).",
 "J. S. Mill: 'What is Poetry?' (1833: eloquence is heard, poetry is overheard), On Liberty (1859), Utilitarianism (1861), The Subjection of Women (1869), Autobiography (1873).",
 "T. B. Macaulay: essay on Milton (1825, Edinburgh Review); Minute on Indian Education (1835): 'a single shelf of a good European library was worth the whole native literature of India and Arabia'; History of England (1848-61).",
 "T. H. Huxley ('Darwin's bulldog'): 'Science and Culture' (1880) debated Arnold's 'Literature and Science' (1882).",
 "R. L. Stevenson's essays Virginibus Puerisque (1881): 'An Apology for Idlers', 'El Dorado' ('to travel hopefully is a better thing than to arrive').")

topic("Virginia Woolf as Essayist",
 "The Common Reader (1925) and The Common Reader: Second Series (1932); title from Johnson's Life of Gray ('I rejoice to concur with the common reader').",
 "'Modern Fiction' (1919 as 'Modern Novels', revised 1925): 'Life is not a series of gig lamps symmetrically arranged; life is a luminous halo'; attacks Bennett, Wells, Galsworthy as 'materialists'.",
 "'Mr. Bennett and Mrs. Brown' (1924): 'On or about December 1910 human character changed'; Edwardians vs Georgians.",
 "A Room of One's Own (1929), from 1928 lectures at Newnham and Girton, Cambridge: 'a woman must have money and a room of her own if she is to write fiction.'",
 "A Room of One's Own: Shakespeare's imagined sister Judith Shakespeare; narrator 'call me Mary Beton, Mary Seton, Mary Carmichael'; Oxbridge and Fernham; the androgynous mind (from Coleridge).",
 "'Professions for Women' (1931 speech): killing 'the Angel in the House' (phrase from Coventry Patmore's poem).",
 "Three Guineas (1938) links patriarchy and war; The Death of the Moth and Other Essays (1942, posthumous).",
 "'The New Biography' (1927): biography should join truth ('granite') and personality ('rainbow'). Biographical works: Orlando: A Biography (1928), Flush (1933), Roger Fry (1940).",
 "Moments of Being (1976, posthumous) contains 'A Sketch of the Past'; Woolf and Leonard founded the Hogarth Press (1917); member of the Bloomsbury Group.")

topic("George Orwell's Essays and Reportage",
 "Orwell = Eric Arthur Blair, born 1903 at Motihari, Bihar; served in the Indian Imperial Police in Burma (1922-27).",
 "'A Hanging' (1931, The Adelphi) and 'Shooting an Elephant' (1936, New Writing) are set in Burma and expose imperialism.",
 "Documentary books: Down and Out in Paris and London (1933), The Road to Wigan Pier (1937), Homage to Catalonia (1938, Spanish Civil War, POUM militia).",
 "'Politics and the English Language' (1946, Horizon): six rules, e.g. 'Never use a long word where a short one will do'; 'If it is possible to cut a word out, always cut it out'; political language makes 'lies sound truthful and murder respectable'.",
 "'Why I Write' (1946): four motives - sheer egoism, aesthetic enthusiasm, historical impulse, political purpose; 'Good prose is like a window pane.'",
 "'Reflections on Gandhi' (1949): 'Saints should always be judged guilty until they are proved innocent.'",
 "Other essays: 'Marrakech' (1939), 'Inside the Whale' (1940), 'Boys' Weeklies' (1940), 'The Lion and the Unicorn' (1941), 'Notes on Nationalism' (1945), 'The Prevention of Literature' (1946), 'Decline of the English Murder' (1946), 'Such, Such Were the Joys' (posthumous 1952).",
 "He wrote the column 'As I Please' for Tribune (1943-47).")

topic("Bertrand Russell and Other Twentieth-Century Essayists",
 "Bertrand Russell won the Nobel Prize in Literature in 1950.",
 "Russell's works: Principia Mathematica (with Whitehead, 1910-13), The Problems of Philosophy (1912), Mysticism and Logic (1918, includes 'A Free Man's Worship', 1903).",
 "Why I Am Not a Christian (lecture 1927), Marriage and Morals (1929), The Conquest of Happiness (1930), In Praise of Idleness (1935), A History of Western Philosophy (1945), Unpopular Essays (1950), Portraits from Memory (1956, includes 'Knowledge and Wisdom').",
 "Prologue to Russell's Autobiography (1967-69), 'What I Have Lived For': 'Three passions, simple but overwhelmingly strong... the longing for love, the search for knowledge, and unbearable pity for the suffering of mankind.'",
 "G. K. Chesterton: Heretics (1905), Orthodoxy (1908), The Victorian Age in Literature (1913); master of paradox. Hilaire Belloc: On Nothing (1908).",
 "A. G. Gardiner wrote as 'Alpha of the Plough' (Pebbles on the Shore, 1916, includes 'On Saying Please'); Robert Lynd wrote as 'Y.Y.'.",
 "E. M. Forster: 'What I Believe' (1938: 'if I had to choose between betraying my country and betraying my friend, I hope I should have the guts to betray my country'), Two Cheers for Democracy (1951).",
 "Other modern essayists: Max Beerbohm, E. V. Lucas, J. B. Priestley, Aldous Huxley; Lytton Strachey's Eminent Victorians (1918) on Manning, Florence Nightingale, Dr Arnold and General Gordon.")

topic("Indian Non-Fiction: Gandhi, Nehru and Ambedkar",
 "Gandhi's Hind Swaraj (1909) was written in Gujarati aboard the Kildonan Castle (London to South Africa); English translation 1910; a dialogue between Reader and Editor attacking modern civilisation.",
 "The Story of My Experiments with Truth: Gujarati 'Satyana Prayogo', serialised in Navajivan 1925-29; English translation by Mahadev Desai; in five parts.",
 "Gandhi's other works: Satyagraha in South Africa (1928), Constructive Programme (1941); journals Indian Opinion (1903), Young India, Navajivan, Harijan (1933). Influences: Ruskin, Tolstoy (The Kingdom of God Is Within You), Thoreau.",
 "Nehru: Letters from a Father to His Daughter (1929), Glimpses of World History (1934, prison letters to Indira 1930-33), An Autobiography (1936; US title Toward Freedom), The Discovery of India (1946, written in Ahmednagar Fort prison 1944).",
 "Nehru's 'Tryst with Destiny' speech: midnight 14-15 August 1947, Constituent Assembly.",
 "Ambedkar: Castes in India: Their Mechanism, Genesis and Development (Columbia seminar paper 1916, published 1917).",
 "Annihilation of Caste (1936): an undelivered address for the Jat-Pat-Todak Mandal of Lahore, published by Ambedkar; Gandhi replied in Harijan and Ambedkar answered in later editions.",
 "Other Ambedkar works: The Problem of the Rupee (1923), Pakistan or the Partition of India (1945), Who Were the Shudras? (1946), The Untouchables (1948), Thoughts on Linguistic States (1955), The Buddha and His Dhamma (1957, posthumous), Waiting for a Visa (autobiographical notes, c. 1935-36).",
 "Ambedkar's journals: Mooknayak (1920), Bahishkrit Bharat (1927), Janata, Prabuddha Bharat.")

topic("Indian Non-Fiction: Tagore, Sen and Other Voices",
 "Tagore's English prose: Sadhana (1913), Nationalism (1917, lectures in Japan and the USA, critical of the Western nation-state), Personality (1917), Creative Unity (1922), The Religion of Man (1931, Hibbert Lectures at Oxford 1930).",
 "Tagore's last essay Crisis in Civilization (1941, read on his 80th birthday); My Reminiscences (Jiban Smriti, English 1917); Letters from Russia (1931).",
 "Amartya Sen (Nobel in Economics, 1998): Poverty and Famines (1981), Development as Freedom (1999), The Argumentative Indian (2005), Identity and Violence: The Illusion of Destiny (2006), The Idea of Justice (2009; niti vs nyaya), An Uncertain Glory (2013, with Jean Dreze), Home in the World (2021, memoir).",
 "Nirad C. Chaudhuri: The Autobiography of an Unknown Indian (1951), dedicated to the memory of the British Empire; sequel Thy Hand, Great Anarch! (1987).",
 "Sake Dean Mahomet's The Travels of Dean Mahomet (1794) is the first book in English by an Indian.",
 "Sri Aurobindo: The Renaissance in India and The Foundations of Indian Culture; Swami Vivekananda's Chicago address (1893).",
 "V. S. Naipaul's India trilogy: An Area of Darkness (1964), India: A Wounded Civilization (1977), India: A Million Mutinies Now (1990).",
 "Other Indian life-writing: Kamala Das, My Story (1976); A. P. J. Abdul Kalam, Wings of Fire (1999); Vikram Seth, From Heaven Lake (1983, travel); Amitav Ghosh, In an Antique Land (1992).",
 "Dalit autobiographies: Daya Pawar, Baluta (Marathi 1978); Sharankumar Limbale, Akkarmashi (1984, tr. The Outcaste); Bama, Karukku (Tamil 1992); Omprakash Valmiki, Joothan (Hindi 1997).")

topic("Biography, Autobiography and Diary",
 "Early English biography: William Roper's Life of Sir Thomas More, George Cavendish's Life of Wolsey; Walton's Lives (1640-78).",
 "Johnson's Lives of the Poets (1779-81) and Boswell's Life of Johnson (1791) set the model of critical and intimate biography.",
 "Nineteenth-century biographies: Southey's Life of Nelson (1813), Lockhart's Life of Scott (1837-38), Elizabeth Gaskell's The Life of Charlotte Bronte (1857), John Forster's Life of Charles Dickens (1872-74).",
 "Lytton Strachey's Eminent Victorians (1918) and Queen Victoria (1921) began the ironic 'new biography'.",
 "Spiritual autobiography: Augustine's Confessions (c. 400), Bunyan's Grace Abounding (1666); Rousseau's Confessions (1782-89) is the model of secular confession.",
 "English autobiographies: Gibbon's Memoirs (1796), Mill's Autobiography (1873), Newman's Apologia (1864), Ruskin's Praeterita, Edmund Gosse's Father and Son (1907).",
 "The word 'autobiography' entered English around 1797-1809 (Southey used it in 1809).",
 "Diaries: Samuel Pepys (1660-69, in shorthand, published 1825), John Evelyn (published 1818), Fanny Burney.",
 "Hagiography = saints' lives; memoir focuses on events and others, autobiography on the self's whole life.")

topic("Travel Writing",
 "The Travels of Sir John Mandeville (c. 1357), largely fictional; Hakluyt's The Principal Navigations (1589, enlarged 1598-1600); Purchas his Pilgrimes (1625).",
 "Thomas Coryat, Coryat's Crudities (1611); he later walked to India and died at Surat (1617).",
 "Defoe's A Tour thro' the Whole Island of Great Britain (1724-27); Smollett's Travels through France and Italy (1766), mocked by Sterne as 'Smelfungus'.",
 "Sterne's A Sentimental Journey through France and Italy (1768), narrator Yorick.",
 "Lady Mary Wortley Montagu's Turkish Embassy Letters (1763); Mary Wollstonecraft's Letters Written during a Short Residence in Sweden, Norway, and Denmark (1796).",
 "Victorian travel: A. W. Kinglake's Eothen (1844); Richard Burton's Pilgrimage to Al-Madinah and Meccah (1855-56); C. M. Doughty's Travels in Arabia Deserta (1888); R. L. Stevenson's Travels with a Donkey in the Cevennes (1879).",
 "Modern travel: D. H. Lawrence's Sea and Sardinia (1921), Robert Byron's The Road to Oxiana (1937), Graham Greene's The Lawless Roads (1939), Paul Theroux's The Great Railway Bazaar (1975), Bruce Chatwin's In Patagonia (1977).")

topic("Periodicals and Reviews",
 "The Gentleman's Magazine (1731, Edward Cave) first used the word 'magazine'; Johnson wrote parliamentary reports for it.",
 "The Edinburgh Review (1802; Francis Jeffrey, Sydney Smith, Henry Brougham), Whig; Jeffrey's review of The Excursion began 'This will never do.'",
 "The Quarterly Review (1809, William Gifford), Tory; J. W. Croker's harsh review of Keats's Endymion (1818).",
 "Blackwood's Edinburgh Magazine (1817); J. G. Lockhart as 'Z' attacked the 'Cockney School of Poetry'. The London Magazine (1820, John Scott) published Lamb, Hazlitt and De Quincey.",
 "The Westminster Review (1824), founded by Bentham for the Philosophical Radicals; Fraser's Magazine (1830) serialised Sartor Resartus.",
 "Dickens's Household Words (1850) and All the Year Round (1859); Punch (1841); The Cornhill Magazine (1860, first editor Thackeray) serialised Unto This Last; The Fortnightly Review (1865).",
 "Twentieth century: The Egoist (1914), T. S. Eliot's The Criterion (1922-39), F. R. Leavis's Scrutiny (1932-53), Cyril Connolly's Horizon (1940-49).")

terms = [
 ("Essay","एस्से (ES-ay)","किसी एक विषय पर छोटा गद्य लेख, लेखक के विचारों के साथ","A short prose composition on a single subject, from French essai ('attempt'), named by Montaigne's Essais (1580) and introduced into English by Bacon (1597)."),
 ("Aphorism","ऐफ़-अ-रिज़्म (AF-uh-riz-um)","छोटी, चुभती हुई सूक्ति जिसमें गहरी बात हो","A concise, pointed statement of a general truth or principle; Bacon's Essays are celebrated for aphoristic sentences."),
 ("Familiar Essay","फ़-मिल-यर एस्से (fuh-MIL-yer ES-ay)","हल्का-फुल्का, बातचीत जैसा निजी निबंध","An informal, personal, conversational essay revealing the writer's personality and moods; perfected by Lamb, Hazlitt and Leigh Hunt."),
 ("Periodical Essay","पी-रि-ऑ-डि-कल एस्से (peer-ee-OD-i-kul ES-ay)","अख़बार/पत्रिका में नियमित छपने वाला निबंध","A short essay published in a regular periodical issue, on manners, morals and taste, typical of The Tatler (1709) and The Spectator (1711)."),
 ("Persona","पर-सो-ना (per-SOH-nuh)","लेखक का गढ़ा हुआ नकली नाम/रूप जो बोलता है","The 'mask' or assumed character through whom an author speaks, e.g. Isaac Bickerstaff, Mr. Spectator, Elia."),
 ("Pseudonym","स्यू-डो-निम (SOO-duh-nim)","उपनाम, लेखक का बदला हुआ नाम","A fictitious name adopted by an author, e.g. Elia (Lamb), Democritus Junior (Burton), George Orwell (Eric Blair)."),
 ("Euphuism","यू-फ़्यू-इज़्म (YOO-fyoo-iz-um)","बहुत सजी-धजी, अलंकारों से भरी गद्य शैली","An elaborate prose style of antithesis, alliteration and learned similes, from John Lyly's Euphues: The Anatomy of Wit (1578)."),
 ("Ciceronian Style","सि-स-रो-नि-यन स्टाइल (sis-uh-ROH-nee-un)","लंबे, संतुलित, घुमावदार वाक्यों वाली शैली","A prose style modelled on Cicero, using long, balanced periodic sentences; contrasted with the Senecan or Attic style."),
 ("Senecan Style","से-ने-कन स्टाइल (SEN-uh-kun)","छोटे, कसे हुए, चुटीले वाक्यों वाली शैली","A terse, pointed, 'curt' prose style modelled on Seneca, favoured by Bacon and Jonson; also called Attic style."),
 ("Baroque Prose","ब-रोक प्रोज़ (buh-ROHK prohz)","भव्य, अलंकृत, लय-भरी 17वीं सदी की गद्य शैली","Ornate, rhythmic, Latinate seventeenth-century prose rich in conceits and digressions, as in Browne and Burton."),
 ("Character (Theophrastan)","थी-ओ-फ़्रास-टन कैरेक्टर (thee-oh-FRAS-tun)","किसी एक प्रकार के इंसान का छोटा शब्द-चित्र","A brief prose sketch of a human type, after Theophrastus' Characters; English examples by Hall (1608), Overbury (1614) and Earle (1628)."),
 ("Polemic","प-ले-मिक (puh-LEM-ik)","किसी मत के ख़िलाफ़ तीखा वाद-विवादी लेखन","A forceful written attack on, or controversy over, an opinion or doctrine, e.g. Milton's anti-prelatical tracts."),
 ("Tract","ट्रैक्ट (trakt)","धार्मिक/राजनीतिक विषय पर छोटी पुस्तिका","A short treatise or pamphlet, usually religious or political, as in Milton's prose and the Tracts for the Times (1833-41)."),
 ("Pamphlet","पैम्फ़-लेट (PAMF-lit)","बिना जिल्द की छोटी प्रचार-पुस्तिका","A short unbound publication on a topical issue, used for political and religious argument (Milton, Swift, Defoe, Carlyle's Latter-Day Pamphlets)."),
 ("Licensing (Censorship)","लाइ-सन-सिंग (LY-sun-sing)","छपने से पहले सरकारी अनुमति की पाबंदी","Pre-publication censorship requiring official approval; the Licensing Order of 1643 provoked Milton's Areopagitica (1644)."),
 ("Coffee-house","कॉफ़ी हाउस (KOF-ee hows)","18वीं सदी के बैठक-स्थल जहाँ लोग अख़बार पढ़ते और बहस करते","Eighteenth-century London meeting places (Will's, Button's) central to the public sphere and to the Tatler and Spectator readership."),
 ("Augustan Age","ऑ-गस-टन एज (aw-GUS-tun)","अंग्रेज़ी साहित्य का क्लासिकी, नियम-प्रिय दौर (लगभग 1700-1745)","The period of Pope, Swift, Addison and Steele, named after Augustus' Rome, valuing reason, decorum and classical correctness."),
 ("Johnsonese","जॉन-सन-ईज़ (jon-suh-NEEZ)","जॉनसन जैसी भारी, लैटिन-शब्दों वाली संतुलित शैली","A heavy, Latinate, antithetical and balanced style associated with Samuel Johnson's Rambler essays."),
 ("Grub Street","ग्रब स्ट्रीट (grub street)","पैसे के लिए लिखने वाले छोटे लेखकों की दुनिया","A London street that became a byword for hack writers; Johnson defined it in his Dictionary (1755)."),
 ("Impassioned Prose","इम-पै-शन्ड प्रोज़ (im-PASH-und prohz)","कविता जैसी भावुक, संगीतमय गद्य शैली","De Quincey's term for his poetic, rhythmic, dream-laden prose, as in Suspiria de Profundis (1845)."),
 ("Literature of Knowledge / Power","लिट-रे-चर ऑफ़ पावर (LIT-ruh-chur uv POW-er)","ज्ञान देने वाला साहित्य बनाम दिल को हिलाने वाला साहित्य","De Quincey's distinction: the function of the first is to teach, of the second to move; set out in 'Letters to a Young Man' (1823) and his essay on Pope (1848)."),
 ("Gusto","गस-टो (GUS-toh)","किसी चीज़ में भरी हुई जोशीली जान/तीव्रता","Hazlitt's term (essay 'On Gusto', 1816, in The Round Table) for 'power or passion defining any object' in art."),
 ("Sage Writing","सेज राइटिंग (sayj)","समाज को नैतिक उपदेश देने वाला विक्टोरियन गद्य","Victorian prose of moral and social prophecy (Carlyle, Ruskin, Arnold, Newman); term popularised by John Holloway, The Victorian Sage (1953)."),
 ("Carlylese","कार-लाइल-ईज़ (kar-ly-LEEZ)","कार्लाइल की जर्मन-प्रभावित, गरजती हुई शैली","Carlyle's idiosyncratic style: Germanic compounds, capitalised abstractions, exclamations and prophetic rhetoric, as in Sartor Resartus."),
 ("Cash Nexus","कैश नेक्सस (kash NEK-sus)","इंसानी रिश्तों को सिर्फ़ पैसे से जोड़ना","Carlyle's phrase (Chartism 1839; Past and Present 1843) for relations reduced to monetary payment."),
 ("Pathetic Fallacy","प-थे-टिक फ़ै-ल-सी (puh-THET-ik FAL-uh-see)","प्रकृति पर इंसानी भावनाएँ थोपना","Ruskin's term (Modern Painters, vol. III, 1856) for attributing human emotions to nature, e.g. 'the cruel, crawling foam'."),
 ("Philistine","फ़ि-लि-स्टाइन (FIL-uh-styn)","संस्कृति से कटा, केवल पैसा-मुनाफ़ा देखने वाला","Arnold's term in Culture and Anarchy (1869) for the materialistic, uncultured middle class (borrowed from German Philister)."),
 ("Hebraism and Hellenism","ही-ब्रे-इज़्म, हे-ले-निज़्म (HEE-bray-iz-um, HEL-uh-niz-um)","नैतिक कठोरता बनाम स्वच्छंद बौद्धिक सौंदर्य","Arnold's two forces in Culture and Anarchy: Hebraism = 'strictness of conscience', Hellenism = 'spontaneity of consciousness'."),
 ("Sweetness and Light","स्वीट-नेस एंड लाइट (SWEET-nis and lyt)","सौंदर्य और बुद्धि, संस्कृति के दो गुण","Beauty and intelligence as the aims of culture; phrase from Swift's The Battle of the Books (1704), used by Arnold in Culture and Anarchy."),
 ("Touchstone","टच-स्टोन (TUCH-stohn)","कसौटी: महान पंक्तियाँ जिनसे दूसरी कविता परखी जाए","Arnold's method in 'The Study of Poetry' (1880) of judging poetry against short passages from the great masters (Homer, Dante, Shakespeare, Milton)."),
 ("High Seriousness","हाई सी-रि-यस-नेस (hy SEER-ee-us-nis)","गहरी, गंभीर नैतिक सच्चाई का भाव","Arnold's criterion (from Aristotle's spoudaiotes) in 'The Study of Poetry'; he found Chaucer and Burns lacking in it."),
 ("Disinterestedness","डिस-इन-ट्र-स्टेड-नेस (dis-IN-tris-tid-nis)","निष्पक्षता, निजी या दलगत स्वार्थ से ऊपर उठना","Arnold's ideal for criticism in 'The Function of Criticism at the Present Time' (1864): free from practical, political or sectarian ends."),
 ("Aestheticism","एस-थे-टि-सिज़्म (es-THET-i-siz-um)","कला सिर्फ़ सुंदरता के लिए, उपदेश के लिए नहीं","The late-nineteenth-century movement holding that art needs no moral or social justification; associated with Pater and Wilde."),
 ("Art for Art's Sake","आर्ट फ़ॉर आर्ट्स सेक (l'art pour l'art)","कला का मक़सद ख़ुद कला है","Slogan of aestheticism; from French 'l'art pour l'art', popularised by Gautier (preface to Mademoiselle de Maupin, 1835)."),
 ("Decadence","डे-क-डेंस (DEK-uh-duns)","1890s का पतनशील, कृत्रिमता-प्रेमी साहित्यिक रुझान","The 1890s movement prizing artifice, sensation and refinement (Wilde, Beardsley, The Yellow Book), following Huysmans and Baudelaire."),
 ("Tractarianism","ट्रैक-टे-रि-य-निज़्म (trak-TAIR-ee-uh-niz-um)","ऑक्सफ़र्ड मूवमेंट, चर्च में कैथलिक परंपरा लौटाने का आंदोलन","The Oxford Movement (1833-45) of Newman, Keble and Pusey, named from the Tracts for the Times."),
 ("Apologia","ऐ-पो-लो-जिया (ap-uh-LOH-jee-uh)","माफ़ी नहीं, अपने विचारों/जीवन का बचाव","A formal written defence of one's opinions or conduct, e.g. Newman's Apologia Pro Vita Sua (1864)."),
 ("Utilitarianism","यू-टि-लि-टे-रि-य-निज़्म (yoo-til-i-TAIR-ee-uh-niz-um)","अधिकतम लोगों का अधिकतम सुख वाला सिद्धांत","The doctrine of Bentham and J. S. Mill that right action produces 'the greatest happiness of the greatest number'; criticised by Carlyle, Ruskin and Dickens."),
 ("Belles-lettres","बेल-लेट्र (bel-LET-ruh)","कलात्मक, सुरुचिपूर्ण साहित्य (ख़ासकर निबंध)","Literature valued for aesthetic qualities rather than information, especially light essays and criticism."),
 ("Biography","बाइ-ऑ-ग्र-फ़ी (by-OG-ruh-fee)","किसी दूसरे व्यक्ति की जीवन-कथा","A written account of another person's life; the word appears in Dryden's Life of Plutarch (1683), defined as 'the history of particular men's lives'."),
 ("Autobiography","ऑ-टो-बाइ-ऑ-ग्र-फ़ी (aw-toh-by-OG-ruh-fee)","अपनी जीवन-कथा ख़ुद लिखना, आत्मकथा","A person's account of his or her own life; the English word came into use c. 1797-1809 (Southey, 1809)."),
 ("Memoir","मेम-वार (MEM-wahr)","संस्मरण: जीवन की कुछ घटनाओं/लोगों की यादें","An account of part of one's life focused on events and people witnessed rather than on the full inner development of the self."),
 ("Hagiography","है-गी-ऑ-ग्र-फ़ी (hag-ee-OG-ruh-fee)","संतों की जीवनी; या किसी की अंधी तारीफ़ वाली जीवनी","Writing on the lives of saints; by extension, an uncritically adulatory biography."),
 ("Travelogue","ट्रै-व-लॉग (TRAV-uh-log)","यात्रा-वृत्तांत","A narrative of travel and of places and peoples encountered, e.g. Sterne's A Sentimental Journey (1768) or Naipaul's An Area of Darkness (1964)."),
 ("New Biography","न्यू बाइ-ऑ-ग्र-फ़ी (nyoo by-OG-ruh-fee)","व्यंग्यपूर्ण, चुनिंदा, व्यक्तित्व पर ज़ोर देने वाली आधुनिक जीवनी","Early twentieth-century ironic, selective biography begun by Strachey's Eminent Victorians (1918); named in Woolf's essay 'The New Biography' (1927)."),
 ("Angel in the House","एंजल इन द हाउस (AYN-jul in the hows)","आदर्श, त्यागी, घरेलू औरत की छवि","The self-sacrificing Victorian ideal of womanhood, from Coventry Patmore's poem (1854-62), which Woolf urges women writers to kill in 'Professions for Women' (1931)."),
 ("Androgynous Mind","ऐन-ड्रॉ-जि-नस माइंड (an-DROJ-uh-nus)","ऐसा मन जिसमें स्त्री और पुरुष दोनों गुण मिले हों","Woolf's ideal, taken from Coleridge, in A Room of One's Own (1929): the great mind is 'man-womanly' and 'woman-manly'."),
 ("Satyagraha","सत्याग्रह (sut-YAA-gruh-huh)","सत्य और अहिंसा पर टिका प्रतिरोध","Gandhi's term ('holding firmly to truth') for non-violent resistance, coined in South Africa (1906-08); see Satyagraha in South Africa (1928)."),
 ("Sarvodaya","सर्वोदय (sur-VOH-duh-yuh)","सबका उदय, सबका कल्याण","'Welfare of all': Gandhi's title for his Gujarati paraphrase (1908) of Ruskin's Unto This Last."),
 ("Swaraj","स्वराज (swuh-RAAJ)","अपना राज, आत्म-शासन","Self-rule; in Gandhi's Hind Swaraj (1909) it means moral self-rule as well as political independence."),
 ("Dalit Autobiography","दलित आत्मकथा (DUH-lit)","जाति-उत्पीड़न का अनुभव बताने वाली आत्मकथा","Life-writing by Dalit authors testifying to caste oppression, e.g. Baluta (1978), Akkarmashi (1984), Karukku (1992), Joothan (1997); often read as testimonio."),
 ("Newspeak","न्यू-स्पीक (NYOO-speek)","सोच को सीमित करने वाली सरकारी नकली भाषा","Orwell's invented language of the Party in Nineteen Eighty-Four (1949), extending the argument of 'Politics and the English Language' (1946)."),
 ("Bloomsbury Group","ब्लूम्ज़-बरी ग्रुप (BLOOMZ-buh-ree)","लंदन के बुद्धिजीवियों-कलाकारों का समूह","An early twentieth-century circle of writers and intellectuals including Virginia and Leonard Woolf, Lytton Strachey, E. M. Forster, Roger Fry and J. M. Keynes."),
]
TERMS=[{"term":a,"pron":b,"hindi":c,"net":d} for a,b,c,d in terms]

M=[]
def q(qq,opts,ans,exp): M.append({"q":qq,"options":opts,"answer":ans,"exp":exp})

q("'Some books are to be tasted, others to be swallowed, and some few to be chewed and digested' occurs in Bacon's essay:",["Of Truth","Of Studies","Of Friendship","Of Adversity"],1,"The line is from Of Studies.")
q("Arrange the editions of Bacon's Essays in chronological order with the number of essays: (i) 58 essays (ii) 10 essays (iii) 38 essays",["(ii), (iii), (i)","(i), (ii), (iii)","(iii), (ii), (i)","(ii), (i), (iii)"],0,"1597 had 10, 1612 had 38, 1625 had 58 essays.")
q("Which of the following is NOT one of Bacon's four Idols in Novum Organum?",["Idols of the Tribe","Idols of the Cave","Idols of the Market-place","Idols of the Temple"],3,"The four are Tribe, Cave, Market-place and Theatre.")
q("Religio Medici, Pseudodoxia Epidemica and Hydriotaphia were written by:",["Robert Burton","Jeremy Taylor","Sir Thomas Browne","Thomas Fuller"],2,"All three are by Sir Thomas Browne of Norwich.")
q("'Who kills a man kills a reasonable creature, God's image; but he who destroys a good book, kills reason itself.' This is from:",["Of Education","Areopagitica","Eikonoklastes","The Tenure of Kings and Magistrates"],1,"Milton's Areopagitica (1644) argues against pre-publication licensing.")
q("Milton's Eikonoklastes (1649) was a reply to:",["Leviathan","Eikon Basilike","Defensio Regia","The Anatomy of Melancholy"],1,"Eikon Basilike was the royalist book attributed to Charles I.")
q("Match the persona with the periodical: (a) Isaac Bickerstaff (b) Mr. Spectator (c) Lien Chi Altangi (d) Elia || (i) The Spectator (ii) The Citizen of the World (iii) The Tatler (iv) London Magazine",["a-iii, b-i, c-ii, d-iv","a-i, b-iii, c-iv, d-ii","a-iii, b-i, c-iv, d-ii","a-ii, b-i, c-iii, d-iv"],0,"Bickerstaff - Tatler; Mr. Spectator - Spectator; Lien Chi Altangi - Goldsmith; Elia - London Magazine.")
q("Which member of the Spectator Club represents the Whig commercial interest?",["Sir Roger de Coverley","Will Honeycomb","Sir Andrew Freeport","Captain Sentry"],2,"Sir Andrew Freeport is the London merchant; Sir Roger is the Tory squire.")
q("Assertion (A): Addison wanted to bring philosophy 'out of closets and libraries' to 'tea-tables and coffee-houses'. Reason (R): The Spectator aimed at the moral and cultural education of the middle-class reading public.",["Both A and R are true and R is the correct explanation of A","Both A and R are true but R is not the correct explanation of A","A is true but R is false","A is false but R is true"],0,"Spectator No. 10 states the aim, which follows from its educative purpose.")
q("Johnson's letter to Lord Chesterfield (1755) concerns:",["The Rambler","Rasselas","A Dictionary of the English Language","Lives of the Poets"],2,"Chesterfield offered patronage only when the Dictionary was about to appear.")
q("In which work does Johnson describe metaphysical wit as 'heterogeneous ideas yoked by violence together'?",["Preface to Shakespeare","Life of Cowley","The Idler","Life of Savage"],1,"It is in the Life of Cowley in Lives of the Poets (1779-81).")
q("'Dream-Children: A Reverie' and 'A Dissertation upon Roast Pig' are essays by:",["Hazlitt","Leigh Hunt","Charles Lamb","De Quincey"],2,"Both are Essays of Elia by Lamb (1823).")
q("Which of the following essays belongs to The Last Essays of Elia (1833)?",["The South-Sea House","Old China","Dream-Children","Christ's Hospital Five and Thirty Years Ago"],1,"'Old China' is in the 1833 collection; the others are in Essays of Elia (1823).")
q("The Spirit of the Age (1825), a series of portraits of contemporaries, was written by:",["Thomas Carlyle","William Hazlitt","Thomas De Quincey","J. S. Mill"],1,"Hazlitt's The Spirit of the Age profiles Bentham, Coleridge, Wordsworth and others.")
q("The 'Ladies of Sorrow' - Mater Lachrymarum, Mater Suspiriorum and Mater Tenebrarum - appear in De Quincey's:",["The English Mail-Coach","Suspiria de Profundis","Confessions of an English Opium-Eater","On Murder Considered as One of the Fine Arts"],1,"'Levana and Our Ladies of Sorrow' is part of Suspiria de Profundis (1845).")
q("The distinction between 'literature of knowledge' and 'literature of power' was made by:",["Hazlitt","Arnold","De Quincey","Pater"],2,"De Quincey: the first teaches, the second moves.")
q("Diogenes Teufelsdrockh, 'Professor of Things in General', is the hero of:",["Past and Present","Sartor Resartus","Heroes and Hero-Worship","Chartism"],1,"Sartor Resartus (1833-34) presents his philosophy of clothes.")
q("In On Heroes, Hero-Worship and the Heroic in History, Carlyle presents Johnson, Rousseau and Burns as the Hero as:",["Poet","Priest","Man of Letters","King"],2,"Dante and Shakespeare are Poets; Johnson, Rousseau and Burns are Men of Letters.")
q("The term 'pathetic fallacy' was coined by Ruskin in:",["The Stones of Venice","Modern Painters, vol. III","Unto This Last","Sesame and Lilies"],1,"Ruskin coined it in Modern Painters III (1856).")
q("Arrange Ruskin's works chronologically: (i) Unto This Last (ii) The Seven Lamps of Architecture (iii) Sesame and Lilies (iv) Praeterita",["(ii), (i), (iii), (iv)","(i), (ii), (iii), (iv)","(ii), (iii), (i), (iv)","(iii), (ii), (i), (iv)"],0,"1849, 1860-62, 1865, 1885-89.")
q("Which work of Ruskin did Gandhi paraphrase in Gujarati as Sarvodaya?",["Fors Clavigera","The Crown of Wild Olive","Unto This Last","Munera Pulveris"],2,"Gandhi's Sarvodaya (1908) is based on Unto This Last.")
q("In Culture and Anarchy, Arnold calls the middle class:",["Barbarians","Philistines","Populace","Hellenes"],1,"Barbarians = aristocracy, Philistines = middle class, Populace = working class.")
q("Arnold borrowed the phrase 'sweetness and light' from:",["Swift's The Battle of the Books","Pope's Essay on Criticism","Addison's Spectator","Carlyle's Sartor Resartus"],0,"Swift used it in the bees-and-spider fable of The Battle of the Books.")
q("'To burn always with this hard, gem-like flame, to maintain this ecstasy, is success in life.' This is from the Conclusion to:",["Wilde's Intentions","Pater's The Renaissance","Ruskin's Modern Painters","Symons' The Symbolist Movement in Literature"],1,"Pater's Studies in the History of the Renaissance (1873).")
q("Newman's Apologia Pro Vita Sua (1864) was written in response to an attack by:",["Thomas Arnold","Charles Kingsley","John Keble","T. H. Huxley"],1,"Kingsley questioned Newman's truthfulness, provoking the Apologia.")
q("'On or about December 1910 human character changed' is from Woolf's:",["Modern Fiction","A Room of One's Own","Mr. Bennett and Mrs. Brown","Three Guineas"],2,"Mr. Bennett and Mrs. Brown (1924) contrasts Edwardians and Georgians.")
q("Which of the following is NOT one of Orwell's four motives in 'Why I Write'?",["Sheer egoism","Aesthetic enthusiasm","Historical impulse","Religious conviction"],3,"The fourth motive is political purpose.")
q("Match the work with the author: (a) Hind Swaraj (b) The Discovery of India (c) Annihilation of Caste (d) Nationalism || (i) Ambedkar (ii) Tagore (iii) Gandhi (iv) Nehru",["a-iii, b-iv, c-i, d-ii","a-iv, b-iii, c-ii, d-i","a-iii, b-i, c-iv, d-ii","a-ii, b-iv, c-i, d-iii"],0,"Gandhi 1909, Nehru 1946, Ambedkar 1936, Tagore 1917.")
q("Amartya Sen's distinction between 'niti' and 'nyaya' is developed in:",["Development as Freedom","The Argumentative Indian","The Idea of Justice","Identity and Violence"],2,"The Idea of Justice (2009) contrasts niti (institutions) and nyaya (realised justice).")
q("Lytton Strachey's Eminent Victorians (1918) contains biographical essays on all EXCEPT:",["Cardinal Manning","Florence Nightingale","Dr Thomas Arnold","John Henry Newman"],3,"The four subjects are Manning, Nightingale, Dr Arnold and General Gordon.")

def find(t): return next(i for i,x in enumerate(T) if x["title"].startswith(t))
def merge(a,ka,b,kb,title):
    ia,ib=find(a),find(b)
    pts=[T[ia]["points"][i] for i in ka]+[T[ib]["points"][i] for i in kb]
    T[ia]={"title":title,"points":pts}; del T[ib]
merge("William Hazlitt",[1,2,3,4,5,6,8],"Thomas De Quincey",[0,2,3,4,6],"Romantic Essayists: Hazlitt, Leigh Hunt and De Quincey")
merge("George Orwell",[0,1,2,3,4,5],"Bertrand Russell",[0,1,2,3,4,6],"Orwell, Russell and Other Modern Essayists")
merge("Travel Writing",[0,1,3,4,5,6],"Periodicals",[1,2,3,4,5,6],"Travel Writing and Periodicals")

TERMS=[t for t in TERMS if t["term"] not in ("Newspeak","Belles-lettres","Grub Street")]
for i,m in enumerate(M):
    tgt=(i*3+1)%4; a=m["answer"]; o=m["options"]
    o[a],o[tgt]=o[tgt],o[a]; m["answer"]=tgt

data={"id":4,"title":"Non-Fictional Prose",
"overview":"Is unit mein English essay aur gadya ka poora safar hai: Bacon aur 17th century prose, Milton ki Areopagitica, Addison-Steele ke periodicals, Johnson, Romantic essayists (Lamb, Hazlitt, De Quincey), Victorian sages (Carlyle, Ruskin, Arnold, Pater, Newman), modern essayists (Woolf, Orwell, Russell) aur Indian non-fiction (Gandhi, Nehru, Ambedkar, Tagore, Sen), saath mein biography, autobiography, travel writing aur periodicals. NET mein yahan se 'kisne likha/kis essay ka quote hai', match-the-following, chronology aur assertion-reason wale sawal aate hain.",
"topics":T,"terms":TERMS,"mcqs":M}
p="/workspace/projects/a829249c-c8af-4f4e-9fab-a2213c15a2ee/app/content/unit4.json"
json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(T),[len(t["points"]) for t in T],len(TERMS),len(M))
