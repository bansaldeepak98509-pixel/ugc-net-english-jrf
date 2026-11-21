# Each non-AR item: (q, [correct, d1, d2, d3], exp) -> rotated at assembly so answers spread 0-3.
# AR items: ("AR", q, answer_index, exp) with fixed standard options.
M = []
# ---- chunk 1: direct (20)
M += [
("The Charter Act that first set aside a sum of not less than one lakh rupees a year for education in India was passed in:",["1813","1833","1853","1793"],"Charter Act 1813 ne pehli baar ek lakh rupaye education ke liye rakhe."),
("The English Education Act of 7 March 1835 was passed by the Governor-General:",["Lord William Bentinck","Lord Auckland","Lord Dalhousie","Lord Cornwallis"],"Bentinck ne Macaulay ka Minute maan kar resolution pass kiya."),
("Wood's Despatch (1854) reached India during the Governor-Generalship of:",["Lord Dalhousie","Lord Canning","Lord Ripon","Lord Curzon"],"1854 mein Dalhousie Governor-General the."),
("The Indian Education Commission of 1882 chaired by W.W. Hunter was appointed under:",["Lord Ripon","Lord Lytton","Lord Curzon","Lord Minto"],"Hunter Commission - Lord Ripon ke time."),
("The Indian Universities Act of 1904 was passed under:",["Lord Curzon","Lord Ripon","Lord Hardinge","Lord Chelmsford"],"Raleigh Commission 1902 ke baad Curzon ne 1904 Act laaya."),
("Which Article of the Indian Constitution declares Hindi in Devanagari script the official language of the Union?",["Article 343","Article 351","Article 345","Article 348"],"Article 343 = Hindi in Devanagari, Union ki official language."),
("The Official Languages Act, which allowed English to continue alongside Hindi, was passed in:",["1963","1950","1956","1968"],"Official Languages Act 1963."),
("'Hobson-Jobson', the glossary of Anglo-Indian words, was compiled by:",["Henry Yule and A.C. Burnell","William Jones and Charles Wilkins","Braj Kachru and Tom McArthur","H.H. Wilson and H.T. Prinsep"],"Yule aur Burnell, 1886."),
("Kachru's model of the Three Concentric Circles was set out in his 1985 essay:",["Standards, Codification and Sociolinguistic Realism","The Alchemy of English","The Circle of World English","English Next"],"1985 essay 'Standards, Codification and Sociolinguistic Realism'."),
("'Linguistic Imperialism' (1992) was written by:",["Robert Phillipson","David Graddol","Edgar Schneider","Tom McArthur"],"Phillipson ne English ke global spread ko imperialism kaha."),
("'Masks of Conquest: Literary Study and British Rule in India' (1989) is by:",["Gauri Viswanathan","Gayatri Spivak","Meenakshi Mukherjee","Rajeswari Sunder Rajan"],"Gauri Viswanathan: English literature as tool of colonial control."),
("In many varieties of Indian English the alveolar stops /t/ and /d/ of RP are typically pronounced as:",["retroflex stops","dental fricatives","glottal stops","aspirated velars"],"Indian English mein /t/ /d/ retroflex ho jaate hain."),
("The invariant tag question typical of Indian English is:",["isn't it?","doesn't he?","won't they?","shall we?"],"'You are coming, isn't it?' - har subject ke saath same tag."),
("The students of Derozio at Hindu College, Calcutta, came to be known as:",["Young Bengal","Brahmo Samaj","Bengal Renaissance Circle","Anushilan Samiti"],"Derozio ke radical students = Young Bengal."),
("'The Captive Ladie' (1849) is a long poem in English by:",["Michael Madhusudan Dutt","Kashiprasad Ghosh","Toru Dutt","Manmohan Ghose"],"Madhusudan Dutt ne pehle English mein likha, phir Bengali mein."),
("Toru Dutt's 'Our Casuarina Tree' appears in:",["Ancient Ballads and Legends of Hindustan","A Sheaf Gleaned in French Fields","The Golden Threshold","The Bird of Time"],"Ancient Ballads (1882, posthumous) mein Casuarina Tree hai."),
("Sri Aurobindo's 'Savitri: A Legend and a Symbol' is an epic written in:",["blank verse","heroic couplets","terza rima","free verse"],"Savitri lambi blank verse epic hai."),
("Writers Workshop, Calcutta, the publisher of many new Indian English poets, was founded in 1958 by:",["P. Lal","Nissim Ezekiel","A.K. Ramanujan","R. Parthasarathy"],"P. Lal ne 1958 mein Writers Workshop shuru kiya."),
("Nissim Ezekiel's 'Night of the Scorpion' was first collected in:",["The Exact Name","A Time to Change","Hymns in Darkness","Latter-Day Psalms"],"Night of the Scorpion - The Exact Name (1965)."),
("Kamala Das's autobiography 'My Story' was first serialised in Malayalam as:",["Ente Katha","Balyakala Smaranakal","Neermathalam Pootha Kalam","Chandana Marangal"],"My Story ka Malayalam roop Ente Katha."),
]
# ---- chunk 2: direct (20)
M += [
("A.K. Ramanujan's 'Speaking of Siva' (1973) translates:",["Kannada vachanas of Virashaiva saints","Tamil Sangam love poems","Tamil hymns to Vishnu by Nammalvar","Telugu padams of Kshetrayya"],"Speaking of Siva = Basavanna, Akka Mahadevi aadi ke vachanas."),
("Keki N. Daruwalla won the Sahitya Akademi Award for:",["The Keeper of the Dead","Under Orion","Apparition in April","Crossing of Rivers"],"Daruwalla - The Keeper of the Dead, SA 1984."),
("Arun Kolatkar's 'Jejuri' is set in a pilgrim town in Maharashtra sacred to:",["Khandoba","Vithoba","Ganapati","Tulja Bhavani"],"Jejuri = Khandoba ka mandir town."),
("The action of Mulk Raj Anand's 'Untouchable' covers:",["a single day in Bakha's life","Bakha's whole childhood","one year in a hill village","the Quit India movement"],"Untouchable ek din ki kahani hai."),
("Margayya is the protagonist of R.K. Narayan's:",["The Financial Expert","Mr. Sampath","The Vendor of Sweets","The Dark Room"],"Margayya - banyan tree ke neeche money-lender."),
("The young Gandhian hero of Raja Rao's 'Kanthapura' is:",["Moorthy","Ramaswamy","Bhatta","Range Gowda"],"Moorthy village ko Gandhi ke raaste le jaata hai."),
("In 1993 'Midnight's Children' was named the:",["Booker of Bookers","Commonwealth Novel of the Century","Nobel Laureate's Choice","Jnanpith Book of the Decade"],"1993 Booker of Bookers; 2008 Best of the Booker bhi."),
("In 'Midnight's Children', the boy whose name-tag is switched with Saleem's at birth is:",["Shiva","Padma","Aadam","Picture Singh"],"Mary Pereira ne Saleem aur Shiva ko badal diya."),
("'The God of Small Things' is set mainly in:",["Ayemenem, Kerala","Kalimpong, Darjeeling","Mano Majra, Punjab","Malgudi, South India"],"Ayemenem, Kerala."),
("In 'The White Tiger', Balram Halwai drives for and later murders his master:",["Ashok","Mukesh","Vitiligo-Lips","the Great Socialist"],"Balram apne master Ashok ko maar deta hai."),
("Khushwant Singh's 'Train to Pakistan' is set in the border village of:",["Mano Majra","Kanthapura","Laxmangarh","Ayemenem"],"Mano Majra on the Sutlej."),
("The narrator of Kamala Markandaya's 'Nectar in a Sieve' is:",["Rukmani","Ira","Kunthi","Janaki"],"Rukmani, peasant woman."),
("In Ananthamurthy's 'Samskara' the crisis begins with the death of:",["Naranappa","Praneshacharya","Chandri","Putta"],"Naranappa ki death - cremation kaun kare?"),
("Bishan Singh, who dies in no-man's land between India and Pakistan, is the central figure of:",["Toba Tek Singh","Lihaaf","Pinjar","Thanda Gosht"],"Manto ki Toba Tek Singh (Urdu)."),
("Geetanjali Shree's 'Ret Samadhi', which won the International Booker Prize in 2022, was translated as 'Tomb of Sand' by:",["Daisy Rockwell","Deepa Bhasthi","Jason Grunebaum","Arunava Sinha"],"Daisy Rockwell ne Hindi se translate kiya."),
("Banu Mushtaq's 'Heart Lamp', winner of the International Booker Prize 2025, was originally written in:",["Kannada","Malayalam","Urdu","Tamil"],"Heart Lamp - Kannada stories, tr. Deepa Bhasthi."),
("'Ghashiram Kotwal' (1972) was originally written in Marathi by:",["Vijay Tendulkar","Mahesh Elkunchwar","Satish Alekar","P.L. Deshpande"],"Tendulkar ka famous Marathi play."),
("'After Amnesia' (1992), which argues that Indian criticism forgot its own traditions under colonialism, is by:",["G.N. Devy","Harish Trivedi","Aijaz Ahmad","Sujit Mukherjee"],"G.N. Devy, SA award winner."),
("'The Twice Born Fiction' (1971) was written by:",["Meenakshi Mukherjee","K.R. Srinivasa Iyengar","M.K. Naik","C.D. Narasimhaiah"],"Meenakshi Mukherjee - Indian English novel par."),
("The dedication 'To the memory of the British Empire in India, which conferred subjecthood on us but withheld citizenship' opens:",["The Autobiography of an Unknown Indian","The Discovery of India","An Area of Darkness","Hind Swaraj"],"Nirad C. Chaudhuri, 1951."),
]
# ---- chunk 3: match (10)
M += [
("Match the commission with its year: (a) Hunter Commission (b) Raleigh Commission (c) Sadler Commission (d) Radhakrishnan Commission -- (i) 1948-49 (ii) 1882 (iii) 1917-19 (iv) 1902",["a-ii, b-iv, c-iii, d-i","a-iv, b-ii, c-i, d-iii","a-ii, b-iii, c-iv, d-i","a-iii, b-iv, c-ii, d-i"],"Hunter 1882, Raleigh 1902, Sadler 1917-19, Radhakrishnan 1948-49."),
("Match the character with the novel: (a) Munoo (b) Margayya (c) Moorthy (d) Juggut Singh -- (i) Kanthapura (ii) Train to Pakistan (iii) Coolie (iv) The Financial Expert",["a-iii, b-iv, c-i, d-ii","a-iv, b-iii, c-ii, d-i","a-iii, b-i, c-iv, d-ii","a-ii, b-iv, c-i, d-iii"],"Munoo-Coolie, Margayya-Financial Expert, Moorthy-Kanthapura, Jugga-Train to Pakistan."),
("Match the poet with the collection: (a) Nissim Ezekiel (b) Kamala Das (c) A.K. Ramanujan (d) Jayanta Mahapatra -- (i) Summer in Calcutta (ii) Relations (iii) A Rain of Rites (iv) The Unfinished Man",["a-iv, b-i, c-ii, d-iii","a-i, b-iv, c-iii, d-ii","a-iv, b-ii, c-i, d-iii","a-ii, b-i, c-iv, d-iii"],"Ezekiel-Unfinished Man, Das-Summer in Calcutta, Ramanujan-Relations, Mahapatra-A Rain of Rites."),
("Match the scholar with the idea: (a) Braj Kachru (b) Robert Phillipson (c) Edgar Schneider (d) Tom McArthur -- (i) Dynamic Model (ii) Circle of World English (iii) Three Concentric Circles (iv) Linguistic Imperialism",["a-iii, b-iv, c-i, d-ii","a-iv, b-iii, c-ii, d-i","a-iii, b-i, c-iv, d-ii","a-ii, b-iv, c-i, d-iii"],"Kachru-Circles, Phillipson-Imperialism, Schneider-Dynamic Model, McArthur-Circle of World English."),
("Match the work with its English translator: (a) Samskara (b) Tomb of Sand (c) Heart Lamp (d) Imaginary Maps -- (i) Gayatri Spivak (ii) Deepa Bhasthi (iii) A.K. Ramanujan (iv) Daisy Rockwell",["a-iii, b-iv, c-ii, d-i","a-iv, b-iii, c-i, d-ii","a-iii, b-ii, c-iv, d-i","a-i, b-iv, c-ii, d-iii"],"Samskara-Ramanujan, Tomb of Sand-Rockwell, Heart Lamp-Bhasthi, Imaginary Maps-Spivak."),
("Match the play with the playwright: (a) Evam Indrajit (b) Adhe Adhure (c) Tughlaq (d) Sakharam Binder -- (i) Mohan Rakesh (ii) Vijay Tendulkar (iii) Badal Sircar (iv) Girish Karnad",["a-iii, b-i, c-iv, d-ii","a-i, b-iii, c-ii, d-iv","a-iii, b-iv, c-i, d-ii","a-iv, b-i, c-iii, d-ii"],"Evam Indrajit-Sircar, Adhe Adhure-Rakesh, Tughlaq-Karnad, Sakharam Binder-Tendulkar."),
("Match the critic with the book: (a) Meenakshi Mukherjee (b) C.D. Narasimhaiah (c) G.N. Devy (d) Tejaswini Niranjana -- (i) Siting Translation (ii) The Twice Born Fiction (iii) After Amnesia (iv) The Swan and the Eagle",["a-ii, b-iv, c-iii, d-i","a-iv, b-ii, c-i, d-iii","a-ii, b-iii, c-iv, d-i","a-iii, b-iv, c-ii, d-i"],"Mukherjee-Twice Born, CDN-Swan and Eagle, Devy-After Amnesia, Niranjana-Siting Translation."),
("Match the opening line with the novel: (a) 'May in Ayemenem is a hot, brooding month.' (b) 'The summer of 1947 was not like other Indian summers.' (c) 'Raju welcomed the intrusion...' (d) 'It was Monday morning. Swaminathan was reluctant to open his eyes.' -- (i) Swami and Friends (ii) The Guide (iii) The God of Small Things (iv) Train to Pakistan",["a-iii, b-iv, c-ii, d-i","a-iv, b-iii, c-i, d-ii","a-iii, b-ii, c-iv, d-i","a-ii, b-iv, c-iii, d-i"],"Ayemenem-GoST, summer 1947-Train to Pakistan, Raju-Guide, Monday morning-Swami."),
("Match the early writer with the work: (a) Derozio (b) Bankim Chandra Chatterjee (c) Kylas Chunder Dutt (d) Krupabai Satthianadhan -- (i) Kamala (ii) The Fakeer of Jungheera (iii) Rajmohan's Wife (iv) A Journal of Forty-Eight Hours of the Year 1945",["a-ii, b-iii, c-iv, d-i","a-iii, b-ii, c-i, d-iv","a-ii, b-iv, c-iii, d-i","a-iv, b-iii, c-ii, d-i"],"Derozio-Fakeer, Bankim-Rajmohan's Wife, Kylas Chunder-Journal, Krupabai-Kamala."),
("Match Amitav Ghosh's novel with its subject: (a) The Hungry Tide (b) The Glass Palace (c) Sea of Poppies (d) The Calcutta Chromosome -- (i) Burma and the fall of Mandalay (ii) the opium trade and the ship Ibis (iii) Ronald Ross and malaria research (iv) the Sundarbans",["a-iv, b-i, c-ii, d-iii","a-i, b-iv, c-iii, d-ii","a-iv, b-ii, c-i, d-iii","a-ii, b-i, c-iv, d-iii"],"Hungry Tide-Sundarbans, Glass Palace-Burma, Sea of Poppies-Ibis/opium, Calcutta Chromosome-malaria."),
]
# ---- chunk 4: assertion-reason (8), chronology (7), correct statement (5)
M += [
("AR","Assertion (A): Macaulay's Minute recommended that the education funds be spent on English education. Reason (R): Macaulay held that Sanskrit and Arabic learning were far inferior to European learning.",0,"Macaulay ki 'single shelf' wali soch hi uski recommendation ka kaaran thi."),
("AR","Assertion (A): Wood's Despatch is called the Magna Carta of English Education in India. Reason (R): Wood's Despatch was issued by Lord Curzon in 1904.",2,"A sahi; R galat - Despatch 1854 ka hai, Charles Wood ka; 1904 Curzon ka Universities Act hai."),
("AR","Assertion (A): In Kachru's model India belongs to the Expanding Circle. Reason (R): In India English has an official and institutional role.",3,"India Outer Circle mein hai, isliye A galat; R sahi hai."),
("AR","Assertion (A): Kamala Das called her English 'half English, half Indian, funny perhaps, but it is honest'. Reason (R): Kamala Das also wrote fiction in Malayalam under the name Madhavikutty.",1,"Dono sahi, par Madhavikutty naam A ko explain nahi karta."),
("AR","Assertion (A): Raja Rao's Kanthapura tries to carry Indian speech rhythms into English. Reason (R): In its Foreword Raja Rao says that the tempo of Indian life must be infused into our English expression.",0,"Foreword ka idea hi novel ki style ko explain karta hai."),
("AR","Assertion (A): Nissim Ezekiel was born into the Bene Israel Jewish community of Bombay. Reason (R): Ezekiel won the Sahitya Akademi Award for The Exact Name.",2,"A sahi; R galat - SA 1983 'Latter-Day Psalms' ke liye mila."),
("AR","Assertion (A): Manto's Toba Tek Singh was originally written in English. Reason (R): Saadat Hasan Manto is best known for his stories of the Partition.",3,"Toba Tek Singh Urdu mein hai, isliye A galat; R sahi."),
("AR","Assertion (A): Aravind Adiga's The White Tiger won the Booker Prize in 2008. Reason (R): Its narrator Balram writes letters to the Chinese Premier Wen Jiabao.",1,"Dono sahi, par letters wali baat Booker jeetne ka kaaran nahi."),
("Arrange in chronological order: I. Macaulay's Minute II. Charter Act of 1813 III. Hunter Commission IV. Ram Mohan Roy's letter to Lord Amherst",["II, IV, I, III","IV, II, I, III","II, I, IV, III","II, IV, III, I"],"1813, 1823, 1835, 1882."),
("Arrange in chronological order: I. National Policy on Education II. Sargent Plan III. Official Languages Act IV. Secondary Education Commission (Mudaliar)",["II, IV, III, I","IV, II, III, I","II, IV, I, III","II, III, IV, I"],"Sargent 1944, Mudaliar 1952-53, OLA 1963, NPE 1968."),
("Arrange in chronological order: I. Gitanjali (English) II. Rajmohan's Wife III. The Golden Threshold IV. A Sheaf Gleaned in French Fields",["II, IV, III, I","IV, II, III, I","II, III, IV, I","II, IV, I, III"],"1864, 1876, 1905, 1912."),
("Arrange Nissim Ezekiel's collections in chronological order: I. The Exact Name II. Hymns in Darkness III. A Time to Change IV. The Unfinished Man",["III, IV, I, II","IV, III, I, II","III, I, IV, II","III, IV, II, I"],"1952, 1960, 1965, 1976."),
("Arrange Salman Rushdie's novels in chronological order: I. The Satanic Verses II. Shame III. The Moor's Last Sigh IV. Midnight's Children",["IV, II, I, III","II, IV, I, III","IV, I, II, III","IV, II, III, I"],"1981, 1983, 1988, 1995."),
("Arrange the plays in chronological order of composition: I. Tughlaq II. Ghashiram Kotwal III. Ashadh Ka Ek Din IV. Evam Indrajit",["III, IV, I, II","IV, III, I, II","III, I, IV, II","III, IV, II, I"],"1958, 1963, 1964, 1972."),
("Arrange Amitav Ghosh's novels in chronological order: I. The Glass Palace II. The Shadow Lines III. The Hungry Tide IV. The Circle of Reason",["IV, II, I, III","II, IV, I, III","IV, I, II, III","IV, II, III, I"],"1986, 1988, 2000, 2004."),
("Which of the following statements is correct?",["Article 343 makes Hindi in Devanagari script the official language of the Union.","English is one of the languages listed in the Eighth Schedule.","The Official Languages Act of 1963 ended the use of English for official purposes.","The Kothari Commission submitted its report in 1949."],"343 sahi; English Eighth Schedule mein nahi; OLA ne English continue ki; Kothari 1964-66."),
("Which of the following statements about Wood's Despatch is correct?",["It recommended universities at Calcutta, Bombay and Madras on the model of London University.","It was written by Macaulay in 1835.","It rejected any role for vernacular languages in education.","It was issued after the Hunter Commission."],"Wood's Despatch 1854 ne London model universities sujhaayi; vernacular schools bhi chahiye the."),
("Which of the following statements about Kachru's model is correct?",["Outer Circle varieties such as Indian English are norm-developing.","Inner Circle varieties are norm-dependent.","Expanding Circle countries use English as an official second language.","China is placed in the Outer Circle."],"Inner norm-providing, Outer norm-developing, Expanding norm-dependent."),
("Which of the following statements about 'Samskara' is correct?",["It was written in Kannada by U.R. Ananthamurthy and translated by A.K. Ramanujan.","It was written in Malayalam by Thakazhi Sivasankara Pillai.","It was translated into English by Gayatri Spivak.","Its protagonist is the Paravan carpenter Velutha."],"Samskara: Kannada, Ananthamurthy (1965), tr. Ramanujan (1976); hero Praneshacharya."),
("Which of the following statements about 'Hobson-Jobson' is correct?",["It is a glossary of Anglo-Indian words and phrases by Yule and Burnell, published in 1886.","It is a novel by G.V. Desani written in hybrid English.","It is Kachru's study of the Indianization of English.","It was compiled by William Jones for the Asiatic Society in 1784."],"Hobson-Jobson 1886, Yule and Burnell."),
]

AR_OPTS = ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
 "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
 "(A) is true but (R) is false",
 "(A) is false but (R) is true"]

def build():
    out=[]; k=0
    for m in M:
        if m[0]=="AR":
            out.append({"q":m[1],"options":AR_OPTS[:],"answer":m[2],"exp":m[3]})
        else:
            q,opts,exp=m; t=k%4; k+=1
            o=opts[1:]; o.insert(t,opts[0])
            out.append({"q":q,"options":o,"answer":t,"exp":exp})
    return out
