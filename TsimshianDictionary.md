

```latex
\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\graphicspath{ {./images/} }
\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan,}
\urlstyle{same}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage[version=4]{mhchem}
\usepackage{stmaryrd}

\title{Dictionary of Shm'algyack }

\author{Juneau, Alaska}
\date{}


\begin{document}
% \maketitle % Typically not needed for direct content extraction like this

% === Metadata Pages (Ignoring for JSONL extraction but kept for context) ===
% \section*{Dictionary of Shm'algyack}
% \begin{center}
% \includegraphics[max width=\textwidth]{2025_04_01_fa2e707e8f3cc318dfbfg-001}
% \end{center}
%
% \section*{TS995R2009}
% ©
%
% \section*{Please return to Alaska Native Language Archive University of Alaska Fairbanks (907) 474-7436 www.uaf.edu/anla}
% \section*{Dictionary of Shm'algyack}
% © 2009 by Sealaska Heritage Institute\\
% All rights reserved. No part of this publication may be reproduced or transmitted in any form or by any means, electronic or mechanical, including photocopy, recording, or any information storage or retrieval system, without permission in writing from the publisher.
%
% ISBN: 1440401195\\
% EAN-13: 9781440401190\\
% Library of Congress Control Number: 2008939132
%
% Sealaska Heritage Institute\\
% One Sealaska Plaza, Suite 301\\
% Juneau, Alaska 99801\\
% 907-463-4844\\
% \href{http://www.sealaskaheritage.org}{www.sealaskaheritage.org}
%
% Printing: Create Space, Scotts Valley, CA, U.S.A.\\
% Front cover design: Kathy Dye\\
% Front cover artwork: Robert Hoffmann\\
% Book design and computational lexicography: Sean M. Burke\\
% Copy editing: Suzanne G. Fox, Red Bird Publishing, Inc., Bozeman, MT
%
% \section*{Table of Contents}
% Acknowledgments................................ 1\\
% Introduction........................................ 3\\
% Dictionary of Shm'algyack\\
% Shm'algyack to English................ 7\\
% English to Shm'algyack................ 67
%
% \section*{Acknowledgments}
% We want to acknowledge the elders from Metlakatla, Alaska, who had the foresight to conceive the concept of this dictionary and compile a list of words more than twenty years ago. Those who have passed on are:
%
% Ira Booth\\
% Lillian Buchert\\
% Frances Duncan\\
% Bernard Guthrie\\
% Solomon Guthrie\\
% Russell Hayward\\
% Harold Hudson Charles Ryan
%
% Additionally, we thank these individuals for their contributions:\\
% Mel and Ruth Booth John Dalton\\
% Doris Reece\\
% Conrad Ryan, Sr.\\
% Sealaska Heritage Institute appreciates their contributions and recognizes their efforts to perpetuate and document Shm'algyack. \(L u\) 'kwil aam wila waalshm!
%
% This project would not have been completed without funding from the Administration for Native Americans and support from Sealaska Corporation. 'Doyckshn!
%
% \section*{Introduction}
% This is a first edition Shm'algyack-English dictionary compiled by Donna May Roberts for the Sealaska Heritage Institute. This dictionary was made possible by funding from the Administration for Native Americans. This edition was produced online as well as in CD-ROM and print formats. While this dictionary does not contain all the words in the Shm'algyack language, it covers the majority of the common vocabulary, and as such will be of great value to beginning and intermediate students of the language.
%
% The first section of this dictionary is Shm'algyack to English, and the second section is English to Shm'algyack.
%
% Guide to the Sounds of Shm'algyack\\
% Shm'algyack has a total of sixteen vowel sounds and thirty-four consonant sounds, yielding a total of fifty distinctive sounds.
%
% Most of the vowel sounds are quite similar to those in English.
%
% \begin{center}
% \begin{tabular}{cll}
% Shm'algyack Vowel &  & English Key Word \\
% \cline { 1 - 1 }
% \(\mathbf{a}\) &  &  \\
% aa & hat, cap, sack &  \\
% aaw & had, cab, sag &  \\
% aay & how, cow, now &  \\
% ai & fried, lied, died &  \\
% aw & pay, way, say &  \\
% \(\mathbf{e}\) & doubt, about, clout &  \\
% ee & bet, set, wet &  \\
% \(\mathbf{i}\) & bee, flee, tree &  \\
% ie & sit, sip, sick &  \\
% \(\mathbf{0}\) & die, lie, pie &  \\
% \(\mathbf{0 a}\) & on, off, often &  \\
% \(\mathbf{0 0}\) & similar to boa &  \\
% \(\mathbf{0 y}\) & room, boom, zoom &  \\
% \(\mathbf{u}\) & boy, toy, Roy &  \\
% \(\mathbf{u u}\) & but, cup, cut &  \\
%  & sounds like oo, with spread lips &  \\
% \end{tabular}
% \end{center}
%
% Many of the consonant sounds are also quite similar to those in English.
%
% \begin{center}
% \begin{tabular}{cll}
% Shm'algyack Consonant &  & English Key Word \\
% \cline { 1 - 1 }
% \(\mathbf{b}\) & big, bag, bug &  \\
% \(\mathbf{d}\) & dog, dig, dug &  \\
% \(\mathbf{d s}\) & beds, heads, weds &  \\
% \(\mathbf{g}\) & gold, got, go &  \\
% gw & Guam, Guatemala, guano &  \\
% gy & give, gig, gill &  \\
% \(\mathbf{h}\) & hot, hop, hock &  \\
% \end{tabular}
% \end{center}
%
% \begin{center}
% \begin{tabular}{ll}
% \(\mathbf{k}\) & con, cop, cot \\
% \(\mathbf{k w}\) & queen, quilt, quit \\
% \(\mathbf{k y}\) & kin, kit, kid \\
% \(\mathbf{l}\) & look, love, line \\
% \(\mathbf{m}\) & more, move, make \\
% \(\mathbf{n}\) & noon, nine, nose \\
% \(\mathbf{p}\) & pig, pick, pit \\
% \(\mathbf{s h}\) & shoe, she, shy \\
% \(\mathbf{t}\) & toe, tea, tie \\
% \(\mathbf{t s}\) & cats, bats, mats \\
% \(\mathbf{w}\) & will, wick, wit \\
% \(\mathbf{y}\) & you, yes, yeah \\
% \end{tabular}
% \end{center}
%
% There are other consonant sounds which are not usually found in English, but which are similar to sounds that some English speakers may know.\\
% ck a rasping sound similar to Scottish loch or German Bach \\
% gg a g sound produced further back in the mouth\\
% hl a hissing sound, like a cross between a whispered \(l\) sound and the English th sound in with. \\
% ' a sight, silent pause separating two sounds, like in English uh-oh \\
%
% Then there are the eleven pinched sounds. These sounds have an extra pinch or pop to them, very different from anything found in English. All of the pinched sounds are written with an apostrophe at the beginning:
%
% \section*{'b 'd 'ds 'k 'kw 'ky 'l 'm 'n 'w 'y}
%
% The writing system used in this dictionary was originally developed by the Elders from Metlakatla, Alaska, with the intention of making it easy for both speakers and learners to use. It has been modified over time to make it as consistent and accurate a system as possible.
%
% This orthography for Alaskan Shm'algyack is somewhat different from the official orthography used for Sm'algyax in British Columbia, as designed by the Sm'algyax Language Authority. The two orthographies have many points in common, however, and it is fairly easy to go back and forth between the two systems with a little bit of practice. The tables on the next page show how the two orthographies match up, first for the vowel sounds and then for the consonants.
%
% Vowels
%
% \begin{center}
% \begin{tabular}{|c|c|c|c|c|c|c|c|}
% \hline
% Alaska & BC &  & Alaska & BC &  & Alaska & BC \\
% \hline
% a & a & e & e &  & \(\mathbf{0 0}\) & uu &  \\
% aa & aa &  & ee & ii & oy & oy &  \\
% aaw & aaw &  & i & i &  & u & u \\
% aay & aay &  & ie & ay & uu & ü &  \\
% ai & ee &  & o & o &  &  &  \\
% aw & aw &  & 0a & \(\mathbf{0 0}\) &  &  &  \\
% \hline
% \end{tabular}
% \end{center}
%
% \section*{Consonants}
%
% \begin{center}
% \begin{tabular}{|c|c|c|c|c|c|}
% \hline
% Alaska & BC & Alaska & BC & Alaska & BC \\
% \hline
% b & b & ky & ky & 'd & \(\mathrm{t}^{\prime}\) \\
% \hline
% ck & \(\mathbf{x}\) & 1 & 1 & 'ds & ts \({ }^{\prime}\) \\
% \hline
% d & d & m & m & 'k & \(\mathrm{k}^{\prime}\) \\
% \hline
% ds & dz & n & n & 'kw & k'w \\
% \hline
% g & g & p & p & 'ky & k'y \\
% \hline
% gg & g & sh & \(s\) & '1 & '1 \\
% \hline
% gw & gw & t & t & 'm & 'm \\
% \hline
% gy & gy & ts & ts & 'n & 'n \\
% \hline
% h & h & w & w & 'w & 'w \\
% \hline
% hl & 1 & y & y & 'y & 'y \\
% \hline
% k & k &  & , &  &  \\
% \hline
% kw & kw & 'b & \(\mathrm{p}^{\prime}\) &  &  \\
% \hline
% \end{tabular}
% \end{center}
%
% Another important difference between the two orthographies is that the accent is not typically marked in the British Columbian orthography. In the Alaskan orthography, the accent can be marked through the use of capital letters (Shm'ALgyack), underlining (Shm'algyack) or italics (Shm'algyack). The accent shows which syllable in the word should be given the most prominence in pronunciation. In this dictionary, we have chosen to use italics for this purpose. Note, however, that we only do this when the word has two or more syllables.
%
% Some speakers and learners may also choose to add hyphens in between the syllables in a word (Shm-'al-gyack). We have chosen not to do that, but users may add them in if they so choose.
%
% The words in this dictionary are arranged in this order:\\
% ABCDEGHIKLMNOPSTUWY'
%

% === Shm'algyack to English Dictionary ===
\section*{aab}
noun my father\\
-Yagwa goom wunsh aabdu. My father is hunting for deer.\\
\section*{aad}
noun; verb net; to seine Plural:ga'aad\\
-Geegsh Dzon shu aad dm hoyt hla aadmhoant. John bought a new net for fishing.\\
\section*{aadm hoan}
verb to fish with a net, seine for fish\\
-Dm aadm hoanm sha gya'wn. We will fish with a net today.\\
\section*{aadsack}
verb to be long enough, reach across PLURAL: ack'aadsack\\
-Aadsacka hagwilhoo. The rope is long enough.\\
-Aadsacka hagwilhoo da na boadm. The rope is long enough for our boat.\\
\section*{aadsik}
verb to be straight\\
-Aadsika guyna da awaa waabn. The path by your house is straight.\\
\section*{aah}
noun edible root; fern-like plant\\
-Ndahl wil 'dahla aah? Where do the edible root plants grow?\\
\section*{aalck}
verb to be bold, brave, courageous PLURAL: al'aalck\\
-Ap lu'kwil al'aalcka hlaagigyad. The old timers were very courageous.\\
\(-\) Lu'kwil al'aalcka gibaaw. The wolf acted very bold.\\
\section*{aam}
verb to be fine, good, well PLURAL: am'aam\\
-Aam wila howyu. I'm feeling good.\\
\(-\) Na sheepg nakshu ashda 'guulda shada dowl mahlda doctor hla aam wila waald gya'win. My wife was sick the other day but the doctor said she's good now.\\
\section*{aamggashgaawt}
verb to be medium size, of a good size\\
-Aamggashgaawt ga yeeh. The King salmon was of a good size.\\
\section*{aamhalaayt}
noun headdress, mask, regalia, shaman's mask; shaman PLURAL: gaamhakhalaayt\\
-Naahl en dsaba aamhalaayt hoysh Dan? Who made the headdress that Dan is wearing?\\
\section*{aamndap}
noun right amount; correct, accurate assessment\\
-Aamndapa sha 'naga taggan. The plank is the right length.\\
\section*{aamshgaboo}
verb to be enough, adequate, ample, plentiful\\
-Hla aamshgaboo wineaya gwa'a. There's enough food here.\\
-Hla aamshgaboo lag. That's enough wood.\\
-Na oom hoan 'yoota gwee da aamshgaboo 'maget. That man went fishing and he got enough.\\
\section*{aamshga'nak}
adverb; verb after a while; to be far enough, long enough\\
-Dm yaawckga'nu dsihla aamshga'nak. I will eat after awhile.\\
\section*{aatk}
noun night\\
-Tcka'nooyu gwitgwineeksh hla aatk. I heard the owl at night.\\
\section*{aa'back}
verb to recall, remember\\
-Aa'backdu shga 'tsamaatga shameeym wun. I remember how good deer meat tastes.\\
\section*{ab}
noun bee, hornet, yellow jacket\\
-Gyehlga'nu ab. I got stung by a bee.\\
\section*{aba'ackshg}
verb to be anxious\\
-Ahlgadee aam shga aba'ackshgn. It's not good that you're so anxious.\\
\(-\) Lu'kwil aam lacka, aba'ackshgu dm 'gwihl yaayu. The weather is real good, I'm anxious to go walking.\\
\section*{aboo}
verb to be a few, some, several\\
-Aboo gyad gatgoidikshd. A few people came.\\
-Lu'kwil aboo hoan 'goahla gwa'a. There's few fish this year.\\
\section*{ada}
conjunction and\\
-Ada weehowtga hana'ack hlat nee wil badsga boad. And the woman cried when she saw the boat arrive.\\
\section*{adaahl}
noun fire in the water; phosphorescent algae\\
-Needsu wil lu'gwil goi'pa adaahl. I see that the fire in the water is very bright.\\
\section*{adaawck}
noun legend, folktale, story; title\\
-Wilaaysh Silas adaawck, aam shm ama amookshn. Silas knows stories, it's good to really listen.\\
\section*{adabeesh}
noun butterfly\\
-Shm mashga adabeesh. The butterfly is very red.\\
\section*{adaggan}
noun ghost bread\\
-Goayu adaggan? What is ghost bread?\\
\section*{adashged}
noun spider\\
-Baasha'nu da adashged. I'm afraid of spiders.\\
\section*{adsiksh}
verb to be arrogant, haughty, proud, snobbish, stand-offish\\
-Adsiksha ggoadu. My heart is proud.\\
-Lu'kwil adsiksha wila how ggoadu da shga hultga hoan da'ackgu. My heart is proud of how much fish I was able to get.\\
\section*{agwee}
prefix distant\\
-Agwee wil 'daa waabsh Li'ihl. Henry's house is in the distance.\\
\section*{agwee hluk'kwdaa'yn}
noun great-grandchildren\\
-Hladm goidiksha agwee hluk'kwdaa'ynu. My great grandchildren will soon be here.\\
\section*{ahl aamdee?}
phrase Is it good? Okay?\\
-Ahl aamdee maay gwa'a? Is this fruit good?\\
-Ahl aamdee hoan gwee? Is it okay to fish there?\\
\section*{ahlga}
prefix not\\
-Ahlgadee aam wila how sha'winshga gwa'a. What this paper says is not good.\\
\section*{ahlgadee goa}
noun nothing\\
-Ahlgadee goahl geegee I bought nothing.\\
\section*{ahlga ga ggontgahl}
verb to be unclear\\
-Ahlga ga ggontgahla wila haw 'yoota. What the man said was not clear.\\
\section*{ahlyeeggawsh}
noun hummingbird\\
-Needsu hailda ahlyeeggawsh da ggaldoa. I saw a lot of hummingbirds where we camped.\\
\section*{ahl'bal}
verb to misbutton\\
-Ahl'bal na kshlushgt. She misbuttoned her blouse.\\
\section*{aigyad}
verb to be durable, live a long life\\
-Aygyadid maata awil amaneedsda goa gubt. Martha lived a very long life because she was careful about what she ate.\\
\section*{aipn}
verb to be lightweight\\
-Aipn hlgu gwai'hl. The sack was pretty light.\\
-Aipn hlgu gwai'hl, da'acklga hlguwoamhlg dmt badst. The sack was pretty light, the little child will be able to lift it.\\
\section*{aishk}
verb to owe; to promise\\
-Nda shgaboo daala aishken? How much money do you owe?\\
\section*{ai'dsm anaay}
noun fried bread\\
-Hashacku aildsm anaay. I want fried bread.\\
\section*{ai'dsm hoan}
noun fried fish\\
-Ai'dsm hoan 'ka 'tsamaa'anu. I like fried fish best.\\
\section*{aksh}
verb; noun to be wet, to drink; water PLURAL: ak'aksh\\
-Gushcka aksha gwa'a. This water is bitter.\\
\(-\) Lu'kwil tsamaatga aksha gwee. That water tastes really good.\\
\section*{akshilshgm maadm}
noun sleet; wet snow\\
-'Dsuu akshilshgm maadm ashda gi'dseeb. There was a lot of wet snow yesterday.\\
\section*{akshyaa}
verb to accumulate, get fat, increase PLUEAL: akshwaalcksh\\
-Dm akshyaa wun da 'goahla gwa'a. There will be more deer this year.\\
-Na dsabu ash asda gi'dseeb da akshyaat dowla dp gubt. I made some soapberries the other day and it increased and we ate it.\\
\section*{akshyaagwa dseewsh}
noun dawn, daybreak\\
-Dm dawhla boad dsihla akshyaagwa dseewsh. The boat will leave at dawn.\\
\section*{ala}
noun chimney, smoke hole\\
-Ahlgandee nee 'dbiyaan a ala. I don't see any smoke coming from the chimney.\\
\section*{alaaysh}
verb to be lazy PLURAL: ak'alaaysh\\
-Giloa alaayshn. Don't be lazy.\\
-Na hootgu hlguhlgu dumt hlimoame bite alaayshd. I called my son to help me but he was lazy.\\
\section*{alashkw}
verb to be diluted, weak PLURAL: huk'alashkw\\
-Na dm badsu 'wee ggan gwee dowl ggal alashkwu, hlgookshnt. I was going to pick up a big wood but I was too weak and I couldn't.\\
\section*{alda}
noun fir tree\\
-Alda hoy gyad hlat dsaba waab. People use fir to build a house.\\
\section*{algyack}
noun; verb spoken or written word; to speak, talk\\
-Aam wila how liplaid hla algyackd. The preacher sounds good when he speaks.\\
\section*{algyackshg}
noun big man, Chief, noble\\
-Wun algyackshg a tcka'nee ggaldsapdsap. There are nobles in every village.\\
\(-\) Lu'kwil algyackshga Shm'oygit. The chief was a very big man.\\
\section*{aloobaa}
verb to run fast\\
\(-\) Lu'kwil aloobaa hlguwoamhlg. The child ran very fast.\\
\section*{amadaalck}
verb to praise, show respect\\
-Amadaalckd melee na hlguhlgm 'yoot. Mary was full of praise for her son.\\
\section*{amadsab}
verb to be completed, well-designed, well-proportioned; to do over, fix, repair\\
-Amadsaba wila waal goa dm wila gyoayu. What I do will be well designed.\\
\section*{ama gyad}
verb to be kind\\
-Anoacku shga ama gyada 'yoota gwee. I like the way that man is very kind.\\
\section*{amane'ets}
verb to be careful, cautious, watchful\\
-Amaneedsin nda wil yaan. Be careful of where you walk.\\
-Amaneedsn wila gyoan, ahlga dm dee shgaaygshgn. Watch what you're doing, it's not good that you get hurt also.\\
\section*{Ama shu'goahl}
phrase Happy New Year\\
-Ama shu'goahl. Happy New Year.\\
\section*{amawaal}
verb to be rich, wealthy\\
-Ha'wahlgadee amawaalu. I'm not wealthy yet.\\
-Amawaal 'yoota gwee, hailda daalat. That man is wealthy, he has a lot of money.\\
\section*{ama'bash}
verb to be beautiful, good looking, handsome, pretty PLURAL: amamacksh\\
-Lu'gwil ama'basht Dan. Dan is very handsome.\\
-Na needsu hlgu hana'ack da lack geeka, dowl lu'kwil ama'basha wila dsabt hla yaat. I saw a woman on the beach and she looked pretty when she walked.\\
\section*{ameelg}
noun disguise, effigy, mask\\
-Goahl wilsh ameelga hoyan? What mask are you wearing?\\
\section*{amgeeg}
noun black duck\\
-Hailda amgeeg wil ggaldsoackum. There are a lot of black ducks where we camped.\\
\section*{amggan}
noun red cedar\\
-Amggan hoy gyad hlat dsaba p'tsaan. People use red cedar to make a totem pole.\\
\section*{amhow}
noun voice\\
-Hoyska amhowsh Debbie hla leemeet. Debbie's voice is beautiful when she sings.\\
\section*{amooksh}
verb to listen, obey, pay attention\\
-Amookshn hla wil algyacka Shm'oygit. Listen when the Chief speaks.\\
\section*{amoosh}
noun corner of house\\
-Shguu ha'li'daa da amoosha waab. Put the chair in the corner of the house.\\
\section*{am'baal}
noun cottonwood tree\\
-Am'baal hoyu da waab shi'biyaanshg. I used cottonwood in the smokehouse.\\
\section*{anaash}
noun hide, skin Plural: ak'anaash\\
-Wok 'dsack'dsackga na anaashu. My skin is itchy.\\
\section*{anaay}
noun bread\\
-Dm geegu anaay da noayu. I am buying some bread for my mom.\\
\section*{aneesh}
noun tree branch\\
-'Gwasha aneesha ggan wil 'tsuu baashg. The tree branch broke during the strong wind.\\
\section*{anoagg}
verb to agree, allow, give permission; to like\\
-Anoaggu dm hee ggaldmwa'atn. I give you permission to go to the store.\\
\section*{anoahl}
verb to allow, let\\
-Ahlgadeet anoahl dm 'dseen doosh. She didn't let the cat come in.\\
\section*{an'on}
noun arm, hand Plural:gga'an'on\\
-'Woamckga an'Onu. My arm is aching.\\
\section*{aplugawdee}
verb to empty, make empty\\
-Aplugawdee ggaldm moan. The salt container is empty.\\
\(-\) Na 'kwihl yaa'nu da guyna da lugawdee aksh dm 'kenu, luyeltgu. I walked around the street and my water ran out, I went back. apluGAWdee\\
\section*{ash}
noun soapberries\\
-Yagwa gubu ash. I am eating soapberries.\\
\section*{ashdee}
prefix to make a mistake\\
-Ashdee waalu hlan geega shu 'dsig'dsig. I made a mistake when I bought a new car.\\
\section*{ashdeewaal}
verb to have an accident, make a mistake\\
-Giloa ashdee waaln. Nee gyad wila gyoan. Don't make mistakes. People see what you're doing.\\
\section*{ashee}
noun foot, leg Plural: ggashishee\\
-Shgaaygshga asheeyu. I foot hurts.\\
\section*{ashguu}
verb to be funny, humorous\\
-Ashguu hlgu hash. The little dog was funny.\\
-Na 'dsilaayu nabeebu da up lu'kwil ashguu wila gyoad. I visited my uncle and he was really funny.\\
\section*{ashgyaback}
noun chatterbox\\
-Du! lu'kwil ashgyabacka 'yoota gwee. Good grief! That man is really a chatterbox.\\
\section*{ashwn}
noun sea urchin\\
-Gilmt nabeebu ashwn da 'koy ada lu'kwil 'tsamaatgt. My uncle gave me sea urchin and it was very tasty.\\
\section*{awaa}
particle at, by, near\\
-'Daan da lack ha'li'daa da awaa likshoack. Sit on the chair by the door.\\
\section*{awaan}
particle there\\
-Shguu ha'li'dameesh da awaan. Put the table there.\\
\section*{A-wil goa?}
interrogative why?\\
-A-wil goa, dayat noat. Her mother said, why?\\
\section*{awsh}
noun sand\\
-'Yagayaayu da geeka, 'waa wil awsh, da 'nee nwil giguul gaboack. I went down the beach, found sand, that's where I looked for cockles.\\
\section*{awta}
noun porcupine\\
-Ha'wahlgandee neehh awta. I haven't seen a porcupine.\\
\section*{awul}
prefix aside, away\\
-Awul gushga gganaow a lack guyna. The frog jumped away from the road.\\
\section*{awul'mag}
verb to put aside, put away; to sidetrack\\
-Ndm awul'maga hoan. I'm going to put the fish aside.\\
\section*{aw'awshg}
verb to be curly\\
\(-\) •u'kwil hashacku aw'awshgm ggowsh. I really want curly hair.\\
\section*{ayaaltg}
verb to be fortunate, lucky\\
-Ayaattga'nm, 'needee? We're lucky, aren't we?\\
-Na oom hoanu ashda 'guulda shada dowl lu'kwil ayaaltgn, da'ackga 'wee yeeh. I was fishing the one day and you were lucky to catch a big King Salmon.\\
\section*{ayaawgg}
noun decree, message, official statement\\
-Ayaawgga Shm'oygit da wila waal shahoan. The Chief gave an official statement about the fishing.\\
\section*{ayam}
verb to throw, pitch\\
-Ayam oy hla'at. Pitch the ball.\\
\section*{ayamgwai}
particle almost there\\
-Hla ayamgwai 'dsig'dsig. The car is almost there.\\
\section*{ayamgwa'a}
particle almost here\\
-Hla ayamgwa'a boad. The boat is almost here.\\
\section*{ayawaa}
verb to shout, yell PLURAL: ayaluwaa\\
-Ayawaa hlguwoamhlg hlat needsu. The child cried out when he saw me.\\
\section*{ayin}
interjection no, not so\\
-Ayin. ahlgadee hashacku uushgmlaan. No. I don't want stink eggs.\\
\section*{ayow}
interjection expression when sighting fish jump\\
-Ayow! Daya gyad hlat nee wil gusha hoan. aYOW! That's what people say when they see fish jump.\\
\section*{aytk}
verb to name, call by name PLURAL: ak'aitk\\
-Wie aam dm aytga na waam 'Tsmshiant. It is time to call her by her 'TsmSHIAN name.\\
\section*{ayuwaan}
verb to stay away for a long time\\
-Giloa ayuwaan Don't stay away.\\
\section*{a'waa'ackshg}
verb to be a hard worker, industrious\\
\(-\) Lu'kwil a'waa'ackshgat Da'apsh. David is very industrious.\\
-Lu'kwil a'waa'ackshga 'yoota gwee dumt wilaay dm hadiksh. That man is working hard to learn how to swim.\\
\section*{baa}
verb to run Plural: 'kahl\\
-Baa hlgu hash hla hashackt dm galmeelgt. The little dog runs when it wants to play.\\
\section*{baahlk}
noun operation, surgery\\
-Ahl sheepga wil baahlgn? Does it hurt where you got operated?\\
\section*{baal}
verb to feel; to try, venture Plural: bubaal\\
-Baaldu ndm guba shameeym ol - ahlgandee anoackt. I tried to eat bear meat - I don't like it.\\
\section*{baal'ack}
noun corpse, ghost Plural: bibaal'ack\\
-Baasha'nu ndm needsu baal'ack. I'm afraid to see a ghost.\\
\section*{baash}
verb to be afraid Plural: lebaash\\
-Baasha doosh hlat nee hash. The cat was afraid when it saw the dog.\\
-Baashu da wila waal ggoadu, mahla doctor shgu dumt dsabt. I was afraid of how my heart was, the doctor said I had to have it fixed.\\
\section*{baashg}
verb; noun to blow; wind\\
-Gatgyeda baashg wil hultga giamg. The wind is strong when the moon is full.\\
\(-\) Na dm hee Gitsgaanu ashda 'guulda sha ggal 'dsuu baashg dowla giloam. I was going to Ketchikan one day and the wind blew too hard so we quit.\\
\section*{babaa}
verb quiver (of the chin), tremble\\
\(-\) Lu'kwil babaa hlgu ahlyeeggawsh. The little hummingbird really trembled.\\
\section*{babood}
verb to wait, await\\
-Giloa aba'ackshgn, baboodee. Don't be anxious, wait for me.\\
-Baboodee. Wait for me.\\
-Baboodihla boad. Wait for the boat.\\
\section*{back}
verb to taste\\
-Backu shameeym ol - ahlgandee anoackt. I tasted bear meat - I don't like it.\\
\section*{backbeega'aksh}
noun gale, waterspout\\
-Backbeega'aksh ashda gi'dseeb. There was a strong gale yesterday.\\
\section*{backyaa}
verb to go, move, walk up along the ground PLURAL: backwaalcksh\\
-Dm backyaam da awaa lack 'daa dm guul maay. We're going to walk up to the lake to gather berries.\\
\section*{bads}
verb to lift\\
-Badsa ha'li'daa ada 'dooshgn da na hluut. Lift the chair and sweep under it.\\
\section*{badsg}
verb to arrive, land\\
-Hla badsga 'yoota gwee dowl awaayu wil goyt. The man arrived and came to me.\\
\section*{baloash}
noun syrup\\
-Baloasha hoyu hlan guba ai'dsum anaay. I use syrup when I eat fried bread.\\
-Da'ackgu ndm ksha guba baloash. I can just eat syrup by itself.\\
\section*{ban}
noun abdomen, belly, stomach, tummy\\
-Sheepga banu hlan guba ggal hailda anaay. My tummy hurts when I eat too much bread.\\
\section*{bana}
noun dip net, net brail\\
-Bana hoy gyad wil hailda hoan. People use a dip net when there are lots of fish.\\
\section*{bashackg}
verb to be divided\\
-Bashackga hla'ashg da lack loab. Divide up the seaweed on the rock.\\
-Labite hlikhloontee gyad dowl bashackghl goa wila waalt. The people got angry then they get divided.\\
\section*{bayck}
verb to tear, pull bark from cedar tree\\
-Ahlgandee da'ackhlga ndm baycka ggan. I'm not able to tear the bark from the tree.\\
\section*{bayckggan}
verb gather cedar bark\\
-Shguu dm bayckggm da dsigi'dseeb. We have to gather cedar bark tomorrow.\\
\section*{ba'a}
noun father\\
-Needsu ba'an da awaa waab shgool. I saw your father by the school.\\
\section*{beeb}
noun uncle\\
-Yagwa goom leetsgut nabeebu. My uncle is hunting for grouse.\\
\section*{bee'eg}
noun falsehood, lie\\
-Giloa bee'egn. Don't lie.\\
\section*{beyaalsh}
noun star\\
-Lu'kwil goi'pa beyaalsha gwee. That star is very bright.\\
\section*{beyaalshm aatk}
noun evening star\\
-Ha'weenhl needsinee beyaalshm aatk? Haven't you seen the evening star?\\
\section*{beyaalshm gganhlaag}
noun morning star\\
-Ha'weenhl needsinee beyaalshm gganhlaag? Haven't you seen the morning star?\\
\section*{be'an}
noun meadowlark; songbird\\
-Ama'basha na leemee hlgu be'an. The meadowlark makes pretty music.\\
\section*{bilaan}
noun belt\\
-Hashacku shu bilaan. I want a new belt.\\
\section*{bilagg}
noun moss\\
\(-\) Lu'kwil goamtga bilagg. The moss is very soft.\\
\section*{bilha}
noun abalone\\
-Ggal hailda gyada en guguul bilha. Too many people are searching for abalone.\\
\section*{bishboosh}
verb to chop, split wood\\
-Bishboosha ggan gwa'a, ggal 'weelaeksht. Chop up this wood, it's too big.\\
-Dm bishbooshu ggan gwee dm shalagshu. I'm going to chop that wood to build a fire.\\
\section*{biyaackl}
noun cliff, rock wall\\
-Shee'nu wil tgineeetsgu da biyaackl. I was dizzy when I looked down the cliff.\\
\section*{boad}
noun boat\\
-Dm kshagyoatguu da Ta'gwaan da 'dsm boad. I am going to Metlakatla by boat.\\
\section*{booboo}
verb to fall, splash\\
-Giloammdz anoacka dm booboo aksh. Don't let the water splash.\\
\section*{boods}
noun boots\\
-Guguul na boodsu. Look for my boots.\\
\section*{boosh}
verb to split, to chop\\
-Ahlgandee bishboosha lag awil 'gwaatga na gigyoatgu. I didn't chop the wood because my axe is lost.\\
\section*{booyshg}
verb to expect, hope for, wait for\\
-Booyshga hlguwoamhlg na noat. The child waited for his mother.\\
-Hla booyshgu dm goidiksha hoan. I'm waiting for the fish to come.\\
\section*{boo'ihl}
verb to get out of the way; to make aware, warn\\
-Ama nee wila yaan. Hla goidiksha 'dsig'dsig, aam boo'ishgn. Be careful where you walk. The car's going to come, you should get out of the way.\\
-Boo'ihla 'dsig'dsig dsihla hloat. Be aware of the car if it's fast.\\
\section*{bou'ish}
noun monkey\\
-Nda bou'ish da Macklackaahla? Where are the monkeys in Metlakatla?\\
\section*{ckaa}
noun slave\\
-Hlgu ckaa en shakshen waab. The slave cleaned the house.\\
\section*{ckaatg}
verb to spoil, decay\\
-Ooshga ckaatgm wineaya. Decayed food smells bad.\\
\section*{ckaaytg}
verb to turn over, upset (of a canoe or boat)\\
\(-\) Lu'kwil baasha'nu dm ckaaytga boad. I'm afraid that the boat will turn over.\\
\section*{ckaldaawckg}
noun medicine\\
-Aam guba ckaldaawckga 'gilmsh noan, sha damoatgn. It's good to eat the medicine your mother gave you, it will save you.\\
\section*{ckaygg}
noun foam\\
-Ahl needsinee wil 'tsuu ckaygg da hahl-geeka? Have you see where there's a lot of foam down the beach?\\
\section*{ckbaala}
noun west wind\\
-Tcka'nooyu dm gatgyada ckbaala dsigi'dseeb. I heard that the west wind will be strong tomorrow.\\
\section*{ckbaickshg}
verb to saw\\
-Ha'weenhl ckbaickshgt George taggan? Hasn't George sawed the planks yet?\\
\section*{ckbashm 'ka'kackd}
particle upside down\\
-Geedsa ckbashm 'ka'kackda ckshoa da wil 'tsuu baashg. The canoe almost turned upside down because of the strong wind.\\
\section*{ckbeesh}
noun box\\
-'Kacka 'ka 'weelaekshm ckbeesh. Open the bigger box.\\
\section*{ckbeeyaa}
verb to deliver information; to walk house to house\\
-Ckbeeyaa 'yoota hla wil goidiksha uua. The man delivered information about the arrival of the ooligans.\\
\section*{ckbeeyay}
noun half, part of\\
-Na goo wunu ashda 'guulda sha, goo wun, da 'gilmu ckbeeyay da hlguyu. I went hunting one day, shot the deer, and I gave half of it to my children.\\
\section*{ckbishmshguu}
verb to bend, bend over, bow\\
-Ckbishmshguu gyada na 'dmggowshd hla gigeengwackhld. People bow their heads when they pray.\\
-Na ckbishmshguu n'dse'etsu hla weehowtgd. My grandmother bent over when she cried.\\
\section*{ckdaiksh}
verb to eat Indian ice cream\\
-Aba'ackshgu dm wil yaa maadm awil lu'kwil anoacku ckdaiksh. I'm anxious for the snow to fall because I really like Indian ice cream.\\
\section*{ckdee}
verb to eat with\\
-Dm ckdeeym wilaayshgm dsihla Ha'li Shgwaitga sha. We're going to eat with our relatives on Sunday.\\
\section*{ckdsee}
verb to be thick (ice, board, fog, etc.)\\
-Hagwil baa boad da wil ckdsee yain. The boat ran slowly when the fog was thick.\\
\section*{ckdso'otsk}
noun hawk\\
-Ahlgandee neehl ckdso'otsk shga 'naga wil ggaldsockm. I haven't seen a hawk since we've been at our camp.\\
\section*{ckgwatksh}
verb feel cold\\
-Lu'kwil ckgwatksha 'woa'da gyad. Elderly people really feel cold.\\
\section*{ckhoan}
verb to eat fish\\
-Wiedsa ckhoanm. Let's eat fish.\\
\section*{ckleeuu}
verb to burst PLURAL: ggackleeuu\\
-Aba'ackshga hana'ack wil ckleeuu hla'at. The woman got anxious when the ball burst.\\
-Ggal 'dsuu wila yaawckgn dowla dm ckleeuu na ggaloashn. If you eat too much your stomach will burst.\\
\section*{cklggoan}
verb to pay\\
-Ayinhl dm cklggoant 'need? Aren't you going to pay him?\\
\section*{cklggoa'oam}
noun payment\\
-Naahl dm en cklggoam da ckshoa? Who will pay us for the canoe?\\
\section*{ckshaan}
noun mosquito larvae\\
-Shguu mdm kwhlee dsaga ckshaan. We need to kill all of the mosquito larvae.\\
\section*{ckshaangg}
verb to disagree, disbelieve, doubt\\
-Ckshaanga'nu goa wila how 'yoota gwee. I disagree with what that man said.\\
\section*{ckshan}
verb to gamble\\
-Ahlgadee aam ckshan gyad. It's not good for people to gamble.\\
\section*{ckshdaa}
verb to win (a game, war)\\
-Dsida ahlgadee ayaaltgn, ahlga dm ckshdaan. If you're not lucky you won't win.\\
\section*{ckshdaamck}
verb to make a loud noise\\
-Lu'kwil ckshdaamcka gga'bala. The gun made a very loud noise.\\
\section*{cksheet}
verb to vomit PLURAL: lacksheet\\
-Cksheeta hlguwoamhlg da ggal 'naga weehowtgt. The child vomited from crying too long.\\
\section*{ckshgeeg}
noun eagle\\
-Hailda ckshgeeg da wil 'daam. There are lots of eagles where we are.\\
\section*{ckshwa'dackg}
noun whistle\\
-Ckshwa'dackga 'yoota hlat nee ama'bashm hana'ack. The man whistled when he saw a beautiful woman.\\
\section*{cksh'dock}
verb to sleep\\
-Ggal giamga waab, 'nee gun geedsa cksh'docku. The house was too warm, that's why I almost fell asleep.\\
\section*{cksh'waanck}
noun herring eggs\\
-Eh! 'Tsamaatga cksh'waanck 'gilm gyad 'kam. Oh boy! The herring eggs that people gave us tastes very good\\
\section*{ck'biyaan}
verb to smoke tobacco\\
-Ahlgadee aam dm ck'biyaan gyad. It's not good for people to smoke.\\
\section*{daahl}
vocative dear miss or woman\\
-Daahl, dm shm amooksha'nu da 'kwan. Dear Miss, I'm really going to listen to you.\\
\section*{daala}
noun money\\
-Giloamdsa 'gwaatga na daalan. Don't lose your money.\\
\section*{daalck}
verb to advise, counsel; to rebuke, scold, talk to in a mean manner\\
-Shm ama 'daa hlguwoamhlg hlat daalckat noat. The child sat still when his mother scolded him.\\
-Na didaalcku hlguhlgm hana'ack goa dm wila gyoat. I advised my daughter about what she should do.\\
\section*{daamshack}
verb to faint, pass out Plural:dmdaamshack\\
-Geedsa daamshacka hana'ack hlat nee shgaboo daala. The woman almost fainted when she saw how much money there was.\\
\section*{daaw}
noun; verb ice; to freeze plural: dudaaw\\
-A-yaaltgm sha gya'wn. Da'ackhlgm dm sha daaw wineayam. We're lucky today. We are able to freeze our food.\\
\section*{daayksh}
noun Indian ice cream\\
-'Guulda waalm da 'nak doashda, dat Peter Fawcett, Peter Wesley 'nahowyu, dsaba daayksh da 'kam, da up oa, wilaay 'yoota gwee dsabt. This is one thing we did, Peter Fawcett, I mean Peter Wesley, made Indian ice cream, and oh boy, that man really knew how to make it.\\
\section*{dackhl}
noun hammer\\
(-)'Gwaatga na dackhlu. My hammer is lost.\\
\section*{dacksh}
noun flounder\\
-Anoacka umsheewa dacksh. White men like flounder.\\
\section*{dackshmhietk}
verb to stand still\\
-Dackshmhietga hlgu hash hlat tcka'noo wil ckshwa'dackga 'yoota. The dog stood still when he heard the man's whistle.\\
\section*{dackshm'daa}
verb to obey, sit still; to stay at home PLURAL: dackshmwun\\
-Shguu dm dackshm'daan ada amookshn da wil howsh noan. You should sit still and listen to what your mother has to say.\\
\section*{dackyaagw}
verb to hold, hold fast, hold tight\\
-Dackyagwa hagwilhoo. Hold the rope tight.\\
\section*{dackya'wa}
verb to grip, hold\\
-Wie dackya'wa an'onu. Labiet shoonsha'nu. Take a hold of my arms. I'm blind.\\
\section*{daintg}
verb to lead\\
-Aam sha daintgu. Lead me.\\
\section*{dakhl}
verb to tie, tie around\\
-Dakhla hagwilhoo da kwduun ckbeesh. Tie the rope around the box.\\
\section*{dal}
noun; verb fight, conflict; to fight Plural: dildal\\
-Hladm dildal hashhaasha gwee. Those dogs are going to fight.\\
\section*{dalbikshg}
verb to shrink\\
-Dalbikshga hoaya dsida ggal giamga aksh. The clothes shrink if the water's too warm.\\
\section*{dalpg}
verb to be short PLURAL: dildalpg\\
-Ggal dalpga taggan 'kotsu. The plank I cut is too short.\\
-Dalpga wila waal 'yoota gwee. It's a short ways to where the man is.\\
\section*{dalpgm gganggan}
phrase short trees\\
-Ahlgandm 'kotsa dalpgm gganggan. I'm not going to cut the short trees.\\
\section*{dam}
verb to hold, hug, squeeze\\
-Ludamsh peda hlgu hasht hlat 'waayt. Peter hugged his dog when it was found.\\
\section*{damckg}
verb to be taut, tight\\
-Damckga ha'li 'yackgu. My clothes line is tight.\\
-Na hailda goa na gubu da 'wee damckga na ggal'oashu. I ate too many things then my stomach was tight.\\
\section*{damckhl}
noun friend\\
-Dm 'gilmu madsiggalay da damckhlu. I'm going to give my friend a flower.\\
\section*{damoatg}
verb to save\\
-Aam dm damoatgm na algyackm. It's good to save our language.\\
\section*{damshg}
verb to hold, squeeze\\
-Giloamdsa damshga hoan. Don't squeeze the fish.\\
\section*{damtee}
noun fern-like plants\\
-Dup 'leedoaym hoan da lack damtee. We put the fish on the fern (leaves).\\
\section*{dap}
noun; verb liver; to judge, try in court, measure\\
-Dm dapmt lalee. We're going to judge Larry.\\
\section*{dashgyan}
noun emery wheel, whet stone\\
-Hashacku shu dashgyan. I want a new whet stone.\\
\section*{daway}
noun goat\\
-Ahlgandee gubhl daway, 'nee gn ahlgandee wilaayhl goahl dm wil howyu da gwa'a. I've never eaten goat, that's why I don't know what to say about it.\\
\section*{dawhl}
verb to depart, go away, leave\\
-Sha gya'win dm wil dawhlsh Dzon da Macklackaahla. John will leave for Metlakatla today.\\
-Na dawhla hlguhlgu da Gitsgaan. My child left for Ketchikan.\\
\section*{dawhln}
verb to go away\\
-Ndahl dm wil daawhln da Gitsgaan? When are you going away to Ketchikan?\\
\section*{da'ackhlg}
verb can, to be able\\
-Da'ackhlgu ndm dsaba waabm hash. I am able to make a dog house.\\
\section*{da'ash}
noun aunt\\
-Dm 'gilmu hoan da da'shu. I'm giving fish to my aunt.\\
\section*{da'ka'aaw}
noun sea anemone\\
-Ahl 'waayanee da'ka'aaw? Have you found any sea anemone?\\
\section*{da'oack}
noun cheek\\
-Hashacku ndm gyehla hlgu da'oackn. I want to poke your little cheeks.\\
\section*{debaa}
verb to run away with\\
-Wiedsa dp debaa boad ada gwin daawhlm da Gitsgaan. Lets run away with the boat and go over to Ketchikan.\\
\section*{debeesh}
noun agility, performance, poise\\
-Lu'kwil debeesha 'yoota hla meelgd. His dancing was done with poise.\\
\section*{deckhlga giamg}
noun halo around the moon\\
-Shanaahlga wil deckhlga giamg. The halo around the moon is amazing.\\
\section*{dedsa'bil}
verb to play with compulsively\\
-Giloama dedsa'bil na ggawshn. Don't play compulsively with your hair.\\
\section*{dee}
noun hill\\
-Lack dee awaan wil wun wun. The deer can be found on the hill there.\\
\section*{deelmckg}
verb to answer, reply\\
-Goahl gn ahlgadee deelumckgt? Why didn't she answer?\\
-Na guuduckdu hlguwoamhlga gwee goa wila gyoat dowla deelmckgt da 'koy. I asked the child what she was doing and she answered me.\\
\section*{deeltg}
verb to retaliate, take revenge\\
(-).Lu'kwil hashacka 'yoota dm deeltgd. The man really wanted to take revenge.\\
\section*{deetck'aksh}
noun high tide\\
-Dm gwindaawhlm da Gitsgaan dsihla deetck'aksh. We'll go over to Ketchikan when the tide is high.\\
\section*{de'kwun}
verb to be very ripe\\
-Ha'weenhl de'kwun moalksh? Aren't the crabapple ripe yet?\\
\section*{diboygid}
noun shrew, small mouse\\
-Na ggalmeelgm da lack geeka dowl dsaggabaa hlgu diboygid. We were playing down on the beach when a little mouse ran across.\\
\section*{didoa}
verb to have, own Plural:doa\\
-Didoa hailda 'dsoacksh da 'koy. I own a lot of shoes.\\
-Doa hailda ggaid da 'koy. I own lots of hats.\\
\section*{didoolsh}
verb to be alive\\
-Hloula didoolsha hlgu 'yoota. The young man is still alive.\\
-Na goo wunu ashda 'guulda sha, goo wun. Hloula didoolsht hla gwn ackgu da awaat. I went hunting one day and I shot a deer. It was still alive when I got there.\\
\section*{dihl}
conjunction and\\
-Hla goamshm dihl magwa'ala dihl goaym. In the early winter, the late winter, and in the spring.\\
\section*{dipckan}
noun stump, old tree still standing\\
-Hloula hietga dipckan. That old cedar stump is still standing.\\
\section*{di'deeld}
verb to do faster, quickly\\
-Di'deelda hahlalsha'nm hla hashackum dm meelgm. We do things faster when we want to dance.\\
\section*{doashda}
noun across the way, the opposite side\\
-Doashda wil wun hailda gibaaw. There are a lot of wolves across the way.\\
\section*{doa'yil}
noun spoiled person\\
-Doa'yil hlguwoamhlg, 'neegn 'naga weehawtgd. The child is spoiled, that's why she cries a long time.\\
\section*{dock}
verb to carry, take\\
-Shgu dm dockm lag. We have to take wood.\\
-Hee Gitsgaanu ashda 'guulda sha dowlan docka wineayam. I went to Ketchikan the other day and I took our food.\\
\section*{dockdock}
verb to hold on to\\
-Shguu mdm dockdocka hagwilhoo dsihla 'dsuu baashg. You have to hold on to the rope when the wind blows hard.\\
\section*{doohlk}
noun cedar bark basket\\
-Lu'kwil ama'basha doohlk dsabs maata. Martha makes beautiful cedar bark baskets.\\
\section*{doola}
noun tongue\\
-Ahlgandee wilaayhl goahl gn geetga na doolayu. I don't know why my tongue is swollen.\\
\section*{doolckg}
verb to be stuck, unable to travel\\
-Doolckga'nu da Gitsgaan da wil haackga lacka. I got stuck in Ketchikan when the weather was bad.\\
-Na dm goyu Ta'gwaan da bite doolckga'nu. I was going to go to Metlakatla but I got stuck.\\
\section*{doosh}
noun cat Plural:dikdoosh\\
-Needsu hash ada doosh. I see a dog and a cat.\\
\section*{dooshm gilhawli}
noun tiger, wildcat\\
-Ha'wahlgndee nee dooshm gilhawli. We've never seen a tiger.\\
\section*{doycksh}
verb to be built strong; to put on warm clothes\\
-Doyckshn, gwatga gyalgg. Dress warm, it's cold outside.\\
\section*{doyksh}
noun rapids, strong tide\\
-Doyksha aksh da awaa 'wee loaba gwee. The rapids are strong by that big rock.\\
\section*{dsaam}
noun jam\\
-Hoyu dsaam da lack anaay. I use jam on my bread.\\
\section*{dsab}
verb to build, construct, make\\
-Goadu ap dee dsabn? What work do you do?\\
\(-\) Lu'kwil wilaay 'yoota gwee dsaba p'tsaan. That man really knows how to make a totem pole.\\
\section*{dsadaawhl}
adverb tonight\\
-Wiedsa shuwil'leenm dsadaawhl. Let's go hunting tonight.\\
\section*{dsag}
verb to die, be dead PLURAL:duu\\
-Dsaga wun. The deer died.\\
-Labite waal wila gyoa hlgu doosha gwee dowla dsagt. That little cat made a mistake and so it died.\\
\section*{dsaggabaashg}
noun crosswind\\
-'Tsuu dsaggabaashg da lackshuulda The cross wind was very strong on the ocean.\\
\section*{dsagga-tgubaa}
verb to spin, run in circle\\
-Dsagga-tgubaa hash hlat shuwileen hlgu doosh. The dog ran in a circle when it chased the little cat.\\
\section*{dsaggayaa}
verb to walk across\\
-Dm dsaggayaa'nu da awaa ggaldmwa'at. I'm going to walk across to the store.\\
\section*{dsagga'acklg}
verb to be able to go across\\
-Dsagga'acklga'nu da 'wee guyna. I made it across the big street.\\
\section*{dsaggm}
prefix ashore, inland\\
-Dm dsaggm yeltgish dup gwa'a. They will return to shore.\\
\section*{dsaggmbaashg}
noun onshore wind\\
(-).Lu'kwil ggatgyada dsaggmbaashg. The onshore wind is very strong.\\
\section*{dsaggmdaawhl}
verb to go ashore\\
-Hladm dsaggmdaawhla ckshoa. The canoe will be going towards shore.\\
\section*{dsagmwaash}
noun south wind\\
-Ahl ggatgyadee dsagmwaash? Is the south wind strong?\\
\section*{dsahl}
verb to consume; to lose a game, war; to be consumed\\
-Dsahlu tcka'nee wineaya 'nee gn ggal 'dsaayu. I finished all the food that's why I'm full.\\
-Galmeelgm ashda 'guulda sha da dsahlu. I was playing the other day and I lost.\\
\section*{dsakshuld}
verb to dampen; to sprinkle\\
-Dsakshulda hoayan nagoacka mdm aidsd. Dampen the clothes before you iron them.\\
\section*{dsalee}
noun old fish\\
-Ahlgadee hashackee dsalee. I don't want an old fish.\\
\section*{dsam}
verb to boil, cook\\
-Dm dsamu hlgumad. I'm going to boil an egg.\\
-Na gidigaadu 'wee hoan dowla dsam noayu dm gubm. I caught a big fish and my mother cooked it for us to eat.\\
\section*{dsawush}
noun laughing berries, salal berries\\
-Wilaay nakshu dsaba dsawush. 'Nee hoym da anaay. My wife knows how to fix laughing berries. That's what we have on bread.\\
\section*{dsayaihl}
noun snare, trap\\
-'Gwaatga dsayaihlm. Our traps are lost.\\
\section*{dsaygg}
noun gray berries along river bank\\
-Ahlgandee anoacka dsaygg. I don't like gray berries.\\
\section*{dsa'bl}
verb to handle, play with compulsively\\
-Ahlgadee aam dm dsa'bl hahlibeeshk, ahlgadee aam da 'kwan. It's not good to play with a knife, it's not good for you.\\
\section*{dsa'ee}
interjection expression used for calling down one who is doing badly\\
-Dsa'ee! Ama nee wila gyoan. Good grief! Watch what you're doing.\\
\section*{dseeb}
verb to defrost, melt, disappear, lose weight or size\\
-Dseeba daaw dsihla ggal gyamg. The ice melts when it's too warm.\\
\section*{dseehl}
noun snipe\\
-'Tsuushgm 'dsu'utsa dseehl. Snipe is a little bird.\\
\section*{dseehldoa}
verb to put away in a corner\\
-Dseehldoa ckbeesh da 'dsm gi'dsoan. Put the box in the corner of the closet.\\
\section*{dseekshhawtksh}
verb to brag a lot\\
-Ggal dseekshhawtksha 'yoota gwee. The man over there brags too much.\\
-Shoonaahla'nu da wila dseekshhawtksha hana'acka gwee. I'm tired of how that woman brags so much.\\
\section*{dseekshhietksh}
verb to stand smartly\\
-Shm dseekshhietksha 'yik'yoota wil algyacka Shm'oygit. The men stood still when the Chief spoke.\\
\section*{dseekshwaaltksh}
verb to show off, to strut your stuff\\
-Ashguu wil dseekshwaaltksha hlguwoamhlg. The child is humorous when he struts her stuff.\\
\section*{dseekshyaaksh}
verb to strut, walk with flair\\
-Giloa dseekshyaakshn. Don't strut your stuff.\\
\section*{dseekwsha}
verb to bail water (out of a canoe, boat)\\
-Dseekwsha aksha da boad. Bail the boat out.\\
-Geedsa hultga boad dowla dseekwsha'nu. My boat almost filled up then I bailed it out.\\
\section*{dseelksh}
verb to melt\\
-Giamg dm endseelkshn daaw. The sun will melt the ice.\\
\section*{dseewsh}
noun daylight, daytime\\
-Dm ggadaawhlm dsihla dseewsh. We'll leave at daylight.\\
\section*{dseeyuu}
noun dolphin, porpoise\\
-Ha'wahlgndee shila hadiksha dseeyuu. I haven't swam with a porpoise\\
\section*{dse nda?}
interrogative when?\\
-Dse ndahl dm goidiksha boad? When is the boat coming?\\
\section*{dse'a}
noun grandmother\\
-Maata na dse'ashu. Martha is my grandmother.\\
\section*{dse'ish}
noun grandmother\\
-Awaash dse'ishu dm goayu. I'm going to my grandmother's house.\\
\section*{dsigi'dseeb}
adverb tomorrow\\
-Dm daawhlm dsigi'dseeb. We'll leave tomorrow.\\
\section*{dsihla}
prefix at this time, this hour\\
-Dm tckoackgm dsihla gwaanksha wineaya. We'll eat at the time the food is done.\\
\section*{dsi'kwe'eds}
noun large sea urchin\\
-Hladm guuldm dsi'kwe'eds. We're going to harvest sea urchins.\\
\section*{dsoack}
\begin{enumerate}
  \item verb to be ashamed Plural: ledsoack\\
-Lu'kwil mashga 'dsalt hla dsoackt. His face is red when he's ashamed.\\
-Labite how 'yoota gwee, labite dsoackt goa wila howt. That man made a mistake, he was ashamed of what he said.
  \item verb to reside\\
-Ndahl wil dsoacksh Maata? Where does Martha reside?
\end{enumerate}

\section*{dushck}
noun squirrel\\
-Dm goom dushcku dsihla dsigi'dseeb. I'm going to hunt for squirrel tomorrow.\\
\section*{duu}
verb to die, be dead\\
-Duu hailda hoan. Lots of fish died.\\
-Hailda gyad shipsheepgd dowla duut. Lots of people got sick then died.\\
\section*{duwaay}
verb to paddle, row\\
-Shguu dm duwaaym ckshoa. We have to paddle the canoe.\\
\section*{ee}
interjection oh!\\
-Ee! Waalhl gubm. Oh! I wish I could have some.\\
\section*{eemck}
noun beard\\
-'Naga eemcka 'yoota. The man's beard is long.\\
\section*{eesh}
noun yeast\\
-Lugowdee ggalm eeshu, shgu ndm gik geegt. My container of yeast is empty, I need to buy it again.\\
\section*{enta hoan}
noun fish, canned\\
(-) Lu'kwil 'tsamaatga meeyoob ada enta hoan. Rice and canned fish taste very good.\\
\section*{gaa}
verb to take\\
-Gaa ckbeesh ada 'gilumt dish noan. Take the box and give it to your mother.\\
\section*{gaalmck}
noun Nass-Gitksan language\\
-Gaalmck hoy Nishgaa. The Nass River people speak another language.\\
\section*{gabids}
noun cabbage\\
-Dm dsamu gabids. I'm going to cook some cabbage.\\
\section*{galmeelg}
verb to play\\
-'Naga galmeelga hlguwoamhlg. The child plays a long time.\\
\section*{galot}
noun carrot\\
-Yagwa na guba galot. I am eating carrots.\\
\section*{gatgyetga baashg}
noun strong wind\\
-Giloadsa kshigyoatgn - ggal gatgyetga baashg. Don't depart - the wind is too strong.\\
\section*{gawdee}
verb to be done with\\
-Lu'kwil kwdee 'yoota gwee 'neegn lugawdee na giehld. That man was very hungry that's why his dish is empty.\\
-Gawdee yaawckgu dowla sha'apyaayu. After I ate I went for a walk.\\
\section*{ga'wa}
verb to agree, consent\\
-Ga'wa'nu hlan tcka'noo wila hawt. I agreed when I heard what he said.\\
\section*{geedsa}
prefix almost, just about\\
-Geedsa shagienayu. I almost fell down.\\
\section*{geek}
noun; verb hemlock (tree or wood); mosquito; to buy; to fly\\
-Hailda geek da lack geeka da 'yagayaayu ndm 'kots'kots. Dm hoyu da na waabu dm sha gyamga waabu. There are lots of hemlock down the beach so I'm going to walk down there and cut them up. I use it to warm up my house.\\
\section*{geeka}
adverb next to the water, at the water's edge\\
-Yagwa sha'dsa'ackm da geeka. We're digging clams next to the water.\\
\section*{geemg}
verb to wipe Plural: leemg\\
-Hla gawdee tckaoackga gyad - geemga ha'litckoackg. The people are done eating - wipe the table.\\
\section*{geen}
verb to give food\\
-Wie geenee da anaay. Hla kwdeeyu. Well, give me the bread. I'm hungry.\\
\section*{geesh}
verb to err, miss, make a mistake, do something wrong\\
-Geesha waalt hlat dsaba gwish'na'ba'la. She made a mistake when sewing the blanket.\\
\section*{geeshk}
verb to dodge; miss\\
-Ahlgadee daacklga'nu ndm geeshga hla'at. I wasn't able to dodge the ball.\\
-Na oyu loab da 'nakshuneeshg dowl labite geeshd. I threw a rock at the window and missed it.\\
\section*{geetg}
verb to rise, be swollen\\
-Geetga an'onu ada ahlgadee da'acklgu ndm hoy gwishgwashm on'onu My hand is swollen and I can't wear my rings.\\
\section*{geetga aksh}
verb to flood\\
-Geetga aksh a lack'daa. The lake is flooding.\\
\section*{ggaagg}
noun raven\\
-Nee wil ggusha 'wee ggaagg da gyalck. See the big raven jumping outside.\\
\section*{ggaaka}
verb to be strong\\
-Ggaaka hagwilhoo hoyu. The rope I'm using is strong.\\
\section*{ggaapck}
verb to scratch\\
-Ggaapcka doosha likshoack hla hashact dm 'dseent. The cat scratched the door when it wanted to come in.\\
\section*{ggaapckan}
verb to rake, scrape\\
-Ggaapckan ggam'do'otsk da 'dsm shdoob. Rake the coals up in the stove.\\
\section*{ggabackshg}
verb to jump with fright, shake, be startled\\
-Sha ggabackshga'nu wil 'wee'amhow 'yoota. I jumped when the man yelled in a loud voice.\\
\section*{ggaboack}
noun cockle\\
-Wiedza sha ggaboackm. Let's gather some cockles.\\
\section*{ggadailpk}
noun anchor\\
-Uksh'oy ggadailpk. Throw out the anchor.\\
\section*{ggadeeshg}
verb to braid\\
-Naahl en ggadeeshga na ggawshn? Who braided your hair?\\
\section*{ggadoahl}
noun humpback salmon, pink salmon\\
-Nee 'wee ggadoahl. Ggal hailda hoan wila waald. See that big humpback salmon. There's lots of fish where it is.\\
\section*{ggadsaagg}
noun cross, gable of roof\\
-Hida ggadsaagg wila dsaba taggan da lack waab. The lumber on the house looked like a cross.\\
\section*{ggadsiksh}
verb down pour\\
-Shuulga wila dsaba lacka hla ggadsiksha waash. The sky looks fearful when the rain pours down.\\
\section*{ggadsikshg}
verb to rain heavily\\
-Giloamdsa 'kotsa kyoack awil ggal ggadsikshga waash. Don't cut the grass because the rain is pouring.\\
\section*{ggadsiwaald}
noun fingers\\
-'Nik'nuunga ggadsiwaalda hlgu 'yoota. The little boy has long fingers.\\
\section*{ggag}
noun swan\\
-Ha'wahlgandee nee ggag. I haven't seen a swan.\\
\section*{ggaggawsh}
noun antler, horn\\
-Nda shgaboo ggaggawsha wun? How many antlers does the deer have?\\
\section*{ggaggoack}
noun fish nose\\
-Ha'weenhl backanee ggaggoackm hoan? Haven't you tasted fish nose yet?\\
\section*{ggagoom}
noun seagull\\
-Na guguuldm ggagoom da lack loab da wil 'ken hlumad da ahlgadee ap 'waad. We looked for seagulls on the rock to find the eggs but couldn't find any.\\
\section*{ggahldikshguu}
verb to lie on one's side\\
-Ggahldikshguu hash hla gawdee tckoackgt. The dog laid on his side when he was done eating.\\
\section*{ggahldikyaa}
verb to go into the woods; to walk to one side\\
-Dm ggahldikyaa'nu da gilhouli. I'm going to walk up in the woods.\\
\section*{ggahlg}
verb to string up, put on drying pole\\
-Hladm ggahlga'nu hoan. I'm going to string up the fish.\\
\section*{ggahlggan}
verb to put on sticks for smoking (as fish, meat)\\
-Ggahlggan shamee awil dm guunksht. Put the meat on sticks so it will dry.\\
\section*{ggahood}
noun beads on a string, necklace\\
-Lu'kwil hoyshga ggahooda hoy hana'ack. The woman is wearing beautiful beads.\\
\section*{ggaid}
noun hat\\
-Ggal 'weelaeksha ggaidu. My hat is too big.\\
\section*{ggaida gganaaw}
noun mushroom\\
-Ahlgadee aam naga'tsaaw ggaida gganaaw. Some mushrooms are not good.\\
\section*{ggaidm boashn}
noun rimmed hat\\
-Ahlgandee anoacka ggaidm boashn hoyn. I don't like the rimmed hat you're wearing.\\
\section*{ggaidm shgyen}
noun rain hat\\
-Sha 'goa'olsh 'yoo'ock na ggaidm shgyent. The boy forgot his rain hat.\\
\section*{ggaidm shihoo}
noun yarn hat\\
-Dsabsh n'dse'etsu hailda ggaidm shihoo. My grandmother made many yarn hats.\\
\section*{ggaidm 'dsagg}
noun cap\\
-Dm 'gilmu ggaidm 'dsagg da nakshu. I'm going to give my husband a cap.\\
\section*{ggaiggai}
noun dead tree branch\\
-Ama needsn da ggaiggai. Watch out for dead tree branches.\\
\section*{ggailkshg}
verb to creep; to sit in protest of moving or going\\
-Ggailkshga hlguwoamhlg hla hloonteed. The child crept along when he was angry.\\
\section*{ggaimggan}
verb to pry with a lever\\
-Shguu mdm kshi ggaimggan 'daa'binshg da ggan. You have to pry the nails out of the wood.\\
\section*{ggaimgganshk}
noun oar\\
-Giloamdsa 'koa'olda ggaimgganshk. Don't forget the oars.\\
\section*{ggain}
noun skunk\\
-Lu'kwil ooshga ggain. The skunk is stink.\\
\section*{ggaklik}
noun rat, rodent\\
-Baasha'nu ndm nee ggaklik. I'm afraid to see a rat.\\
\section*{ggaksh}
prefix just started or happened\\
-Ggaksh sha'da'ama meelg. The dance just started.\\
\section*{ggakshwil}
conjunction that's when, then\\
-Hla 'dsilm gawdee gyad 'nee ggakshwil sha'dac'amat. When everyone was in, that's when they started.\\
\section*{ggakshwil a'aamt}
verb to get better\\
-Ggakshwil a'aamta hana'ack hla wil gigeengwackhla gyad. The woman got better after the people prayed.\\
\section*{ggal}
verb; prefix to come, come here; too, also\\
-Ggal. Hashacku ndm shilahown. Come here. I want to talk with you.\\
\section*{ggalaag}
verb to be cracked; to be crazed\\
-Ggalaaga hlgumadm ggaguum da lack kyoack. The seagull egg cracked on the grass.\\
\section*{ggalaaw}
noun red cedar tree\\
-Ndahl dm wil 'wayy ggalaaw? Where will we find the red cedar trees?\\
\section*{ggalbailtg}
number two boats or canoes\\
-Ggalbailtga ckshoa hla badsgt. Two canoes have arrived.\\
\section*{ggalbash}
verb to be empty, not there\\
-Ggalbasha goack. The basket was empty.\\
\section*{ggaldm}
noun container\\
-Yoaksha na ggaldm yaawckgn. Wash the container you used for eating.\\
\section*{ggaldmwa'at}
noun store\\
-Dm kshagyoatga'nj da ggaldmwa'at. I'm going by boat to the store.\\
\section*{ggaldm'aksh}
noun bucket, pail, water container\\
-Tckayaagwa ggaldm'aksh. Bring the bucket with you.\\
\section*{ggaldoa}
noun camp\\
-Lu'kwil anoacku ggaldoa gwa'a. I really like this camp.\\
\section*{ggaldsap}
noun village\\
-Macklackaahla na ggaldsap wil 'waatgu. Metlakatla is the village where I'm from.\\
\section*{ggaldsock}
verb to camp\\
-Dm ggaldsock'nu shuunta gya'win. I'm going to go camping this summer.\\
-Awaa China Town wil ggaldsockm. We went camping at China Town.\\
\section*{ggaleemksh}
noun gospel\\
-Shmhow na ggaleemksha Shm'oygit ga Lackaga. God's word is the truth.\\
\section*{ggalgwai'hl}
noun empty sack\\
-Goahl gun ggalgwai'hla gwa'a? Why is this sack empty?\\
\section*{ggal haild}
quantifier too many\\
-Ggal hailda gyad da 'dsm boad. There are too many people in the boat.\\
\section*{ggalipleep}
noun cannon; thunder\\
-Wee howtga hlguwoamhlg hlat tcka'noo ggalipleep. The child cried when she heard the thunder.\\
\section*{ggalkshaggush}
verb to jump rope\\
-'Naga ggalkshaggusha hlguwoamhlg da gyalck. The child jumped for a long time outside.\\
\section*{ggalm'algyack}
noun spokesman\\
-Naayu na ggalm'algyacka Shm'oygit? Who is the Chief's spokesperson?\\
\section*{ggalooy}
noun wart\\
-Hashacka 'yoota dumt sha 'kotsa ggalooy da an'ont. The man wants to cut the wart off his arm.\\
\section*{ggalsh}
noun dried cockles\\
-Hashacku ggalsh. I want dried cockles.\\
\section*{ggalshm}
interjection come!\\
-Ggalshm! Hladm tckoackgm. Come! It's time to eat.\\
\section*{ggalshm hoa}
interjection come!\\
-Ggalshm hoa! Hladm leemeeym. Come! We're going to sing.\\
\section*{ggaltsggan}
number three long objects\\
-Ggaltsggan taggan dm geegu ndm ama dsaba guyna. I'm going to buy three planks to fix the street.\\
\section*{ggaltsggantg}
number three boats or canoes\\
-Ggaltsggantga ckshoa needsu. I see three canoes.\\
\section*{ggal'dsuu}
verb to talk, say, claim too much\\
-Ggal'dsuu algyacka 'yoota. The man claims too much.\\
\section*{ggal'kieshuu}
noun knee\\
-Sheepga ggal'kieshuuyu. Ggoadu ggal 'naga da yaayu ashda gi'dseeb. My knee hurts. I think it's because I walked too long yesterday.\\
\section*{ggal'oa}
verb to drop, let go\\
-Geedsa ggal'oadu ckbeesh awil lu'kwil 'balgiackshgt. I almost dropped the box because it was very heavy.\\
-Ggal'oadu noahl. I dropped a plate.\\
-Na mungaadu 'wee loaba gwee dowl ggal'oat. I lifted the rock and then dropped it.\\
\section*{ggal'oash}
noun stomach\\
-Sheepga ggal'oashu. My stomach hurts.\\
\section*{ggal'tsushg}
verb to be too small\\
-Ggal'tsushga na ggaidn. Your hat is too small.\\
-Na geegish nagwaadu 'backsh da ggal'dsooshgd da 'koy. My father bought me pants but they were too small for me.\\
\section*{ggal'uunck}
noun Indian box, storage box\\
-Ggal'uunck na dee hoy gyad hla 'nag hlat damoatga na wineayat. People used Indian boxes long ago to save their food.\\
\section*{ggal'waatk}
verb unlucky; come empty handed\\
-Giloa yaan da gwee, ggal'waatgd. He should not go there because he is unlucky.\\
\section*{ggamckbaickshk}
noun sawdust\\
-Na 'yagayaam da moolaa laa da hailda ggamckbaickshg, da 'nee hoym da lack yuubm. I went down to the sawmill where there was a lot of sawdust and that's what we used on our ground.\\
\section*{ggamggantk}
noun door\\
-Shga'doosha ggamggantk. Close the door.\\
\section*{ggamhlabeeshk}
noun shavings\\
-Ggamhlabeeshk hoyu hlan gwal'kn lag. I use shavings to turn the wood.\\
\section*{ggamwaal}
noun poor stuff, cheap things\\
-Ahlgadee hashacka dm geega ggamwaal. I don't want to buy cheap things.\\
\section*{ggam'dooshk}
noun sweepings\\
-Dm gwal'ka'nu ggam'dooshk. I'm going to burn the sweepings.\\
\section*{ggam'do'otsk}
noun charcoal, coal, soot\\
-Ggam'do'otskga hoy gyad hla shagamaashgit. People use charcoal when they paint.\\
\section*{ggan}
noun tree, wood\\
-Ndm ama haboalda ggan gwee. I'm going to take good care of that tree.\\
\section*{gganahietg}
verb to lean against (a wall, firm object)\\
-Oa, hla gganahietgu da waaba gwa'a, hla geedsa shonaahlu. Yes, I leaned against this house, when I almost got tired.\\
\section*{gganaow}
noun frog\\
-Tcka'nooyu gganaow da awaa lack'daa. I heard a frog by the lake.\\
\section*{gganawulee}
noun backpack; strap to carry things\\
-Gi'dsoan na wil nee gganawulee. I saw the backpack in the back room.\\
\section*{gganeesh}
verb to be the youngest male\\
-Gganeesht Lobat. Robert is the youngest male.\\
\section*{gganggan}
noun forest; pieces of wood\\
-Shackdoa gganggan. Gather more pieces of wood.\\
\section*{ggangwal'ka}
noun kindling\\
-Tcka'nee gganhlaag ggangwal'ka dee 'kotsu. I cut up kindling every morning.\\
\section*{Gganhaada}
noun Raven Clan (crest)\\
-Gganhaada nagwaads Ruth. Ruther's father is Raven.\\
-Gganhaada wil hokshgush nagwaadu. My father's moiety is Raven.\\
\section*{gganhlaag}
noun morning\\
-Oomhoant nagwaadu ashda gganhlaag. My father went fishing this morning.\\
\section*{gganhlaan}
noun wooden body armor\\
-Shgu dm hoym gganhlaan da lack ha'liwildoolgit. We need to wear body armor when we go onto the battlefield.\\
\section*{gganhla'ka'winshk}
noun clothespin, scissor-like tool\\
-'Gwaatga tcka'nee gganhla'ka'winshk. All the clothes pins are gone.\\
\section*{gganlugoy'pa}
noun window, light source\\
-Dm 'daayu da awaa gganlugoy'pa. I'm going to sit by the window.\\
\section*{ggantk}
verb to be dried hard, stiff with cold\\
-Geedsa ggantka ggaidu awil lu'kwil gwatka lacka. My hat almost dried hard because the weather was so cold.\\
\section*{gganwaal}
noun cheap goods\\
-Gway'a wila dsaba gganwaalt. His things look very cheap.\\
\section*{gganwaay}
noun oar lock\\
-Lu 'ken ggaimgganshk da gganwaay. Put the oar in the oar lock.\\
\section*{gganyishya'tsa}
noun suspenders\\
-Dm geegu shu gganyishya'tsa da nakshu. I'm going to buy new suspenders for my spouse.\\
\section*{ggan'dameesh}
noun marker, pencil\\
-Ahl shguuhl ggan'dameesh da 'kwan? Do you have a pencil?\\
\section*{ggan'doa}
noun button, clasp to hold cape on; safety pin\\
-Ndsu ggan'doa. Give me the safety pin.\\
\section*{ggapshil}
verb to blink, wink\\
-Ap ahlgadee ggapshil 'yoota gwee. That man doesn't blink.\\
-Na lukhleedaawhl ligigoa da 'dsm 'dsalu dowla ggapshilu. When something goes in my eye, then I blink.\\
\section*{ggashgaatsg}
verb to be rough (like sandpaper)\\
-Ggashgaatsga na anaashu awil 'tsuu baashk. My skin is rough because of the strong wind.\\
\section*{ggashgaawt}
verb to be of a certain size\\
-Nda ggashggaw ha'li-tckoackga dm dsabm? How big is the table that we're going to make?\\
\section*{ggashggaads}
noun dog fish\\
-Ahl dee 'tsamaa'anee ggashggaads? Do you like the taste of dogfish?\\
\section*{ggashishee}
noun feet\\
-Shgaaygshga ggashishee hlgu 'yoota dawil ggusht. The boy's feet were hurt when he jumped.\\
\section*{ggatgyad}
verb to be strong (physically or orally)\\
-Ap shm lu'kwil ggatgyada 'yoota. The man is really strong.\\
-Lu'kwil ggatgyada wila gyoa 'wee 'yoota gwee. That man is very strong at what he's doing.\\
\section*{ggatgyatga baashg}
noun gale, strong wind\\
-Ggatgyatga baashg ashda gi'dseeb. There was a strong gale yesterday.\\
\section*{ggawaaym 'tu'utsk}
noun sword\\
-Ggawaaym 'tu'utsga hoy hlaagi gyad hla dildalt. People in the old times used a sword to fight.\\
\section*{ggawn}
verb to chew Plural:gganggawn\\
-Kwhlee ggawn goa gubn. Completely chew up what you eat.\\
(-).Lu'kwil wilaay 'yoota gweet ggawn goa gubed. That man knows how to chew what he eats.\\
\section*{ggawsh}
noun hair\\
-Nahl en ggadeeshga na ggawshn? Who braided your hair?\\
\section*{ggayg}
noun chest PLURAL: ggaggaygt\\
-Sheepga ggaygt. His/her chest hurts.\\
\section*{ggayneesh}
noun chum salmon, dog salmon\\
-Hailda ggayneesh da awaa Macklackaahla. There's a lot of dog salmon by Metlakatla.\\
\section*{gga'bala}
noun gun\\
-Hoyu gga'bala hladm goo wunu. I use a gun when I shoot deer.\\
\section*{gga'bilaash}
noun larvae\\
-Lu doa gga'bilaash da 'dsm 'nhla'naggan. There are mosquito larvae in the barrel.\\
\section*{gga'dsihlshagya}
verb to pull down\\
-Gga'dsihlshagya 'nakshuuneeshg. Pull down the window.\\
\section*{gga'dsihl'doosh}
verb to push down\\
-Needsu wil gga'dsihl'doosha hoguwoamhlg na hlmkdeet. I saw the child push his brother down.\\
\section*{gga'dsihl'oksh}
verb to fall down\\
-Geedsa gga'dsihl'oksha ggan da wil ggal 'balgiackshga maadm. The tree almost fell down because the snow was too heavy.\\
\section*{gga'dsiyoahl}
verb to slide (on feet, with a sled)\\
-Gga'dsiyoahla hlguwoamhlg da lack daaw. The child slid on the ice.\\
\section*{gga'eemck}
noun White man, bearded man\\
-Hailda gga'eemck dsoackt da Gitsgaan. There are a lot of Europeans living in Ketchikan.\\
-Needsm hailda gga'eemck. We saw a lot of Europeans (Whiteman).\\
\section*{gga'gwaa'gw}
noun low profile, low status, a worthless person\\
-Ahlgadee aam dm gga'gwaa'gwn. Don't be a worthless person.\\
\section*{gga'kai}
noun wing\\
-'Nik'noonga gga'kai ckshgeeg. The eagle has long wings.\\
\section*{gga'koacksh}
noun salmonberry bushes\\
-Ahlgadee macksha gga'koacksh da gwa'a. The salmon berry bush doesn't grow here.\\
\section*{gga'kowtg}
verb to howl like a wolf; to sound in loud tone\\
-Gga'kowtga 'yoota hlat tcka'noo gibaaw. The man howled when he heard the wolf.\\
\section*{gga'kuhl}
verb to shiver\\
-Gga'kuhla'nu hla ckgwatkshu. I shiver when I'm cold.\\
\section*{ggiehl}
noun bowl\\
-Kshi'nag de hoyu hla lu 'dsaicka wineaya da ggiehlu. I use my middle finger when I lick out my bowl.\\
\section*{ggiehlam'do'otsk}
noun iron dish\\
-Ggiehlam'do'otsk hoy nakshu hla googt. My wife uses an iron dish when she cooks.\\
-Yoaksha ggiehlam'do'otsk. Wash the iron pot.\\
\section*{ggoab}
noun waves\\
-'Tsuu ggoab da wil gatgyada baashg. There are lots of waves when the wind is strong.\\
\section*{ggoad}
noun heart\\
-Ama ggoada 'wee 'yoota gwee. That man is very kind.\\
\section*{ggoash}
verb to cool, simmer down\\
-Aam mdm ggoasha aksh. It's good to cool the water down.\\
-Aam mdm ggoasha aksh, ggal gyamgd. It's good to cool the water down, it's too warm.\\
\section*{ggogg}
verb to bend forward, bow, stoop\\
-Ggoggn da nhluu hahloam giamg. Bow your head under the flag.\\
-Hla ggoagga 'wee 'yoota gwee hla gawdee algyackt. That man bowed after he talked.\\
\section*{ggol}
verb to come apart, be irreparable; to be strewn loosely Plural:ggolggol\\
-Ggol waabsh Dzon. John's house tumbled down.\\
-Ggol 'dsilaa awil ggal hultgid. The basket came apart because it was too full.\\
\section*{ggolee}
noun hair, scalp\\
(-).Shm 'nuunga ggolee 'wee 'yoota gwee. That man's hair is really long.\\
\section*{ggol'ge}
noun yellow berries on muskeg\\
-Ha'weenhl needsinee ggol'ge? Haven't you seen the yellow berries on the muskeg?\\
\section*{ggontgahl}
verb to be clear, evident, visible\\
-Lu'kwil amookshu da wila how 'yoota gwee da up ahlga ggontgahla wila howd. I really listened to what that man said but it's not clear what he said.\\
\section*{ggush}
verb to jump\\
-Nee wil ggusha hoan. Look where the fish jumps.\\
\section*{gibaaw}
noun wolf\\
-Hailda gibaaw da lack'daa gwee. There are many wolves on that island.\\
\section*{gig}
noun house fly\\
(-) Lu'kwil hamoolga gig da na 'dsalu. The fly is really bothering my face.\\
\section*{gigeengwackhl}
verb to pray\\
-Alik dm gigeengwackhlt nagoaga dm sha'daa'amum. Alec will pray before we start.\\
\section*{gigim'uugg}
noun blond or reddish hair; horsefly\\
-Gigim'uugga hana'acka gwee. That woman has blond hair.\\
\section*{gigi'oashg}
verb to be stubborn\\
-Gigi'oashga hoguwoamhlg hlat how noat dm yaawcktgt. The child was stubborn when the mother said to eat.\\
\section*{gigyoaksh}
noun something that floats\\
-Na waaym da wite gwashga da goa 'wee loagsh, aam shga'nag dowla gigyoaksht dowla awaa Ta'gwaan habm. We rowed way over there to get a log, after a while it floated then we went to Metlakatla.\\
\section*{gigyoatk}
noun axe, hatchet\\
-'Gwatga na gigyoatgu. I lost my hatchet.\\
\section*{gik}
prefix again\\
-Gik hown. Say it again.\\
\section*{gilaan}
noun aft of boat, back end, rear, stern\\
-Gilaan dm dee wil hietgn. You will stand in the stern.\\
\section*{giladse'eds}
noun dragonfly\\
-Lu'kwil 'weelaeksha nagga'dsaaw giladse'eds. Some of the dragon flies are very big.\\
\section*{gilakyo}
noun robin\\
-Nee wila loa 'guba gilakyo, yagwa sha laaldid. Look what the little robins are doing, they're gathering worms.\\
\section*{gilhowlee}
adverb in the woods or forest\\
-Wie, gilhowlee wil 'dahla wun. 'Nee dm goym da gganhlaag. We're going to collect berries up in the woods.\\
\section*{gilksh}
prefix to be self-inflicted, toward oneself\\
-Gilksh amaneedsn, dayat n'dse'etsu da 'koy. Take care of yourself, that's what my grandmother said to me.\\
\section*{gilksh-shamackshd}
verb to be willing to die\\
-Gilksh-shamacksha nagwaada hlguwoamhlg awil dm didoolsht. The child's father was willing to die so that his child might live.\\
\section*{gilkshtckal'da'minshg}
verb to draw, take a picture\\
-Hoyshga gilkshtckal'da'minshga dsaba 'yoota. The picture the man made is beautiful.\\
\section*{gilksh'ietksh}
verb to repent, be sorry for\\
-Gilksh'ietksha hlguwoamhlg awilt oy loab da 'nakshuuneeshg. The child was sorry that he threw a rock at the window.\\
\section*{giloa}
verb to stop, not do\\
-Giloadsa oyan liploab. Don't throw the rocks.\\
\section*{gil'aksh}
verb to give a drink\\
-Wie gwinaat. Gil'akshe. Well, fellow. Give me a drink of water.\\
\section*{ginamaan}
verb to be left over (food)\\
-Hailda goa ginamaant. There are a lot of things left over.\\
-Na shagiet wunm ashda 'guulda sha, tckoackgm dowla ginamaan hailda goa dm gubm. We got together one day, we ate and there were a lot of leftovers to eat.\\
\section*{gina-shawaal}
verb to be unexpected\\
-Gina-shawaal gyad da wil dsoackm. People showed up unexpectedly where we live.\\
\section*{ginawaal}
verb to stay behind\\
-Ginawaalt Peda awil ggal 'tsuu lacka. Peter stayed behind because the weather was bad.\\
\section*{gipaig}
verb to fly, glide in the air Plural: lapaig\\
-Ahlga dm gipaiga'nu da sha gya'wn. We're not going to fly today.\\
-Ahlga dm gipaiga'nu da Gitsgaan da sha gya'win. We're not going to fly to Ketchikan today.\\
\section*{Gishbackloa'ds}
noun People of the Elderberries\\
-Hla badsga Gishbackloa'ds da ggaldsabm. The People of the Elderberries have arrived at our village.\\
\section*{Gish-budwada}
noun Killer Whale Clan\\
-Gish-budwada wil hokshgu. I belong to the Killer Whale Clan.\\
\section*{gish doa}
verb to move over\\
-Hlimoamee ndm gish doa ha'li'dameesh. Help me move the table over.\\
\section*{gishihaywaash}
noun northeast wind\\
-Gishiwaashga baashg. There's a northeasterly blowing.\\
\section*{gishiyaashg}
noun north wind\\
-Ap shm luguuye gishiyaashg wil wuwaalm. The north wind is really blowing where we are.\\
\section*{gish'daa}
verb to move over, sit in another place\\
-Gish'daan da awaayu. Move over by me.\\
\section*{gitckawtk}
adverb some time ago\\
-Wite gitckawtk wil dsaga nabeebu. My uncle passed away some time ago.\\
\section*{Gitdsacklahl}
noun People of the Shrubs\\
-'Woo Gitdsacklahl tcka'neesh 'nuum. People of the Shrubs have invited all of us.\\
\section*{Gitdseesh}
noun People of the Salmon (Seal) Traps\\
-Lu'kwil aam 'kawtsi dsaba Gitdseesh. People of the Salmon Traps make good ooligan grease.\\
\section*{Gitlan}
noun People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes\\
-Lu'kwil hailda Gitlan. There are a lot of People of Two Passing Canoes.\\
\section*{Gitnack'angeek}
noun People of the Mosquitoes\\
-Ndahl wil dsoockdu Gitnack'angeek? Where do the people of the Mosquitoes live?\\
\section*{gitwaaltk}
noun enemy intruders, raiders\\
-Giloamdsa 'gilm ligigoa da gitwaaltgm gyad. Don't give anything to enemy raiders.\\
\section*{Gitwilgyots}
noun People of the (Sea) Kelp\\
-Gitwilgyots ndm wil geega laan. I'm going to buy fish eggs from the People of the Kelp.\\
\section*{Git'ando}
noun People of the Other Side (Wiers)\\
-Ha'wahlgandee tckal'waay Git'ando. I haven't met any People of the Other Side.\\
\section*{Git'dsilaashu}
noun People of the Way Inside\\
-Wilaay Git'dsilaashu aadmhoan. People of the Way Inside are good fishermen.\\
\section*{Git'nadoyksh}
noun People of the Swift Waters\\
-Lu'kwil hoyshga dsaba Git'nadoyksh. The work done by the People of the Swift Waters is beautiful.\\
\section*{giyaaksh}
adverb out on the water\\
-Ahl needsinee boad da wiet giyaaksh? Do you see the boat that's way out on the water?\\
\section*{gi'dseeb}
noun yesterday\\
-Nda wila waal lacka ashda gi'dseeb? How was the weather yesterday?\\
\section*{gi'dsoan}
noun back room\\
-Gi'dsoan wil shguu ha'dooshg. The broom is in the back room.\\
\section*{gi'dsoygg}
noun bow (of boat)\\
-'Nuuyu dm 'daam da gi'dsoygg. I'll sit in the bow.\\
\section*{gi'goahl}
adverb years ago; long ago\\
-Aa'backdu wila leemee hlaa gigyad ashda wite gi'goahl. I remember how the old people used to sing many years ago.\\
\section*{goa}
interrogative what?\\
-Goahl wilgyedu gwa'a? What color is this?\\
\section*{goabackga lacka}
noun overcast sky\\
-Wukdsan en goabacka lacka. The rain clouds have made it an overcast day.\\
\section*{goabackga sha}
noun overcast day\\
-Anoacku dm hahlalshu da gyalck wil goabacka sha. I like to work outside when the day is overcast.\\
\section*{goack}
noun basket\\
-Goacka hoy 'gubatguuhlg hla ggashimaayt. The children used small berry baskets to pick berries.\\
\section*{goadsagid}
noun container\\
-Nda goadsagid dm hoyu da 'kawtsi? Where's the container I'm going to use for the ooligan grease?\\
\section*{goamshm}
noun winter\\
(-).Lu'kwil anoacku daayksh hla yaa maadm da goamshm. I really like Indian ice cream when the snow falls in the winter.\\
\section*{goamtg}
verb to be soft\\
-Goamtga mahluu. The pillow is soft.\\
(-).Lu'kwil goamtga an'on hana'acka gwee. The woman's hand is very soft.\\
\section*{goaym}
noun spring (season)\\
-Luaam ggoadu hla daawhla goamshm ada hla badsga goaym. I'm happy when the winter leaves and spring arrives.\\
\section*{goa'opshgn}
number two long objects\\
-Goa'opshgn ggan'dameesh dm 'gilmu da hlguwoamhlg. I'm going to give the child two pencils.\\
\section*{golksh}
noun scarf\\
-Aam mdm hoy golksh, hailda geega da gyalck. It's good for you to wear a scarf, there are a lot of mosquito's outside.\\
\section*{goo}
verb to shoot; to vote by hand or ballot\\
-Giloamdsa goo gibaaw. Don't you shoot a wolf.\\
\section*{gooda'ats}
noun coat\\
-Ndadu gooda'atsn? Where is your coat?\\
\section*{gooda'atsm shgyen}
noun raincoat\\
-Ndayu na gooda'atsm shgyenu? Where's my raincoat?\\
\section*{gool}
noun gold\\
-'Waaysh Alik gool da lack shga'neesh. Alec found gold on the mountain.\\
\section*{goomaa}
noun angel fish, rat fish\\
-Naahl en guba goomaa? Who eats rat fish?\\
\section*{goowaagg}
noun elderberry jam\\
-Lu'kwil 'tsamaatga goowaagg da lack giamgm anaay. Elderberry jam is very good on warm bread.\\
\section*{goo'bl}
number two abstract objects\\
-Goo'bl likshgyadm wileelm tgwa hoyu. I use two different kinds of eyeglasses.\\
\section*{goy}
verb to go\\
-Wie ndahl dm dee goyn? Where are you going?\\
\section*{goydiksh}
verb to arrive\\
-Ndahl dm wil goydikshgt Donna May? When is Donna May coming?\\
-Na goydiksha 'wee shdeem boad da Ta'gwaan dun nee wila loa gyad. A big steamer came to Metlakatla and I saw what the people did.\\
\section*{goy'ba}
verb to be bright\\
-Ggal goy'ba laakwsh. The light is too bright.\\
(-) Lu'kwil goy'ba laakwsha hoyshm. The light you are using is bright.\\
\section*{gub}
verb to eat PLURAL: tckoackg\\
-Goadu dm gubn? What are you going to eat?\\
-Hladm googs noayu mdm gubt gya'wn. My mother is going to cook and we'll eat now.\\
\section*{guguul}
verb to search for\\
-Yagwan guguul ma'koacksh. I'm looking for salmon berries.\\
\section*{gugwalksh}
verb to be polished, shiny\\
-Alu'daa wil gugwalksha gahooda hlgu hana'ack. You can really see how shiny the woman's necklace is.\\
\section*{gugwnyaa}
verb to walk toward\\
-Hagwil gugwnyaa hash da awaayu. The dog walked slowly toward me.\\
\section*{guksh}
verb to jump (of fish)\\
-Hashacku ndm 'waay wil gukshga hoan. I want to find where the fish jump.\\
\section*{gukshg}
verb to wake up\\
-Ahlgadee hashackaa hlguwoamhlg dm gukshgt. The child doesn't want to wake up.\\
\section*{gushck}
verb to be bitter\\
-Na dsaba hlgu hana'ack goa dm gubm, da ahlgadeet wilaay goahl wila gyoad dowla lu'kwil gushcka gubm. The little girl was cooking what we were going to eat and didn't know what she was doing so what we ate was bitter.\\
\section*{gushguuds}
noun sparrow\\
(-).Lu'kwil ckshdaamcka wil how gushguuds. The sparrows sound is very loud.\\
\section*{guudack}
verb to ask, inquire\\
-Ahlgandee wilaayhl goa dm wila gyoayu dun guudacka n'dse'etsu goa dm wila gyoayu. I didn't know what to do so I asked my grandmother what to do.\\
\section*{guul}
verb to harvest, reap, pick (of food)\\
-Wie dm guul maay sha gya'wn. Hla hailda mikmeegt. Well, we're going to pick berries today. A lot are ripe.\\
\section*{guulka}
noun westerly wind\\
-Hailda ggoab hla baa guulka. There are a lot of waves when the westerly wind blows.\\
\section*{guunksh}
verb to be dry\\
-Hladm guunksha na lumaakshu. The clothes will soon be dry.\\
-Hla luguunksha ggiehlam'do'otsk. The iron pot has gone dry.\\
-Na yoaksha nakshu na hoyayu dowla ahlgandee daackga ndm hoyt. Dsihla guunksht dowla daackgu ndm hoyt. My wife washed my clothes and I couldn't wear them. When they were dry I was able to wear them.\\
\section*{guunkshm hoan}
noun dried fish PLURAL: luunkshm hoan\\
-Hashackanee guunkshm hoan? Do you want dried fish?\\
\section*{guyna}
noun path, road, trail\\
-Yaaka guyna da ggaldsap. Follow the trail to the next village.\\
\section*{gwaanksh}
verb to be cooked, done\\
-Hla gwaanksha wineaya. The food is done.\\
-Hla gwaanksha goa dm gubm aam dowla 'dseen. Our food to eat is cooked so come right in.\\
\section*{gwaantg}
verb to touch PLURAL: gwitgwaantg\\
-Giloamdsa gwaantga 'nakshuuneeshg. Don't touch the window.\\
\section*{gwaashg}
verb to borrow PLURAL: gwishgwaashg\\
-Ahlgadee aam dm gwaashgn dish ligit naa. It's not good to borrow from anybody.\\
(-).Na 'gwinooy hlgu 'yoota gwee daala da 'koy, hashackt dm gwaashgt da 'koy. The young man asked me for money because he wanted to borrow it from me.\\
\section*{gwai'hl}
noun sack\\
-Sha hailda gwai'hla gyad, 'nee hoym hla sha hla'ashgm. We have lots of sacks, that's what we use when we gather seaweed.\\
\section*{gwalg}
verb to burn\\
-Hla gwalga lag. The fire is burning.\\
-Na gwalga waaba gwee. That house burned.\\
\section*{gwalka}
verb to trim hair by burning ends\\
-Ha'wahlgandee nee wil gwalka gyad na ggawsht. I haven't seen people trim their hair by burning the ends.\\
\section*{gwal'kan}
verb to turn on (of electricity)\\
-Wie hla aam dm gwal'kan laakwsh. Well it's good to the lights on.\\
\section*{gwan}
number three fish or flat objects\\
-Gwan shgaboo hoan 'gilmsh Peda da 'kam. Peter gave us three fish.\\
\section*{gwashga}
adverb in that direction, over there\\
-Wie gwashga dm habm. Well, we'll go over there.\\
-Gwashga dm wil waalckshm. We're going to walk over there.\\
\section*{gwashoa}
noun pig\\
-Baasha'nu da gwashoa. I'm afraid of pigs.\\
\section*{gwatg}
verb to be cold\\
-Gwatga sha. The day is cold.\\
-Ggal 'naga waalu dowla gwatga goa dm gubu. I took too long and my food got cold.\\
\section*{gway'a}
verb to be poor\\
-Gway'a wila dsaba waab. That house is pitiful.\\
-Lu'kwil gway'a wila waal hlgu 'yoota gwee. That little boy is doing poorly.\\
\section*{gwa'a}
adverb here\\
-Ayam gwa'a wil 'daan. Sit right here.\\
\section*{gwee}
particle that, there\\
-Naa an'on da gwee? Whose hand is that?\\
\section*{gweekw}
noun groundhog\\
-Ha'wahlgandee neehl gweekw, 'nee gun ahlgandee wilaayhl goahl dm wila howyu. I've never seen a groundhog, that's why I don't know what to say.\\
\section*{gwilm ggawdee}
verb to get ready\\
-Wie aam gwilm ggawdeeym. Dm hailda wila gyoam dsidaawhl. Let's get ready. We're going to do a lot of things tonight.\\
\section*{gwiloan}
number three people\\
-Gwiloan gyad gatgoidikshd. Three people arrived.\\
\section*{gwinaat}
noun poor fellow\\
-Ahl sheepganee, gwinaat? Are you sick, poor fellow?\\
\section*{gwineeshk}
verb to appear\\
-Ahlgadee gwineeshga 'yoota gwee dm hahlalsht. That man didn't appear for work.\\
\section*{gwinee'dsn}
verb to show\\
-Hashacku ndm gwinee'dsn shu gooda'atsu da 'kwan. I want to show you my new coat.\\
\section*{gwishgwaash}
noun blue jay\\
-'Daa gwishgwaashg da lack ggan. There's a blue jay in the tree.\\
\section*{gwishgwashg}
verb to be blue (in color)\\
-Dm geegu gwishgwaashgm ggoda'ats. I'm going to buy a blue coat.\\
\section*{gwishgwashm an'on}
noun ring\\
-Naahl en dsaba gwishgwashm an'on hoyen? Who made the ring that you're wearing?\\
\section*{gwish-halayt}
noun robe for dancing\\
-Hashacksh dup gwee dumt dsaba gwish-halayt. They want to make a robe for dancing.\\
\section*{gwishmatee}
noun goat skin coat\\
-Dm kshagaadu na gwishmateeyu dsihla 'dsuuhl gwatg. I'm going to get out my mountain goat skin coat when it gets really cold.\\
\section*{gwish'dseeg}
noun fawn\\
-Hlgu gwish'dseeg hahlyaat da hahlgeeka. There's a little fawn walking on the beach.\\
\section*{gwish'na'ba'la}
noun button blanket PLURAL: gukgwish'na'ba'la\\
-Yagwa loo'bishgat da gwish'na'ba'la. He/she is sewing a button blanket.\\
\section*{gwitgwineeksh}
noun owl\\
-Ahl tckanooyanee gwitgwineeksh? Do you hear the owl?\\
\section*{gyab}
verb to dip, draw water\\
-Gyaba aksh dish 'need. Draw water for her.\\
-Gyaba aksha awaan dowl 'gilmd da hlguhlgn. Dip that water and give it to your child.\\
\section*{gyabn}
verb to come up above the water\\
-Gyabn 'wee 'naackhl. The whale came out of the water.\\
-Na gyabn 'wee uula da gwashga. The seal came out of the water over there.\\
\section*{gyad}
noun people\\
-Ndada tckash 'goahl wil goo gyada wun? What part of the year do people shoot deer?\\
\section*{gyalck}
adverb in the open air, outside\\
-Gyalck dm habm. Ggal lu giamga 'tsawaab. We'll go outside. It's too warm in the house.\\
\section*{gyamg}
noun; verb month; sun, heat; to be hot, warm Plural:lamg\\
-Ggalgyamga 'dsm waaba gwa'a. This house is too warm.\\
\section*{gyamgmdseewsh}
noun sun\\
-Hashacku dm gukshgu nagoacka dm kshagwaantga gyamgmdseewsh. I want to wake up before the sun comes up.\\
\section*{gyamgm'aatk}
noun moon\\
-Hladm hultga gyamgm'aatk dsadaawhl. The moon will be full tonight.\\
\section*{gyantee}
noun sea cucumber\\
-Yagwa shagyantee 'guba 'yoota. The young men are gathering sea cucumber.\\
\section*{gya'galtk}
verb to roll\\
-Mun gya'galtga sha'winshk and lu oyt da 'dsm shdoob. Roll up the paper and throw it in the stove.\\
\section*{gya'wn}
adverb now, today\\
-Ahlgadee aam lacka da sha gya'wn. The weather is not good today.\\
-Dowla gya'win! Right now!\\
\section*{gyehlk}
verb to spear, stab Plural: gyehlgyehlk\\
-Gyehlgt Everett hoan da 'kala aksh. Everett speared the fish in the river.\\
\section*{gyeksh}
verb to be calm\\
-Hla gyeksha baashg gya'win. The wind is calm now.\\
-Na oom hoanu ashda 'guulda sha da hu'kwil gyeksha na goyu. I went fishing the other day and it was calm where I went.\\
\section*{gyelkwsh}
verb to feel something will happen; admonition\\
-Gyelkwshu wil lu'dauckga ggoadn. I feel it when you are sad.\\
\section*{gyelsh}
noun mussel\\
-Yagwa sha gyelshd. He is picking mussels.\\
\section*{gyem}
noun Saskatoon berries\\
-Ndahl wil 'waay gyad gyem? Where do people find Saskatoon berries?\\
\section*{gyepsh}
noun; adverb hill, mountain; up high\\
-Mun gyepsh wil 'dahla hlgumadm ggagoom. Seagull eggs will be found up high.\\
\section*{gyeshg}
verb to be jealous\\
(-)-Lu'kwil gyeshgm ggoada hana'ack da shu waabm. That woman is very jealous of our new house.\\
\section*{gyoash}
noun flat leaf of kelp\\
-Anoacku cksh'waanck da lack gyoash. I like herring eggs on the flat kelp.\\
\section*{gyuwadun}
noun horse\\
-Ahlga 'dahla gyuwadun da gwa'a, ksha geeka wil 'dahlt. There are no horses here, just down below.\\
\section*{haackg}
verb not easy, work hard against odds, suffer PLURAL: hackhaackg\\
-Shm haackga da 'koy ndm dsabt. It's not easy for me to do it.\\
\section*{haad}
noun intestine\\
-Na labiethow na gyadu, dowla haada labiet waald, dsabtda doctor. My intestine was bad and the doctor fixed it.\\
\section*{haada uula}
noun seal intestines\\
-Anoacka gga'dsaaw gyad haada uula. Some people like the intestine of the seal.\\
\section*{haahlggan}
noun wall\\
-'Yacka gilkshtckal'damtk da haahlggan. Hang the picture on the wall.\\
\section*{haash}
noun fireweed\\
-Anoacku wil gyeda haash. I like the color of the fireweed.\\
\section*{haaya}
noun wood, rotted\\
-Ahlgadee hashacku dm haaya na boadu. I don't want my boat to rot.\\
\section*{haboal}
verb to keep, take care of\\
-Ama haboald na 'gilm gyad da 'kwan. Take good care of what people give you.\\
\section*{haboo'yil}
verb to get things ready\\
-Haboo'yil tcka'nee goa dm wa'atm. Get the things ready that we're going to sell.\\
\section*{hackback}
noun pocket knife\\
-Shguu ndm gee na hackbacku. I need to sharpen my pocket knife.\\
\section*{hackbayckshg}
noun saw\\
-Wie ndsu hackbayckshg. Give me the saw.\\
\section*{hackdek}
noun bow; tool\\
-Goahl wilsh hackdek dm hoyu? What tool shall I use?\\
-Dm dsabu hackdek ndm gaa wineaya da hlguyu. I'm going to make a bow so I can get food for my family.\\
\section*{hackshgweekwshg}
noun instrument with holes; whistle\\
(-)-Lu'kwil aam wila how hackshgweekwshg dsabn. The sound of the whistle you made is very good.\\
\section*{hack'biyaan}
noun pipe for smoking\\
-Gishya'an hack'biyaan. Pass the pipe around.\\
\section*{hadaay}
noun steering wheel\\
-Labite hlgookshn dm daayu da boad, labite waal na hadaayu. I wasn't able to steer the boat, my steering wheel went out.\\
\section*{hadahaw}
verb to like to do, spend time doing\\
-Hadahawyu hla lu'bishu. I like to sew.\\
\section*{hadiksh}
verb to swim Plural:lahadiksh\\
-Lu'kwil hashacku dm hadikshu dsihla shuunt. I really want to swim when summer is here.\\
\section*{hadsag}
verb to be fatal\\
-Ha'dackgm sheepg wil hadsagt. He died from syphilis.\\
\section*{hadsikshm gik hawn}
verb to say again\\
-Hadsikshm gik hawn - ggal ckshdaamcka 'dsig'dsig. Say it again - the car was too loud.\\
\section*{hadsikshm gik waan}
verb to do again, repeat\\
-Hoyshga leemeeyn, hadsikshm gik waan. Your singing is beautiful, do it again.\\
\section*{hadsm}
prefix again\\
(-)-Hadsm kshidaawhld. She went out again.\\
\section*{ha-geemgm noahl}
noun dish cloth\\
-Shguu ndm yoaksha noahl. I have to wash the dish towels.\\
\section*{hageem'ka}
noun cloth to wipe with\\
(-)-Ndsu hageem'ka. Give me the cloth to wipe with.\\
\section*{haggagietk}
noun scissors\\
-Noayu en dsaba na hoyayu, hoy haggagietk dumt 'kotsa dm hoyt. My mother made my clothes, she used scissors to cut what she used.\\
\section*{hagwil}
prefix slowly\\
-Hagwil yaa 'yoota awil sheepga ggal'oasht. The man walked slowly because his stomach hurt.\\
\section*{hagwilhoo}
noun rope\\
-Wie 'dsuu hagwilhoo, 'nee dm hoyu hla oom hoanu. Well, the rope is strong, it's what I use to go fishing.\\
\section*{hagwil waan}
prefix to do slowly, slow down\\
-Hagwil waan hla yaawckgn. Eat slowly.\\
-Ggal 'deelda wila gyoan, hagwil waan. You're doing it too fast, slow down.\\
\section*{hagwilyaa}
verb to walk slowly\\
-Hagwil yaa 'yoota awil sheepga ggal'oasht. The man walked slowly because his stomach hurt.\\
\section*{hagwilya'dsa}
verb to ring bell slowly\\
-Hagwilya'dsa hashoicka waab dsuds wil dsaga gyad. The bell rings slowly at the church when someone dies.\\
\section*{hagwn}
noun horse mussel\\
-Eh! 'Tsamaatga 'guba hagwn. 'Nee guulm hla geeka aksh. Oh boy! The horse mussel tastes very good. That's what we get when the tide is low.\\
\section*{hagyoaksh}
noun keel\\
-Shgu ndm ama dsaba hagyoaksh. I have to repair the keel.\\
\section*{hahlalsh}
verb to work, labor\\
-'Tsuu hahlalsha hana'ack hlat shakshil waab. The woman worked hard when she cleaned the house.\\
\section*{hahldoa}
verb to put in front of fire\\
-Hahldoa loagakshgm hoaya da awaa lag. Put the soaked clothes by the fire.\\
\section*{hahldock}
verb to take along the beach\\
-Hahldocka ggan da 'kala aksh. Take the wood along the beach.\\
\section*{hahlgeeka}
adverb down the beach Plural:hak-hahlgeeka\\
-Ndm tckal'waayan da hahlgeeka. I'll meet you on the beach.\\
\section*{hahlibeeshk}
noun knife Plural:hakhahlibeeshk\\
-Ndsu hahlibeeshk. Dm sha shackanu. Give me the knife. I'm going to sharpen it.\\
\section*{hahloa}
noun cloth Plural:hakhahloa\\
(-)Lu'kwil goamtga hahloa gwa'a. This cloth is very soft.\\
\section*{hahloamboad}
noun sailboat\\
-Dm kshagyoatgu da Ta'gwaan da 'dsm hahloamboad. I am going to Metlakatla by sailboat.\\
\section*{hahloam gyamg}
noun flag Plural:hakhahloam gyamg\\
-Shguu hahloam gyamg da 'kam. We have a flag.\\
\section*{hahlwaal}
adverb along the beach\\
-Ama doa ckbeesh da hahlwaal 'kala aksh. Put the boxes nicely along the beach.\\
\section*{hahlyaa}
verb to walk along the beach\\
-Wiedsa hahlyaa'nm da 'kala aksh. Let's walk along the beach of the river.\\
\section*{hahlyaagw}
verb to hold skins toward fire to roast\\
-'Tsamaatga hoan na hahlyaagwda gyad da awaa lag. Fish whose skins are roasted by the fire taste good.\\
\section*{hahow}
noun what people are saying\\
-Hahow gyad hla goidiksha uuah. People are saying that the ooligans have arrived.\\
\section*{haickal}
verb to be determined, persistent\\
-Dm haickalan mdm wila da'ackhlga goa hashackan. You have to be persistent, then you will get what you want.\\
-Haickala hlguwoamhlg hla oom hoant. The child was determined when he went fishing.\\
\section*{haig}
noun aroma, smell; spirit\\
-Wudi 'biyaan na haigt. They smell like smoke.\\
\section*{haild}
quantifier many\\
-Wilaayu hailda maay. I know there's lots of fruit.\\
\section*{hakk}
noun goose\\
-Ha'weenhl backanee yoam hakk? Haven't you tasted roasted goose?\\
\section*{hakshm}
adverb again\\
-Hakshm leemeeyn, aam wila howt. Sing again, it sounded good.\\
\section*{haldaaksh}
noun ointment, medicine\\
-Ama haldaaksha woamsh. Devil's club is good medicine.\\
\section*{haldaaw}
verb to treat with medicine\\
-Haldaaw wil gwalga an'ont. Treat his hand with medicine where it is burned.\\
\section*{haldaawgit}
noun witchcraft\\
-Lebaasha gyad da haldaawgit. People are afraid of witchcraft.\\
\section*{haldm}
prefix to bring up, lift\\
-Haldm gaa likshoack. Bring up the door.\\
-Haldm gaa likshoack da awaayu. Bring up the door to me.\\
\section*{haldmbaa}
verb to agree to go with; to arise\\
-Haldmbaa hana'ack hlat tckanoo boad. The woman got up when she heard the boat.\\
-'Kineetgu ashda gganhlaag da haldmbaayu dm hahlalshu. I got up in the morning to go to work.\\
\section*{haldm'acklg}
verb to arise, to get up\\
-'Wee amhown dish maata - shguu dm haldm'acklgt. Holler at Martha - she has to get up.\\
\section*{haldm'oy}
verb to wake up\\
-Haldm'oy nakshn, hladm laaltgd da hahlalsht. Wake up your husband, he'll be late for work.\\
\section*{haleemee}
noun musical instrument\\
-Yagwat shiwilaaykwshgish Kayla haleemee. Kayla is learning to play the piano.\\
\section*{halhal}
noun something that spins; toy top\\
(-)Lu'kwil anoacka hlguwoamhlg halhal 'gilumu dish 'need. The child really like the top that I gave her.\\
\section*{hamoolg}
noun; verb bothersome thing, nuisance; to be bothered\\
-Hamoolgsh malee hla wil ayawa 'yoota. Mary is bothered when the man shouts.\\
\section*{hana'ack}
noun girl, lady, woman\\
-Ndayu na hlguhlgm hana'ackn? Where is your little girl?\\
\section*{hapckdooweew}
noun horn spoon\\
-Hapckdooweew dsaba gyad da ggan, 'nee hoym hla tckoackgm. People made horn spoons out of wood, that's what we use when we eat.\\
\section*{hapshgoulg}
noun spoon\\
-Yagwa sha hapshgoulgu. I am carving a spoon.\\
\section*{hapshgoulgm ggan}
noun wooden spoon\\
-Hashacku ndm geega hapshgoulgm ggan dsabn. I want to buy the wooden spoon you made.\\
\section*{hap'dsee}
noun comb\\
-Shakshen na hap'dseeyn. Clean your comb.\\
\section*{hash}
noun dog Plural:hashhaash\\
(-) Needsu hash ada doosh. I see a dog and a cat.\\
\section*{hashack}
verb to want\\
-Hashacku shameeym wun. I want deer meat.\\
\section*{hashdalksh}
noun ring finger\\
-Ggal geetga hashdalksha hana'ack dumt hoy gwishgwashm an'ont. The woman's ring finger is too swollen to wear her ring.\\
\section*{hasheepg}
noun sickness\\
-Luwantga ggoadu ndm gidigaa hasheepg. I'm worried that I might catch a sickness.\\
\section*{hashooshk}
noun trouble\\
-Hashooshga ligi goa waal hlgu 'yoota gwee. Whatever that boy does seems to cause trouble.\\
\section*{hashoyck}
noun bell\\
-Yedsa hashoyck dsida hashackanee. Ring the bell when you want me.\\
\section*{hathot'dackg}
verb to boil\\
-Hla hathot'dackga shgoosheed. The potatoes are boiling.\\
\section*{hawaalt}
noun arrow, spear, sharp fighting equipment\\
-Dsabish Joe hawaalt. Joe made an arrow.\\
\section*{hawala'awa}
noun weapon\\
-Goahl wilsh hawala'awa dm gaadn? What weapon are you going to take?\\
\section*{hawhaw}
noun lion\\
-Ha'weenhl needsinee hawhaw? Haven't you seen a lion?\\
\section*{hayaawckg}
noun fork\\
-Anoaggu shga 'naga hayaawckga hoyn. I like the length of the fork you're using.\\
\section*{hayatsk}
noun copper shield\\
(-) Lu'kwil hlu'daka hlaagigyad hayatsk. The old people treasured their copper shields.\\
\section*{ha'aksh}
noun dipper to drink with\\
-Dee lup shguu ha'akshu. I have my own dipper.\\
\section*{ha'ashya}
verb to sneeze\\
-Ashguu ha'ashya hlguwoamhlg. The child's sneeze is funny.\\
\section*{ha'ats}
noun tree stump\\
-Ggal 'weelaeksha ha'ats gwa'a. This stump is too big.\\
\section*{ha'bish}
noun cover, top of an object\\
-'Gwaatga ha'bisha ggaldm shikopee. The lid to the coffee pot is lost.\\
\section*{ha'dackg}
verb to be bad\\
-Lu'kwil ha'dackga lacka. The weather is bad.\\
-Ha'dackga wila gyoa hlgu 'yoota gwee, baashu goa dm wila walt. That young man is doing something wrong, I'm afraid of what he'll do.\\
\section*{ha'dackgm sheepg}
noun syphilis\\
-Ahlgadee aam ha'dackgm sheepg. Syphilis is not good.\\
-Labite waal 'yoota gwee, 'ken ha'dackgm sheepg dish 'need dowl sheepgt. That man messed up, he got syphilis, and got sick.\\
\section*{ha'dal}
noun cedar bark strips for baskets\\
-'Gilmsh Dzaak ha'dal dish 'need. Jack gave her cedar bark.\\
\section*{ha'dooshg}
noun broom\\
-Macka ha'dooshg. Put the broom away.\\
\section*{ha'dsaick}
noun index finger\\
(-).Na hoyu ha'dsaick ndm wilaay goa dm needsu lack book. I use my index finger to know what I'm seeing on the book. (Turn pages with it.)\\
\section*{ha'dsalt}
noun devil fish\\
(-) Lu'kwil hashacku ndm backa ha'dsalt. I really want to taste devil fish.\\
\section*{ha'dseekwsha}
noun wooden bailer for water\\
-Ndahl wil shguhl ha'dseekwsha? Where is the wooden brailer?\\
\section*{ha'dsinaash}
verb to have good luck, be lucky\\
-Aam dsa ap ha'dsinaasha shuunta gwa'a. It will be nice to have good luck this summer.\\
\section*{ha'dsiyaan}
verb to be lucky\\
-Ahl ha'dsiyaanee da sha gya'wn? Do you feel lucky today?\\
\section*{ha'dsi'uult}
noun snail\\
-Ama nee wila yaan, hailda ha'dsi'uult da gwa'a. Watch where you walk, there are lots of snails here.\\
\section*{ha'kalaaw}
noun club for killing slaves, fish or animals\\
-Ndsu ha'kalaaw awaan. Give me that seal club.\\
\section*{ha'kan}
noun to make it tough for\\
(-)Lu'kwil ha'kanm 'yoota hla baaldm dm hlimoamt. The man made it hard onus when we tried to help him.\\
\section*{ha'kayaan}
noun wooden war club, wooden slave killer\\
-Shuulga ha'kayaan hoy hlaagi gyad. The clubs used by people in the past were dreaded.\\
\section*{ha'koa}
noun back\\
-'Man ha'koayu. Rub my back.\\
\section*{ha'li}
prefix upon\\
-Shgu ha'li'daa da awaa 'nakshuneeshg. Put the chair by the window.\\
\section*{ha'libaashagganshk}
noun place to dry seaweed\\
-Sheeds dm hoym da ha'libaashagganshgm. We're going to use sheets for drying the seaweed.\\
\section*{ha'lickbaickshg}
noun sawhorse\\
-Na dsaba nagwaadu waab adat hoy ha'lickbaickshg. My father built a house and he used a sawhorse.\\
\section*{ha'lidal}
noun battlefield\\
-Goayu ha'lidalshm? What are you fighting over?\\
\section*{ha'lidsogg}
noun earth, world\\
-Hashacku dm gyeksha ha'lidsogg. I want peace on the earth.\\
\section*{ha'ligalmeelg}
noun playground\\
-Wie dm dsabm ha'ligalmeelg. Well, we'll fix up the playground.\\
\section*{ha'liggoad}
verb to assume, guess, think\\
-Ahl 'nee dee ha'liggoadn? Is that what you think too?\\
-Ha'liggoadu hladm yaa waash. I think it's going to rain.\\
-Ha'li ggoadu ndm goy Ta'gwaan. I think I'm going to go to Metlakatla.\\
\section*{Ha'li goo'bl Sha}
noun Tuesday\\
-Hla Ha'li goo'bl Sha gya'wn. Today is Tuesday.\\
\section*{Ha'li Kwshdoonsha Sha}
noun Friday\\
-Hla Ha'li Kwishdoonsha Sha gya'wn. Today is Friday.\\
\section*{ha'limalshk}
noun altar, pulpit\\
-Lu'kwil anoaggu ha'limalshga dsaba gyad. I really like the altar that the people made.\\
\section*{ha'linoak}
noun bed Plural:ha'liaahlg\\
-Ha'liggoadu nhluu ha'linoak wil shguu 'dsoacksh. I think the shoes are under the bed.\\
\section*{Ha'li Shgwaitga Sha}
noun Sunday\\
-Ha'li Shgwaitg dowl ggadsudsm, dowl leemeeym da 'dsm na Waabsh Shm'oygit ga Lackaga. On Sunday we go to church and sing the Lord's house.\\
\section*{Ha'li tckaalpcka Sha}
noun Thursday\\
-Dm gwindaawhl da Gitsgaan dsihla Ha'li tckaalpcka Sha. I'm going over to Ketchikan on Thursday.\\
\section*{ha'litckoackg}
noun dinner table\\
-Hailda wineaya da lack ha'litckoackg. There's lots of food on the table.\\
\section*{ha'litoa}
noun shelf\\
-'Lee shguu sha'winshk da lack ha'litoa. Put your books on the shelf.\\
\section*{ha'litoamnoahl}
noun cabinet, dish rack\\
-'Dsm waabtckoackga wil shguu ha'litoamnoahl. The cabinet is in the dining room.\\
\section*{ha'liwaalcksh}
noun floor\\
-Dm 'daayu da lack ha'liwaalcksh I'm going to sit on the floor.\\
\section*{ha'liwildoolgit}
noun battleground\\
-Ha'wahlgandee nee ha'liwildoolgit shawaadida Viet Nam. I haven't seen the battleground that's called Viet Nam.\\
\section*{Ha'li yaygga Sha}
noun Saturday\\
-Hla Hali yaygg dowla Gitsgaan habn, dm geegu wineaya. On Saturday we go to Kethikan to buy food.\\
\section*{ha'li'daa}
noun chair\\
-Ha'li'daa hashacksh noayu. My mother wants a chair.\\
\section*{ha'li'dameesh}
noun desk, table\\
-'Lee shguu ckbeesh da lack ha'li'dameesh. Put the box on the table.\\
\section*{ha'li'doygg}
noun day to greet people\\
-Lu amaam ggaggoada gyad da hla ha'li'doygg. People are happy on the day to greet people.\\
\section*{ha'li'dsul}
noun equipment for filleting fish; place for filleting fish\\
-Lu'kwil ama ha'li'dsulsh maata. Martha made a good place to fillet fish.\\
\section*{Ha'li 'Guul Sha}
noun Monday\\
-Hla Ha'li 'Guul Sha gwa'a. This is Monday.\\
\section*{Ha'li 'Gwilee Sha}
noun Wednesday\\
-Ndm tckal'waayn da waab tckoackg dsihla Hali'Gwilee Sha. I'll meet you at the restaurant on Wednesday.\\
\section*{ha'tsal}
noun octopus, squid, devil fish\\
-Wilaaysh Doreen ai'dsm ha'tsal. Doreen knows how to fry devilfish.\\
\section*{ha'wahlg}
verb to be against custom or law, forbidden\\
-Ha'wahlgadee badsgt. They haven't arrived yet.\\
-Na shguu gga'bala da 'koy dowl ha'wahlga dumt 'gwinoo gyad dumt hoyt. I have a gun but I don't allow anyone to ask to use it.\\
\section*{ha'weeni}
verb to wait\\
-'Ka ha'weeni, ndm hlimoamn! Wait a minute, I'll help you!\\
\section*{hieda}
noun Haida person\\
-'Dsuu hlgu hieda 'yoota gwa'a da'al aam wila Shm'algyackt. This young man is Haida but he speaks good 'TsmSHIAN language.\\
\section*{hiedmck}
noun Haida language\\
-Dee hashacku ndm wilaay hiedmck. I want to know the Haida language, too.\\
\section*{hieds}
verb to send\\
-Hiedsihla ckbeesh dish Dzon. Send the box to John.\\
\section*{hietg}
verb to stand Plural: macksh\\
-Ama hietga ggadsaagg da lack yuub. The cross stands good on the ground.\\
\section*{hiwaash}
noun southeast wind\\
-Giloamdsa 'goa'olda gooda'atsm shgyan dsihla gwaantga hiwaash. Don't forget your raincoat when the southeast wind starts.\\
\section*{hlaagi gyad}
noun olden times, old people\\
-Shaggiet waal hlaagi gyad. The old people are meeting together.\\
\section*{hlacksh}
noun claw Plural:hlikhlacksh\\
-Shuulga hlacksha 'kalmoash. The crab's claws are fearsome.\\
\section*{hlackshmshee}
noun toenail\\
-Ggal 'nik'nuunga hlackshmsheeyn. Your toenails are too long.\\
\section*{hlackshm'dsiwaalt}
noun fingernail\\
-Ama'basha wil gyeda hlackshm'dsiwaaltn. Your fingernails are a pretty color.\\
\section*{hlaggiack}
noun; verb curved knife for carving; to be bent\\
-Shgu ndm geega shu hlaggiack. I have to buy a new carving knife.\\
\section*{hla tgiyaa sha}
noun dusk\\
(-).Lu'kwil gyeksha wil hla tgiyaa sha. It's peaceful at dusk.\\
\section*{hla'ashg}
noun seaweed\\
(-).Na dsaba nakshu hla'ashg ashda gi'dseeb da up lu'kwil 'tsamaatgd. My wife made some seaweed yesterday and it tasted real good.\\
\section*{hla'at}
noun ball Plural:hlikhlaat\\
-Ggal 'weelaeksha hla'ata gwee. That ball is too big.\\
\section*{hla'kiackshg}
verb to climb\\
-Mun hla'kiackshga hlgu awta da lack ggan. The porcupine climbed up the tree.\\
-Na hla'kiackshgu da lackoa waab da geedsa tgeokshe. I climbed up on the roof and almost fell down.\\
\section*{hla'kods}
noun rhubarb\\
-Aam dm guulda hla'kods da gyalck. Hla meegt. It's time to gather the rhubarb outside. They're ripe.\\
\section*{hlgaawg}
noun sister\\
-Eh! lu'kwil ama'basha hlgaawgu. Wow! My sister is very pretty.\\
\section*{hlgookshn}
verb to be unable, can't Plural: hlackhlgookshn\\
(-)Hlgookshu dm hadikshu. I'm not able to swim.\\
-Lu'kwil wilaay wila gyoa 'yoota bite hlgooksh'nu ndm hoy'ant. That man knows what he doing and I can't do it like him.\\
\section*{hlguhlg}
noun small child\\
-Lu'kwil wilgoashga na hlguhlgu. My small child is very intelligent.\\
\section*{hlguhlgm noahlt}
noun doll\\
-Yagwan dsaba dm na'acka hlguhlgm noahlsh Kayla. I am making a dress for Kayla's doll.\\
\section*{hlgumad}
noun egg\\
-Hailda hlgumad da ggagoom. The seagull has lots of eggs.\\
\section*{hlgumadm ggagoom}
noun seagull egg\\
-Hla guul gyad hlgumadm ggagoom. lu'kwil 'tsamaatgt gya'wn. People are looking for seagull eggs. It really tastes good now.\\
\section*{hlgu shggay}
noun little finger, pinky\\
-Sheepga hlgu shggayu. My little finger hurts.\\
\section*{hlgutcka'oa}
noun cousin\\
-Hashacku ndm nee hlgutcka'oayu. I want to see my cousin.\\
\section*{hlguwoamhlg}
noun child, infant\\
-Amaggoada hlguwoamhlga gwee. That little child over there is always friendly.\\
\section*{hlgu 'yoota}
noun boy\\
-Nagwaada hlgu 'yoota gwee. That is the boy's father.\\
\section*{hlimoam}
verb to help\\
-Aam hlimoamsh dp gwa'a. ahlgadee shm ggal aamhl wila load. Let's help these. They aren't doing well.\\
\section*{hli'oan}
noun Indian bread\\
-Eh! Wilaay nakshu dsaba hli'oan. Wow! My wife sure knows how to make Indian bread.\\
\section*{hlmkdee}
noun brother\\
-Yagwa goo hlmkdeeyu 'tu'itsgm ol. My brother is hunting for black bear.\\
\section*{hloa}
verb to be fast, go fast\\
-Lu'kwil hloa 'dsig'dsig da lack guyna. The car goes really fast on the road.\\
-Lu'kwil hloa boadsh John Leask. John Leask's boat is really fast.\\
\section*{hload}
verb to honor, respect\\
-Wie aam mdm hloada 'yoota, aam wila howd da 'kam. Well, we should respect the man, what he says is good.\\
-Hloadm na waabsh Shm'oygit ga Lackaga. We respect the house of the Lord.\\
\section*{hloontee}
verb to be angry Plural:lukhloontee\\
-Sha hloontee na shila hahlalshu. My coworker got angry all of a sudden.\\
-Na hloontee n'dse'etsu awil ahlgandee dsabhl guyna. My grandmother got mad because I didn't fix the street.\\
\section*{hlub}
verb to be deep\\
-Hluba aksh dm wil hadikshu. The water is deep where I'm going to swim.\\
-Na oom hoanu dowl hluba wil 'ken yeeh. I went fishing and the King Salmon was in deep water.\\
\section*{hluk'kwdaa'yn}
noun grandchildren\\
-Yagwa shayuu hlgu hluk'kwdaa'yn da 'koy. My little grandchild is hiding from me.\\
\section*{hlumsh}
noun in-law\\
-Hailda hlumshu gya'wn. I have a lot of in-laws now.\\
\section*{hoan}
noun fish, salmon\\
-Yagwa guba nagwaadu hoan. My father is eating fish.\\
\section*{hoaya}
noun clothing Plural: hakhoaya\\
-Hashacku shu hoaya. I want new clothes.\\
\section*{homhom}
noun ankle\\
-Sheepga homhomu. My ankle hurts.\\
\section*{hoom}
verb to smell\\
-Hoomu 'biyaan. I smell smoke.\\
\section*{hoom'tsack}
verb to kiss\\
-Oy hoom'tsack da hlgu teedsa. Throw the teacher a kiss.\\
\section*{hoo'bl}
adverb at night\\
-Hoo'bl dee wil gakshga na gga'dsaaw gyad. Some people are really awake at night.\\
\section*{hou'ts}
noun duck\\
-Ha'wahlgan dee nee wil gipaiga hou'ts I haven't seen the ducks fly.\\
\section*{how}
noun voice\\
-Gakshga hlguwoamhlg hlat tcka'noo na howsh noat. The child woke up when she heard her mother's voice.\\
\section*{hoy}
verb to use, wear\\
-Hoy bilaan, ggal 'weelaeksha na 'backshn. Wear a belt, your pants are too big.\\
\section*{hoyack}
verb to be correct\\
-'Hoyacka wila how hana'ack. The woman sounds right.\\
(-)Lu'kwil aam wila gyoan. hoyacka hoyen. You're doing real well. What you're using is correct.\\
\section*{hoyshg}
verb to be handsome, nice looking, pretty\\
-Hoyshga madsiggalay. The flower is beautiful.\\
-Hoyshga madsiggalay macksht da awaa waabn. The flowers by your house are beautiful.\\
\section*{hukdsab}
noun somebody who can do many things well\\
-Needsu shga hukdsabsh Tony. I see how many things Tony can do.\\
\section*{hultg}
verb to be full Plural:halhultg\\
-Hultga waabu da wineaya. My house is full of food.\\
-Na aadm da gwashga, gawdee aadm dowla lu 'kend da lack boad dowla hultga'nm. We went fishing over there, when we were done fishing the boat was full.\\
\section*{hultga giamg}
noun full moon\\
-Dm gik hultga giamg dsidaawhl. It will be a full moon again tonight.\\
\section*{ihlay}
noun blood\\
-Ihlay 'dmggowsha doosha gwee. That cat's head is bleeding.\\
\section*{kboal}
number ten people\\
-Kboal shgaboo gyad dm tckoackgt. Ten people will eat.\\
\section*{klushmsh}
noun Nass River\\
-Shayaa shgaboo hoan da klushmsh. There are fewer fish in the Nass River.\\
\section*{kshabatsk}
verb to stick out\\
-Ahlgadee aamhl dm kshabatsga gga'bala da 'newalee. It's not good to have the gun stick out from the backpack.\\
\section*{kshadsackoatg}
verb to be naked, nude, without clothing\\
-Kshadsack'oatga 'yoota hla hadiksht. They were naked on the beach.\\
\section*{kshagaa}
verb to take out\\
-Kshagaa loagikshgm goda'ats ada 'yackt. Take out the soaking wet coat and hang it.\\
\section*{kshagwaantg}
verb to come out\\
-Hashacku dm 'kwihlbaayu hla kshagwaantga giamg. I want to run about when the moon comes out.\\
-Ashda giyaatg dowla kshagwaantga 'wee giamg. Last night the big moon came out.\\
\section*{kshalacklack}
verb to be born\\
-Shuunt wil kshalacklackgu. I was born in the summer.\\
-Gganhaada dee wil kshalacklackgn. You were born of the Raven.\\
\section*{kshashashee}
verb to be barefooted\\
-Kshasha ggashishee 'gubatguuhlg da gyalck. The children were barefooted outside.\\
-Kshasha ggashishee 'gubatguuhlg, ahlgadeet da'acklga gyad dumt geega 'dsoacksh. The children were barefooted because the people weren't able to buy shoes.\\
\section*{ksha'anaash}
verb to be naked, nude, without clothing\\
-Ksha'anaash Hukdsab hla hadiksht. Tony went swimming naked.\\
-Ahlgandee neehl wil ksha'anaash gyad hla hadiksht. I haven't seen people go swimming naked.\\
\section*{ksha'dsal}
noun half-dried fish\\
-Ahl anoackanee ksha'dsal? Do you like half-dried fish?\\
\section*{kshda'moash}
number nine abstract, round or flat objects\\
-Kshda'moasha shgaboo noahl dm yoakshm. We're going to wash nine plates.\\
\section*{kshdm'ashoal}
number nine people\\
-Kshdm'ashoal gyad gwin daawhld da Gitsgaan. Nine people went over to Ketchikan.\\
\section*{kshdnshoal}
number five people\\
-Ksha kshdnshoal shaboo gyad dm leemeet. Only five people are going to sing.\\
\section*{kshdsood}
noun waiter\\
-'Tsuu hahlalsha kshdsood da wil loolgita gyad. The waiter worked hard where the people feasted.\\
\section*{ksheel}
noun tear, teardrop Plural:ggaksheelt\\
-Kshabaa ksheel hal wil shgaaygshgt. Her tears ran when she got hurt.\\
-Hla weehowtgu da ksheelu. When I cry the teardrops come out.\\
\section*{ksheeshg}
verb to settle for damages done\\
-Luamaam ggaggoadm hla wil ksheeshga 'yoota. We were happy when the man settled for the damages.\\
\section*{kshgoack}
verb to be first, ahead\\
-Kshgoackt Nancy da 'koy. Nancy is first before me.\\
-Na sha'apyaa'nu da lack geeka dowl ksgoacka nakshu. I was walking on the beach and my wife was ahead of me.\\
\section*{kshi'nag}
noun middle finger\\
-Kshi'nag de hoyu hlan lu 'dsaicka wineaya da ggiehlu. I use my middle finger to lick out the bowl.\\
\section*{kshlushg}
noun shirt Plural:ggakshlushg\\
-Aam 'ka shakshn kshlushgn. 'tsa'tsiksht. Clean your shirt. It's dirty.\\
\section*{kshlushgm noak}
noun nightgown\\
-Dm hoyu kshlushgm noak dsihla noakee. I'm going to wear a nightgown when I go to bed.\\
\section*{kshuud}
noun autumn, fall\\
-Dm guuldm hoan dsihla kshuud deehl goamshm. We'll harvest fish in the fall and winter.\\
\section*{kwdacksh}
verb to go away from, leave a place\\
-Dm kwdackshm ggaldoa. Dm luyeltgm hloula aam lacka. We're going to leave the village. We'll return while the weather's good.\\
\section*{kwdag}
verb to shoot (arrow, gun)\\
-Ggabackshga'nu hla kwdaga 'yoota. I was startled when the man shot the gun.\\
\section*{kwdee}
verb to be hungry Plural:lukwdee\\
-Hla kwdeeyu. I'm hungry.\\
-Na shaupwaalckshm ashda 'guulda shada dowl lu'kwil kwdeeyu dowla luyeltgm. We went walking the other day and I got hungry so we came home.\\
\section*{kwdoosh}
noun knife\\
-Giloamdsa 'koa'olda kwdoosh. Don't forget the knife.\\
\section*{kwhlacksh}
verb to kick; to press, put weight on\\
-Kwhlackshu hla'at da awaa 'yoota gwee. I kicked the ball to the man there.\\
\section*{kwhlackshhla'at}
noun football\\
-Goahl shm anoacka gyad kwhlackshhla'at? Why do people really like football?\\
\section*{kwhleeggiackn}
verb to scrape, grind to pieces\\
-Shu mdm kwhleeggiackn na anaasha wun. You have to really scrape the deer hide.\\
\section*{kwhlee ggolggol}
verb to come apart entirely, to be nothing left\\
-Kwhlee ggolggol boad da wil 'dsuu baashg. The wind tore the boat apart until it was gone.\\
\section*{kwhleeyedsg}
verb to pound\\
-'Naga hahlalsht n'dse'etsu hlat kwhleeyedsa hla'ashg. My grandmother worked a long time when she pounded the seaweed.\\
\section*{kwhlee'ba'gya}
verb to be dented; to bend, dent badly\\
-Kwhlee'ba'gya 'dsig'dsig da wil oksha 'wee loab. The big rock that fell dented the car.\\
\section*{kwhlee'doosh}
verb to punch; to knock out\\
-Da'apsh en kwhlee'doosht Dan. David knocked Dan out.\\
\section*{kwhlee'kayaan}
verb to hit, beat up with a club\\
-Kwhlee'kayaan 'wee hoan, hloula didoolsht. Hit the big fish, it's still alive.\\
\section*{kwhl'aack}
noun lips\\
-Ashguu kwhl'aacka hlguwoamhlg hla hloonteed. The child's lips are funny when he's angry.\\
\section*{kwshdoonsh}
number five flat, round or abstract objects\\
-Kwshdoonsha mashgm 'na'ba'la dm geegu. I'm going to buy five red buttons.\\
\section*{kw'dsag}
noun slingshot\\
-Kw'dsag hoysh Kayla hlat goo hla'at. Kayla used a slingshot to shoot the ball.\\
\section*{kyoagg}
noun grass\\
-Lu'kwil meehoksha kyoagg hla 'kotst. Grass smells really good when it's cut.\\
\section*{laaksha aksh}
noun high tide\\
-Dm shigyoatgm dsihla laaksha aksh. We will leave at high tide.\\
\section*{laakwsh}
noun light\\
(-).Lu'kwil hailda laakwsh da lack guyna. There are lots of lights on the street.\\
\section*{laald}
noun worm\\
-Needsu laald da nhluu loab. I saw a worm under the rock.\\
\section*{laaltg}
verb to be slow Plural:ggalaaltg\\
-Labite laaltga wila gyoa 'yoota gwee. That man is slow.\\
\section*{laam}
noun alcohol\\
-Giloamdsa geega laam. Don't buy alcohol.\\
\section*{laan}
noun salmon eggs\\
-Shm ama goa laan, 'nee dm hoym hla goog hla'ashgm. Fish eggs are really good, that's what we'll use when we cook seaweed.\\
\section*{laandsa}
prefix to start\\
-Laandsa shaggiet 'koal ggaggoadm. Let's all be of one heart.\\
\section*{laa'wil}
verb to wrap up\\
-Laa'wil ckbeesh nagoaga mdm hiedst. Wrap up the box before you send it.\\
\section*{labaalck}
verb to detest, hate\\
-Ahlgadee shguuhl dm labaalcka shila gyadn. You don't have to hate your fellow man.\\
-Labite hloontee wila waal 'yoota gwee da labaalcku wila howt. That man was angry and I detested what he was saying.\\
\section*{labaggietwaal}
verb to do something wrong, make a mistake\\
-Ahlgadee hashacku dm labaggietwaalu. I don't want to do something wrong.\\
-Lu'kwil ahlgadee aamhl wila gyoa 'yoota gwee, labitewaalt. That man did not do good, he did something wrong.\\
\section*{laba'on}
noun arm muscle\\
-'Weelaeksha laba'onsh Alik. Alec has large arm muscles.\\
\section*{lack}
prefix on, upon\\
-'Lee shguu wush da lack ha'li'dameesh. Put the blanket upon the table.\\
\section*{lacka}
noun sky\\
-'Kineetgu ashda gganhlaaga dowl lacka wil nee'etsgu ndm nee dsihla waash. When I woke up the other morning and I looked up to the sky to see if it would rain.\\
\section*{Lackaga}
noun above, Heavens, weather\\
-Ahl tckanooynee goal dm wila waal Lackaga dsigi'dseeb? Have you heard what the weather is going to do tomorrow?\\
\section*{lackdee}
adverb on the hill\\
-Needsu wun da lackdee. I can see the deer on the hill.\\
\section*{Lack-giboo}
noun Wolf Clan\\
-Lack-giboo wil hokshgt nakshu. My husband belongs to the Wolf Clan.\\
\section*{lack guyna}
adverb on the road\\
-Lu'kwil hloa wila baa 'dsig'dsig a lack guyna. The car is going to fast on the road.\\
\section*{lackhoo}
noun sand bar\\
-Na 'yagayaam da lackhoo, nayaayu, gwinee'dsn da wil 'ken ha'dsalt, dowlt 'waad da lack loab. My grandfather and I walked down to the sandbar and he showed me where the devilfish was and we found it on the rock.\\
\section*{Lack-shgeeg}
noun Eagle Clan\\
-Lack-shgeeg wil hokshgu. I belong to the Eagle Clan.\\
\section*{lackshumaay}
noun month of picking berries, summertime\\
-Yagwa shamaayt. He/she is picking berries.\\
\section*{lackshuulda}
noun ocean\\
-Baasha'nu hla 'weelaeksha ggoab da lackshuulda. I get afraid when the waves on the ocean are big.\\
\section*{lack waalee magwa'ala}
verb to have hard times\\
-Tckanooyu wil lack waalee magwa'ala hlaagigyad. I heard that old people had hard times.\\
\section*{lackyuub}
adverb on the ground\\
-'Lee shguu lag da lackyuub. Lay the firewood on the ground.\\
\section*{lack'aksh}
adverb on the water\\
-Gyoaksha 'wee ggan a lack'aksh. The tree is floating on the water.\\
\section*{lack'anaaym uua}
verb to boil ooligans in a pot\\
-Wie dsa dup dsam lack'anaaym uua. Let's boil some ooligans in a pot.\\
\section*{lack'awsh}
adverb on the sand\\
-Wiedsa sha lagm da lack'awsh. Lets build a fire on the sandy beach.\\
\section*{lack'daa}
noun lake\\
-Hailda 'ts'uu'uts da lack'daa. 'Nee dm goym. There are a lot of birds on the lake. That's where we're going.\\
\section*{lack'dsimaay}
adverb on the barnacles\\
-Ama needsn da lack'dsimaay. Be careful on the barnacles.\\
\section*{lack'oa}
noun top of\\
-'Lee shguu sha'winshg da lack'oa ha'li'dameesh. Put the paper on the table.\\
\section*{lack'oa waab}
noun roof\\
-Na hla'kiackshgu da lack'oa waabu da goadsa wila waalu, ahlgadee da'ackgu dm tgiyaayu. I climbed on my roof and couldn't do anything, I wasn't able to get down.\\
\section*{lack'U}
noun muskeg; upon muskeg\\
-Ama needsa wila yaan da lack'U. You have to walk carefully on the muskeg.\\
\section*{lag}
noun fire, firewood\\
-Wie dsadp shietdoa lag. Let's gather wood.\\
\section*{lageel}
noun eyebrow, eyelashes\\
-Yagwat 'kockda hana'ack na lageelt. The woman is plucking her eyebrows.\\
\section*{laggee}
noun hair-kelp for herring eggs to cling to\\
-'Ka anoacku cksh'waanck da lack laggee. I like herring eggs on hair kelp the best.\\
\section*{laguulgit}
noun; verb burnt possessions of a dead person; to burn possessions of a dead person\\
-'Guul ganootg dm daawhlt nagoacka dm laguulgita gyad. People are supposed to wait one week before they burn.\\
\section*{lapwail}
noun frying pan\\
-Lu tckalgwalga na lapwailu. My frying pan is burned inside.\\
\section*{lawaal}
noun happening\\
-Luamaam ggaggoada gyad da lawaalt. The people were happy at the gathering.\\
\section*{la'uu}
noun trout\\
-Ggal hailda shayb da la'uu, 'nee gn ahlgndee anoackt. There are too many bones in a trout, that's why I don't like it.\\
\section*{lebilt haaw}
verb to argue against\\
-Lebilt haaw hana'ack hlat tckanoo wil bee'ega hlguhlgt. The woman argued when she heard her child lie.\\
\section*{leediksh}
verb to awaken\\
-Leedikshgn 'gubatguuhlg. Wake up children.\\
-Leedikshga hlguyu dm ggashgoolt gganhlaagagwa'a. My children woke up to go to school this morning.\\
\section*{leemee}
noun; verb song; to sing\\
-Hla dsudsu dowla leemeeym da Shm'oygit 'dsm lacka. We went to church and sang to God in Heaven.\\
\section*{leemya'tseshg}
noun fur animal\\
-Hailda leemya'tseshga wil 'kohla 'dsig'dsig. There's a lot of animal fur on the highway.\\
\section*{leetsg}
noun; verb grouse; to count\\
-Moakshga na shamee leetsg. Grouse meat is white.\\
\section*{le'wul}
noun drops of water, water drops\\
-'Nawinoa le'wul da lack wileelm tgwayu. The water drops on my eyeglasses are annoying.\\
\section*{ligeetnaa}
noun anybody, anyone, anything, somebody, someone, something\\
-Ligeetnaa dm ent geega gwa'a. Anyone will buy this.\\
\section*{liggiwaal}
noun belongings, possessions, clothing\\
-'Gwaatga tcka'nee na liggiwaalsh Peda da 'dsm lag. All of Peter's belongings were lost in the house fire.\\
\section*{ligi}
conjunction or\\
-'Nuuyu ligit 'nuun dm daawhlt da Gitsgaan. Either you or I will go to Ketchikan.\\
\section*{likshgyad}
noun something else, a different thing\\
-Likshgyadm ggaldsap wil 'waatgm. We come from a different village.\\
\section*{likshgyadmgyad}
noun a different person, someone else\\
-Likshgyadmgyad 'daad da awaayu. A different person sat by me.\\
\section*{likshoack}
noun door\\
-'Kacka likshoack. giamga gyalck. Open the door. It's warm outside.\\
\section*{liksh'daa}
noun island\\
-Liksh'daa gyalck wil wun shgoosheedm. The island is where we plant potatoes.\\
\section*{lipgeekhl}
interjection Buy it yourself!\\
-Lipgeekhl. Buy it yourself.\\
\section*{liphahaw}
verb to be ineffective\\
-Ahlgadee amooksha gyad dish 'need awil liphahawd. Nobody listens to her because she's ineffective.\\
\section*{liphown!}
interjection Say it yourself!\\
-Liphown na algyacka Shm'oygit ga Lackaga awil dm ggatgyadn. Say the words of God to yourself so you will be strong.\\
\section*{liplaid}
noun minister, pastor, preacher, priest\\
-Shmhow algyacka liplaid. The pastor preached the truth.\\
-Gatgyada amhow liplai da gwa'a. The pastor has a strong voice.\\
\section*{lipnahow}
verb to talking to oneself\\
-Shiggene'etsga gyad da hana'ack hla lipnahowt. People stared at the woman when she talked to herself.\\
\section*{lish'yaan}
noun boil (on the skin); mink\\
-Dm 'manu haldaaksh da lish'yaan. I'm going rub medicine on boil.\\
-Hailda lish'yaan da nlack yuubu. There are a lot of mink on my trap line.\\
\section*{loab}
noun rock, stone Plural:liploab\\
-Geedsa sha'okshu da lack loab. I almost fell down on the rock.\\
\section*{loan}
noun horse clam\\
-Wilaaym wil 'dahla loan. We know where the horse clam can be found.\\
\section*{loa'ds}
noun elderberries\\
-Dm guuldm loa'ds dsihla dsigi'dseeb. We'll pick elderberries tomorrow.\\
\section*{loolgit}
noun feast\\
-Dm hoym gwish'na'ba'la dsihla loolgit. We will wear a button blanket when there is a feast.\\
\section*{loolp}
noun fish trap\\
-Ahlgadeet naa en hoy loolp da sha gya'wn. Nobody uses fish traps today.\\
\section*{loonda hloadihl}
verb to put together\\
-Yagwat loonda hloadihla taggan awil dmt dsaba guyna. He's putting the planks together because he's making a path.\\
\section*{loopg}
verb to sew\\
-Hla loopgat noayu shu goda'ats. My mother is sewing a new coat.\\
\section*{loyg}
verb to move camp\\
-Ggal hailda loygn. You packed too many things with you.\\
\section*{ludaaltg}
verb to meet\\
-Ndm ludaaltgn da awaa ggaldmwa'at. I will meet you at the store.\\
\section*{ludaawhla giamg}
noun afternoon\\
-Shoonaahla'nu hla ludaawhla giamg. I am tired in the afternoon.\\
\section*{ludamdam}
verb to hug\\
-Needsu wil ludamdamcksh Dush hlgu 'yoota. I saw Doris hug the man.\\
\section*{ludoa}
verb to be inside\\
-Ludoa hoan da 'dsm gwai'hl. Put the fish in the sack.\\
\section*{ludoahl}
verb to put inside\\
-Ludoahl da 'dsm gi'dsoan. Put it into the closet.\\
\section*{lugowshga aksh}
noun low tide\\
-Wie hla lugowshga aksh. Aam dm sha ggaboackm. The tide is low. Let's get some cockles.\\
\section*{lugwaantg}
noun time for\\
-Hla lugwaantga dm wil yaawckga hlguwoamhlg. It's time for the little child to eat.\\
\section*{luhoa'Nhl}
verb to fill\\
-Luhoa'N oomhl da 'koy? Will you fill the bucket for me?\\
\section*{lukhleehoaya}
noun undergarment\\
-Ahl shakshakshga na lukkwhleehoyyan? Are your underclothes clean?\\
\section*{lukhleekshlushg}
noun undershirt\\
-Ggal gyamga hlguwoamhlg, 'nee gun ahlgadeet hoy lukhleekshlushg. The child was too warm, that's why he didn't wear an undershirt.\\
\section*{lukhlee'backsh}
noun underpants\\
-Hoy lukhlee'backsh da nhluu 'backsha dsinan. Wear underpants under your jeans.\\
\section*{lumaaksh}
verb to wash clothing or soft material\\
-Yagwat lumaaksha lukhleehoyyat. She is washing her undergarments.\\
\section*{lup na waal}
verb to fight, compete against each other\\
-Lu'kwil lup na waal hlaagi gyad. Our ancestors competed against each other.\\
-Lup na waalm hla hla'atm da Town Hall. We compete against each other when we play basketball at the Town Hall.\\
\section*{luwantg}
verb to worry\\
-Luwantga ggoada hana'ack hla 'gwaatga naksht. The woman worried when her husband was lost.\\
\section*{luwantgmggoad}
verb to be worried\\
-Luwantgmggoadu hla 'tsuu baashg. I get worried when the wind is strong.\\
\section*{luyeltg}
verb to return, turn back\\
-Dm luyeltga'nu da awaash noayu. I'm returning to mothers.\\
\section*{lu'bish}
verb to sew\\
-Yagwat lu'bishga gwish'na'ba'lat. She is sewing on her button blanket.\\
\section*{lu'dsakya}
verb to go out (of fire)\\
-Hl'loontee hana'ack hla lu'dsakya lag. The woman was angry when the fire went out.\\
\section*{lu'gen}
verb to put in\\
-Lu'gen ggan'dameesh da 'dsm ckbeesh. Put the pencil in the box.\\
\section*{lu'kwil}
verb to be many, very\\
(-)-Lu'kwil 'tsimaatga ai'dsm tckow. Fried halibut tastes very good.\\
\section*{lu'kwil ama ggoad}
verb to be a kind person\\
(-)'Lu'kwil ama ggoadish Meli. Mary is very kind.\\
-Lu'kwil ama ggoada 'yoota gwee dat 'gilm daala da 'koy. That man is very kind and he gave me money.\\
\section*{lu'wai}
verb to get caught in the act, be found out\\
-Lu'wai nakst da wila loat. His wife found out what they were doing.\\
\section*{lu'wal}
leak\\
-Luwantga ggoada 'yoota hlat nee wil lu'wal ckshoa. The man was worried when he saw that his canoe leaked.

% === English to Shm'algyack Dictionary ===
\section*{abalone}
abalone: bilha.\\
\section*{abdomen}
abdomen, belly, stomach, tummy: ban.\\
\section*{able}
can, to be able: da'ackhlg.\\
\section*{above}
above, Heavens, weather: Lackaga.\\
\section*{accident}
to have an accident, make a mistake: ashdeewaal.\\
\section*{accompany}
to accompany: shdool.\\
\section*{accumulate}
to accumulate, get fat, increase: akshyaa.\\
\section*{accurate}
right amount; correct, accurate assessment: aamndap.\\
\section*{across}
across the way, the opposite side: doashda. to be able to go across: dsagga'acklg. to walk across: dsaggayaa.\\
\section*{adaptable}
to be adaptable: tckalaam.\\
\section*{add}
to add to, bring to, tie to: tckalhokshnhl.\\
\section*{adequate}
to be enough, adequate, ample, plentiful: aamshgaboo.\\
\section*{advise}
to advise, counsel; to rebuke, scold, talk to in a mean manner: daalck.\\
\section*{adze}
adze: 'dackwunsh.\\
\section*{a few}
a few, some: na gga'dsaaw.\\
\section*{afraid}
to be afraid: baash.\\
\section*{aft}
aft of boat, back end, rear, stern: gilaan.\\
\section*{after a while}
after a while; to be far enough, long enough: aamshga'nak.\\
\section*{afternoon}
afternoon: ludaawhla giamg.\\
\section*{again}
again: gik, hakshm, hadsm. to do again, repeat: hadsikshm gik waan.\\
\section*{against}
to be against custom or law, forbidden: ha'wahlg.\\
\section*{agility}
agility, performance, poise: debeesh.\\
\section*{ago}
some time ago: gitckawtk. years ago; long ago: gi'goahl.\\
\section*{agree}
to agree, allow, give permission; to like: anoagg. to agree, consent: ga'wa. to agree to go with; to arise: haldmbaa.\\
\section*{aground}
to run aground: 'dseeka.\\
\section*{ahead}
to be first, ahead: kshgoack.\\
\section*{alcohol}
alcohol: laam.\\
\section*{alive}
to be alive: didoolsh.\\
\section*{all}
all: tcka'nee.\\
\section*{all of}
all of, the entire: 'gipcka.\\
\section*{allow}
to agree, allow, give permission; to like: anoagg. to allow, let: anoahl.\\
\section*{almost}
almost here: ayamgwa'a. almost, just about: geedsa. almost there: ayamgwai.\\
\section*{alright}
alright!; behold!; well now; let's start!; okay!: wie wa!.\\
\section*{also}
to come, come here; too, also: ggal.\\
\section*{altar}
altar, pulpit: ha'limalshk.\\
\section*{amazing}
to be amazing: shanaahlg.\\
\section*{amen}
amen: 'Neehlwaan.\\
\section*{among}
among, between: shbaggiet.\\
\section*{ample}
to be enough, adequate, ample, plentiful: aamshgaboo.\\
\section*{anchor}
anchor: ggadailpk.\\
\section*{and}
and: ada, dihl.\\
\section*{angel fish}
angel fish, rat fish: goomaa.\\
\section*{angry}
to be angry: hloontee.\\
\section*{animal}
animal: ya'tseshg.\\
\section*{ankle}
ankle: homhom.\\
\section*{annoying}
to be bothersome, annoying: 'nawinoa.\\
\section*{anoint}
to anoint, grease, massage, oil, rub: 'man.\\
\section*{answer}
to answer, reply: deelmckg.\\
\section*{antler}
antler, horn: ggaggawsh.\\
\section*{anus}
anus: 'dsm'kol.\\
\section*{anxious}
to be anxious: aba'ackshg.\\
\section*{anybody}
anybody, anyone, anything, somebody, someone, something: ligeetnaa.\\
\section*{anyone}
anybody, anyone, anything, somebody, someone, something: ligeetnaa.\\
\section*{anything}
anybody, anyone, anything, somebody, someone, something: ligeetnaa.\\
\section*{apparition}
apparition, ghost, spirit, vision: noogit.\\
\section*{appear}
to appear: gwineeshk.\\
\section*{applaud}
to applaud, clap hands: 'daashg.\\
\section*{apple}
crabapple: moalksh.\\
\section*{appreciation}
to express appreciation, thank: 'doycksh. to thank, express appreciation: 'doyck.\\
\section*{approach}
to approach shore: 'nadalpg.\\
\section*{argue}
to argue against: lebilt haaw.\\
\section*{arise}
to agree to go with; to arise: haldmbaa. to arise, to get up: haldm'acklg.\\
\section*{arm}
arm, hand: an'on. arm muscle: laba'on. shoulder, upper arm: 'dm'kie.\\
\section*{armor}
wooden body armor: gganhlaan .\\
\section*{armpit}
armpit: 'tsm'tsansh.\\
\section*{aroma}
aroma, smell; spirit: haig.\\
\section*{arrive}
to arrive: goydiksh. to arrive, land: badsg.\\
\section*{arrogant}
to be arrogant, haughty, proud, snobbish, stand-offish: adsiksh.\\
\section*{arrow}
arrow: 'daish. arrow, spear, sharp fighting equipment: hawaalt.\\
\section*{ascend}
to ascend, go up, walk up: munyaa.\\
\section*{ashamed}
to be ashamed: dsoack.\\
\section*{ashes}
ashes from a fire: oonkshig.\\
\section*{ashore}
ashore, inland: dsaggm. to go ashore: dsaggmdaawhl.\\
\section*{aside}
aside, away: awul.\\
\section*{ask}
to ask, inquire: guudack.\\
\section*{assume}
to assume, guess, think: ha'liggoad.\\
\section*{astonished}
to be astonished, surprised: shanaahlg.\\
\section*{at}
at, by, near: awaa.\\
\section*{athlete's foot}
athlete's foot, toes that have a smell: sh'kaancksh.\\
\section*{attempt}
to attempt: she'ehl.\\
\section*{attention}
to listen, obey, pay attention: amooksh.\\
\section*{aunt}
aunt: da'ash.\\
\section*{autumn}
autumn, fall: kshuud.\\
\section*{await}
to wait, await: babood.\\
\section*{awaken}
to awaken: leediksh.\\
\section*{aware}
to get out of the way; to make aware, warn: boo'ihl.\\
\section*{away}
aside, away: awul. to stay away for a long time: ayuwaan.\\
\section*{axe}
axe, hatchet: gigyoatk.\\
\section*{baby}
baby boy: 'yoo'uck.\\
\section*{back}
back: ha'koa.\\
\section*{backbone}
backbone: 'dm'koa.\\
\section*{back end}
aft of boat, back end, rear, stern: gilaan.\\
\section*{backpack}
backpack: 'newalee. backpack; strap to carry things: gganawulee.\\
\section*{back room}
back room: gi'dsoan.\\
\section*{backwards}
to run backwards: 'dsnkbaa. to walk backwards: 'dsnkyaa.\\
\section*{bad}
to be bad: ha'dackg.\\
\section*{bail}
to bail water (out of a canoe, boat): dseekwsha.\\
\section*{bailer}
wooden bailer for water: ha'dseekwsha.\\
\section*{bait}
bait: 'naa. halibut bait: 'naam tckaw.\\
\section*{ball}
ball: hla'at.\\
\section*{barefooted}
to be barefooted: kshashashee.\\
\section*{bark}
bark (of a tree); leg cramp: maash. gather cedar bark: bayckggan.\\
\section*{barnacle}
barnacles; great-great-grandchildren: 'dsimaay.\\
\section*{barnacles}
on the barnacles: lack'dsimaay.\\
\section*{barrel}
keg, barrel: 'nhla'naggan.\\
\section*{basket}
basket: goack. basket : 'dsilaa. cedar bark basket: doohlk.\\
\section*{battlefield}
battlefield: ha'lidal.\\
\section*{battleground}
battleground: ha'liwildoolgit.\\
\section*{beach}
along the beach: hahlwaal. down the beach: hahlgeeka. to take along the beach: hahldock. to walk along the beach: hahlyaa.\\
\section*{beads}
beads on a string, necklace: ggahood.\\
\section*{bear}
bear: ol. bear, brown bear, grizzly bear: madeeg. black bear: 'tu'utsgm ol. brown bear: mashgm'ol, mish'ol. polar bear: moakshgm'ol.\\
\section*{bear berries}
bear berries: maaym ol.\\
\section*{beard}
beard: eemck. White man, bearded man: gga'eemck.\\
\section*{beat}
to hit, beat up with a club: kwhlee'kayaan.\\
\section*{beaten up}
to be beaten up, exhausted, overworked: plakshkw.\\
\section*{beautiful}
to be beautiful, good looking, handsome, pretty: ama'bash.\\
\section*{beaver}
beaver: sh'dsoal.\\
\section*{bed}
bed: ha'linoak.\\
\section*{bee}
bee, hornet, yellow jacket: ab.\\
\section*{begin}
to begin: sha'daa.\\
\section*{behind}
to stay behind: ginawaal.\\
\section*{behold}
alright!; behold!; well now; let's start!; okay!: wie wa!.\\
\section*{believe}
something that one believes in; to promise: nashmhowtksh.\\
\section*{bell}
bell: hashoyck. to ring bell slowly: hagwilya'dsa.\\
\section*{belly}
abdomen, belly, stomach, tummy: ban.\\
\section*{belongings}
belongings, possessions, clothing: liggiwaal.\\
\section*{belt}
belt: bilaan.\\
\section*{bend}
to be dented; to bend, dent badly: kwhlee'ba'gya. to bend, bend over, bow: ckbishmshguu. to bend forward, bow, stoop: ggogg.\\
\section*{bent}
curved knife for carving; to be bent: hlaggiack.\\
\section*{bentwood box}
bentwood box: uunck.\\
\section*{berries}
bark container to pick berries in: 'yoo. bear berries: maaym ol. berries : 'dmmeet. berries, fruit: maay. elderberries: loa'ds. gray berries along river bank: dsaygg. laughing berries, salal berries: dsawush. month of picking berries, summertime: lackshumaay. raven berries: maaym ggaagg. rope berry, trailing blackberry: maayha gwilhoo. Saskatoon berries: gyem. thunder berries: maaym ggalipleeb. yellow berries on muskeg: ggol'ge.\\
\section*{better}
to get better: ggakshwil a'aamt.\\
\section*{between}
among, between: shbaggiet.\\
\section*{big}
to be big: 'weelaeksh.\\
\section*{bigger}
to be bigger: 'ka 'weelaeksh.\\
\section*{big man}
big man, Chief, noble: algyackshg.\\
\section*{big toe}
big toe: moashm shee.\\
\section*{bind}
to be caught in a bind, tight space: 'dsaab. to bind against: tckal'dsaab.\\
\section*{bird}
bird: 'tsu'uts.\\
\section*{bitter}
to be bitter: gushck.\\
\section*{black}
to be black: 'tu'utsg.\\
\section*{black bear}
black bear: 'tu'utsgm ol.\\
\section*{blackberry}
rope berry, trailing blackberry: maayha gwilhoo.\\
\section*{blackboard}
blackboard, chalkboard: 'lee'dameeshm ggan.\\
\section*{black duck}
black duck: amgeeg.\\
\section*{blanket}
blanket: wush. button blanket: gwish'na'ba'la.\\
\section*{blind}
to be blind: shuunsh.\\
\section*{blink}
to blink, wink: ggapshil.\\
\section*{blizzard}
north blizzard, snow on north side of tree: shda'magsha shdoa ggan.\\
\section*{blond}
blond or reddish hair; horsefly: gigim'uugg.\\
\section*{blood}
blood: ihlay.\\
\section*{blow}
to blow: shwun. to blow; wind: baashg.\\
\section*{blue}
to be blue (in color): gwishgwashg.\\
\section*{blueberry}
blueberry: 'tu'utsgm maay.\\
\section*{blue jay}
blue jay: gwishgwaash.\\
\section*{boat}
boat: boad. fishing boat: shacksh oomhoan.\\
\section*{body}
body: tcka'moa.\\
\section*{boil}
boil (on the skin); mink: lish'yaan. to boil: hathot'dackg. to boil, cook: dsam. to boil ooligans in a pot: lack'anaaym uua.\\
\section*{boiled}
boiled whole fish: tckadsmpshg.\\
\section*{bold}
to be bold, brave, courageous: aalck.\\
\section*{bone}
bones: shayb.\\
\section*{bone marrow}
bone marrow: 'dsee'dsee.\\
\section*{boots}
boots: hoods.\\
\section*{born}
to be born: kshalacklack. to be soaking wet; to be just born: 'nabaa.\\
\section*{borrow}
to borrow: gwaashg.\\
\section*{both}
both: mela goo'bl.\\
\section*{bother}
to bother, chase, go after, hunt: shuwileen.\\
\section*{bothered}
bothersome thing, nuisance; to be bothered: hamoolg.\\
\section*{bothersome}
bothersome thing, nuisance; to be bothered: hamoolg. to be bothersome, annoying: 'nawinoa.\\
\section*{bow}
bow (of boat): gi'dsoygg. bow; tool: hackdek. to bend, bend over, bow: ckbishmshguu. to bend forward, bow, stoop: ggogg.\\
\section*{bowl}
bowl: ggiehl.\\
\section*{box}
bentwood box: uunck. box: ckbeesh. Indian box, storage box: ggal'uunck.\\
\section*{boy}
baby boy: 'yoo'uck. boy: hlgu 'yoota.\\
\section*{brag}
to brag a lot: dseekshhawtksh.\\
\section*{braid}
to braid: ggadeeshg.\\
\section*{brail}
to brail, bring above water: 'dsab.\\
\section*{brain}
brain: woon ggawsh.\\
\section*{branch}
dead tree branch: ggaiggai. tree branch: aneesh.\\
\section*{brave}
to be bold, brave, courageous: aalck.\\
\section*{bread}
bread: anaay. fried bread: ai'dsm anaay. ghost bread: adaggan. Indian bread: hli'oan. to make bread: sha'anaayshk.\\
\section*{break}
to break (bread, dried food): 'ba'an. to break, crack: 'gwash. to break in, break open (with hammer, axe): 'nayets.\\
\section*{break up}
to break up, chop, club, hit, pound: yeds.\\
\section*{breast}
milk, woman's breast: me'ish.\\
\section*{breath}
breath; who?: naa.\\
\section*{breathe}
miracle, wonder; to breathe: shanaahl.\\
\section*{bright}
to be bright: goy'ba.\\
\section*{bring}
to add to, bring to, tie to: tckalhokshnhl. to bring along: tckayaagwihl. to bring towards, pull in: tckalshagihl.\\
\section*{bring food}
to bring food, pack a lunch: 'dsiloom.\\
\section*{bring up}
to bring up: mundockhl. to bring up, lift: haldm.\\
\section*{broken}
to be broken : 'gwish'gwash.\\
\section*{broom}
broom: ha'dooshg.\\
\section*{brother}
brother: hlmkdee. our brothers: wakyam.\\
\section*{brothers}
our brothers, our own people: nlip 'dsabam.\\
\section*{brown bear}
bear, brown bear, grizzly bear: madeeg. brown bear: mashgm'ol, mish'ol.\\
\section*{bucket}
bucket, pail: oomhl. bucket, pail, water container: ggaldm'aksh.\\
\section*{build}
to build, construct, make: dsab.\\
\section*{build a fire}
to build a fire: shalagsh.\\
\section*{built strong}
to be built strong; to put on warm clothes: doycksh.\\
\section*{bull}
bull, cattle, cow: mishmoosh.\\
\section*{burn}
burnt possessions of a dead person; to burn possessions of a dead person: laguulgit. to burn: gwalg. to burn up: 'dsee'bltk. to trim hair by burning ends: gwalka.\\
\section*{burnt}
burnt possessions of a dead person; to burn possessions of a dead person: laguulgit.\\
\section*{burp full}
to be full; to burp: 'dsaay.\\
\section*{burst}
to burst: ckleeuu.\\
\section*{bush}
elderberry bush: shggan loa'ds. salmonberry bushes: gga'koacksh.\\
\section*{butterfly}
butterfly: adabeesh.\\
\section*{button}
button: 'na'ba'la. button, clasp to hold cape on; safety pin: ggan'doa. to button up: 'bal.\\
\section*{button blanket}
button blanket: gwish'na'ba'la.\\
\section*{buy}
Buy it yourself!: lipgeekhl. hemlock (tree or wood); mosquito; to buy; to fly: geek.\\
\section*{by}
at, by, near: awaa.\\
\section*{cabbage}
cabbage: gabids.\\
\section*{cabinet}
cabinet, dish rack: ha'litoamnoahl.\\
\section*{calendar}
calendar: sha'winshgm giamg.\\
\section*{call}
to name, call by name: aytk.\\
\section*{call down}
expression used for calling down one who is doing badly: dsa'ee.\\
\section*{calm}
calm in the weather: maadm gyekshg. to be calm: shagyeksh, gyeksh.\\
\section*{camp}
camp: ggaldoa. fish camp on Annette Island: Nadzaheen. to camp: ggaldsock. to cohabit, picnic, play camp, have a small party: shishdsoacksh. to move camp: loyg.\\
\section*{can}
can, to be able: da'ackhlg.\\
\section*{cane}
cane: 'ka'at.\\
\section*{cannon}
cannon; thunder: ggalipleep.\\
\section*{canoe}
People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes: Gitlan.\\
\section*{can't}
to be unable, can't: hlgookshn.\\
\section*{cap}
cap: ggaidm 'dsagg.\\
\section*{car}
car, wagon, vehicle: 'dsig'dsig.\\
\section*{careful}
to be careful, cautious, watchful: amane'ets.\\
\section*{careless}
to be careless: 'wa'ama ne'ets.\\
\section*{caribou}
caribou, reindeer: woo'dsee.\\
\section*{carrot}
carrot: galot.\\
\section*{carry}
to carry along with other things: muntckadockhl. to carry, take: dock. to carry, take along: shndock. to take, carry along: tckalgaa.\\
\section*{cat}
cat: doosh.\\
\section*{catch}
place to catch fish: 'na'oomhoan. to fish, catch salmon: 'mag.\\
\section*{cattle}
bull, cattle, cow: mishmoosh.\\
\section*{caught}
to be caught in a bind, tight space: 'dsaab.\\
\section*{caught}
to get caught in the act, be found out : lu'wai.\\
\section*{caulk}
to caulk an opening; to grow: 'bash. to caulk, seal: 'bish'bash.\\
\section*{cautious}
to be careful, cautious, watchful: amane'ets.\\
\section*{cave}
cave: 'tsmloab.\\
\section*{cedar}
red cedar: amggan. red cedar tree: ggalaaw. yellow cedar: wahl.\\
\section*{cedar bark}
cedar bark strips for baskets: ha'dal. gather cedar bark: bayckggan.\\
\section*{cedar bark basket}
cedar bark basket: doohlk.\\
\section*{celery}
wild celery: 'beensh.\\
\section*{centennial}
centennial (100 yrs): 'gyaba wil 'gyap'gyaba 'goahl.\\
\section*{chair}
chair: ha'li'daa.\\
\section*{chalkboard}
blackboard, chalkboard: 'lee'dameeshm ggan.\\
\section*{challenging}
to be expensive; difficult; challenging; steep; valuable: 'doackg.\\
\section*{channel}
through a sea channel: mackla.\\
\section*{charcoal}
charcoal, coal, soot: ggam'do'otsk.\\
\section*{chase}
to bother, chase, go after, hunt: shuwileen.\\
\section*{chatterbox}
chatterbox: ashgyaback.\\
\section*{cheap}
cheap goods: gganwaal. poor stuff, cheap things: ggamwaal.\\
\section*{cheater}
cheater, trickster: nacknockm 'yood. clever woman, woman cheater, woman trickster: nacknockm hana'ack.\\
\section*{cheek}
cheek: da'oack.\\
\section*{chest}
chest: ggayg.\\
\section*{chew}
to chew: ggawn.\\
\section*{Chief}
big man, Chief, noble: algyackshg. Chief, head of: meyaan. Git Lan Chief: Neesh hlagganoosh. leader, person of high ranking, Chief, Mayor: Shm'oygit.\\
\section*{Chief of the Heavens}
Chief of the Heavens, God: Shm'oygit ga Lackaga.\\
\section*{child}
child, infant: hlguwoamhlg. small child: hlguhlg.\\
\section*{children}
children: 'gubatguuhlg.\\
\section*{chimney}
chimney, smoke hole: ala.\\
\section*{chin}
chin: maaw. chin, indentation under the lip: 'kowts.\\
\section*{China slipper}
China slippers: 'dsak.\\
\section*{Chinook salmon}
King salmon, Chinook salmon: yeeh.\\
\section*{choke}
to choke, get something caught in the throat: 'gyag.\\
\section*{chop}
to break up, chop, club, hit, pound: yeds. to chop out: shmksheeyeds. to chop, split wood: bishboosh. to split, to chop: boosh.\\
\section*{chum salmon}
chum salmon, dog salmon: ggayneesh.\\
\section*{circle}
to spin, run in circle: dsagga-tgubaa.\\
\section*{citrus}
to taste sour, citrusy: moalkshack.\\
\section*{claim}
to talk, say, claim too much: ggal'dsuu.\\
\section*{clam}
clam: 'dsa'ack. horse clam: loan.\\
\section*{clan}
clan: pdeack. Eagle Clan: Lack-shgeeg. Killer Whale Clan: Gish-budwada. Wolf Clan: Lack-giboo.\\
\section*{clap}
to applaud, clap hands: 'daashg.\\
\section*{clasp}
button, clasp to hold cape on; safety pin: ggan'doa.\\
\section*{claw}
claw: hlacksh.\\
\section*{clean}
to be clean: shakshg.\\
\section*{clear}
to be clear, evident, visible: ggontgahl.\\
\section*{clever}
clever woman, woman cheater, woman trickster: nacknockm hana'ack.\\
\section*{cliff}
cliff, rock wall: biyaackl.\\
\section*{climb}
to climb: hla'kiackshg.\\
\section*{clock}
clock, watch: waads.\\
\section*{close}
to close, shut: shga'doosh.\\
\section*{cloth}
cloth: hahloa. cloth to wipe with: hageem'ka. dish cloth: ha-geemgm noahl.\\
\section*{clothespin}
clothespin, scissor-like tool: gganhla'ka'winshk.\\
\section*{clothing}
belongings, possessions, clothing: liggiwaal. clothing: hoaya.\\
\section*{cloud}
cloud, day: sha.\\
\section*{club}
club for killing slaves, fish or animals: ha'kalaaw. to break up, chop, club, hit, pound: yeds. to hit, beat up with a club: kwhlee'kayaan. to hit with a stick or club: 'galyeds. wooden war club, wooden slave killer: ha'kayaan.\\
\section*{coal}
charcoal, coal, soot: ggam'do'otsk.\\
\section*{coat}
coat: gooda'ats. goat skin coat: gwishmatee. raincoat: gooda'atsm shgyen.\\
\section*{cockle}
cockle: ggaboack.\\
\section*{cockles}
dried cockles: ggalsh.\\
\section*{coffin}
coffin : 'nishuushg.\\
\section*{cohabit}
to cohabit, picnic, play camp, have a small party: shishdsoacksh.\\
\section*{coho}
coho salmon: uuck.\\
\section*{cold}
to be cold: gwatg.\\
\section*{color}
color: wilgyed.\\
\section*{comb}
comb: hap'dsee.\\
\section*{come}
come!: ggalshm hoa, ggalshm. to come, come here; too, also: ggal.\\
\section*{come apart}
to come apart, be irreparable; to be strewn loosely: ggol. to come apart entirely, to be nothing left: kwhlee ggolggol.\\
\section*{come back}
to come back out of the woods: 'nayeltg.\\
\section*{come empty handed}
unlucky; come empty handed: ggal'waatk.\\
\section*{come from}
to be found; to come from: 'waatg.\\
\section*{come in}
to come in, enter, go in: 'dseen.\\
\section*{come out}
to come out: kshagwaantg.\\
\section*{come up}
to come up above the water: gyabn.\\
\section*{compassion}
compassion: 'kaa ggoadn.\\
\section*{compassion}
compassion: shila ndmhow.\\
\section*{compete}
to fight, compete against each other: lup na waal.\\
\section*{competent}
to be competent, healthy, lucky: wukdsab.\\
\section*{completed}
to be completed, well-designed, well-proportioned; to do over, fix, repair : amadsab.\\
\section*{conflict}
fight, conflict; to fight: dal.\\
\section*{consent}
to agree, consent: ga'wa.\\
\section*{construct}
to build, construct, make: dsab.\\
\section*{consume}
to consume; to lose a game, war; to be consumed: dsahl.\\
\section*{container}
bark container to pick berries in: 'yoo. container: goadsagid, nta, ggaldm.\\
\section*{cook}
to boil, cook: dsam. to cook potatoes in sand near fire: ood.\\
\section*{cooked}
to be cooked, done: gwaanksh.\\
\section*{cool}
to cool, simmer down: ggoash.\\
\section*{copper shield}
copper shield: hayatsk.\\
\section*{corduroy pants}
corduroy pants: 'backshm ggaboack.\\
\section*{corner}
corner of house: amoosh. to put away in a corner: dseehldoa.\\
\section*{corpse}
corpse, ghost: baal'ack.\\
\section*{correct}
right amount; correct, accurate assessment: aamndap. to be correct: hoyack.\\
\section*{cottonwood}
cottonwood tree: am'baal.\\
\section*{counsel}
to advise, counsel; to rebuke, scold, talk to in a mean manner: daalck.\\
\section*{count}
grouse; to count: leetsg.\\
\section*{courageous}
to be bold, brave, courageous: aalck.\\
\section*{cousin}
cousin: hlgutcka'oa. female cousin: oa'ash.\\
\section*{cover}
box cover, lid: nahaapt. cover, top of an object: ha'bish. to cover: 'leetlumhlk. to sprinkle on: 'lee'buul.\\
\section*{cow}
bull, cattle, cow: mishmoosh.\\
\section*{crab}
crab: 'kalmoash.\\
\section*{crabapple}
crabapple: moalksh. crabapple tree: shggan moalksh.\\
\section*{crack}
to break, crack: 'gwash.\\
\section*{cracked}
to be cracked; to be crazed: ggalaag.\\
\section*{cramp}
bark (of a tree); leg cramp: maash.\\
\section*{crazed}
to be cracked; to be crazed: ggalaag.\\
\section*{crazy}
to be crazy: moamsh.\\
\section*{creek}
creek, river, stream: 'kala aksh.\\
\section*{creep}
to creep; to sit in protest of moving or going: ggailkshg.\\
\section*{cross}
cross, gable of roof: ggadsaagg.\\
\section*{crosswind}
crosswind: dsaggabaashg.\\
\section*{crow}
crow: 'kaw'kaaw.\\
\section*{crush}
to crush, mash: 'beehl.\\
\section*{cry}
to cry, weep: weehawtg.\\
\section*{curious}
to be curious of details, inquire into: maggoanshga.\\
\section*{curly}
to be curly: aw'awshg.\\
\section*{custom}
to be against custom or law, forbidden: ha'wahlg.\\
\section*{cut}
to cut, saw off: shackaicksh-ga. to cut, slice: 'kots.\\
\section*{cut off}
to cut off, get rid of: sha'kots.\\
\section*{dampen}
to dampen; to sprinkle: dsakshuld.\\
\section*{dance}
to dance: meelg. to dance in: 'dsilmmeelg.\\
\section*{darkness}
darkness: shgaaytg.\\
\section*{dawn}
dawn, daybreak: akshyaagwa dseewsh.\\
\section*{day}
cloud, day: sha. day to greet people: ha'li'doygg.\\
\section*{daybreak}
dawn, daybreak: akshyaagwa dseewsh.\\
\section*{daylight}
daylight, daytime: dseewsh.\\
\section*{daytime}
daylight, daytime: dseewsh.\\
\section*{dead}
burnt possessions of a dead person; to burn possessions of a dead person: laguulgit. to die, be dead: duu, dsag.\\
\section*{dear}
dear miss or woman: daahl. term of endearment towards a male: naat.\\
\section*{decay}
to spoil, decay: ckaatg.\\
\section*{decoration}
decoration: noo'anshg.\\
\section*{decree}
decree, message, official statement: ayaawgg.\\
\section*{deep}
to be deep: hlub.\\
\section*{deep winter}
deep winter, hard times: magwa'ala.\\
\section*{deer}
deer: wun.\\
\section*{deer meat}
deer meat: shameeym wun.\\
\section*{defrost}
to defrost, melt, disappear, lose weight or size: dseeb.\\
\section*{dent}
to be dented; to bend, dent badly: kwhlee'ba'gya.\\
\section*{dented}
to be dented; to bend, dent badly: kwhlee'ba'gya.\\
\section*{depart}
to depart, go away, leave: dawhl.\\
\section*{descend}
dusk; to descend, go down;: tgiyaa.\\
\section*{desk}
desk, table: ha'li'dameesh.\\
\section*{determined}
to be determined, persistent: haickal.\\
\section*{detest}
to detest, hate: labaalck.\\
\section*{develop}
to develop, enlarge, expand, grow, increase: tckalyaa.\\
\section*{devil fish}
devil fish: ha'dsalt. octopus, squid, devil fish: ha'tsal.\\
\section*{devil's club}
devil's club: woamsh.\\
\section*{diaper}
diaper: 'bashee.\\
\section*{die}
to be willing to die: gilksh-shamackshd. to die, be dead: duu, dsag.\\
\section*{different}
a different person, someone else: likshgyadmgyad. something else, a different thing: likshgyad.\\
\section*{difficult}
to be expensive; difficult; challenging; steep; valuable: 'doackg.\\
\section*{diluted}
to be diluted, weak: alashkw.\\
\section*{dinner table}
dinner table: ha'litckoackg.\\
\section*{dip}
to dip, draw water: gyab.\\
\section*{dip net}
dip net, net brail: bana.\\
\section*{dipper}
dipper to drink with: ha'aksh.\\
\section*{dirty}
to be dirty, dusty, soiled: 'dsa'dsiksh.\\
\section*{disagree}
to disagree, disbelieve, doubt: ckshaangg.\\
\section*{disappear}
to defrost, melt, disappear, lose weight or size: dseeb.\\
\section*{disbelieve}
to disagree, disbelieve, doubt: ckshaangg.\\
\section*{disguise}
disguise, effigy, mask: ameelg.\\
\section*{dish}
dishes: noahl. iron dish: ggiehlam'do'otsk.\\
\section*{dish cloth}
dish cloth: ha-geemgm noahl.\\
\section*{dish rack}
cabinet, dish rack: ha'litoamnoahl.\\
\section*{distant}
distant: agwee.\\
\section*{distribution}
distribution: ya'anshg.\\
\section*{divided}
to be divided: bashackg.\\
\section*{dizzy}
to get dizzy, drunk: sheen.\\
\section*{dodge}
to dodge; miss: geeshk. to dodge, move out of the way: shageeshk.\\
\section*{dog fish}
dog fish: ggashggaads.\\
\section*{dog salmon}
chum salmon, dog salmon: ggayneesh.\\
\section*{doll}
doll: hlguhlgm noahlt.\\
\section*{dolphin}
dolphin, porpoise: dseeyuu.\\
\section*{done}
to be cooked, done: gwaanksh.\\
\section*{door}
door: likshoack, ggamggantk.\\
\section*{do over}
to be completed, well-designed, well-proportioned; to do over, fix, repair : amadsab.\\
\section*{doubt}
to disagree, disbelieve, doubt: ckshaangg.\\
\section*{do well}
somebody who can do many things well: hukdsab.\\
\section*{down}
chief's headgear; eagle down: 'bilgwa. down, downward: tgi.\\
\section*{downpour}
down pour: ggadsiksh.\\
\section*{Do your best!}
Do your best! Wishing you well!: sha'aamdza waan.\\
\section*{dragonfly}
dragonfly: giladse'eds.\\
\section*{draw}
to dip, draw water: gyab. to draw, take a picture: gilkshtckal'da'minshg. to draw, write: na'dum.\\
\section*{dreaded}
middle; something fearful; to be dreaded, fearful: shuulg.\\
\section*{dress}
baby sister; dress, skirt: na'ack.\\
\section*{dressed up}
to get dressed up: nootg.\\
\section*{dried}
to be dried hard, stiff with cold: ggantk.\\
\section*{dried fish}
dried fish: guunkshm hoan.\\
\section*{dried fish strips}
dried fish strips: 'kiewoaksh.\\
\section*{drift}
to drift away: shagyoaksh.\\
\section*{driftwood}
driftwood; White person, European: umsheewa.\\
\section*{drink}
to be wet, to drink; water: aksh. to give a drink: gil'aksh.\\
\section*{drop}
drops of water, water drops: le'wul. to drop, let go: ggal'oa.\\
\section*{drum}
drum: 'noahl.\\
\section*{drunk}
to get dizzy, drunk: sheen.\\
\section*{dry}
dry items (clothes, fish): shiloonu. place to dry seaweed: ha'libaashagganshk. to be dry: guunksh. to dry: shiloonksh. to string up, put on drying pole: ggahlg.\\
\section*{dry rot}
dry rot: mahaaya.\\
\section*{duck}
black duck: amgeeg. duck: hou'ts.\\
\section*{durable}
to be durable, live a long life: aigyad.\\
\section*{duration}
duration, length (of time, space): shga'nakt.\\
\section*{dusk}
dusk: hla tgiyaa sha. dusk; to descend, go down;: tgiyaa.\\
\section*{dusty}
to be dirty, dusty, soiled: 'dsa'dsiksh.\\
\section*{each}
each: mihla.\\
\section*{eagle}
eagle: ckshgeeg.\\
\section*{Eagle Clan}
Eagle Clan: Lack-shgeeg.\\
\section*{ear}
ear: 'tsimoo.\\
\section*{earth}
earth, ground, land, soil: yuub. earth, world: ha'lidsogg.\\
\section*{earthquake}
earthquake: 'yaagw.\\
\section*{eat}
to eat: gub, yaawckg. to eat fish: ckhoan. to eat Indian ice cream: ckdaiksh. to eat with: ckdee.\\
\section*{eclipse}
moon eclipse: 'dseen gyamgm'aatk. sun or moon eclipse: 'dseen giamgm'aatk.\\
\section*{edge}
next to the water, at the water's edge: geeka.\\
\section*{effigy}
disguise, effigy, mask: ameelg.\\
\section*{egg}
egg: hlgumad. seagull egg: hlgumadm ggagoom.\\
\section*{eggs}
herring eggs: cksh'waanck. salmon eggs: laan.\\
\section*{eight}
eight abstract, round or flat objects: 'yee-kwdal. eight people: 'ye-kwhladoal.\\
\section*{elbow}
elbow; night pot: ma'oan.\\
\section*{elderberries}
elderberries: loa'ds. People of the Elderberries: Gishbackloa'ds.\\
\section*{elderberry bush}
elderberry bush: shggan loa'ds.\\
\section*{elderberry jam}
elderberry jam: goowaagg.\\
\section*{eldest}
eldest one: sheelgit.\\
\section*{electricity}
electricity, lightning: 'dsamtee.\\
\section*{else}
a different person, someone else: likshgyadmgyad. something else, a different thing: likshgyad.\\
\section*{emery wheel}
emery wheel, whet stone: dashgyan.\\
\section*{empty}
to be empty, not there: ggalbash. to empty, make empty: aplugawdee.\\
\section*{end}
end: 'dsiwaand.\\
\section*{enemy}
enemy intruders, raiders: gitwaaltk.\\
\section*{English}
English language: Umsheewaamck.\\
\section*{enlarge}
to develop, enlarge, expand, grow, increase: tckalyaa.\\
\section*{enough}
to be enough, adequate, ample, plentiful: aamshgaboo. to be not enough: wanoack. to lack, not to have enough: shgoaksh.\\
\section*{enter}
to come in, enter, go in: 'dseen.\\
\section*{entire}
all of, the entire: 'gipcka.\\
\section*{erase}
to erase: shahleel.\\
\section*{err}
to err, miss, make a mistake, do something wrong: geesh.\\
\section*{escape}
to escape, run away, flee: 'gyaickg.\\
\section*{European}
driftwood; White person, European: umsheewa.\\
\section*{evening star}
evening star: beyaalshm aatk.\\
\section*{everybody}
everybody: tcka'nee gyad.\\
\section*{everyone}
everyone: tcka'nee mihla 'goald.\\
\section*{everything}
everything: tcka'nee goa.\\
\section*{evident}
to be clear, evident, visible: ggontgahl.\\
\section*{exchange}
to exchange, pay back, reciprocate, return: shidyaawd.\\
\section*{exhausted}
to be beaten up, exhausted, overworked: plakshkw.\\
\section*{expand}
to develop, enlarge, expand, grow, increase: tckalyaa.\\
\section*{expect}
to expect, hope for, wait for: booyshg.\\
\section*{expensive}
to be expensive; difficult; challenging; steep; valuable: 'doackg.\\
\section*{eye}
eye: wileel.\\
\section*{eyebrow}
eyebrow, eyelashes: lageel.\\
\section*{eyeglasses}
eyeglasses: wileelm tgwa.\\
\section*{eyelashes}
eyebrow, eyelashes: lageel.\\
\section*{face}
face; to fillet fish: 'dsal.\\
\section*{faint}
to faint: ma'ul. to faint, pass out: daamshack.\\
\section*{fall}
autumn, fall: kshuud. to fall: tgi'oksh. to fall down: shaguyna, gga'dsihl'oksh. to fall, splash: booboo. to fall; to hit: oksh. to fall to one side: 'kahl'oksh.\\
\section*{falsehood}
falsehood, lie: bee'eg.\\
\section*{far away}
far away: wietdoa, wil'nak.\\
\section*{far enough}
after a while; to be far enough, long enough: aamshga'nak.\\
\section*{fart}
to fart: 'bashu, 'poo'a.\\
\section*{fast}
to be fast, go fast: hloa. to be fast, quick; to go fast: 'dmyaa. to do faster, quickly: di'deeld. to do quickly, work fast: 'deeld. to hold, hold fast, hold tight: dackyaagw.\\
\section*{fasten}
to fasten: tckal'daabit. to fasten to, tie on: tckal'dseeb.\\
\section*{fat}
to accumulate, get fat, increase: akshyaa.\\
\section*{fatal}
to be fatal: hadsag.\\
\section*{father}
father: ba'a. my father: aab, nagwaadu.\\
\section*{father of}
father of: nagwaat.\\
\textbf{fawn}\\
fawn: gwish'dseeg.\\
\textbf{fearful}\\
middle; something fearful; to be dreaded, fearful: shuulg.\\
\textbf{feast}\\
feast: loolgit.\\
\textbf{feel}\\
to feel something will happen; admonition: gyelkwsh. to feel; to try, venture: baal.\\
\textbf{feet}\\
feet: ggashishee.\\
\textbf{fellow}\\
poor fellow: gwinaat.\\
\textbf{fern}\\
edible root; fern-like plant: aah. fern-like plants: damtee.\\
\textbf{few}\\
a few, some; to be a few: shgaboo. to be a few, some, several: aboo.\\
\textbf{fight}\\
fight, conflict; to fight: dal. to fight, compete against each other: lup na waal.\\
\textbf{fill}\\
to fill: luhoa'Nhl.\\
\textbf{fillet}\\
equipment for filleting fish; place for filleting fish: ha'li'dsul. face; to fillet fish: 'dsal.\\
\textbf{find}\\
to find: 'waay.\\
\textbf{fine}\\
to be fine, good, well: aam.\\
\textbf{finger}\\
finger: 'dsiwaalt. index finger: ha'dsaick. little finger, pinky: hlgu shggay.\\
\textbf{fingernail}\\
fingernail: hlackshm'dsiwaalt.\\
\textbf{fingers}\\
fingers: ggadsiwaald.\\
\textbf{finished}\\
to be done with: gawdee.\\
\textbf{fire}\\
fire, firewood: lag. fire in the water; phosphorescent algae: adaahl. open fire: shmlag. to build a fire: shalagsh. to put in front of fire: hahldoa.\\
\textbf{fireplace}\\
fireplace: nlag.\\
\textbf{fireweed}\\
fireweed: haash.\\
\textbf{firewood}\\
fire, firewood: lag.\\
\textbf{first}\\
to be first, ahead: kshgoack.\\
\textbf{fir tree}\\
fir tree: alda.\\
\textbf{fish}\\
boiled whole fish: tckadsmpshg. dried fish: guunkshm hoan. dried fish strips: 'kiewoaksh. expression when sighting fish jump: ayow. fish, salmon: hoan. fried fish: ai'dsm hoan. half-dried fish: ksha'dsal. old fish: dsalee. place to catch fish: 'na'oomhoan. salted fish: moanm hoan. to eat fish: ckhoan. to fish, catch salmon: 'mag. to fish for rock cod: oom ggaagg. to fish with a net, seine for fish: aadm hoan. to gather fish, work on fish: shihoan.\\
\textbf{fish camp}\\
fish camp on Annette Island: Nadzaheen.\\
\textbf{fish head}\\
fish head: 'dmggowshm hoan.\\
\textbf{fish hook}\\
fish hook: 'da'wil.\\
\textbf{fishing}\\
to fish, troll: oom hoan.\\
\textbf{fishing boat}\\
fishing boat: shacksh oomhoan.\\
\textbf{fish nose}\\
fish nose: ggaggoack.\\
\textbf{fish slime}\\
fish slime: yehl.\\
\textbf{fish tail}\\
fish tail: na'dsiksh.\\
\textbf{fish trap}\\
fish trap: loolp. fish trap; to hurry: 'deen.\\
\textbf{fist}\\
to hit, push with fist: 'doosh. to hit with fist, punch: 'gal'doosh.\\
\textbf{five}\\
five flat, round or abstract objects: kwshdoonsh. five people: kshdnshoal.\\
\textbf{fix}\\
to be completed, well-designed, well-proportioned; to do over, fix, repair: amadsab.\\
\textbf{flag}\\
flag: hahloam gyamg.\\
\textbf{flair}\\
to strut, walk with flair: dseekshyaaksh.\\
\textbf{flannel blanket}\\
flannel blanket, sheet: sheedsm wush.\\
\textbf{flee}\\
to escape, run away, flee: 'gyaickg.\\
\textbf{flesh}\\
flesh, meat: shamee.\\
\textbf{float}\\
something that floats: gigyoaksh.\\
\textbf{flood}\\
to flood: geetga aksh.\\
\textbf{floor}\\
floor: ha'liwaalcksh.\\
\textbf{flounder}\\
flounder: dacksh.\\
\textbf{flower}\\
flower: madsiggalay.\\
\textbf{fly}\\
hemlock (tree or wood); mosquito; to buy; to fly: geek. house fly: gig. to fly, glide in the air: gipaig.\\
\textbf{foam}\\
foam: ckaygg.\\
\textbf{fog}\\
fog: yain.\\
\textbf{fold}\\
to fold over: 'da'kil.\\
\textbf{folktale}\\
legend, folktale, story; title: adaawck.\\
\textbf{food}\\
food: wineaya. food you take from a meal: shoa. Indian food: wineaym 'Tsmshian. smoked food: shi'biyaanshk. to give food: geen. to have too much food in one's throat: 'da'giackshg. to want someone's food: mat.\\
\textbf{foot}\\
foot, leg: ashee.\\
\textbf{football}\\
football : kwhlackshhla'at.\\
\textbf{forbidden}\\
to be against custom or law, forbidden: ha'wahlg.\\
\textbf{forehead}\\
forehead: woapck.\\
\textbf{forest}\\
forest; pieces of wood: gganggan. in the woods or forest: gilhowlee.\\
\textbf{fork}\\
fork: hayaawckg.\\
\textbf{forsake}\\
to forsake: 'nu'ud'ood.\\
\textbf{fortunate}\\
to be fortunate, lucky: ayaaltg.\\
\textbf{found}\\
to be found; to come from: 'waatg.\\
\textbf{found out}\\
to get caught in the act, be found out : lu'wai.\\
\textbf{four}\\
four boats or canoes: tckaalpckshg. four flat, abstract or round objects: tckaalpck. four long objects: ta'apshgn. four people: tckalpckdoal.\\
\textbf{fragrant}\\
to be fragrant, smell good: meehoksh.\\
\textbf{freeze}\\
ice; to freeze: daaw.\\
\textbf{Friday}\\
Friday: Ha'li Kwshdoonsha Sha.\\
\textbf{fried bread}\\
fried bread: ai'dsm anaay.\\
\textbf{fried fish}\\
fried fish: ai'dsm hoan.\\
\textbf{friend}\\
friend: damckhl. friend, sweetheart: 'nashee'bnshk.\\
\textbf{fright}\\
to jump with fright, shake, be startled: ggabackshg.\\
\textbf{frog}\\
frog: gganaow.\\
\textbf{front}\\
to walk to the front: 'dmyaa.\\
\textbf{fruit}\\
berries, fruit: maay.\\
\textbf{frying pan}\\
frying pan: lapwail.\\
\textbf{full}\\
to be full: hultg.\\
\textbf{full moon}\\
full moon: hultga giamg.\\
\textbf{funny}\\
to act silly, funny: shishnankshg. to be funny, humorous: ashguu.\\
\textbf{fur animal}\\
fur animal: leemya'tseshg.\\
\textbf{gable}\\
cross, gable of roof: ggadsaagg.\\
\textbf{gale}\\
gale, strong wind: ggatgyatga baashg. gale, waterspout: backbeega'aksh.\\
\textbf{gamble}\\
to gamble: ckshan.\\
\textbf{garden}\\
garden: shi'indoyntk.\\
\textbf{gather}\\
gather cedar bark: bayckggan. to gather: shackdoa.\\
\textbf{generous}\\
to be generous: o'yoonsh.\\
\textbf{get}\\
to go up and get: manggoahl.\\
\textbf{get better}\\
to get better: ggakshwil a'aamt.\\
\textbf{get rid}\\
to cut off, get rid of: sha'kots.\\
\textbf{get up}\\
to arise, to get up: haldm'acklg. to rise, get up from laying down: 'gineetg.\\
\textbf{ghost}\\
apparition, ghost, spirit, vision: noogit. corpse, ghost: baal'ack.\\
\textbf{ghost bread}\\
ghost bread: adaggan.\\
\textbf{gift}\\
donate: 'dsayck.\\
\textbf{girl}\\
girl, lady, woman: hana'ack.\\
\textbf{Git Lan Chief}\\
Git Lan Chief: Neesh hlagganoosh.\\
\textbf{give}\\
to give, hand to: 'gilum.\\
\textbf{give a drink}\\
to give a drink: gil'aksh.\\
\textbf{give food}\\
to give food: geen.\\
\textbf{give help}\\
donate: 'dsayck.\\
\textbf{give service}\\
donate: 'dsayck.\\
\textbf{glass}\\
glass; around the point: tgwa.\\
\textbf{glide}\\
to fly, glide in the air: gipaig.\\
\textbf{glove}\\
cotton gloves: 'balda hahloa. glove: 'balt.\\
\textbf{go}\\
to go: goy. to go, move, walk up along the ground: backyaa.\\
\textbf{go across}\\
to go across: shgadawhl.\\
\textbf{go after}\\
to bother, chase, go after, hunt: shuwileen.\\
\textbf{goat}\\
goat: daway.\\
\textbf{goat skin coat}\\
goat skin coat: gwishmatee.\\
\textbf{go away}\\
go away!; how, when, where: nda. to depart, go away, leave: dawhl. to go away: dawhln. to go away from, leave a place: kwdacksh.\\
\textbf{God}\\
Chief of the Heavens, God: Shm'oygit ga Lackaga.\\
\textbf{go down}\\
dusk; to descend, go down;: tgiyaa.\\
\textbf{go fast}\\
to be fast, quick; to go fast: 'dmyaa.\\
\textbf{go in}\\
to come in, enter, go in: 'dseen.\\
\textbf{gold}\\
gold: gool.\\
\textbf{good}\\
Is it good? Okay?: ahl aamdee?. to be fine, good, well: aam.\\
\textbf{good looking}\\
to be beautiful, good looking, handsome, pretty: ama'bash.\\
\textbf{good luck}\\
to have good luck, be lucky: ha'dsinaash.\\
\textbf{goose}\\
goose: hakk.\\
\textbf{go out}\\
to go out (of fire): lu'dsakya.\\
\textbf{gospel}\\
gospel: ggaleemksh.\\
\textbf{gossip}\\
to gossip, talk about: 'bilhow.\\
\textbf{go up}\\
to ascend, go up, walk up: munyaa.\\
\textbf{grandchildren}\\
grandchildren: hluk'kwdaa'yn.\\
\textbf{grandfather}\\
grandfather: nayaa. his/her grandfather: nayaat. my grandfather: nayaayu. your grandfather: nayaan.\\
\textbf{grandfather of}\\
grandfather of: neeyaash.\\
\textbf{grandmother}\\
grandmother: n'tse'ets, dse'a, dse'ish. my grandmother: n'tse'etsu.\\
\textbf{grass}\\
grass: kyoagg.\\
\textbf{grease}\\
ooligan grease: 'kawtsi. to anoint, grease, massage, oil, rub: 'man.\\
\textbf{great-grandchildren}\\
great-grandchildren: agwee hluk'kwdaa'yn.\\
\textbf{great-grandmother}\\
great-grandmother: oo'alsh.\\
\textbf{great-great-grandchildren}\\
barnacles; great-great-grandchildren: 'dsimaay.\\
\textbf{green}\\
green: mihleetg.\\
\textbf{greet}\\
day to greet people: ha'li'doygg.\\
\textbf{grind}\\
to scrape, grind to pieces: kwhleeggiackn.\\
\textbf{grip}\\
to grip, hold: dackya'wa.\\
\textbf{grizzly bear}\\
bear, brown bear, grizzly bear: madeeg.\\
\textbf{ground}\\
earth, ground, land, soil: yuub. on the ground: Jackyuub.\\
\textbf{groundhog}\\
groundhog: gweekw.\\
\textbf{grouse}\\
grouse; to count: leetsg.\\
\textbf{grow}\\
to caulk an opening; to grow: 'bash. to develop, enlarge, expand, grow, increase: tckalyaa.\\
\textbf{guess}\\
to assume, guess, think: ha'liggoad.\\
\textbf{gum}\\
gum, pitch, lead: shgyen.\\
\textbf{gumboots}\\
gumboots: 'yaansh.\\
\textbf{gun}\\
gun: gga'bala.\\
\textbf{Haida}\\
Haida language: hiedmck. Haida person: hieda.\\
\textbf{hair}\\
blond or reddish hair; horsefly: gigim'uugg. hair: ggawsh. hair, scalp: ggolee. to trim hair by burning ends: gwalka.\\
\textbf{half}\\
half: shdoa. half, part of: ckbeeyay.\\
\textbf{half-dried fish}\\
half-dried fish: ksha'dsal.\\
\textbf{half moon}\\
half moon: 'na shdoa giamg.\\
\textbf{halibut}\\
halibut: tckow.\\
\textbf{halibut bait}\\
halibut bait: 'naam tckaw.\\
\textbf{halibut hook}\\
halibut hook: noo.\\
\textbf{hallowed}\\
to be hallowed, sacred: 'nahloamshk.\\
\textbf{halo}\\
halo around the moon: deckhlga giamg.\\
\textbf{hammer}\\
hammer: dackhl. to hit with, hammer; to hit, tap: 'taab.\\
\textbf{hand}\\
arm, hand: an'on. to give, hand to: 'gilum.\\
\textbf{handle}\\
to handle, play with compulsively: dsa'bl.\\
\textbf{handsome}\\
to be beautiful, good looking, handsome, pretty: ama'bash. to be handsome, nice looking, pretty: hoyshg.\\
\textbf{hang}\\
to hang: 'yack.\\
\textbf{happening}\\
happening: lawaal.\\
\textbf{happy}\\
to be happy: shilu'aamggoad. to make happy: shilu'aam.\\
\textbf{Happy New Year}\\
Happy New Year: Ama shu'goahl.\\
\textbf{hard}\\
to be dried hard, stiff with cold: ggantk. to be hard: shiepg.\\
\textbf{hard times}\\
deep winter, hard times: magwa'ala. to have hard times: lack waalee magwa'ala.\\
\textbf{harvest}\\
to harvest, reap, pick (of food): guul.\\
\textbf{hat}\\
hat: ggaid. rain hat: ggaidm shgyen. rimmed hat: ggaidm boashn. yarn hat: ggaidm shihoo.\\
\textbf{hatchet}\\
axe, hatchet: gigyoatk.\\
\textbf{hate}\\
to detest, hate: labaalck.\\
\textbf{haughty}\\
to be arrogant, haughty, proud, snobbish, stand-offish: adsiksh.\\
\textbf{have}\\
to have, own: didoa. what you got; what you have: na'waan.\\
\textbf{hawk}\\
hawk: ckdso'otsk.\\
\textbf{he}\\
he, she, it: 'neet.\\
\textbf{head}\\
Chief, head of: meyaan. fish head: 'dmggowshm hoan. head: 'dmggowsh.\\
\textbf{headdress}\\
headdress, mask, regalia, shaman's mask; shaman: aamhalaayt.\\
\textbf{headgear}\\
chief's headgear; eagle down: 'bilgwa.\\
\textbf{healthy}\\
to be competent, healthy, lucky: wukdsab.\\
\textbf{hear}\\
to hear: 'nack'noo, tcka'noo.\\
\textbf{heart}\\
heart: ggoad.\\
\textbf{heat}\\
month; sun, heat; to be hot, warm: gyamg.\\
\textbf{Heavens}\\
above, Heavens, weather: Lackaga.\\
\textbf{heavy}\\
to be heavy: 'balgiackshg.\\
\textbf{help}\\
to help: hlimoam.\\
\textbf{hemlock}\\
hemlock (tree or wood); mosquito; to buy; to fly: geek.\\
\textbf{here}\\
here: gwa'a.\\
\textbf{herring}\\
herring: shga. rake to catch herring in water: 'gidaa.\\
\textbf{herring eggs}\\
herring eggs: cksh'waanck.\\
\textbf{hide}\\
hide, skin: anaash. to hide away: yuu.\\
\textbf{high}\\
hill, mountain; up high: gyepsh.\\
\textbf{high rank}\\
leader, person of high ranking, Chief, Mayor: Shm'oygit. person of high ranking: 'weelaekshm gyad.\\
\textbf{high tide}\\
high tide: laaksha aksh, deetck'aksh.\\
\textbf{hill}\\
hill: dee. hill, mountain; up high: gyepsh. on the hill: lackdee.\\
\textbf{hit}\\
to break up, chop, club, hit, pound: yeds. to fall; to hit: oksh. to hit, beat up with a club: kwhlee'kayaan. to hit, push with fist: 'doosh. to hit with a stick or club: 'galyeds. to hit with a thrown object: 'gal'oy. to hit with fist, punch: 'gal'doosh. to hit with, hammer; to hit, tap: 'taab.\\
\textbf{hold}\\
to grip, hold: dackya'wa. to hold: shnyaagw. to hold, hold fast, hold tight: dackyaagw. to hold, hug, squeeze: dam. to hold on to: dockdock. to hold, squeeze: damshg.\\
\textbf{home}\\
to obey, sit still; to stay at home: dackshm'daa.\\
\textbf{honor}\\
to honor, respect: hload.\\
\textbf{hope}\\
to expect, hope for, wait for: booyshg. to hope, trust: 'wayoaksh.\\
\textbf{horn}\\
antler, horn: ggaggawsh.\\
\textbf{hornet}\\
bee, hornet, yellow jacket: ab.\\
\textbf{horn spoon}\\
horn spoon: hapckdooweew.\\
\textbf{horse}\\
horse: gyuwadun.\\
\textbf{horse clam}\\
horse clam: loan.\\
\textbf{horsefly}\\
blond or reddish hair; horsefly: gigim'uugg.\\
\textbf{horse mussel}\\
horse mussel: hagwn.\\
\textbf{hot}\\
month; sun, heat; to be hot, warm: gyamg.\\
\textbf{hour}\\
at this time, this hour: dsihla.\\
\textbf{house}\\
house: waab. to run into a house: 'dsilmbaa.\\
\textbf{house fly}\\
house fly: gig.\\
\textbf{how}\\
go away!; how, when, where: nda.\\
\textbf{howl}\\
to howl like a wolf; to sound in loud tone: gga'kowtg.\\
\textbf{huckleberry}\\
huckleberry: wihlaaycksh.\\
\textbf{Hudson Bay tea}\\
Hudson Bay tea: 'gwilamacksh.\\
\textbf{hug}\\
to hold, hug, squeeze: dam. to hug: ludamdam.\\
\textbf{hummingbird}\\
hummingbird: ahlyeeggawsh.\\
\textbf{humorous}\\
to be funny, humorous: ashguu.\\
\textbf{humpback salmon}\\
humpback salmon, pink salmon: ggadoahl.\\
\textbf{hungry}\\
to be hungry: kwdee.\\
\textbf{hunt}\\
to bother, chase, go after, hunt: shuwileen.\\
\textbf{hurry}\\
fish trap; to hurry: 'deen. to hurry, be in a hurry: mala. to hurry while doing something: malamwaal.\\
\textbf{hurt}\\
to be hurt, wounded; to hurt, wound: shgaaygshg.\\
\textbf{I}\\
I: 'nuuyu.\\
\textbf{ice}\\
ice; to freeze: daaw.\\
\textbf{ice cream}\\
to eat Indian ice cream: ckdaiksh.\\
\textbf{idea}\\
to start thinking about, have an idea about: shiggoatg.\\
\textbf{image}\\
sculpture, statue, painting, image; to paint: tckal'dsa'ba.\\
\textbf{increase}\\
to accumulate, get fat, increase: akshyaa. to develop, enlarge, expand, grow, increase: tckalyaa.\\
\textbf{index finger}\\
index finger: ha'dsaick.\\
\textbf{Indian box}\\
Indian box, storage box: ggal'uunck.\\
\textbf{Indian bread}\\
Indian bread: hli'oan.\\
\textbf{Indian food}\\
Indian food: wineaym 'Tsmshian.\\
\textbf{Indian ice cream}\\
Indian ice cream: daayksh. to eat Indian ice cream: ckdaiksh.\\
\textbf{Indian rice}\\
Indian rice: meeyoobm 'Tsmshian.\\
\textbf{industrious}\\
to be a hard worker, industrious: a'waa'ackshg. to be industrious, hard working: 'gwiloa'ack.\\
\textbf{ineffective}\\
to be ineffective: liphahaw.\\
\textbf{infant}\\
child, infant: hlguwoamhlg.\\
\textbf{information}\\
to deliver information; to walk house to house: ckbeeyaa.\\
\textbf{inland}\\
ashore, inland: dsaggm.\\
\textbf{in-law}\\
in-law: hlumsh.\\
\textbf{inquire}\\
to ask, inquire: guudack. to be curious of details, inquire into: maggoanshga.\\
\textbf{inside}\\
People of the Way Inside: Git'dsilaashu. to be inside: ludoa. to put inside: ludoahl.\\
\textbf{inside of the mouth}\\
inside of the mouth: 'tsm aack.\\
\textbf{instrument}\\
instrument with holes; whistle: hackshgweekwshg. musical instrument: haleemee.\\
\textbf{intestine}\\
intestine: haad.\\
\textbf{intestines}\\
seal intestines: haada uula.\\
\textbf{intruder}\\
enemy intruders, raiders: gitwaaltk.\\
\textbf{iron dish}\\
iron dish: ggiehlam'do'otsk.\\
\textbf{irreparable}\\
to come apart, be irreparable; to be strewn loosely: ggol.\\
\textbf{island}\\
island: liksh'daa.\\
\textbf{it}\\
he, she, it: 'neet.\\
\textbf{jam}\\
jam: dsaam.\\
\textbf{jealous}\\
to be jealous: gyeshg.\\
\textbf{jeans}\\
jeans: 'backsha dsina.\\
\textbf{judge}\\
liver; to judge, try in court, measure: dap.\\
\textbf{jump}\\
expression when sighting fish jump: ayow. to jump: ggush. to jump (of fish): guksh. to jump with fright, shake, be startled: ggabackshg.\\
\textbf{jump rope}\\
to jump rope: ggalkshaggush.\\
\textbf{just}\\
just started or happened: ggaksh.\\
\textbf{just about}\\
almost, just about: geedsa.\\
\textbf{keel}\\
keel: hagyoaksh.\\
\textbf{keep}\\
to keep, take care of: haboal.\\
\textbf{keg}\\
keg, barrel: 'nhla'naggan.\\
\textbf{kelp}\\
flat leaf of kelp: gyoash. hair-kelp for herring eggs to cling to: laggee. kelp, rock weed: 'ba'atsa. People of the (Sea) Kelp: Gitwilgyots.\\
\textbf{kick}\\
to kick; to press, put weight on: kwhlacksh.\\
\textbf{killer whale}\\
killer whale, whale: 'naackhl.\\
\textbf{Killer Whale Clan}\\
Killer Whale Clan: Gish-budwada.\\
\textbf{kind}\\
a very kind person: moa'ackg. to be a kind person: lu'kwil ama ggoad. to be kind: ama gyad.\\
\textbf{kindling}\\
kindling: ggangwal'ka.\\
\textbf{kingfisher}\\
kingfisher: 'tsiyol'g.\\
\textbf{King salmon}\\
King salmon, Chinook salmon: yeeh.\\
\textbf{kiss}\\
to kiss: hoom'tsack.\\
\textbf{knead}\\
to knead, press down: tgi'doosh.\\
\textbf{knee}\\
knee: ggal'kieshuu.\\
\textbf{knife}\\
curved knife for carving; to be bent: hlaggiack. knife: hahlibeeshk, kwdoosh. pocket knife: hackback.\\
\textbf{knock out}\\
to punch; to knock out: kwhlee'doosh.\\
\textbf{know}\\
to know: wilaay.\\
\textbf{labor}\\
to work, labor: hahlalsh.\\
\textbf{labret}\\
labret worn in lip: 'ka'awts.\\
\textbf{lack}\\
to lack, not to have enough: shgoaksh.\\
\textbf{lady}\\
girl, lady, woman: hana'ack.\\
\textbf{lake}\\
lake: lack'daa.\\
\textbf{lame}\\
to be lame: 'kabaa.\\
\textbf{land}\\
earth, ground, land, soil: yuub. to arrive, land: badsg.\\
\textbf{land otter}\\
land otter: 'watsa.\\
\textbf{lapel}\\
item worn on a lapel: 'na'taash.\\
\textbf{large}\\
to be large: 'weelaeksha ggashgaawt.\\
\textbf{larvae}\\
larvae: gga'bilaash. mosquito larvae: ckshaan.\\
\textbf{last}\\
last one: shgalaan.\\
\textbf{laugh}\\
to laugh; to make laugh: shish'aacksh.\\
\textbf{laughing berries}\\
laughing berries, salal berries: dsawush.\\
\textbf{law}\\
to be against custom or law, forbidden: ha'wahlg.\\
\textbf{lazy}\\
to be lazy: alaaysh.\\
\textbf{lead}\\
gum, pitch, lead: shgyen. to lead: daintg.\\
\textbf{leader}\\
leader, person of high ranking, Chief, Mayor: Shm'oygit.\\
\textbf{leaf}\\
flat leaf of kelp: gyoash. leaf of a tree: 'yansh.\\
\textbf{leak}\\
to be left by the tide; to leak: 'dsee'g.\\
\textbf{lean}\\
to lean against (a wall, firm object): gganahietg.\\
\textbf{learn}\\
to learn: shiwilaaykwsh.\\
\textbf{leave}\\
to depart, go away, leave: dawhl. to go away from, leave a place: kwdacksh.\\
\textbf{left}\\
to be left by the tide; to leak: 'dsee'g.\\
\textbf{left behind}\\
to stay behind, be left behind: 'dsnshloyg.\\
\textbf{left over}\\
to be left over (food): ginamaan.\\
\textbf{leg}\\
foot, leg: ashee.\\
\textbf{leg cramp}\\
bark (of a tree); leg cramp: maash.\\
\textbf{legend}\\
legend, folktale, story; title: adaawck.\\
\textbf{length}\\
duration, length (of time, space): shga'nakt.\\
\textbf{let}\\
to allow, let: anoahl.\\
\textbf{let go}\\
to drop, let go: ggal'oa.\\
\textbf{lever}\\
to pry with a lever: ggaimggan.\\
\textbf{lick}\\
to lick: 'dsaick.\\
\textbf{licorice root}\\
licorice root: mi'tsa 'ka'aam.\\
\textbf{lid}\\
box cover, lid: nahaapt.\\
\textbf{lie}\\
falsehood, lie: bee'eg. to lie on one's side: ggahldikshguu. to lie, tell a lie: sha bee'eg.\\
\textbf{lie down}\\
to lie down: noak.\\
\textbf{life}\\
to be durable, live a long life: aigyad.\\
\textbf{lift}\\
to bring up, lift: haldm. to lift: bads. to lift up; up towards: mungaa.\\
\textbf{light}\\
light: laakwsh.\\
\textbf{lightning}\\
electricity, lightning: 'dsamtee.\\
\textbf{light source}\\
window, light source: gganlugoy'pa.\\
\textbf{lightweight}\\
to be lightweight: aipn.\\
\textbf{like}\\
to agree, allow, give permission; to like: anoagg. to like to do, spend time doing: hadahaw.\\
\textbf{lion}\\
lion: hawhaw.\\
\textbf{lip}\\
chin, indentation under the lip: 'kowts.\\
\textbf{lips}\\
lips: kwhl'aack.\\
\textbf{list}\\
to list to one side: 'gahlgyoa.\\
\textbf{listen}\\
someone who never listens: 'wa'dsimoo. to listen, obey, pay attention: amooksh.\\
\textbf{little}\\
to be little, small: 'tsushg.\\
\textbf{little finger}\\
little finger, pinky: hlgu shggay.\\
\textbf{live}\\
to be durable, live a long life: aigyad.\\
\textbf{liver}\\
liver; to judge, try in court, measure: dap.\\
\textbf{lonesome}\\
to miss, be lonesome for: 'gwaa'dish. to miss, feel loss of, be lonesome for: 'weegyat.\\
\textbf{long}\\
to be long: 'nak.\\
\textbf{long enough}\\
after a while; to be far enough, long enough: aamshga'nak. to be long enough, reach across: aadsack.\\
\textbf{look}\\
to look down: tgine'etsg.\\
\textbf{look at}\\
to look at: ne'etsg. to look at, see: nee.\\
\textbf{lose}\\
to defrost, melt, disappear, lose weight or size: dseeb. to drop, let go: ggal'oa.\\
\textbf{loss}\\
to miss, feel loss of, be lonesome for: 'weegyat.\\
\textbf{lost}\\
to be lost: 'gwit'gwaatg. to be lost, missing: 'gwaatg.\\
\textbf{loud}\\
to make a loud noise: ckshdaamck.\\
\textbf{low}\\
low profile, low status, a worthless person: gga'gwaa'gw. to howl like a wolf; to sound in loud tone: gga'kowtg.\\
\textbf{low tide}\\
low tide: lugowshga aksh.\\
\textbf{lucky}\\
to be competent, healthy, lucky: wukdsab. to be fortunate, lucky: ayaaltg. to be lucky: ha'dsiyaan. to have good luck, be lucky: ha'dsinaash.\\
\textbf{lumber}\\
plank, lumber: taggan.\\
\textbf{mad}\\
to get mad all of a sudden: shahloontee.\\
\textbf{make}\\
to build, construct, make: dsab.\\
\textbf{male}\\
to be the youngest male: gganeesh.\\
\textbf{man}\\
man: 'yoota.\\
\textbf{many}\\
many: haild. to be many, very: lu'kwil. too many: ggal haild.\\
\textbf{marker}\\
marker, pencil: ggan'dameesh.\\
\textbf{marrow}\\
bone marrow: 'dsee'dsee.\\
\textbf{marry}\\
spouse; to marry: naksh.\\
\textbf{mash}\\
to crush, mash: 'beehl.\\
\textbf{mask}\\
disguise, effigy, mask: ameelg. headdress, mask, regalia, shaman's mask; shaman: aamhalaayt.\\
\textbf{massage}\\
to anoint, grease, massage, oil, rub: 'man.\\
\textbf{mat}\\
woven mat: shggan.\\
\textbf{Mayor}\\
leader, person of high ranking, Chief, Mayor: Shm'oygit.\\
\textbf{me}\\
me: 'koy.\\
\textbf{meadowlark}\\
meadowlark; songbird: be'an.\\
\textbf{mean}\\
to advise, counsel; to rebuke, scold, talk to in a mean manner: daalck.\\
\textbf{measure}\\
liver; to judge, try in court, measure: dap.\\
\textbf{meat}\\
deer meat: shameeym wun. dried meat: 'dsa'oamtee. flesh, meat: shamee.\\
\textbf{medicine}\\
medicine: ckaldaawckg. ointment, medicine: haldaaksh.\\
\textbf{medicine plant}\\
medicine plant: madsigga'aam.\\
\textbf{medium}\\
to be medium size, of a good size: aamggashgaawt.\\
\textbf{meet}\\
to meet: ludaaltg, tckal'waa.\\
\textbf{melt}\\
to defrost, melt, disappear, lose weight or size: dseeb. to melt: dseelksh. to melt away: shadseelksh.\\
\textbf{message}\\
decree, message, official statement: ayaawgg.\\
\textbf{middle}\\
middle; something fearful; to be dreaded, fearful: shuulg.\\
\textbf{middle finger}\\
middle finger: kshi'nag.\\
\textbf{midnight}\\
midnight: shuulga aatk.\\
\textbf{milk}\\
milk, woman's breast: me'ish.\\
\textbf{minister}\\
minister, pastor, preacher, priest: liplaid.\\
\textbf{mink}\\
boil (on the skin); mink: lish'yaan.\\
\textbf{miracle}\\
miracle, wonder; to breathe: shanaahl.\\
\textbf{mirror}\\
mirror: 'nakshuuneeshgm 'dsal. mirror, window: 'nakshuuneeshg.\\
\textbf{mis}\\
to err, miss, make a mistake, do something wrong: geesh.\\
\textbf{misbehave}\\
to misbehave: nanu.\\
\textbf{misbutton}\\
to misbutton: 'bahl'bal, ahl'bal.\\
\textbf{miss}\\
to dodge; miss: geeshk. to miss, be lonesome for: 'gwaa'dish. to miss, feel loss of, be lonesome for: 'weegyat.\\
\textbf{missing}\\
to be lost, missing: 'gwaatg.\\
\textbf{mist}\\
misty rain: waashm yain.\\
\textbf{mistake}\\
to do something wrong, make a mistake: labaggietwaal. to err, miss, make a mistake, do something wrong: geesh. to have an accident, make a mistake: ashdeewaal. to make a mistake: ashdee.\\
\textbf{Monday}\\
Monday: Ha'li 'Guul Sha.\\
\textbf{money}\\
money: daala.\\
\textbf{monkey}\\
monkey: bou'ish.\\
\textbf{month}\\
month; sun, heat; to be hot, warm: gyamg.\\
\textbf{moon}\\
full moon: hultga giamg. half moon: 'na shdoa giamg. moon: gyamgm'aatk.\\
\textbf{morning}\\
morning: gganhlaag.\\
\textbf{morning star}\\
morning star: beyaalshm gganhlaag.\\
\textbf{mosquito}\\
hemlock (tree or wood); mosquito; to buy; to fly: geek. mosquito larvae: ckshaan. People of the Mosquitoes: Gitnack'angeek.\\
\textbf{moss}\\
moss: bilagg.\\
\textbf{mother}\\
mother: na'a, noa, naay.\\
\textbf{mountain}\\
hill, mountain; up high: gyepsh. mountain: shga'neesh.\\
\textbf{mouse}\\
mouse: wu'tseen. shrew, small mouse: diboygid.\\
\textbf{mouth}\\
inside of the mouth: 'tsm aack.\\
\textbf{move}\\
to dodge, move out of the way: shageeshk. to go, move, walk up along the ground: backyaa.\\
\textbf{move camp}\\
to move camp: loyg.\\
\textbf{move over}\\
to move over: gish doa. to move over, sit in another place: gish'daa.\\
\textbf{muscle}\\
arm muscle: laba'on.\\
\textbf{mushroom}\\
mushroom: ggaida gganaaw.\\
\textbf{muskeg}\\
muskeg; upon muskeg: lack'U.\\
\textbf{mussel}\\
horse mussel: hagwn. mussel: gyelsh.\\
\textbf{nail}\\
nail : 'daa'binshg. to nail on: tckal'daabhl.\\
\textbf{naked}\\
to be naked, nude, without clothing: ksha'anaash, kshadsackoatg.\\
\textbf{name}\\
name: waa. to name, call by name: aytk.\\
\textbf{nape}\\
neck, nape: 'dsm'dee.\\
\textbf{narrate}\\
story, tale; to narrate, tell: malshg.\\
\textbf{Nass-Gitksan}\\
Nass-Gitksan language: gaalmck.\\
\textbf{Nass River}\\
Nass River: klushmsh.\\
\textbf{Nass River people}\\
Nass River people: Nishgaa.\\
\textbf{navel}\\
navel: 'di'ik.\\
\textbf{near}\\
at, by, near: awaa.\\
\textbf{neck}\\
neck: 'dmlaanee. neck, nape: 'dsm'dee.\\
\textbf{necklace}\\
beads on a string, necklace: ggahood. tie; necklace: 'yootishg.\\
\textbf{needle}\\
needle: 'lagg.\\
\textbf{net}\\
net; to seine: aad. to fish with a net, seine for fish: aadm hoan.\\
\textbf{net brail}\\
dip net, net brail: bana.\\
\textbf{nettles}\\
stinging nettles: shdatee.\\
\textbf{new}\\
to be new: shu.\\
\textbf{newspaper}\\
newspaper: malshgm sha'winshg.\\
\textbf{next to}\\
next to the water, at the water's edge: geeka.\\
\textbf{nice looking}\\
to be handsome, nice looking, pretty: hoyshg.\\
\textbf{night}\\
at night: hoo'bl. night: aatk.\\
\textbf{nightgown}\\
nightgown: kshlushgm noak.\\
\textbf{night pot}\\
elbow; night pot: ma'oan.\\
\textbf{nine}\\
nine abstract, round or flat objects: kshda'moash. nine people: kshdm'ashoal.\\
\textbf{no}\\
no, not so: ayin.\\
\textbf{noble}\\
big man, Chief, noble: algyackshg.\\
\textbf{noise}\\
to make a loud noise: ckshdaamck.\\
\textbf{noon}\\
noon: shuulga sha.\\
\textbf{north}\\
north blizzard, snow on north side of tree: shda'magsha shdoa ggan.\\
\textbf{northeast wind}\\
northeast wind: gishih aywaash.\\
\textbf{north wind}\\
north wind: gishiyaashg.\\
\textbf{nose}\\
fish nose: ggaggoack. nose: 'tsack.\\
\textbf{nostril}\\
nostril: 'tsm'tsack.\\
\textbf{not}\\
not: ahlga.\\
\textbf{not easy}\\
not easy, work hard against odds, suffer: haackg.\\
\textbf{nothing}\\
nothing: ahlgadee goa. to come apart entirely, to be nothing left: kwhlee ggolggol.\\
\textbf{nothingness}\\
nothingness, spirit: oa'dsn.\\
\textbf{not so}\\
no, not so: ayin.\\
\textbf{not there}\\
to be empty, not there: ggalbash.\\
\textbf{now}\\
just now: shugya'wn. now, today: gya'wn.\\
\textbf{nude}\\
to be naked, nude, without clothing: ksha'anaash, kshadsackoatg.\\
\textbf{nuisance}\\
bothersome thing, nuisance; to be bothered: hamoolg.\\
\textbf{oar}\\
oar: ggaimgganshk.\\
\textbf{oar lock}\\
oar lock: gganwaay.\\
\textbf{obey}\\
to listen, obey, pay attention: amooksh. to obey, sit still; to stay at home: dackshm'daa.\\
\textbf{ocean}\\
ocean: lackshuulda.\\
\textbf{octopus}\\
octopus, squid, devil fish: ha'tsal.\\
\textbf{offshore wind}\\
offshore wind: ukshbaashg.\\
\textbf{oh}\\
oh!: ee.\\
\textbf{oil}\\
to anoint, grease, massage, oil, rub: 'man.\\
\textbf{ointment}\\
ointment, medicine: haldaaksh.\\
\textbf{okay}\\
alright!; behold!; well now; let's start!; okay!: wie wa!. Is it good? Okay?: ahl aamdee?. okay: wie aam.\\
\textbf{olden times}\\
olden times, old people: hlaagi gyad.\\
\textbf{old people}\\
olden times, old people: hlaagi gyad.\\
\textbf{on}\\
on, upon: lack.\\
\textbf{one}\\
one abstract or round thing: 'guul. one boat or canoe: 'kamea. one flat object: 'gyaag. one person: 'goal. to be as one: shagiet 'koal.\\
\textbf{onshore wind}\\
onshore wind: dsaggmbaashg.\\
\textbf{ooligan}\\
ooligan: uuah. to boil ooligans in a pot: lack'anaaym uua.\\
\textbf{ooligan grease}\\
ooligan grease: 'kawtsi.\\
\textbf{open}\\
to open: 'kack.\\
\textbf{open air}\\
in the open air, outside: gyalck.\\
\textbf{operation}\\
operation, surgery: baahlk.\\
\textbf{opposite}\\
across the way, the opposite side: doashda.\\
\textbf{or}\\
or: ligi.\\
\textbf{otter}\\
land otter: 'watsa. sea otter: phloan.\\
\textbf{ouch}\\
ouch! : ock.\\
\textbf{our}\\
our own, ours: 'gynnm.\\
\textbf{out of the way}\\
to get out of the way; to make aware, warn: boo'ihl.\\
\textbf{out on the water}\\
out on the water: giyaaksh.\\
\textbf{outside}\\
in the open air, outside: gyalck.\\
\textbf{out to sea}\\
to go out to sea: ukshdawhl.\\
\textbf{overcast}\\
overcast day: goabackga sha. overcast sky: goabackga lacka.\\
\textbf{over there}\\
in that direction, over there: gwashga.\\
\textbf{overworked}\\
to be beaten up, exhausted, overworked: plakshkw.\\
\textbf{owe}\\
to owe; to promise: aishk.\\
\textbf{owl}\\
owl: gwitgwineeksh.\\
\textbf{own}\\
to have, own: didoa.\\
\textbf{pack lunch}\\
to bring food, pack a lunch: 'dsiloom.\\
\textbf{paddle}\\
to paddle, row: duwaay, waay.\\
\textbf{pail}\\
bucket, pail: oomhl. bucket, pail, water container: ggaldm'aksh.\\
\textbf{paint}\\
sculpture, statue, painting, image; to paint: tckal'dsa'ba. to paint: shagamaashgit.\\
\textbf{painting}\\
sculpture, statue, painting, image; to paint: tckal'dsa'ba.\\
\textbf{palm}\\
palm of hand: 'dsm'an'on.\\
\textbf{pan}\\
frying pan: lapwail.\\
\textbf{pants}\\
pants, trousers: 'backsh.\\
\textbf{paper}\\
paper: sha'winshk.\\
\textbf{part}\\
half, part of: ckbeeyay.\\
\textbf{party}\\
to cohabit, picnic, play camp, have a small party: shishdsoacksh.\\
\textbf{pass around}\\
to pass around: ya'an.\\
\textbf{pass out}\\
to faint, pass out: daamshack.\\
\textbf{pastor}\\
minister, pastor, preacher, priest: liplaid.\\
\textbf{path}\\
path, road, trail: guyna.\\
\textbf{pay}\\
to pay: cklggoan.\\
\textbf{pay attention}\\
to listen, obey, pay attention: amooksh.\\
\textbf{pay back}\\
to exchange, pay back, reciprocate, return: shidyaawd.\\
\textbf{payment}\\
payment: cklggoa'oam.\\
\textbf{pencil}\\
marker, pencil: ggan'dameesh.\\
\textbf{people}\\
our brothers, our own people: nlip 'dsabam. people: gyad.\\
\textbf{People of the Elderberries}\\
People of the Elderberries: Gishbackloa'ds.\\
\textbf{People of the Mosquitoes}\\
People of the Mosquitoes: Gitnack'angeek.\\
\textbf{People of the Other Side}\\
People of the Other Side (Wiers): Git'ando.\\
\textbf{People of the Salmon (Seal) Traps}\\
People of the Salmon (Seal) Traps: Gitdseesh.\\
\textbf{People of the (Sea) Kelp}\\
People of the (Sea) Kelp: Gitwilgyots.\\
\textbf{People of the Shrubs}\\
People of the Shrubs: Gitdsacklahl.\\
\textbf{People of the Swift Waters}\\
People of the Swift Waters: Git'nadoyksh.\\
\textbf{People of the Way Inside}\\
People of the Way Inside: Git'dsilaashu.\\
\textbf{People of Two Passing Canoes}\\
People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes: Gitlan.\\
\textbf{People Where the Salmon Spawn}\\
People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes: Gitlan.\\
\textbf{People who sit in the Stern of Canoes}\\
People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes: Gitlan.\\
\textbf{performance}\\
agility, performance, poise: debeesh.\\
\textbf{permission}\\
to agree, allow, give permission; to like: anoagg.\\
\textbf{persistent}\\
to be determined, persistent: haickal.\\
\textbf{phosphorescent algae}\\
fire in the water; phosphorescent algae: adaahl.\\
\textbf{pick}\\
to harvest, reap, pick (of food): guul.\\
\textbf{pick up}\\
to pick up: mungaahl.\\
\textbf{picnic}\\
to cohabit, picnic, play camp, have a small party: shishdsoacksh.\\
\textbf{picture}\\
to draw, take a picture: gilkshtckal'da'minshg.\\
\textbf{pig}\\
pig: gwashoa.\\
\textbf{pillow}\\
pillow: mahluu.\\
\textbf{pink salmon}\\
humpback salmon, pink salmon: ggadoahl.\\
\textbf{pinky}\\
little finger, pinky: hlgu shggay.\\
\textbf{pipe}\\
pipe for smoking: hack'biyaan.\\
\textbf{pitch}\\
gum, pitch, lead: shgyen. to throw, pitch: ayam.\\
\textbf{place}\\
to place, put: shguu.\\
\textbf{plank}\\
plank, lumber: taggan.\\
\textbf{play}\\
to handle, play with compulsively: dsa'bl. to play: galmeelg. to play with compulsively: dedsa'bil.\\
\textbf{playground}\\
playground: ha'ligalmeelg.\\
\textbf{plentiful}\\
to be enough, adequate, ample, plentiful: aamshgaboo.\\
\textbf{pocket}\\
pocket: 'ntawa'at.\\
\textbf{pocket knife}\\
pocket knife: hackback.\\
\textbf{point}\\
to point: 'ge'ets. to point at, point out: 'ge'etsckan.\\
\textbf{Point Davidson}\\
Point Davidson: Tgwahahay.\\
\textbf{poise}\\
agility, performance, poise: debeesh.\\
\textbf{polar bear}\\
polar bear: moakshgm'ol.\\
\textbf{pole}\\
totem pole: p'tsaan.\\
\textbf{polished}\\
to be polished, shiny: gugwalksh.\\
\textbf{poor}\\
poor stuff, cheap things: ggamwaal. to be poor: gway'a.\\
\textbf{poor fellow}\\
poor fellow: gwinaat.\\
\textbf{porcupine}\\
porcupine: awta.\\
\textbf{porpoise}\\
dolphin, porpoise: dseeyuu.\\
\textbf{possessions}\\
belongings, possessions, clothing: liggiwaal. burnt possessions of a dead person; to burn possessions of a dead person: laguulgit.\\
\textbf{potato}\\
potatoes: shgoosheed. to cook potatoes in sand near fire: ood.\\
\textbf{pound}\\
to break up, chop, club, hit, pound: yeds. to pound: kwhleeyedsg.\\
\textbf{praise}\\
to praise, show respect: amadaalck.\\
\textbf{pray}\\
to pray: gigeengwackhl.\\
\textbf{preacher}\\
minister, pastor, preacher, priest: liplaid.\\
\textbf{press}\\
to kick; to press, put weight on: kwhlacksh. to knead, press down: tgi'doosh.\\
\textbf{pretty}\\
to be beautiful, good looking, handsome, pretty: ama'bash. to be handsome, nice looking, pretty: hoyshg.\\
\textbf{priest}\\
minister, pastor, preacher, priest: liplaid.\\
\textbf{promise}\\
something that one believes in; to promise: nashmhowtksh. to owe; to promise: aishk.\\
\textbf{proud}\\
to be arrogant, haughty, proud, snobbish, stand-offish: adsiksh.\\
\textbf{pry}\\
to pry with a lever: ggaimggan.\\
\textbf{pull cedar bark}\\
to tear, pull bark from cedar tree: bayck.\\
\textbf{pull down}\\
to pull down: gga'dsihlshagya.\\
\textbf{pull in}\\
to bring towards, pull in: tckalshagihl.\\
\textbf{pulpit}\\
altar, pulpit: ha'limalshk.\\
\textbf{punch}\\
to hit with fist, punch: 'gal'doosh. to punch; to knock out: kwhlee'doosh.\\
\textbf{push}\\
to hit, push with fist: 'doosh. to push: sha'doosh. to push up: mun'doosh.\\
\textbf{push down}\\
to push down: gga'dsihl'doosh.\\
\textbf{put}\\
to place, put: shguu. to put in front of fire: hahldoa.\\
\textbf{put aside}\\
to put aside, put away; to sidetrack: awul'mag.\\
\textbf{put away}\\
to put aside, put away; to sidetrack: awul'mag. to put away: 'dahla awaan. to put away in a corner: dseehldoa.\\
\textbf{put down}\\
to put down: tgi'gen.\\
\textbf{put in}\\
to put in: lu'gen.\\
\textbf{put inside}\\
to put inside: ludoahl.\\
\textbf{put on}\\
to be built strong; to put on warm clothes: doyksh. to put on: 'leeshguu. to put on sticks for smoking (as fish, meat): ggahlggan.\\
\textbf{put out}\\
to put out : 'dsakyl.\\
\textbf{put together}\\
to put together: loonda hloadihl.\\
\textbf{quick}\\
to be fast, quick; to go fast: 'dmyaa. to do faster, quickly: di'deeld. to do quickly, work fast: 'deeld.\\
\textbf{quiver}\\
quiver (of the chin), tremble: babaa.\\
\textbf{race}\\
to run a race against each other: mala'ka'kuhl.\\
\textbf{rack}\\
cabinet, dish rack: ha'litoamnoahl.\\
\textbf{raider}\\
enemy intruders, raiders: gitwaaltk.\\
\textbf{rain}\\
misty rain: waashm yain. rain: waash. to rain heavily: ggadsikshg.\\
\textbf{rainbow}\\
rainbow: maackee.\\
\textbf{raincoat}\\
raincoat: gooda'atsm shgyen.\\
\textbf{rain hat}\\
rain hat: ggaidm shgyen.\\
\textbf{rake}\\
rake to catch herring in water: 'gidaa. to rake, scrape: ggaapckan.\\
\textbf{rapids}\\
rapids, strong tide: doyksh. swift rapids, waterfall, gorge, canyon: 'tsilaashu.\\
\textbf{raspberries}\\
raspberries: naashu.\\
\textbf{rat}\\
rat, rodent: ggaklik.\\
\textbf{rat fish}\\
angel fish, rat fish: goomaa.\\
\textbf{rattle}\\
rattle for dancing: shoashoa.\\
\textbf{raven}\\
raven: ggaagg.\\
\textbf{Raven}\\
Raven : tckaamshm. Raven Clan (crest): Gganhaada.\\
\textbf{raven berries}\\
raven berries: maaym ggaagg.\\
\textbf{reach}\\
to be long enough, reach across: aadsack.\\
\textbf{ready}\\
to get ready: gwilm ggawdee. to get things ready: haboo'yil.\\
\textbf{reap}\\
to harvest, reap, pick (of food): guul.\\
\textbf{rear}\\
aft of boat, back end, rear, stern: gilaan.\\
\textbf{rebuke}\\
to advise, counsel; to rebuke, scold, talk to in a mean manner: daalck.\\
\textbf{recall}\\
to recall, remember: aa'back.\\
\textbf{reciprocate}\\
to exchange, pay back, reciprocate, return: shidyaawd.\\
\textbf{red}\\
blond or reddish hair; horsefly: gigim'uugg. red: mashg.\\
\textbf{red cedar}\\
red cedar: amggan. red cedar tree: ggalaaw.\\
\textbf{red salmon}\\
sockeye salmon, red salmon: mishoa.\\
\textbf{red snapper}\\
red snapper: 'dsmhoan.\\
\textbf{regalia}\\
headdress, mask, regalia, shaman's mask; shaman: aamhalaayt.\\
\textbf{reindeer}\\
caribou, reindeer: woo'dsee.\\
\textbf{relative}\\
relative: wilaayshg.\\
\textbf{remember}\\
to recall, remember: aa'back.\\
\textbf{remove}\\
to remove, take off (singular): shagaa. to remove, to take off (plural): shadoack.\\
\textbf{repair}\\
to be completed, well-designed, well-proportioned; to do over, fix, repair: amadsab.\\
\textbf{repeat}\\
to do again, repeat: hadsikshm gik waan.\\
\textbf{repent}\\
to repent, be sorry for: gilksh'ietksh.\\
\textbf{reply}\\
to answer, reply: deelmckg.\\
\textbf{rescue}\\
to rescue, save: moatg.\\
\textbf{reside}\\
to reside: dsoack.\\
\textbf{respect}\\
to honor, respect: hload. to praise, show respect: amadaalck.\\
\textbf{respected}\\
to be respected, sacred: 'nhloamshg.\\
\textbf{rest}\\
to rest: shgwaitg.\\
\textbf{restaurant}\\
restaurant: waab tckoackg.\\
\textbf{retaliate}\\
to retaliate, take revenge: deeltg.\\
\textbf{return}\\
to exchange, pay back, reciprocate, return: shidyaawd. to return, turn back: luyeltg.\\
\textbf{revenge}\\
to retaliate, take revenge: deeltg.\\
\textbf{rhubarb}\\
rhubarb: hla'kods.\\
\textbf{rib}\\
rib: pdal.\\
\textbf{ribbon}\\
ribbon : 'na'bahloanshg.\\
\textbf{rice}\\
Indian rice: meeyoobm 'Tsmshian. rice: meeyoob.\\
\textbf{rich}\\
to be rich, wealthy: amawaal.\\
\textbf{right}\\
right?: 'needee. right amount; correct, accurate assessment: aamndap.\\
\textbf{rimmed hat}\\
rimmed hat: ggaidm boashn.\\
\textbf{ring}\\
ring: gwishgwashm an'on.\\
\textbf{ring bell}\\
to ring bell slowly: hagwilya'dsa.\\
\textbf{ring finger}\\
ring finger: hashdalksh.\\
\textbf{rinse}\\
to rinse out: shidyoaksh.\\
\textbf{ripe}\\
to be very ripe: de'kwun.\\
\textbf{rise}\\
to rise, be swollen: geetg. to rise, get up from laying down: 'gineetg.\\
\textbf{river}\\
creek, river, stream: 'kala aksh.\\
\textbf{road}\\
on the road: lack guyna. path, road, trail: guyna.\\
\textbf{roast}\\
something you use to roast: 'nayoa. to hold skins toward fire to roast: hahlyaagw. to roast on open fire: yoa.\\
\textbf{robe}\\
robe for dancing: gwish-halayt.\\
\textbf{robin}\\
robin: gilakyo.\\
\textbf{rock}\\
rock, stone: loab.\\
\textbf{rock cod}\\
to fish for rock cod: oom ggaagg.\\
\textbf{rock wall}\\
cliff, rock wall: biyaackl.\\
\textbf{rock weed}\\
kelp, rock weed: 'ba'atsa.\\
\textbf{rodent}\\
rat, rodent: ggaklik.\\
\textbf{roll}\\
to roll: gya'galtk.\\
\textbf{roof}\\
roof: lack'oa waab.\\
\textbf{room}\\
back room: gi'dsoan.\\
\textbf{root}\\
edible root; fern-like plant: aah.\\
\textbf{rope}\\
rope: hagwilhoo. to jump rope: ggalkshaggush. to tie a rope : 'dseeba hagwilhoo.\\
\textbf{rope berry}\\
rope berry, trailing blackberry: maayha gwilhoo.\\
\textbf{rose}\\
rose, wild rose: 'kalaamsh.\\
\textbf{rot}\\
dry rot: mahaaya.\\
\textbf{rotten}\\
something rotten, unsanitary: mitmaatg.\\
\textbf{rough}\\
to be rough (like sandpaper): ggashgaatsg.\\
\textbf{row}\\
to paddle, row: duwaay, waay.\\
\textbf{rub}\\
to anoint, grease, massage, oil, rub: 'man.\\
\textbf{run}\\
to run: baa. to run a race against each other: mala'ka'kuhl. to run fast: aloobaa. to run into a house: 'dsilmbaa. to spin, run in circle: dsagga-tgubaa.\\
\textbf{run aground}\\
to run aground: 'dseeka.\\
\textbf{run away}\\
run away from: 'dsnshhood. to escape, run away, flee: 'gyaickg. to run away with: debaa.\\
\textbf{run backwards}\\
to run backwards: 'dsnkbaa.\\
\textbf{sack}\\
empty sack: ggalgwai'hl. sack: gwai'hl.\\
\textbf{sacred}\\
to be hallowed, sacred: 'nahloamshk. to be respected, sacred: 'nhloamshg.\\
\textbf{safety pin}\\
button, clasp to hold cape on; safety pin: ggan'doa.\\
\textbf{sailboat}\\
sailboat: hahloamboad.\\
\textbf{salal berries}\\
laughing berries, salal berries: dsawush.\\
\textbf{salmon}\\
chum salmon, dog salmon: ggayneesh. coho salmon: uuck. fish, salmon: hoan. humpback salmon, pink salmon: ggadoahl. King salmon, Chinook salmon: yeeh. sockeye salmon, red salmon: mishoa. to fish, catch salmon: 'mag.\\
\textbf{salmonberry}\\
salmonberry: ma'koacksh.\\
\textbf{salmonberry bushes}\\
salmonberry bushes: gga'koacksh.\\
\textbf{salmon eggs}\\
salmon eggs: laan.\\
\textbf{salmon stomach}\\
salmon stomach: 'gweentee.\\
\textbf{salmon trap}\\
People of the Salmon (Seal) Traps: Gitdseesh.\\
\textbf{salt}\\
salt: moan.\\
\textbf{salted fish}\\
salted fish: moanm hoan.\\
\textbf{sand}\\
on the sand: lack'awsh. sand: awsh.\\
\textbf{sand bar}\\
sand bar: lackhoo.\\
\textbf{Saskatoon berries}\\
Saskatoon berries: gyem.\\
\textbf{Saturday}\\
Saturday: Ha'li yaygga Sha.\\
\textbf{save}\\
to rescue, save: moatg. to save: damoatg. to save for later: yoo hoosh.\\
\textbf{saw}\\
saw: hackbayckshg. to cut, saw off: shackaicksh-ga. to saw: ckbaickshg.\\
\textbf{sawdust}\\
sawdust: ggamckbaickshk.\\
\textbf{sawhorse}\\
sawhorse: ha'lickbaickshg.\\
\textbf{sawmill}\\
sawmill: moolaa.\\
\textbf{say}\\
Say it yourself!: liphown!. to say again: hadsikshm gik hawn. to talk, say, claim too much: ggal'dsuu. what people are saying: hahow.\\
\textbf{scalp}\\
hair, scalp: ggolee.\\
\textbf{scarf}\\
scarf: golksh.\\
\textbf{school}\\
school: shgool. school (lit. house of learning): waab shiwilaaykwsha.\\
\textbf{schoolhouse}\\
schoolhouse: waabshgool.\\
\textbf{scissors}\\
clothespin, scissor-like tool: gganhla'ka'winshk. scissors: haggagietk.\\
\textbf{scold}\\
to advise, counsel; to rebuke, scold, talk to in a mean manner: daalck.\\
\textbf{scrape}\\
to rake, scrape: ggaapckan. to scrape, grind to pieces: kwhleeggiackn.\\
\textbf{scratch}\\
to scratch: ggaapck.\\
\textbf{sculpture}\\
sculpture, statue, painting, image; to paint: tckal'dsa'ba.\\
\textbf{sea anemone}\\
sea anemone: da'ka'aaw.\\
\textbf{sea cucumber}\\
sea cucumber: gyantee.\\
\textbf{seagull}\\
seagull: ggagoom.\\
\textbf{seagull egg}\\
seagull egg: hlgumadm ggagoom.\\
\textbf{seal}\\
seal: uula. to caulk, seal: 'bish'bash.\\
\textbf{seal intestines}\\
seal intestines: haada uula.\\
\textbf{sea lion}\\
sea lion: 'deebn.\\
\textbf{seal trap}\\
People of the Salmon (Seal) Traps: Gitdseesh.\\
\textbf{sea otter}\\
sea otter: phloan.\\
\textbf{search}\\
to search for: guguul.\\
\textbf{seasick}\\
to be seasick: maggoab.\\
\textbf{sea urchin}\\
large sea urchin: dsi'kwe'eds. sea urchin: ashwn.\\
\textbf{seaweed}\\
chopped seaweed: yeds hla'ashk. dried seaweed: 'bihloashk. place to dry seaweed: ha'libaashagganshk. seaweed: hla'ashg. toasted seaweed: shackul'ka.\\
\textbf{second finger}\\
middle finger: kshi'nag.\\
\textbf{see}\\
to look at, see: nee.\\
\textbf{seine}\\
net; to seine: aad. to fish with a net, seine for fish: aadm hoan.\\
\textbf{self-inflicted}\\
to be self-inflicted, toward oneself: gilksh.\\
\textbf{sell}\\
to sell: wa'at.\\
\textbf{send}\\
to send: hieds.\\
\textbf{serve}\\
to serve (food): 'dilgyad.\\
\textbf{settle}\\
to settle for damages done: ksheeshg.\\
\textbf{seven}\\
seven abstract, round or flat objects: 'tapckoald. seven people: 'tapckaldoal.\\
\textbf{several}\\
to be a few, some, several: aboo.\\
\textbf{sew}\\
to sew: loopg. to sew : lu'bish.\\
\textbf{shake}\\
to jump with fright, shake, be startled: ggabackshg.\\
\textbf{shaman}\\
headdress, mask, regalia, shaman's mask; shaman: aamhalaayt.\\
\textbf{shavings}\\
shavings: ggamhlabeeshk.\\
\textbf{she}\\
he, she, it: 'neet.\\
\textbf{sheep}\\
sheep: mati.\\
\textbf{sheet}\\
flannel blanket, sheet: sheedsm wush. sheet: sheeds.\\
\textbf{shelf}\\
shelf: ha'litoa.\\
\textbf{shell}\\
shells : 'dsee'k.\\
\textbf{shield}\\
copper shield: hayatsk.\\
\textbf{shiny}\\
to be polished, shiny: gugwalksh.\\
\textbf{ship}\\
navy ship, ship of war: malwoa.\\
\textbf{shirt}\\
shirt: kshlushg.\\
\textbf{shiver}\\
to shiver: gga'kuhl.\\
\textbf{shoe}\\
tennis shoes: 'dsoackshm hahloa.\\
\textbf{shoes}\\
shoes: 'dsoacksh.\\
\textbf{shoot}\\
to shoot (arrow, gun): kwdag. to shoot; to vote by hand or ballot: goo.\\
\textbf{shore}\\
to approach shore: 'nadalpg.\\
\textbf{short}\\
short trees: dalpgm gganggan. to be short: dalpg.\\
\textbf{shoulder}\\
shoulder, upper arm: 'dm'kie.\\
\textbf{shout}\\
to shout, yell: ayawaa.\\
\textbf{show}\\
to show: gwinee'dsn.\\
\textbf{show off}\\
to show off, to strut your stuff: dseekshwaaltksh.\\
\textbf{shrew}\\
shrew, small mouse: diboygid.\\
\textbf{shrink}\\
to shrink: dalbikshg.\\
\textbf{shrub}\\
People of the Shrubs: Gitdsacklahl.\\
\textbf{shut}\\
to close, shut: shga'doosh. to slam, swing shut: tckal'oy.\\
\textbf{sick}\\
to be sick; to be hurt: sheepg.\\
\textbf{sickness}\\
sickness: hasheepg.\\
\textbf{side}\\
to go into the woods; to walk to one side: ggahldikyaa. to lie on one's side: ggahldikshguu.\\
\textbf{sidetrack}\\
to put aside, put away; to sidetrack: awul'mag.\\
\textbf{silly}\\
to act silly: ma'watsa. to act silly, funny: shishnankshg.\\
\textbf{simmer down}\\
to cool, simmer down: ggoash.\\
\textbf{sing}\\
song; to sing: leemee.\\
\textbf{sink}\\
to sink: tgidaawhl. to sink below the surface: sha'dsool'biksh.\\
\textbf{sister}\\
baby sister; dress, skirt: na'ack. sister: hlgaawg.\\
\textbf{sit}\\
to creep; to sit in protest of moving or going: ggailkshg. to move over, sit in another place: gish'daa. to sit: 'daa.\\
\textbf{sit still}\\
to obey, sit still; to stay at home: dackshm'daa.\\
\textbf{six}\\
six abstract, flat or round objects: 'goald. six people: 'galdoal.\\
\textbf{size}\\
to be medium size, of a good size: aamggashgaawt. to be of a certain size: ggashgaawt.\\
\textbf{skin}\\
hide, skin: anaash. to hold skins toward fire to roast: hahlyaagw.\\
\textbf{skirt}\\
baby sister; dress, skirt: na'ack.\\
\textbf{skull}\\
skull: 'dmwaalgit.\\
\textbf{skunk}\\
skunk: ggain.\\
\textbf{skunk cabbage}\\
skunk cabbage: woanoack.\\
\textbf{sky}\\
overcast sky: goabackga lacka. sky: lacka.\\
\textbf{slam}\\
to slam, swing shut: tckal'oy.\\
\textbf{slave}\\
slave: ckaa.\\
\textbf{slave killer}\\
wooden war club, wooden slave killer: ha'kayaan.\\
\textbf{sleep}\\
to sleep: cksh'dock.\\
\textbf{sleet}\\
sleet; wet snow: akshilshgm maadm.\\
\textbf{slice}\\
to cut, slice: 'kots.\\
\textbf{slide}\\
to slide: 'dsoahl. to slide down: tgi'dsoahl. to slide (on feet, with a sled): gga'dsiyoahl.\\
\textbf{slime}\\
fish slime: yehl.\\
\textbf{slingshot}\\
slingshot: kw'dsag.\\
\textbf{slipper}\\
China slippers: 'dsak. slippers: 'dsoacksha 'tsawaab.\\
\textbf{slow}\\
to be slow: laaltg.\\
\textbf{slowly}\\
slowly: hagwil. to do slowly, slow down: hagwil waan.\\
\textbf{small}\\
to be little, small: 'tsushg. to be small: shishoosh. to be too small: ggal'tsushg.\\
\textbf{smaller}\\
to be smaller: 'ka 'tsushg.\\
\textbf{smear}\\
to smear, spread: 'dahl.\\
\textbf{smell}\\
aroma, smell; spirit: haig. to smell: hoom.\\
\textbf{smell good}\\
to be fragrant, smell good: meehoksh.\\
\textbf{smoke}\\
smoke: 'biyaan. to put on sticks for smoking (as fish, meat): ggahlggan. to smoke tobacco: ck'biyaan.\\
\textbf{smoked food}\\
smoked food: shi'biyaanshk.\\
\textbf{smoke hole}\\
chimney, smoke hole: ala.\\
\textbf{smooth}\\
to be smooth: yehlg.\\
\textbf{snail}\\
snail: ha'dsi'uult.\\
\textbf{snare}\\
snare, trap: dsayaihl.\\
\textbf{snipe}\\
snipe: dseehl.\\
\textbf{snobbish}\\
to be arrogant, haughty, proud, snobbish, stand-offish: adsiksh.\\
\textbf{snow}\\
falling snow: maadm. north blizzard, snow on north side of tree: shda'magsha shdoa ggan. sleet; wet snow: akshilshgm maadm. snow on the ground: moaksh. to snow: yaa moaksh. wet snow: 'maakwsh.\\
\textbf{snowstorm}\\
snowstorm: shda'magsh.\\
\textbf{soaking}\\
to be soaking wet; to be just born: 'nabaa.\\
\textbf{soapberries}\\
soapberries: ash.\\
\textbf{sob}\\
to sob: yackya'oack.\\
\textbf{sockeye salmon}\\
sockeye salmon, red salmon: mishoa.\\
\textbf{soft}\\
to be soft: goamtg.\\
\textbf{soil}\\
earth, ground, land, soil: yuub.\\
\textbf{soiled}\\
to be dirty, dusty, soiled: 'dsa'dsiksh.\\
\textbf{some}\\
a few, some: na gga'dsaaw. a few, some; to be a few: shgaboo. to be a few, some, several: aboo.\\
\textbf{somebody}\\
anybody, anyone, anything, somebody, someone, something: ligeetnaa.\\
\textbf{someone}\\
anybody, anyone, anything, somebody, someone, something: ligeetnaa.\\
\textbf{something}\\
anybody, anyone, anything, somebody, someone, something: ligeetnaa.\\
\textbf{some time ago}\\
some time ago: gitckawtk.\\
\textbf{song}\\
song; to sing: leemee. to have no song: 'waleemee.\\
\textbf{songbird}\\
meadowlark; songbird: be'an.\\
\textbf{soot}\\
charcoal, coal, soot: ggam'do'otsk.\\
\textbf{sorry}\\
to repent, be sorry for: gilksh'ietksh.\\
\textbf{sound}\\
to howl like a wolf; to sound in loud tone: gga'kowtg.\\
\textbf{sour}\\
to taste sour, citrusy: moalkshack.\\
\textbf{southeast wind}\\
southeast wind: hiwaash.\\
\textbf{south wind}\\
south wind: dsagmwaash.\\
\textbf{sparrow}\\
sparrow: gushguuds.\\
\textbf{spawn}\\
People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes: Gitlan.\\
\textbf{speak}\\
spoken or written word; to speak, talk: algyack.\\
\textbf{spear}\\
arrow, spear, sharp fighting equipment: hawaalt. to spear, stab: gyehlk.\\
\textbf{spend time}\\
to like to do, spend time doing: hadahaw.\\
\textbf{spider}\\
spider: adashged.\\
\textbf{spin}\\
something that spins; toy top: halhal. to spin, run in circle: dsagga-tgubaa.\\
\textbf{spirit}\\
apparition, ghost, spirit, vision: noogit. aroma, smell; spirit: haig. nothingness, spirit: oa'dsn.\\
\textbf{spit}\\
to spit: pukshg.\\
\textbf{splash}\\
to fall, splash: booboo.\\
\textbf{split}\\
to chop, split wood: bishboosh. to split, to chop: boosh.\\
\textbf{spoiled}\\
spoiled person: doa'yil.\\
\textbf{spokesman}\\
spokesman: ggalm'algyack.\\
\textbf{spoon}\\
horn spoon: hapckdooweew. spoon: hapshgoulg. wooden spoon: hapshgoulgm ggan.\\
\textbf{spouse}\\
spouse; to marry: naksh.\\
\textbf{spread}\\
to smear, spread: 'dahl. to spread: 'leebahla.\\
\textbf{spring}\\
spring (season): goaym.\\
\textbf{sprinkle}\\
to dampen; to sprinkle: dsakshuld.\\
\textbf{spruce}\\
spruce: sha'mn.\\
\textbf{squall}\\
squall: meeg.\\
\textbf{squeeze}\\
to hold, hug, squeeze: dam. to hold, squeeze: damshg.\\
\textbf{squid}\\
octopus, squid, devil fish: ha'tsal.\\
\textbf{squirrel}\\
squirrel: dushck.\\
\textbf{stab}\\
to spear, stab: gyehlk. to stab: 'dsaa.\\
\textbf{stand}\\
to stand: hietg. to stand near the water; to stand out: ukshhietg. to stand smartly: dseekshhietksh.\\
\textbf{stand-offish}\\
to be arrogant, haughty, proud, snobbish, stand-offish: adsiksh.\\
\textbf{stand still}\\
to stand still: dackshmhietk.\\
\textbf{star}\\
evening star: beyaalshm aatk. morning star: beyaalshm gganhlaag. star: beyaalsh.\\
\textbf{stare}\\
to stare at: shigeene'etsg.\\
\textbf{start}\\
alright!; behold!; well now; let's start!; okay!: wie wa!. to start: laandsa. to start off: sha'daatg.\\
\textbf{startled}\\
to jump with fright, shake, be startled: ggabackshg.\\
\textbf{statement}\\
decree, message, official statement: ayaawgg.\\
\textbf{statue}\\
sculpture, statue, painting, image; to paint: tckal'dsa'ba.\\
\textbf{stay}\\
to stay away for a long time: ayuwaan.\\
\textbf{stay at home}\\
to obey, sit still; to stay at home: dackshm'daa.\\
\textbf{stay behind}\\
to stay behind: ginawaal. to stay behind, be left behind: 'dsnshloyg.\\
\textbf{steal}\\
to steal: 'kaal'g, 'dsa'wulsh.\\
\textbf{steelhead trout}\\
steelhead trout: mileed.\\
\textbf{steep}\\
to be expensive; difficult; challenging; steep; valuable: 'doackg.\\
\textbf{steering wheel}\\
steering wheel: hadaay.\\
\textbf{steersman}\\
steersman; stern (of a boat): 'dmlaan.\\
\textbf{stern}\\
aft of boat, back end, rear, stern: gilaan. People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes: Gitlan. steersman; stern (of a boat): 'dmlaan.\\
\textbf{stick}\\
to hit with a stick or club: 'galyeds. to put on sticks for smoking (as fish, meat): ggahlggan.\\
\textbf{stick out}\\
to stick out: kshabatsk.\\
\textbf{stiff}\\
to be dried hard, stiff with cold: ggantk.\\
\textbf{stinging nettles}\\
stinging nettles: shdatee.\\
\textbf{stink}\\
to stink: ooshg.\\
\textbf{stink eggs}\\
stink eggs : ooshgmlaan.\\
\textbf{stomach}\\
abdomen, belly, stomach, tummy: ban. salmon stomach: 'gweentee. stomach: ggal'oash. to have an upset stomach: 'la 'daa ggoadu.\\
\textbf{stone}\\
rock, stone: loab.\\
\textbf{stoop}\\
to bend forward, bow, stoop: ggogg.\\
\textbf{stop}\\
to stop, not do: giloa.\\
\textbf{store}\\
store: ggaldmwa'at.\\
\textbf{story}\\
legend, folktale, story; title: adaawck. story, tale; to narrate, tell: malshg.\\
\textbf{straight}\\
to be straight: aadsik.\\
\textbf{strap}\\
backpack; strap to carry things: gganawulee.\\
\textbf{strawberry}\\
strawberry: magool.\\
\textbf{stream}\\
creek, river, stream: 'kala aksh.\\
\textbf{strewn}\\
to come apart, be irreparable; to be strewn loosely: ggol.\\
\textbf{string}\\
to string up, put on drying pole: ggahlg.\\
\textbf{strip}\\
dried fish strips: 'kiewoaksh.\\
\textbf{strong}\\
to be built strong; to put on warm clothes: doyksh. to be strong: ggaaka. to be strong (physically or orally): ggatgyad.\\
\textbf{strong tide}\\
rapids, strong tide: doyksh.\\
\textbf{strut}\\
to show off, to strut your stuff: dseekshwaaltksh. to strut, walk with flair: dseekshyaaksh.\\
\textbf{stubborn}\\
to be stubborn: gigi'oashg.\\
\textbf{stuck}\\
to be stuck, unable to travel: doolckg.\\
\textbf{stump}\\
stump, old tree still standing: dipckan. tree stump: ha'ats.\\
\textbf{suck}\\
to suck: 'doagg.\\
\textbf{suffer}\\
not easy, work hard against odds, suffer: haackg.\\
\textbf{summer}\\
summer: shuunt.\\
\textbf{summertime}\\
month of picking berries, summertime: lackshumaay.\\
\textbf{sun}\\
month; sun, heat; to be hot, warm: gyamg. sun: gyamgmdseewsh.\\
\textbf{Sunday}\\
Sunday: Ha'li Shgwaitga Sha.\\
\textbf{sunshine}\\
sunshine: shaggagiamg.\\
\textbf{supernatural}\\
supernatural being, power: nacknock.\\
\textbf{suprised}\\
to be astonished, surprised: shanaahlg.\\
\textbf{surgery}\\
operation, surgery: baahlk.\\
\textbf{surprise}\\
to surprise: shagaksh.\\
\textbf{suspenders}\\
suspenders: gganyishya'tsa.\\
\textbf{swan}\\
swan: ggag.\\
\textbf{sweep}\\
to sweep: 'doo. to sweep with branch or broom: 'dooshg.\\
\textbf{sweepings}\\
sweepings: ggam'dooshk.\\
\textbf{sweetheart}\\
friend, sweetheart: 'nashee'bnshk.\\
\textbf{swift}\\
People of the Swift Waters: Git'nadoyksh.\\
\textbf{swim}\\
to swim: hadiksh.\\
\textbf{swing}\\
to slam, swing shut: tckal'oy.\\
\textbf{swollen}\\
to rise, be swollen: geetg.\\
\textbf{sword}\\
sword: ggawaaym 'tu'utsk.\\
\textbf{syphilis}\\
syphilis: ha'dackgm sheepg.\\
\textbf{syrup}\\
syrup: baloash.\\
\textbf{table}\\
desk, table: ha'li'dameesh. dinner table: ha'litckoackg.\\
\textbf{tail}\\
fish tail: na'dsiksh.\\
\textbf{take}\\
to carry, take: dock. to carry, take along: shndock. to take: gaa. to take along the beach: hahldock. to take, carry along: tckalgaa.\\
\textbf{take along}\\
to take along: tckaldock.\\
\textbf{take a picture}\\
to draw, take a picture: gilkshtckal'da'minshg.\\
\textbf{take a walk}\\
to take a walk: sha'up yaa.\\
\textbf{take away}\\
to take away: shilmdock.\\
\textbf{take care}\\
to keep, take care of: haboal.\\
\textbf{take in}\\
to take in: 'dsilmgaa.\\
\textbf{take off}\\
to remove, take off (singular): shagaa. to remove, to take off (plural): shadoack.\\
\textbf{take out}\\
to take out: kshagaa, ukshdockhl, shm'okshdock. to take out, unpack: ukshdock.\\
\textbf{Taku people}\\
Taku people; Metlakatla: Ta'gwaan.\\
\textbf{tale}\\
story, tale; to narrate, tell: malshg.\\
\textbf{talk}\\
spoken or written word; to speak, talk: algyack. to gossip, talk about: 'bilhow. to talking to oneself: lipnahow. to talk, say, claim too much: ggal'dsuu.\\
\textbf{tall}\\
to be tall: 'naphlackhl.\\
\textbf{tap}\\
to hit with, hammer; to hit, tap: 'taab.\\
\textbf{taste}\\
feeling of strong taste in throat: 'geelg. to taste: back.\\
\textbf{taste good}\\
to taste good: 'tsamaatg.\\
\textbf{tasty}\\
to be tasty: 'dsimaatk.\\
\textbf{taut}\\
to be taut, tight: damckg.\\
\textbf{tea}\\
Hudson Bay tea: 'gwilamacksh.\\
\textbf{teach}\\
teacher; to teach: shiwilaay'yamck.\\
\textbf{teacher}\\
teacher; to teach: shiwilaay'yamck.\\
\textbf{tear}\\
tear, teardrop: ksheel. to tear, pull bark from cedar tree: bayck.\\
\textbf{teardrop}\\
tear, teardrop: ksheel.\\
\textbf{telephone}\\
telephone: malshgm 'tu'itsg.\\
\textbf{tell}\\
story, tale; to narrate, tell: malshg. to tell: mahl.\\
\textbf{tell the truth}\\
to tell the truth: shmhow.\\
\textbf{ten}\\
ten abstract, round or flat objects: 'gyap. ten people: kboal.\\
\textbf{tennis shoe}\\
tennis shoes: 'dsoackshm hahloa.\\
\textbf{thank}\\
to express appreciation, thank: 'doycksh. to thank, express appreciation: 'doyck.\\
\textbf{that}\\
that, there: gwee.\\
\textbf{that direction}\\
in that direction, over there: gwashga.\\
\textbf{then}\\
that's when, then: ggakshwil.\\
\textbf{there}\\
that, there: gwee. there: awaan.\\
\textbf{thick}\\
to be thick (ice, board, fog, etc.): ckdsee.\\
\textbf{thief}\\
thief: wuk'dsa'wulsh.\\
\textbf{think}\\
to assume, guess, think: ha'liggoad. to start thinking about, have an idea about: shiggoatg.\\
\textbf{third finger}\\
ring finger: hashdalksh.\\
\textbf{thread}\\
thread: nloo'bish.\\
\textbf{three}\\
three abstract or round things: 'gwilee. three boats or canoes: ggaltsggantg. three fish or flat objects: gwan. three long objects: ggaltsggan. three people: gwiloan.\\
\textbf{throat}\\
throat: 'kalmhow. to have too much food in one's throat: 'da'giackshg.\\
\textbf{through}\\
through a sea channel: mackla.\\
\textbf{throw}\\
to hit with a thrown object: 'gal'oy. to throw, pitch: ayam.\\
\textbf{throw away}\\
to throw away: sha'oyhl.\\
\textbf{thumb}\\
thumb: moash.\\
\textbf{thunder}\\
cannon; thunder: ggalipleep.\\
\textbf{thunder berries}\\
thunder berries: maaym ggalipleeb.\\
\textbf{Thursday}\\
Thursday: Ha'li tckaalpcka Sha.\\
\textbf{tickle}\\
to tickle: 'tsack'tsackg.\\
\textbf{tide}\\
high tide: deetck'aksh. to be left by the tide; to leak: 'dsee'g.\\
\textbf{tie}\\
tie; necklace: 'yootishg. to add to, bring to, tie to: tckalhokshnhl. to tie: 'dseeb. to tie a rope : 'dseeba hagwilhoo. to tie, tie around: dakhl.\\
\textbf{tie on}\\
to fasten to, tie on: tckal'dseeb. to tie on (with ribbon, twine): tckaldakhl.\\
\textbf{tiger}\\
tiger, wildcat: dooshm gilhawli.\\
\textbf{tight}\\
to be taut, tight: damckg. to hold, hold fast, hold tight: dackyaagw.\\
\textbf{time}\\
at this time, this hour: dsihla. time for: lugwaantg.\\
\textbf{tired}\\
to be tired: shoonaahl.\\
\textbf{title}\\
legend, folktale, story; title: adaawck.\\
\textbf{today}\\
now, today: gya'wn. today: sha gya'wn.\\
\textbf{toe}\\
athlete's foot, toes that have a smell: sh'kaancksh. big toe: moashm shee.\\
\textbf{toenail}\\
toenail: hlackshmshee.\\
\textbf{to feel cold}\\
feel cold: ckgwatksh.\\
\textbf{tomorrow}\\
tomorrow: dsigi'dseeb.\\
\textbf{tongue}\\
tongue: doola.\\
\textbf{tonight}\\
tonight: dsadaawhl.\\
\textbf{too}\\
to come, come here; too, also: ggal.\\
\textbf{tool}\\
bow; tool: hackdek. tools: 'nahoa'ya.\\
\textbf{too many}\\
too many: ggal haild.\\
\textbf{too much}\\
to talk, say, claim too much: ggal'dsuu.\\
\textbf{tooth}\\
teeth: 'waan.\\
\textbf{top}\\
cover, top of an object: ha'bish. something that spins; toy top: halhal. top of: lack'oa.\\
\textbf{to sneeze}\\
to sneeze: ha'ashya.\\
\textbf{to spoil}\\
to spoil, decay: ckaatg.\\
\textbf{totem pole}\\
totem pole: p'tsaan.\\
\textbf{touch}\\
to touch: gwaantg.\\
\textbf{tough}\\
to make it tough for: ha'kan.\\
\textbf{toward oneself}\\
to be self-inflicted, toward oneself: gilksh.\\
\textbf{trail}\\
path, road, trail: guyna.\\
\textbf{trailing blackberry}\\
rope berry, trailing blackberry: maayha gwilhoo.\\
\textbf{train}\\
train: shdeem boadm gilhouli.\\
\textbf{trap}\\
fish trap: loolp. fish trap; to hurry: 'deen. snare, trap: dsayaihl.\\
\textbf{treat}\\
to treat with medicine: haldaaw.\\
\textbf{tree}\\
short trees: dalpgm gganggan. stump, old tree still standing: dipckan. tall trees, trees: 'nuk 'nuungm gganggan. tree, wood: ggan.\\
\textbf{tremble}\\
quiver (of the chin), tremble: babaa.\\
\textbf{trickster}\\
cheater, trickster: nacknockm 'yood. clever woman, woman cheater, woman trickster: nacknockm hana'ack.\\
\textbf{trim}\\
to trim hair by burning ends: gwalka.\\
\textbf{troll}\\
to troll: oo.\\
\textbf{trolling}\\
to fish, troll: oom hoan.\\
\textbf{trouble}\\
trouble: hashooshk.\\
\textbf{trousers}\\
pants, trousers: 'backsh.\\
\textbf{trout}\\
steelhead trout: mileed. trout: la'uu.\\
\textbf{trust}\\
to hope, trust: 'wayoaksh.\\
\textbf{truth}\\
to tell the truth: shmhow.\\
\textbf{try}\\
liver; to judge, try in court, measure: dap. to feel; to try, venture: baal.\\
\textbf{Tsimshian}\\
Tsimshian: 'Tsmshian.\\
\textbf{'TsmSHIAN}\\
'TsmSHIAN language (lit. The True Language): Shm'algyack.\\
\textbf{Tuesday}\\
Tuesday: Ha'li goo'bl Sha.\\
\textbf{tummy}\\
abdomen, belly, stomach, tummy: ban.\\
\textbf{turn around}\\
to turn around: tgwayeltg.\\
\textbf{turn back}\\
to return, turn back: luyeltg.\\
\textbf{turn off}\\
to turn off: 'dsakya.\\
\textbf{turn on}\\
to turn on (of electricity): gwal'kan.\\
\textbf{turn over}\\
to turn over, upset (of a canoe or boat): ckaaytg.\\
\textbf{twenty}\\
twenty flat objects: 'gideelt.\\
\textbf{two}\\
two abstract objects: goo'bl. two boats or canoes: ggalbailtg. two fish, animals or flat things: 'tapckaad. two long objects: goa'opshgn. two people: 'tapckadool.\\
\textbf{ugly}\\
to be ugly: shga'dsuu.\\
\textbf{unable}\\
to be unable, can't: hlgookshn.\\
\textbf{uncle}\\
uncle: beeb.\\
\textbf{unclear}\\
to be unclear: ahlga ga ggontgahl.\\
\textbf{under}\\
to be under: nhluu.\\
\textbf{undergarment}\\
undergarment: lukhleehoaya.\\
\textbf{underpants}\\
underpants: lukhlee'backsh.\\
\textbf{undershirt}\\
undershirt: lukhleekshlushg.\\
\textbf{unexpected}\\
to be unexpected: gina-shawaal.\\
\textbf{unlucky}\\
unlucky; come empty handed: ggal'waatk.\\
\textbf{unpack}\\
to take out, unpack: ukshdock.\\
\textbf{unsanitary}\\
something rotten, unsanitary: mitmaatg.\\
\textbf{up high}\\
hill, mountain; up high: gyepsh.\\
\textbf{upon}\\
on, upon: lack. upon: ha'li.\\
\textbf{upset}\\
to turn over, upset (of a canoe or boat): ckaaytg.\\
\textbf{upset stomach}\\
to have an upset stomach: 'la 'daa ggoadu.\\
\textbf{upside down}\\
upside down: ckbashm 'ka'kackd.\\
\textbf{upwards}\\
upwards: mun.\\
\textbf{urchin}\\
sea urchin: ashwn.\\
\textbf{use}\\
to use, wear: hoy.\\
\textbf{valuable}\\
to be expensive; difficult; challenging; steep; valuable: 'doackg.\\
\textbf{vehicle}\\
car, wagon, vehicle: 'dsig'dsig.\\
\textbf{venture}\\
to feel; to try, venture: baal.\\
\textbf{very}\\
to be many, very: lu'kwil.\\
\textbf{village}\\
village: ggaldsap.\\
\textbf{visible}\\
to be clear, evident, visible: ggontgahl.\\
\textbf{vision}\\
apparition, ghost, spirit, vision: noogit.\\
\textbf{visit}\\
to visit: 'dsilaay.\\
\textbf{voice}\\
voice: how, amhow.\\
\textbf{vomit}\\
to vomit: cksheet.\\
\textbf{vote}\\
to shoot; to vote by hand or ballot: goo.\\
\textbf{wagon}\\
car, wagon, vehicle: 'dsig'dsig.\\
\textbf{wait}\\
to expect, hope for, wait for: booyshg. to wait: ha'weeni. to wait, await: babood.\\
\textbf{waiter}\\
waiter: kshdsood.\\
\textbf{wake up}\\
to wake up: gukshg, haldm'oy.\\
\textbf{walk}\\
to deliver information; to walk house to house: ckbeeyaa. to go into the woods; to walk to one side: ggahldikyaa. to go, move, walk up along the ground: backyaa. to take a walk: sha'up yaa. to walk: yaa, waalck. to walk across: dsaggayaa. to walk along the beach: hahlyaa. to walk over here: yanna gee. to walk slowly: hagwilyaa. to walk to the front: 'dmyaa.\\
\textbf{walk backwards}\\
to walk backwards: 'dsnkyaa.\\
\textbf{walk toward}\\
to walk toward: gugwnyaa.\\
\textbf{walk up}\\
to ascend, go up, walk up: munyaa.\\
\textbf{wall}\\
wall: haahlggan.\\
\textbf{want}\\
to want: hashack. to want someone's food: mat.\\
\textbf{war club}\\
wooden war club, wooden slave killer: ha'kayaan.\\
\textbf{warm}\\
month; sun, heat; to be hot, warm: gyamg. to be built strong; to put on warm clothes: doycksh.\\
\textbf{warn}\\
to get out of the way; to make aware, warn: boo'ihl.\\
\textbf{wart}\\
wart: ggalooy.\\
\textbf{wash}\\
to wash: yoaksh. to wash clothing or soft material: lumaaksh.\\
\textbf{watch}\\
clock, watch: waads. wristwatch: waadsm an'on.\\
\textbf{watchful}\\
to be careful, cautious, watchful: amane'ets.\\
\textbf{water}\\
drops of water, water drops: le'wul. next to the water, at the water's edge: geeka. on the water: lack'aksh. out on the water: giyaaksh. to be wet, to drink; water: aksh. to dip, draw water: gyab.\\
\textbf{water container}\\
bucket, pail, water container: ggaldm'aksh.\\
\textbf{waterfall}\\
swift rapids, waterfall, gorge, canyon: 'tsilaashu.\\
\textbf{waterspout}\\
gale, waterspout: backbeega'aksh.\\
\textbf{wave}\\
waves: ggoab.\\
\textbf{we}\\
we: 'nuum.\\
\textbf{weak}\\
to be diluted, weak: alashkw.\\
\textbf{wealthy}\\
to be rich, wealthy: amawaal.\\
\textbf{weapon}\\
weapon: hawala'awa.\\
\textbf{wear}\\
to use, wear: hoy.\\
\textbf{weather}\\
above, Heavens, weather: Lackaga.\\
\textbf{Wednesday}\\
Wednesday: Ha'li 'Gwilee Sha.\\
\textbf{weep}\\
to cry, weep: weehawtg.\\
\textbf{weight}\\
to kick; to press, put weight on: kwhlacksh.\\
\textbf{well}\\
to be fine, good, well: aam.\\
\textbf{well-designed}\\
to be completed, well-designed, well-proportioned; to do over, fix, repair: amadsab.\\
\textbf{well now}\\
alright!; behold!; well now; let's start!; okay!: wie wa!.\\
\textbf{well-proportioned}\\
to be completed, well-designed, well-proportioned; to do over, fix, repair : amadsab.\\
\textbf{westerly wind}\\
westerly wind: guulka.\\
\textbf{west wind}\\
west wind: ckbaala.\\
\textbf{wet}\\
to be soaking wet; to be just born: 'nabaa. to be wet, to drink; water: aksh.\\
\textbf{whale}\\
killer whale, whale: 'naackhl.\\
\textbf{what}\\
what?: goa.\\
\textbf{wheel}\\
steering wheel: hadaay.\\
\textbf{when}\\
go away!; how, when, where: nda. that's when, then: ggakshwil. when?: dse nda?.\\
\textbf{where}\\
go away!; how, when, where: nda. where?: ndashda, ndada.\\
\textbf{whet stone}\\
emery wheel, whet stone: dashgyan.\\
\textbf{whirlpool}\\
whirlpool: 'dsalksh.\\
\textbf{whirlwind}\\
wind, whirlwind: 'dag.\\
\textbf{whistle}\\
instrument with holes; whistle: hackshgweekwshg. whistle: ckshwa'dackg.\\
\textbf{white}\\
driftwood; White person, European: umsheewa. white: moakshg.\\
\textbf{White}\\
White man, bearded man: gga'eemck.\\
\textbf{who}\\
breath; who?: naa.\\
\textbf{why}\\
why?: A-wil goa?.\\
\textbf{wier}\\
People of the Other Side (Wiers): Git'ando.\\
\textbf{wildcat}\\
tiger, wildcat: dooshm gilhawli.\\
\textbf{wild celery}\\
wild celery: 'beensh.\\
\textbf{win}\\
to win (a game, war): ckshdaa.\\
\textbf{wind}\\
crosswind: dsaggabaashg. gale, strong wind: ggatgyatga baashg. northeast wind: gishihaywaash. north wind: gishiyaashg. offshore wind: ukshbaashg. onshore wind: dsaggmbaashg. southeast wind: hiwaash. south wind: dsagmwaash. strong wind: gatgyetga baashg. to blow; wind: baashg. westerly wind: guulka. west wind: ckbaala. wind, whirlwind: 'dag.\\
\textbf{window}\\
mirror, window: 'nakshuuneeshg. window, light source: gganlugoy'pa.\\
\textbf{windy}\\
to be very windy: 'dsuu baashg.\\
\textbf{wing}\\
wing: gga'kai.\\
\textbf{wink}\\
to blink, wink: ggapshil.\\
\textbf{winter}\\
deep winter, hard times: magwa'ala. winter: goamshm.\\
\textbf{wipe}\\
to wipe: geemg.\\
\textbf{Wishing you well!}\\
Do your best! Wishing you well!: sha'aamdza waan.\\
\textbf{witchcraft}\\
witchcraft: haldaawgit.\\
\textbf{within}\\
within: 'dsm.\\
\textbf{without}\\
without: 'wa.\\
\textbf{wolf}\\
to howl like a wolf; to sound in loud tone: gga'kowtg. wolf: gibaaw.\\
\textbf{Wolf Clan}\\
Wolf Clan: Lack-giboo.\\
\textbf{woman}\\
clever woman, woman cheater, woman trickster: nacknockm hana'ack. girl, lady, woman: hana'ack.\\
\textbf{wonder}\\
miracle, wonder; to breathe: shanaahl.\\
\textbf{wood}\\
forest; pieces of wood: gganggan. to chop, split wood: bishboosh. tree, wood: ggan.\\
\textbf{woods}\\
in the woods or forest: gilhowlee. to come back out of the woods: 'nayeltg. to go into the woods; to walk to one side: ggahldikyaa.\\
\textbf{woon}\\
wood, rotted: haaya.\\
\textbf{word}\\
spoken or written word; to speak, talk: algyack.\\
\textbf{work}\\
hard working person: 'gwaloa'am gyad. to be a hard worker, industrious: a'waa'ackshg. to be industrious, hard working: 'gwiloa'ack. to work, labor: hahlalsh.\\
\textbf{work hard against odds}\\
not easy, work hard against odds, suffer: haackg.\\
\textbf{world}\\
earth, world: ha'lidsogg.\\
\textbf{worm}\\
worm: laald.\\
\textbf{worried}\\
to be worried: luwantgmggoad.\\
\textbf{worry}\\
to worry: luwantg.\\
\textbf{worthless}\\
low profile, low status, a worthless person: gga'gwaa'gw.\\
\textbf{wound}\\
to be hurt, wounded; to hurt, wound: shgaaygshg.\\
\textbf{wounded}\\
to be hurt, wounded; to hurt, wound: shgaaygshg.\\
\textbf{wrap up}\\
to wrap up: laa'wil.\\
\textbf{wristwatch}\\
wristwatch: waadsm an'on.\\
\textbf{write}\\
to draw, write: na'dum. to write: na'dum, 'dum. to write; written material: 'dameesh.\\
\textbf{written material}\\
to write; written material: 'dameesh.\\
\textbf{wrong}\\
to do something wrong, make a mistake: labaggietwaal. to err, miss, make a mistake, do something wrong: geesh.\\
\textbf{yarn hat}\\
yarn hat: ggaidm shihoo.\\
\textbf{year}\\
year: 'goahl.\\
\textbf{years ago}\\
years ago; long ago: gi'goahl.\\
\textbf{yeast}\\
yeast: eesh.\\
\textbf{yell}\\
to shout, yell: ayawaa.\\
\textbf{yellow cedar}\\
yellow cedar: wahl.\\
\textbf{yellow jacket}\\
bee, hornet, yellow jacket: ab.\\
\textbf{yes}\\
yes: oa, n'neet.\\
\textbf{yesterday}\\
yesterday: gi'dseeb.\\
\textbf{you}\\
you: 'nuun.\\
\textbf{young}\\
to be young; young person: shu'bash.\\
\textbf{youngest male}\\
to be the youngest male: gganeesh.\\
\textbf{young people}\\
young people: shumacksh.\\


\end{document}
```

**2. JSONL Extraction:**

Now, I will parse the corrected LaTeX structure and output the dictionary entries in JSONL format.

```jsonl
{"headword": "aab", "definition": "noun my father\n-Yagwa goom wunsh aabdu. My father is hunting for deer."}
{"headword": "aad", "definition": "noun; verb net; to seine Plural:ga'aad\n-Geegsh Dzon shu aad dm hoyt hla aadmhoant. John bought a new net for fishing."}
{"headword": "aadm hoan", "definition": "verb to fish with a net, seine for fish\n-Dm aadm hoanm sha gya'wn. We will fish with a net today."}
{"headword": "aadsack", "definition": "verb to be long enough, reach across PLURAL: ack'aadsack\n-Aadsacka hagwilhoo. The rope is long enough.\n-Aadsacka hagwilhoo da na boadm. The rope is long enough for our boat."}
{"headword": "aadsik", "definition": "verb to be straight\n-Aadsika guyna da awaa waabn. The path by your house is straight."}
{"headword": "aah", "definition": "noun edible root; fern-like plant\n-Ndahl wil 'dahla aah? Where do the edible root plants grow?"}
{"headword": "aalck", "definition": "verb to be bold, brave, courageous PLURAL: al'aalck\n-Ap lu'kwil al'aalcka hlaagigyad. The old timers were very courageous.\n(-) Lu'kwil al'aalcka gibaaw. The wolf acted very bold."}
{"headword": "aam", "definition": "verb to be fine, good, well PLURAL: am'aam\n-Aam wila howyu. I'm feeling good.\n(-) Na sheepg nakshu ashda 'guulda shada dowl mahlda doctor hla aam wila waald gya'win. My wife was sick the other day but the doctor said she's good now."}
{"headword": "aamggashgaawt", "definition": "verb to be medium size, of a good size\n-Aamggashgaawt ga yeeh. The King salmon was of a good size."}
{"headword": "aamhalaayt", "definition": "noun headdress, mask, regalia, shaman's mask; shaman PLURAL: gaamhakhalaayt\n-Naahl en dsaba aamhalaayt hoysh Dan? Who made the headdress that Dan is wearing?"}
{"headword": "aamndap", "definition": "noun right amount; correct, accurate assessment\n-Aamndapa sha 'naga taggan. The plank is the right length."}
{"headword": "aamshgaboo", "definition": "verb to be enough, adequate, ample, plentiful\n-Hla aamshgaboo wineaya gwa'a. There's enough food here.\n-Hla aamshgaboo lag. That's enough wood.\n-Na oom hoan 'yoota gwee da aamshgaboo 'maget. That man went fishing and he got enough."}
{"headword": "aamshga'nak", "definition": "adverb; verb after a while; to be far enough, long enough\n-Dm yaawckga'nu dsihla aamshga'nak. I will eat after awhile."}
{"headword": "aatk", "definition": "noun night\n-Tcka'nooyu gwitgwineeksh hla aatk. I heard the owl at night."}
{"headword": "aa'back", "definition": "verb to recall, remember\n-Aa'backdu shga 'tsamaatga shameeym wun. I remember how good deer meat tastes."}
{"headword": "ab", "definition": "noun bee, hornet, yellow jacket\n-Gyehlga'nu ab. I got stung by a bee."}
{"headword": "aba'ackshg", "definition": "verb to be anxious\n-Ahlgadee aam shga aba'ackshgn. It's not good that you're so anxious.\n(-) Lu'kwil aam lacka, aba'ackshgu dm 'gwihl yaayu. The weather is real good, I'm anxious to go walking."}
{"headword": "aboo", "definition": "verb to be a few, some, several\n-Aboo gyad gatgoidikshd. A few people came.\n-Lu'kwil aboo hoan 'goahla gwa'a. There's few fish this year."}
{"headword": "ada", "definition": "conjunction and\n-Ada weehowtga hana'ack hlat nee wil badsga boad. And the woman cried when she saw the boat arrive."}
{"headword": "adaahl", "definition": "noun fire in the water; phosphorescent algae\n-Needsu wil lu'gwil goi'pa adaahl. I see that the fire in the water is very bright."}
{"headword": "adaawck", "definition": "noun legend, folktale, story; title\n-Wilaaysh Silas adaawck, aam shm ama amookshn. Silas knows stories, it's good to really listen."}
{"headword": "adabeesh", "definition": "noun butterfly\n-Shm mashga adabeesh. The butterfly is very red."}
{"headword": "adaggan", "definition": "noun ghost bread\n-Goayu adaggan? What is ghost bread?"}
{"headword": "adashged", "definition": "noun spider\n-Baasha'nu da adashged. I'm afraid of spiders."}
{"headword": "adsiksh", "definition": "verb to be arrogant, haughty, proud, snobbish, stand-offish\n-Adsiksha ggoadu. My heart is proud.\n-Lu'kwil adsiksha wila how ggoadu da shga hultga hoan da'ackgu. My heart is proud of how much fish I was able to get."}
{"headword": "agwee", "definition": "prefix distant\n-Agwee wil 'daa waabsh Li'ihl. Henry's house is in the distance."}
{"headword": "agwee hluk'kwdaa'yn", "definition": "noun great-grandchildren\n-Hladm goidiksha agwee hluk'kwdaa'ynu. My great grandchildren will soon be here."}
{"headword": "ahl aamdee?", "definition": "phrase Is it good? Okay?\n-Ahl aamdee maay gwa'a? Is this fruit good?\n-Ahl aamdee hoan gwee? Is it okay to fish there?"}
{"headword": "ahlga", "definition": "prefix not\n-Ahlgadee aam wila how sha'winshga gwa'a. What this paper says is not good."}
{"headword": "ahlgadee goa", "definition": "noun nothing\n-Ahlgadee goahl geegee I bought nothing."}
{"headword": "ahlga ga ggontgahl", "definition": "verb to be unclear\n-Ahlga ga ggontgahla wila haw 'yoota. What the man said was not clear."}
{"headword": "ahlyeeggawsh", "definition": "noun hummingbird\n-Needsu hailda ahlyeeggawsh da ggaldoa. I saw a lot of hummingbirds where we camped."}
{"headword": "ahl'bal", "definition": "verb to misbutton\n-Ahl'bal na kshlushgt. She misbuttoned her blouse."}
{"headword": "aigyad", "definition": "verb to be durable, live a long life\n-Aygyadid maata awil amaneedsda goa gubt. Martha lived a very long life because she was careful about what she ate."}
{"headword": "aipn", "definition": "verb to be lightweight\n-Aipn hlgu gwai'hl. The sack was pretty light.\n-Aipn hlgu gwai'hl, da'acklga hlguwoamhlg dmt badst. The sack was pretty light, the little child will be able to lift it."}
{"headword": "aishk", "definition": "verb to owe; to promise\n-Nda shgaboo daala aishken? How much money do you owe?"}
{"headword": "ai'dsm anaay", "definition": "noun fried bread\n-Hashacku aildsm anaay. I want fried bread."}
{"headword": "ai'dsm hoan", "definition": "noun fried fish\n-Ai'dsm hoan 'ka 'tsamaa'anu. I like fried fish best."}
{"headword": "aksh", "definition": "verb; noun to be wet, to drink; water PLURAL: ak'aksh\n-Gushcka aksha gwa'a. This water is bitter.\n(-) Lu'kwil tsamaatga aksha gwee. That water tastes really good."}
{"headword": "akshilshgm maadm", "definition": "noun sleet; wet snow\n-'Dsuu akshilshgm maadm ashda gi'dseeb. There was a lot of wet snow yesterday."}
{"headword": "akshyaa", "definition": "verb to accumulate, get fat, increase PLUEAL: akshwaalcksh\n-Dm akshyaa wun da 'goahla gwa'a. There will be more deer this year.\n-Na dsabu ash asda gi'dseeb da akshyaat dowla dp gubt. I made some soapberries the other day and it increased and we ate it."}
{"headword": "akshyaagwa dseewsh", "definition": "noun dawn, daybreak\n-Dm dawhla boad dsihla akshyaagwa dseewsh. The boat will leave at dawn."}
{"headword": "ala", "definition": "noun chimney, smoke hole\n-Ahlgandee nee 'dbiyaan a ala. I don't see any smoke coming from the chimney."}
{"headword": "alaaysh", "definition": "verb to be lazy PLURAL: ak'alaaysh\n-Giloa alaayshn. Don't be lazy.\n-Na hootgu hlguhlgu dumt hlimoame bite alaayshd. I called my son to help me but he was lazy."}
{"headword": "alashkw", "definition": "verb to be diluted, weak PLURAL: huk'alashkw\n-Na dm badsu 'wee ggan gwee dowl ggal alashkwu, hlgookshnt. I was going to pick up a big wood but I was too weak and I couldn't."}
{"headword": "alda", "definition": "noun fir tree\n-Alda hoy gyad hlat dsaba waab. People use fir to build a house."}
{"headword": "algyack", "definition": "noun; verb spoken or written word; to speak, talk\n-Aam wila how liplaid hla algyackd. The preacher sounds good when he speaks."}
{"headword": "algyackshg", "definition": "noun big man, Chief, noble\n-Wun algyackshg a tcka'nee ggaldsapdsap. There are nobles in every village.\n(-) Lu'kwil algyackshga Shm'oygit. The chief was a very big man."}
{"headword": "aloobaa", "definition": "verb to run fast\n(-).Lu'kwil aloobaa hlguwoamhlg. The child ran very fast."}
{"headword": "amadaalck", "definition": "verb to praise, show respect\n-Amadaalckd melee na hlguhlgm 'yoot. Mary was full of praise for her son."}
{"headword": "amadsab", "definition": "verb to be completed, well-designed, well-proportioned; to do over, fix, repair\n-Amadsaba wila waal goa dm wila gyoayu. What I do will be well designed."}
{"headword": "ama gyad", "definition": "verb to be kind\n-Anoacku shga ama gyada 'yoota gwee. I like the way that man is very kind."}
{"headword": "amane'ets", "definition": "verb to be careful, cautious, watchful\n-Amaneedsin nda wil yaan. Be careful of where you walk.\n-Amaneedsn wila gyoan, ahlga dm dee shgaaygshgn. Watch what you're doing, it's not good that you get hurt also."}
{"headword": "Ama shu'goahl", "definition": "phrase Happy New Year\n-Ama shu'goahl. Happy New Year."}
{"headword": "amawaal", "definition": "verb to be rich, wealthy\n-Ha'wahlgadee amawaalu. I'm not wealthy yet.\n-Amawaal 'yoota gwee, hailda daalat. That man is wealthy, he has a lot of money."}
{"headword": "ama'bash", "definition": "verb to be beautiful, good looking, handsome, pretty PLURAL: amamacksh\n-Lu'gwil ama'basht Dan. Dan is very handsome.\n-Na needsu hlgu hana'ack da lack geeka, dowl lu'kwil ama'basha wila dsabt hla yaat. I saw a woman on the beach and she looked pretty when she walked."}
{"headword": "ameelg", "definition": "noun disguise, effigy, mask\n-Goahl wilsh ameelga hoyan? What mask are you wearing?"}
{"headword": "amgeeg", "definition": "noun black duck\n-Hailda amgeeg wil ggaldsoackum. There are a lot of black ducks where we camped."}
{"headword": "amggan", "definition": "noun red cedar\n-Amggan hoy gyad hlat dsaba p'tsaan. People use red cedar to make a totem pole."}
{"headword": "amhow", "definition": "noun voice\n-Hoyska amhowsh Debbie hla leemeet. Debbie's voice is beautiful when she sings."}
{"headword": "amooksh", "definition": "verb to listen, obey, pay attention\n-Amookshn hla wil algyacka Shm'oygit. Listen when the Chief speaks."}
{"headword": "amoosh", "definition": "noun corner of house\n-Shguu ha'li'daa da amoosha waab. Put the chair in the corner of the house."}
{"headword": "am'baal", "definition": "noun cottonwood tree\n-Am'baal hoyu da waab shi'biyaanshg. I used cottonwood in the smokehouse."}
{"headword": "anaash", "definition": "noun hide, skin Plural: ak'anaash\n-Wok 'dsack'dsackga na anaashu. My skin is itchy."}
{"headword": "anaay", "definition": "noun bread\n-Dm geegu anaay da noayu. I am buying some bread for my mom."}
{"headword": "aneesh", "definition": "noun tree branch\n-'Gwasha aneesha ggan wil 'tsuu baashg. The tree branch broke during the strong wind."}
{"headword": "anoagg", "definition": "verb to agree, allow, give permission; to like\n-Anoaggu dm hee ggaldmwa'atn. I give you permission to go to the store."}
{"headword": "anoahl", "definition": "verb to allow, let\n-Ahlgadeet anoahl dm 'dseen doosh. She didn't let the cat come in."}
{"headword": "an'on", "definition": "noun arm, hand Plural:gga'an'on\n-'Woamckga an'Onu. My arm is aching."}
{"headword": "aplugawdee", "definition": "verb to empty, make empty\n-Aplugawdee ggaldm moan. The salt container is empty.\n(-) Na 'kwihl yaa'nu da guyna da lugawdee aksh dm 'kenu, luyeltgu. I walked around the street and my water ran out, I went back. apluGAWdee"}
{"headword": "ash", "definition": "noun soapberries\n-Yagwa gubu ash. I am eating soapberries."}
{"headword": "ashdee", "definition": "prefix to make a mistake\n-Ashdee waalu hlan geega shu 'dsig'dsig. I made a mistake when I bought a new car."}
{"headword": "ashdeewaal", "definition": "verb to have an accident, make a mistake\n-Giloa ashdee waaln. Nee gyad wila gyoan. Don't make mistakes. People see what you're doing."}
{"headword": "ashee", "definition": "noun foot, leg Plural: ggashishee\n-Shgaaygshga asheeyu. I foot hurts."}
{"headword": "ashguu", "definition": "verb to be funny, humorous\n-Ashguu hlgu hash. The little dog was funny.\n-Na 'dsilaayu nabeebu da up lu'kwil ashguu wila gyoad. I visited my uncle and he was really funny."}
{"headword": "ashgyaback", "definition": "noun chatterbox\n-Du! lu'kwil ashgyabacka 'yoota gwee. Good grief! That man is really a chatterbox."}
{"headword": "ashwn", "definition": "noun sea urchin\n-Gilmt nabeebu ashwn da 'koy ada lu'kwil 'tsamaatgt. My uncle gave me sea urchin and it was very tasty."}
{"headword": "awaa", "definition": "particle at, by, near\n-'Daan da lack ha'li'daa da awaa likshoack. Sit on the chair by the door."}
{"headword": "awaan", "definition": "particle there\n-Shguu ha'li'dameesh da awaan. Put the table there."}
{"headword": "A-wil goa?", "definition": "interrogative why?\n-A-wil goa, dayat noat. Her mother said, why?"}
{"headword": "awsh", "definition": "noun sand\n-'Yagayaayu da geeka, 'waa wil awsh, da 'nee nwil giguul gaboack. I went down the beach, found sand, that's where I looked for cockles."}
{"headword": "awta", "definition": "noun porcupine\n-Ha'wahlgandee neehh awta. I haven't seen a porcupine."}
{"headword": "awul", "definition": "prefix aside, away\n-Awul gushga gganaow a lack guyna. The frog jumped away from the road."}
{"headword": "awul'mag", "definition": "verb to put aside, put away; to sidetrack\n-Ndm awul'maga hoan. I'm going to put the fish aside."}
{"headword": "aw'awshg", "definition": "verb to be curly\n(-).•u'kwil hashacku aw'awshgm ggowsh. I really want curly hair."}
{"headword": "ayaaltg", "definition": "verb to be fortunate, lucky\n-Ayaattga'nm, 'needee? We're lucky, aren't we?\n-Na oom hoanu ashda 'guulda shada dowl lu'kwil ayaaltgn, da'ackga 'wee yeeh. I was fishing the one day and you were lucky to catch a big King Salmon."}
{"headword": "ayaawgg", "definition": "noun decree, message, official statement\n-Ayaawgga Shm'oygit da wila waal shahoan. The Chief gave an official statement about the fishing."}
{"headword": "ayam", "definition": "verb to throw, pitch\n-Ayam oy hla'at. Pitch the ball."}
{"headword": "ayamgwai", "definition": "particle almost there\n-Hla ayamgwai 'dsig'dsig. The car is almost there."}
{"headword": "ayamgwa'a", "definition": "particle almost here\n-Hla ayamgwa'a boad. The boat is almost here."}
{"headword": "ayawaa", "definition": "verb to shout, yell PLURAL: ayaluwaa\n-Ayawaa hlguwoamhlg hlat needsu. The child cried out when he saw me."}
{"headword": "ayin", "definition": "interjection no, not so\n-Ayin. ahlgadee hashacku uushgmlaan. No. I don't want stink eggs."}
{"headword": "ayow", "definition": "interjection expression when sighting fish jump\n-Ayow! Daya gyad hlat nee wil gusha hoan. aYOW! That's what people say when they see fish jump."}
{"headword": "aytk", "definition": "verb to name, call by name PLURAL: ak'aitk\n-Wie aam dm aytga na waam 'Tsmshiant. It is time to call her by her 'TsmSHIAN name."}
{"headword": "ayuwaan", "definition": "verb to stay away for a long time\n-Giloa ayuwaan Don't stay away."}
{"headword": "a'waa'ackshg", "definition": "verb to be a hard worker, industrious\n(-) Lu'kwil a'waa'ackshgat Da'apsh. David is very industrious.\n-Lu'kwil a'waa'ackshga 'yoota gwee dumt wilaay dm hadiksh. That man is working hard to learn how to swim."}
{"headword": "baa", "definition": "verb to run Plural: 'kahl\n-Baa hlgu hash hla hashackt dm galmeelgt. The little dog runs when it wants to play."}
{"headword": "baahlk", "definition": "noun operation, surgery\n-Ahl sheepga wil baahlgn? Does it hurt where you got operated?"}
{"headword": "baal", "definition": "verb to feel; to try, venture Plural: bubaal\n-Baaldu ndm guba shameeym ol - ahlgandee anoackt. I tried to eat bear meat - I don't like it."}
{"headword": "baal'ack", "definition": "noun corpse, ghost Plural: bibaal'ack\n-Baasha'nu ndm needsu baal'ack. I'm afraid to see a ghost."}
{"headword": "baash", "definition": "verb to be afraid Plural: lebaash\n-Baasha doosh hlat nee hash. The cat was afraid when it saw the dog.\n-Baashu da wila waal ggoadu, mahla doctor shgu dumt dsabt. I was afraid of how my heart was, the doctor said I had to have it fixed."}
{"headword": "baashg", "definition": "verb; noun to blow; wind\n-Gatgyeda baashg wil hultga giamg. The wind is strong when the moon is full.\n(-) Na dm hee Gitsgaanu ashda 'guulda sha ggal 'dsuu baashg dowla giloam. I was going to Ketchikan one day and the wind blew too hard so we quit."}
{"headword": "babaa", "definition": "verb quiver (of the chin), tremble\n(-) Lu'kwil babaa hlgu ahlyeeggawsh. The little hummingbird really trembled."}
{"headword": "babood", "definition": "verb to wait, await\n-Giloa aba'ackshgn, baboodee. Don't be anxious, wait for me.\n-Baboodee. Wait for me.\n-Baboodihla boad. Wait for the boat."}
{"headword": "back", "definition": "verb to taste\n-Backu shameeym ol - ahlgandee anoackt. I tasted bear meat - I don't like it."}
{"headword": "backbeega'aksh", "definition": "noun gale, waterspout\n-Backbeega'aksh ashda gi'dseeb. There was a strong gale yesterday."}
{"headword": "backyaa", "definition": "verb to go, move, walk up along the ground PLURAL: backwaalcksh\n-Dm backyaam da awaa lack 'daa dm guul maay. We're going to walk up to the lake to gather berries."}
{"headword": "bads", "definition": "verb to lift\n-Badsa ha'li'daa ada 'dooshgn da na hluut. Lift the chair and sweep under it."}
{"headword": "badsg", "definition": "verb to arrive, land\n-Hla badsga 'yoota gwee dowl awaayu wil goyt. The man arrived and came to me."}
{"headword": "baloash", "definition": "noun syrup\n-Baloasha hoyu hlan guba ai'dsum anaay. I use syrup when I eat fried bread.\n-Da'ackgu ndm ksha guba baloash. I can just eat syrup by itself."}
{"headword": "ban", "definition": "noun abdomen, belly, stomach, tummy\n-Sheepga banu hlan guba ggal hailda anaay. My tummy hurts when I eat too much bread."}
{"headword": "bana", "definition": "noun dip net, net brail\n-Bana hoy gyad wil hailda hoan. People use a dip net when there are lots of fish."}
{"headword": "bashackg", "definition": "verb to be divided\n-Bashackga hla'ashg da lack loab. Divide up the seaweed on the rock.\n-Labite hlikhloontee gyad dowl bashackghl goa wila waalt. The people got angry then they get divided."}
{"headword": "bayck", "definition": "verb to tear, pull bark from cedar tree\n-Ahlgandee da'ackhlga ndm baycka ggan. I'm not able to tear the bark from the tree."}
{"headword": "bayckggan", "definition": "verb gather cedar bark\n-Shguu dm bayckggm da dsigi'dseeb. We have to gather cedar bark tomorrow."}
{"headword": "ba'a", "definition": "noun father\n-Needsu ba'an da awaa waab shgool. I saw your father by the school."}
{"headword": "beeb", "definition": "noun uncle\n-Yagwa goom leetsgut nabeebu. My uncle is hunting for grouse."}
{"headword": "bee'eg", "definition": "noun falsehood, lie\n-Giloa bee'egn. Don't lie."}
{"headword": "beyaalsh", "definition": "noun star\n-Lu'kwil goi'pa beyaalsha gwee. That star is very bright."}
{"headword": "beyaalshm aatk", "definition": "noun evening star\n-Ha'weenhl needsinee beyaalshm aatk? Haven't you seen the evening star?"}
{"headword": "beyaalshm gganhlaag", "definition": "noun morning star\n-Ha'weenhl needsinee beyaalshm gganhlaag? Haven't you seen the morning star?"}
{"headword": "be'an", "definition": "noun meadowlark; songbird\n-Ama'basha na leemee hlgu be'an. The meadowlark makes pretty music."}
{"headword": "bilaan", "definition": "noun belt\n-Hashacku shu bilaan. I want a new belt."}
{"headword": "bilagg", "definition": "noun moss\n(-)-Lu'kwil goamtga bilagg. The moss is very soft."}
{"headword": "bilha", "definition": "noun abalone\n-Ggal hailda gyada en guguul bilha. Too many people are searching for abalone."}
{"headword": "bishboosh", "definition": "verb to chop, split wood\n-Bishboosha ggan gwa'a, ggal 'weelaeksht. Chop up this wood, it's too big.\n-Dm bishbooshu ggan gwee dm shalagshu. I'm going to chop that wood to build a fire."}
{"headword": "biyaackl", "definition": "noun cliff, rock wall\n-Shee'nu wil tgineeetsgu da biyaackl. I was dizzy when I looked down the cliff."}
{"headword": "boad", "definition": "noun boat\n-Dm kshagyoatguu da Ta'gwaan da 'dsm boad. I am going to Metlakatla by boat."}
{"headword": "booboo", "definition": "verb to fall, splash\n-Giloammdz anoacka dm booboo aksh. Don't let the water splash."}
{"headword": "boods", "definition": "noun boots\n-Guguul na boodsu. Look for my boots."}
{"headword": "boosh", "definition": "verb to split, to chop\n-Ahlgandee bishboosha lag awil 'gwaatga na gigyoatgu. I didn't chop the wood because my axe is lost."}
{"headword": "booyshg", "definition": "verb to expect, hope for, wait for\n-Booyshga hlguwoamhlg na noat. The child waited for his mother.\n-Hla booyshgu dm goidiksha hoan. I'm waiting for the fish to come."}
{"headword": "boo'ihl", "definition": "verb to get out of the way; to make aware, warn\n-Ama nee wila yaan. Hla goidiksha 'dsig'dsig, aam boo'ishgn. Be careful where you walk. The car's going to come, you should get out of the way.\n-Boo'ihla 'dsig'dsig dsihla hloat. Be aware of the car if it's fast."}
{"headword": "bou'ish", "definition": "noun monkey\n-Nda bou'ish da Macklackaahla? Where are the monkeys in Metlakatla?"}
{"headword": "ckaa", "definition": "noun slave\n-Hlgu ckaa en shakshen waab. The slave cleaned the house."}
{"headword": "ckaatg", "definition": "verb to spoil, decay\n-Ooshga ckaatgm wineaya. Decayed food smells bad."}
{"headword": "ckaaytg", "definition": "verb to turn over, upset (of a canoe or boat)\n(-)-Lu'kwil baasha'nu dm ckaaytga boad. I'm afraid that the boat will turn over."}
{"headword": "ckaldaawckg", "definition": "noun medicine\n-Aam guba ckaldaawckga 'gilmsh noan, sha damoatgn. It's good to eat the medicine your mother gave you, it will save you."}
{"headword": "ckaygg", "definition": "noun foam\n-Ahl needsinee wil 'tsuu ckaygg da hahl-geeka? Have you see where there's a lot of foam down the beach?"}
{"headword": "ckbaala", "definition": "noun west wind\n-Tcka'nooyu dm gatgyada ckbaala dsigi'dseeb. I heard that the west wind will be strong tomorrow."}
{"headword": "ckbaickshg", "definition": "verb to saw\n-Ha'weenhl ckbaickshgt George taggan? Hasn't George sawed the planks yet?"}
{"headword": "ckbashm 'ka'kackd", "definition": "particle upside down\n-Geedsa ckbashm 'ka'kackda ckshoa da wil 'tsuu baashg. The canoe almost turned upside down because of the strong wind."}
{"headword": "ckbeesh", "definition": "noun box\n-'Kacka 'ka 'weelaekshm ckbeesh. Open the bigger box."}
{"headword": "ckbeeyaa", "definition": "verb to deliver information; to walk house to house\n-Ckbeeyaa 'yoota hla wil goidiksha uua. The man delivered information about the arrival of the ooligans."}
{"headword": "ckbeeyay", "definition": "noun half, part of\n-Na goo wunu ashda 'guulda sha, goo wun, da 'gilmu ckbeeyay da hlguyu. I went hunting one day, shot the deer, and I gave half of it to my children."}
{"headword": "ckbishmshguu", "definition": "verb to bend, bend over, bow\n-Ckbishmshguu gyada na 'dmggowshd hla gigeengwackhld. People bow their heads when they pray.\n-Na ckbishmshguu n'dse'etsu hla weehowtgd. My grandmother bent over when she cried."}
{"headword": "ckdaiksh", "definition": "verb to eat Indian ice cream\n-Aba'ackshgu dm wil yaa maadm awil lu'kwil anoacku ckdaiksh. I'm anxious for the snow to fall because I really like Indian ice cream."}
{"headword": "ckdee", "definition": "verb to eat with\n-Dm ckdeeym wilaayshgm dsihla Ha'li Shgwaitga sha. We're going to eat with our relatives on Sunday."}
{"headword": "ckdsee", "definition": "verb to be thick (ice, board, fog, etc.)\n-Hagwil baa boad da wil ckdsee yain. The boat ran slowly when the fog was thick."}
{"headword": "ckdso'otsk", "definition": "noun hawk\n-Ahlgandee neehl ckdso'otsk shga 'naga wil ggaldsockm. I haven't seen a hawk since we've been at our camp."}
{"headword": "ckgwatksh", "definition": "verb feel cold\n-Lu'kwil ckgwatksha 'woa'da gyad. Elderly people really feel cold."}
{"headword": "ckhoan", "definition": "verb to eat fish\n-Wiedsa ckhoanm. Let's eat fish."}
{"headword": "ckleeuu", "definition": "verb to burst PLURAL: ggackleeuu\n-Aba'ackshga hana'ack wil ckleeuu hla'at. The woman got anxious when the ball burst.\n-Ggal 'dsuu wila yaawckgn dowla dm ckleeuu na ggaloashn. If you eat too much your stomach will burst."}
{"headword": "cklggoan", "definition": "verb to pay\n-Ayinhl dm cklggoant 'need? Aren't you going to pay him?"}
{"headword": "cklggoa'oam", "definition": "noun payment\n-Naahl dm en cklggoam da ckshoa? Who will pay us for the canoe?"}
{"headword": "ckshaan", "definition": "noun mosquito larvae\n-Shguu mdm kwhlee dsaga ckshaan. We need to kill all of the mosquito larvae."}
{"headword": "ckshaangg", "definition": "verb to disagree, disbelieve, doubt\n-Ckshaanga'nu goa wila how 'yoota gwee. I disagree with what that man said."}
{"headword": "ckshan", "definition": "verb to gamble\n-Ahlgadee aam ckshan gyad. It's not good for people to gamble."}
{"headword": "ckshdaa", "definition": "verb to win (a game, war)\n-Dsida ahlgadee ayaaltgn, ahlga dm ckshdaan. If you're not lucky you won't win."}
{"headword": "ckshdaamck", "definition": "verb to make a loud noise\n-Lu'kwil ckshdaamcka gga'bala. The gun made a very loud noise."}
{"headword": "cksheet", "definition": "verb to vomit PLURAL: lacksheet\n-Cksheeta hlguwoamhlg da ggal 'naga weehowtgt. The child vomited from crying too long."}
{"headword": "ckshgeeg", "definition": "noun eagle\n-Hailda ckshgeeg da wil 'daam. There are lots of eagles where we are."}
{"headword": "ckshwa'dackg", "definition": "noun whistle\n-Ckshwa'dackga 'yoota hlat nee ama'bashm hana'ack. The man whistled when he saw a beautiful woman."}
{"headword": "cksh'dock", "definition": "verb to sleep\n-Ggal giamga waab, 'nee gun geedsa cksh'docku. The house was too warm, that's why I almost fell asleep."}
{"headword": "cksh'waanck", "definition": "noun herring eggs\n-Eh! 'Tsamaatga cksh'waanck 'gilm gyad 'kam. Oh boy! The herring eggs that people gave us tastes very good"}
{"headword": "ck'biyaan", "definition": "verb to smoke tobacco\n-Ahlgadee aam dm ck'biyaan gyad. It's not good for people to smoke."}
{"headword": "daahl", "definition": "vocative dear miss or woman\n-Daahl, dm shm amooksha'nu da 'kwan. Dear Miss, I'm really going to listen to you."}
{"headword": "daala", "definition": "noun money\n-Giloamdsa 'gwaatga na daalan. Don't lose your money."}
{"headword": "daalck", "definition": "verb to advise, counsel; to rebuke, scold, talk to in a mean manner\n-Shm ama 'daa hlguwoamhlg hlat daalckat noat. The child sat still when his mother scolded him.\n-Na didaalcku hlguhlgm hana'ack goa dm wila gyoat. I advised my daughter about what she should do."}
{"headword": "daamshack", "definition": "verb to faint, pass out Plural:dmdaamshack\n-Geedsa daamshacka hana'ack hlat nee shgaboo daala. The woman almost fainted when she saw how much money there was."}
{"headword": "daaw", "definition": "noun; verb ice; to freeze plural: dudaaw\n-A-yaaltgm sha gya'wn. Da'ackhlgm dm sha daaw wineayam. We're lucky today. We are able to freeze our food."}
{"headword": "daayksh", "definition": "noun Indian ice cream\n-'Guulda waalm da 'nak doashda, dat Peter Fawcett, Peter Wesley 'nahowyu, dsaba daayksh da 'kam, da up oa, wilaay 'yoota gwee dsabt. This is one thing we did, Peter Fawcett, I mean Peter Wesley, made Indian ice cream, and oh boy, that man really knew how to make it."}
{"headword": "dackhl", "definition": "noun hammer\n(-)'Gwaatga na dackhlu. My hammer is lost."}
{"headword": "dacksh", "definition": "noun flounder\n-Anoacka umsheewa dacksh. White men like flounder."}
{"headword": "dackshmhietk", "definition": "verb to stand still\n-Dackshmhietga hlgu hash hlat tcka'noo wil ckshwa'dackga 'yoota. The dog stood still when he heard the man's whistle."}
{"headword": "dackshm'daa", "definition": "verb to obey, sit still; to stay at home PLURAL: dackshmwun\n-Shguu dm dackshm'daan ada amookshn da wil howsh noan. You should sit still and listen to what your mother has to say."}
{"headword": "dackyaagw", "definition": "verb to hold, hold fast, hold tight\n-Dackyagwa hagwilhoo. Hold the rope tight."}
{"headword": "dackya'wa", "definition": "verb to grip, hold\n-Wie dackya'wa an'onu. Labiet shoonsha'nu. Take a hold of my arms. I'm blind."}
{"headword": "daintg", "definition": "verb to lead\n-Aam sha daintgu. Lead me."}
{"headword": "dakhl", "definition": "verb to tie, tie around\n-Dakhla hagwilhoo da kwduun ckbeesh. Tie the rope around the box."}
{"headword": "dal", "definition": "noun; verb fight, conflict; to fight Plural: dildal\n-Hladm dildal hashhaasha gwee. Those dogs are going to fight."}
{"headword": "dalbikshg", "definition": "verb to shrink\n-Dalbikshga hoaya dsida ggal giamga aksh. The clothes shrink if the water's too warm."}
{"headword": "dalpg", "definition": "verb to be short PLURAL: dildalpg\n-Ggal dalpga taggan 'kotsu. The plank I cut is too short.\n-Dalpga wila waal 'yoota gwee. It's a short ways to where the man is."}
{"headword": "dalpgm gganggan", "definition": "phrase short trees\n-Ahlgandm 'kotsa dalpgm gganggan. I'm not going to cut the short trees."}
{"headword": "dam", "definition": "verb to hold, hug, squeeze\n-Ludamsh peda hlgu hasht hlat 'waayt. Peter hugged his dog when it was found."}
{"headword": "damckg", "definition": "verb to be taut, tight\n-Damckga ha'li 'yackgu. My clothes line is tight.\n-Na hailda goa na gubu da 'wee damckga na ggal'oashu. I ate too many things then my stomach was tight."}
{"headword": "damckhl", "definition": "noun friend\n-Dm 'gilmu madsiggalay da damckhlu. I'm going to give my friend a flower."}
{"headword": "damoatg", "definition": "verb to save\n-Aam dm damoatgm na algyackm. It's good to save our language."}
{"headword": "damshg", "definition": "verb to hold, squeeze\n-Giloamdsa damshga hoan. Don't squeeze the fish."}
{"headword": "damtee", "definition": "noun fern-like plants\n-Dup 'leedoaym hoan da lack damtee. We put the fish on the fern (leaves)."}
{"headword": "dap", "definition": "noun; verb liver; to judge, try in court, measure\n-Dm dapmt lalee. We're going to judge Larry."}
{"headword": "dashgyan", "definition": "noun emery wheel, whet stone\n-Hashacku shu dashgyan. I want a new whet stone."}
{"headword": "daway", "definition": "noun goat\n-Ahlgandee gubhl daway, 'nee gn ahlgandee wilaayhl goahl dm wil howyu da gwa'a. I've never eaten goat, that's why I don't know what to say about it."}
{"headword": "dawhl", "definition": "verb to depart, go away, leave\n-Sha gya'win dm wil dawhlsh Dzon da Macklackaahla. John will leave for Metlakatla today.\n-Na dawhla hlguhlgu da Gitsgaan. My child left for Ketchikan."}
{"headword": "dawhln", "definition": "verb to go away\n-Ndahl dm wil daawhln da Gitsgaan? When are you going away to Ketchikan?"}
{"headword": "da'ackhlg", "definition": "verb can, to be able\n-Da'ackhlgu ndm dsaba waabm hash. I am able to make a dog house."}
{"headword": "da'ash", "definition": "noun aunt\n-Dm 'gilmu hoan da da'shu. I'm giving fish to my aunt."}
{"headword": "da'ka'aaw", "definition": "noun sea anemone\n-Ahl 'waayanee da'ka'aaw? Have you found any sea anemone?"}
{"headword": "da'oack", "definition": "noun cheek\n-Hashacku ndm gyehla hlgu da'oackn. I want to poke your little cheeks."}
{"headword": "debaa", "definition": "verb to run away with\n-Wiedsa dp debaa boad ada gwin daawhlm da Gitsgaan. Lets run away with the boat and go over to Ketchikan."}
{"headword": "debeesh", "definition": "noun agility, performance, poise\n-Lu'kwil debeesha 'yoota hla meelgd. His dancing was done with poise."}
{"headword": "deckhlga giamg", "definition": "noun halo around the moon\n-Shanaahlga wil deckhlga giamg. The halo around the moon is amazing."}
{"headword": "dedsa'bil", "definition": "verb to play with compulsively\n-Giloama dedsa'bil na ggawshn. Don't play compulsively with your hair."}
{"headword": "dee", "definition": "noun hill\n-Lack dee awaan wil wun wun. The deer can be found on the hill there."}
{"headword": "deelmckg", "definition": "verb to answer, reply\n-Goahl gn ahlgadee deelumckgt? Why didn't she answer?\n-Na guuduckdu hlguwoamhlga gwee goa wila gyoat dowla deelmckgt da 'koy. I asked the child what she was doing and she answered me."}
{"headword": "deeltg", "definition": "verb to retaliate, take revenge\n(-).Lu'kwil hashacka 'yoota dm deeltgd. The man really wanted to take revenge."}
{"headword": "deetck'aksh", "definition": "noun high tide\n-Dm gwindaawhlm da Gitsgaan dsihla deetck'aksh. We'll go over to Ketchikan when the tide is high."}
{"headword": "de'kwun", "definition": "verb to be very ripe\n-Ha'weenhl de'kwun moalksh? Aren't the crabapple ripe yet?"}
{"headword": "diboygid", "definition": "noun shrew, small mouse\n-Na ggalmeelgm da lack geeka dowl dsaggabaa hlgu diboygid. We were playing down on the beach when a little mouse ran across."}
{"headword": "didoa", "definition": "verb to have, own Plural:doa\n-Didoa hailda 'dsoacksh da 'koy. I own a lot of shoes.\n-Doa hailda ggaid da 'koy. I own lots of hats."}
{"headword": "didoolsh", "definition": "verb to be alive\n-Hloula didoolsha hlgu 'yoota. The young man is still alive.\n-Na goo wunu ashda 'guulda sha, goo wun. Hloula didoolsht hla gwn ackgu da awaat. I went hunting one day and I shot a deer. It was still alive when I got there."}
{"headword": "dihl", "definition": "conjunction and\n-Hla goamshm dihl magwa'ala dihl goaym. In the early winter, the late winter, and in the spring."}
{"headword": "dipckan", "definition": "noun stump, old tree still standing\n-Hloula hietga dipckan. That old cedar stump is still standing."}
{"headword": "di'deeld", "definition": "verb to do faster, quickly\n-Di'deelda hahlalsha'nm hla hashackum dm meelgm. We do things faster when we want to dance."}
{"headword": "doashda", "definition": "noun across the way, the opposite side\n-Doashda wil wun hailda gibaaw. There are a lot of wolves across the way."}
{"headword": "doa'yil", "definition": "noun spoiled person\n-Doa'yil hlguwoamhlg, 'neegn 'naga weehawtgd. The child is spoiled, that's why she cries a long time."}
{"headword": "dock", "definition": "verb to carry, take\n-Shgu dm dockm lag. We have to take wood.\n-Hee Gitsgaanu ashda 'guulda sha dowlan docka wineayam. I went to Ketchikan the other day and I took our food."}
{"headword": "dockdock", "definition": "verb to hold on to\n-Shguu mdm dockdocka hagwilhoo dsihla 'dsuu baashg. You have to hold on to the rope when the wind blows hard."}
{"headword": "doohlk", "definition": "noun cedar bark basket\n-Lu'kwil ama'basha doohlk dsabs maata. Martha makes beautiful cedar bark baskets."}
{"headword": "doola", "definition": "noun tongue\n-Ahlgandee wilaayhl goahl gn geetga na doolayu. I don't know why my tongue is swollen."}
{"headword": "doolckg", "definition": "verb to be stuck, unable to travel\n-Doolckga'nu da Gitsgaan da wil haackga lacka. I got stuck in Ketchikan when the weather was bad.\n-Na dm goyu Ta'gwaan da bite doolckga'nu. I was going to go to Metlakatla but I got stuck."}
{"headword": "doosh", "definition": "noun cat Plural:dikdoosh\n-Needsu hash ada doosh. I see a dog and a cat."}
{"headword": "dooshm gilhawli", "definition": "noun tiger, wildcat\n-Ha'wahlgndee nee dooshm gilhawli. We've never seen a tiger."}
{"headword": "doycksh", "definition": "verb to be built strong; to put on warm clothes\n-Doyckshn, gwatga gyalgg. Dress warm, it's cold outside."}
{"headword": "doyksh", "definition": "noun rapids, strong tide\n-Doyksha aksh da awaa 'wee loaba gwee. The rapids are strong by that big rock."}
{"headword": "dsaam", "definition": "noun jam\n-Hoyu dsaam da lack anaay. I use jam on my bread."}
{"headword": "dsab", "definition": "verb to build, construct, make\n-Goadu ap dee dsabn? What work do you do?\n(-)Lu'kwil wilaay 'yoota gwee dsaba p'tsaan. That man really knows how to make a totem pole."}
{"headword": "dsadaawhl", "definition": "adverb tonight\n-Wiedsa shuwil'leenm dsadaawhl. Let's go hunting tonight."}
{"headword": "dsag", "definition": "verb to die, be dead PLURAL:duu\n-Dsaga wun. The deer died.\n-Labite waal wila gyoa hlgu doosha gwee dowla dsagt. That little cat made a mistake and so it died."}
{"headword": "dsaggabaashg", "definition": "noun crosswind\n-'Tsuu dsaggabaashg da lackshuulda The cross wind was very strong on the ocean."}
{"headword": "dsagga-tgubaa", "definition": "verb to spin, run in circle\n-Dsagga-tgubaa hash hlat shuwileen hlgu doosh. The dog ran in a circle when it chased the little cat."}
{"headword": "dsaggayaa", "definition": "verb to walk across\n-Dm dsaggayaa'nu da awaa ggaldmwa'at. I'm going to walk across to the store."}
{"headword": "dsagga'acklg", "definition": "verb to be able to go across\n-Dsagga'acklga'nu da 'wee guyna. I made it across the big street."}
{"headword": "dsaggm", "definition": "prefix ashore, inland\n-Dm dsaggm yeltgish dup gwa'a. They will return to shore."}
{"headword": "dsaggmbaashg", "definition": "noun onshore wind\n(-).Lu'kwil ggatgyada dsaggmbaashg. The onshore wind is very strong."}
{"headword": "dsaggmdaawhl", "definition": "verb to go ashore\n-Hladm dsaggmdaawhla ckshoa. The canoe will be going towards shore."}
{"headword": "dsagmwaash", "definition": "noun south wind\n-Ahl ggatgyadee dsagmwaash? Is the south wind strong?"}
{"headword": "dsahl", "definition": "verb to consume; to lose a game, war; to be consumed\n-Dsahlu tcka'nee wineaya 'nee gn ggal 'dsaayu. I finished all the food that's why I'm full.\n-Galmeelgm ashda 'guulda sha da dsahlu. I was playing the other day and I lost."}
{"headword": "dsakshuld", "definition": "verb to dampen; to sprinkle\n-Dsakshulda hoayan nagoacka mdm aidsd. Dampen the clothes before you iron them."}
{"headword": "dsalee", "definition": "noun old fish\n-Ahlgadee hashackee dsalee. I don't want an old fish."}
{"headword": "dsam", "definition": "verb to boil, cook\n-Dm dsamu hlgumad. I'm going to boil an egg.\n-Na gidigaadu 'wee hoan dowla dsam noayu dm gubm. I caught a big fish and my mother cooked it for us to eat."}
{"headword": "dsawush", "definition": "noun laughing berries, salal berries\n-Wilaay nakshu dsaba dsawush. 'Nee hoym da anaay. My wife knows how to fix laughing berries. That's what we have on bread."}
{"headword": "dsayaihl", "definition": "noun snare, trap\n-'Gwaatga dsayaihlm. Our traps are lost."}
{"headword": "dsaygg", "definition": "noun gray berries along river bank\n-Ahlgandee anoacka dsaygg. I don't like gray berries."}
{"headword": "dsa'bl", "definition": "verb to handle, play with compulsively\n-Ahlgadee aam dm dsa'bl hahlibeeshk, ahlgadee aam da 'kwan. It's not good to play with a knife, it's not good for you."}
{"headword": "dsa'ee", "definition": "interjection expression used for calling down one who is doing badly\n-Dsa'ee! Ama nee wila gyoan. Good grief! Watch what you're doing."}
{"headword": "dseeb", "definition": "verb to defrost, melt, disappear, lose weight or size\n-Dseeba daaw dsihla ggal gyamg. The ice melts when it's too warm."}
{"headword": "dseehl", "definition": "noun snipe\n-'Tsuushgm 'dsu'utsa dseehl. Snipe is a little bird."}
{"headword": "dseehldoa", "definition": "verb to put away in a corner\n-Dseehldoa ckbeesh da 'dsm gi'dsoan. Put the box in the corner of the closet."}
{"headword": "dseekshhawtksh", "definition": "verb to brag a lot\n-Ggal dseekshhawtksha 'yoota gwee. The man over there brags too much.\n-Shoonaahla'nu da wila dseekshhawtksha hana'acka gwee. I'm tired of how that woman brags so much."}
{"headword": "dseekshhietksh", "definition": "verb to stand smartly\n-Shm dseekshhietksha 'yik'yoota wil algyacka Shm'oygit. The men stood still when the Chief spoke."}
{"headword": "dseekshwaaltksh", "definition": "verb to show off, to strut your stuff\n-Ashguu wil dseekshwaaltksha hlguwoamhlg. The child is humorous when he struts her stuff."}
{"headword": "dseekshyaaksh", "definition": "verb to strut, walk with flair\n-Giloa dseekshyaakshn. Don't strut your stuff."}
{"headword": "dseekwsha", "definition": "verb to bail water (out of a canoe, boat)\n-Dseekwsha aksha da boad. Bail the boat out.\n-Geedsa hultga boad dowla dseekwsha'nu. My boat almost filled up then I bailed it out."}
{"headword": "dseelksh", "definition": "verb to melt\n-Giamg dm endseelkshn daaw. The sun will melt the ice."}
{"headword": "dseewsh", "definition": "noun daylight, daytime\n-Dm ggadaawhlm dsihla dseewsh. We'll leave at daylight."}
{"headword": "dseeyuu", "definition": "noun dolphin, porpoise\n-Ha'wahlgndee shila hadiksha dseeyuu. I haven't swam with a porpoise"}
{"headword": "dse nda?", "definition": "interrogative when?\n-Dse ndahl dm goidiksha boad? When is the boat coming?"}
{"headword": "dse'a", "definition": "noun grandmother\n-Maata na dse'ashu. Martha is my grandmother."}
{"headword": "dse'ish", "definition": "noun grandmother\n-Awaash dse'ishu dm goayu. I'm going to my grandmother's house."}
{"headword": "dsigi'dseeb", "definition": "adverb tomorrow\n-Dm daawhlm dsigi'dseeb. We'll leave tomorrow."}
{"headword": "dsihla", "definition": "prefix at this time, this hour\n-Dm tckoackgm dsihla gwaanksha wineaya. We'll eat at the time the food is done."}
{"headword": "dsi'kwe'eds", "definition": "noun large sea urchin\n-Hladm guuldm dsi'kwe'eds. We're going to harvest sea urchins."}
{"headword": "dsoack", "definition": "1. verb to be ashamed Plural: ledsoack\n-Lu'kwil mashga 'dsalt hla dsoackt. His face is red when he's ashamed.\n-Labite how 'yoota gwee, labite dsoackt goa wila howt. That man made a mistake, he was ashamed of what he said.\n2. verb to reside\n-Ndahl wil dsoacksh Maata? Where does Martha reside?"}
{"headword": "dushck", "definition": "noun squirrel\n-Dm goom dushcku dsihla dsigi'dseeb. I'm going to hunt for squirrel tomorrow."}
{"headword": "duu", "definition": "verb to die, be dead\n-Duu hailda hoan. Lots of fish died.\n-Hailda gyad shipsheepgd dowla duut. Lots of people got sick then died."}
{"headword": "duwaay", "definition": "verb to paddle, row\n-Shguu dm duwaaym ckshoa. We have to paddle the canoe."}
{"headword": "ee", "definition": "interjection oh!\n-Ee! Waalhl gubm. Oh! I wish I could have some."}
{"headword": "eemck", "definition": "noun beard\n-'Naga eemcka 'yoota. The man's beard is long."}
{"headword": "eesh", "definition": "noun yeast\n-Lugowdee ggalm eeshu, shgu ndm gik geegt. My container of yeast is empty, I need to buy it again."}
{"headword": "enta hoan", "definition": "noun fish, canned\n(-)-Lu'kwil 'tsamaatga meeyoob ada enta hoan. Rice and canned fish taste very good."}
{"headword": "gaa", "definition": "verb to take\n-Gaa ckbeesh ada 'gilumt dish noan. Take the box and give it to your mother."}
{"headword": "gaalmck", "definition": "noun Nass-Gitksan language\n-Gaalmck hoy Nishgaa. The Nass River people speak another language."}
{"headword": "gabids", "definition": "noun cabbage\n-Dm dsamu gabids. I'm going to cook some cabbage."}
{"headword": "galmeelg", "definition": "verb to play\n-'Naga galmeelga hlguwoamhlg. The child plays a long time."}
{"headword": "galot", "definition": "noun carrot\n-Yagwa na guba galot. I am eating carrots."}
{"headword": "gatgyetga baashg", "definition": "noun strong wind\n-Giloadsa kshigyoatgn - ggal gatgyetga baashg. Don't depart - the wind is too strong."}
{"headword": "gawdee", "definition": "verb to be done with\n-Lu'kwil kwdee 'yoota gwee 'neegn lugawdee na giehld. That man was very hungry that's why his dish is empty.\n-Gawdee yaawckgu dowla sha'apyaayu. After I ate I went for a walk."}
{"headword": "ga'wa", "definition": "verb to agree, consent\n-Ga'wa'nu hlan tcka'noo wila hawt. I agreed when I heard what he said."}
{"headword": "geedsa", "definition": "prefix almost, just about\n-Geedsa shagienayu. I almost fell down."}
{"headword": "geek", "definition": "noun; verb hemlock (tree or wood); mosquito; to buy; to fly\n-Hailda geek da lack geeka da 'yagayaayu ndm 'kots'kots. Dm hoyu da na waabu dm sha gyamga waabu. There are lots of hemlock down the beach so I'm going to walk down there and cut them up. I use it to warm up my house."}
{"headword": "geeka", "definition": "adverb next to the water, at the water's edge\n-Yagwa sha'dsa'ackm da geeka. We're digging clams next to the water."}
{"headword": "geemg", "definition": "verb to wipe Plural: leemg\n-Hla gawdee tckaoackga gyad - geemga ha'litckoackg. The people are done eating - wipe the table."}
{"headword": "geen", "definition": "verb to give food\n-Wie geenee da anaay. Hla kwdeeyu. Well, give me the bread. I'm hungry."}
{"headword": "geesh", "definition": "verb to err, miss, make a mistake, do something wrong\n-Geesha waalt hlat dsaba gwish'na'ba'la. She made a mistake when sewing the blanket."}
{"headword": "geeshk", "definition": "verb to dodge; miss\n-Ahlgadee daacklga'nu ndm geeshga hla'at. I wasn't able to dodge the ball.\n-Na oyu loab da 'nakshuneeshg dowl labite geeshd. I threw a rock at the window and missed it."}
{"headword": "geetg", "definition": "verb to rise, be swollen\n-Geetga an'onu ada ahlgadee da'acklgu ndm hoy gwishgwashm on'onu My hand is swollen and I can't wear my rings."}
{"headword": "geetga aksh", "definition": "verb to flood\n-Geetga aksh a lack'daa. The lake is flooding."}
{"headword": "ggaagg", "definition": "noun raven\n-Nee wil ggusha 'wee ggaagg da gyalck. See the big raven jumping outside."}
{"headword": "ggaaka", "definition": "verb to be strong\n-Ggaaka hagwilhoo hoyu. The rope I'm using is strong."}
{"headword": "ggaapck", "definition": "verb to scratch\n-Ggaapcka doosha likshoack hla hashact dm 'dseent. The cat scratched the door when it wanted to come in."}
{"headword": "ggaapckan", "definition": "verb to rake, scrape\n-Ggaapckan ggam'do'otsk da 'dsm shdoob. Rake the coals up in the stove."}
{"headword": "ggabackshg", "definition": "verb to jump with fright, shake, be startled\n-Sha ggabackshga'nu wil 'wee'amhow 'yoota. I jumped when the man yelled in a loud voice."}
{"headword": "ggaboack", "definition": "noun cockle\n-Wiedza sha ggaboackm. Let's gather some cockles."}
{"headword": "ggadailpk", "definition": "noun anchor\n-Uksh'oy ggadailpk. Throw out the anchor."}
{"headword": "ggadeeshg", "definition": "verb to braid\n-Naahl en ggadeeshga na ggawshn? Who braided your hair?"}
{"headword": "ggadoahl", "definition": "noun humpback salmon, pink salmon\n-Nee 'wee ggadoahl. Ggal hailda hoan wila waald. See that big humpback salmon. There's lots of fish where it is."}
{"headword": "ggadsaagg", "definition": "noun cross, gable of roof\n-Hida ggadsaagg wila dsaba taggan da lack waab. The lumber on the house looked like a cross."}
{"headword": "ggadsiksh", "definition": "verb down pour\n-Shuulga wila dsaba lacka hla ggadsiksha waash. The sky looks fearful when the rain pours down."}
{"headword": "ggadsikshg", "definition": "verb to rain heavily\n-Giloamdsa 'kotsa kyoack awil ggal ggadsikshga waash. Don't cut the grass because the rain is pouring."}
{"headword": "ggadsiwaald", "definition": "noun fingers\n-'Nik'nuunga ggadsiwaalda hlgu 'yoota. The little boy has long fingers."}
{"headword": "ggag", "definition": "noun swan\n-Ha'wahlgandee nee ggag. I haven't seen a swan."}
{"headword": "ggaggawsh", "definition": "noun antler, horn\n-Nda shgaboo ggaggawsha wun? How many antlers does the deer have?"}
{"headword": "ggaggoack", "definition": "noun fish nose\n-Ha'weenhl backanee ggaggoackm hoan? Haven't you tasted fish nose yet?"}
{"headword": "ggagoom", "definition": "noun seagull\n-Na guguuldm ggagoom da lack loab da wil 'ken hlumad da ahlgadee ap 'waad. We looked for seagulls on the rock to find the eggs but couldn't find any."}
{"headword": "ggahldikshguu", "definition": "verb to lie on one's side\n-Ggahldikshguu hash hla gawdee tckoackgt. The dog laid on his side when he was done eating."}
{"headword": "ggahldikyaa", "definition": "verb to go into the woods; to walk to one side\n-Dm ggahldikyaa'nu da gilhouli. I'm going to walk up in the woods."}
{"headword": "ggahlg", "definition": "verb to string up, put on drying pole\n-Hladm ggahlga'nu hoan. I'm going to string up the fish."}
{"headword": "ggahlggan", "definition": "verb to put on sticks for smoking (as fish, meat)\n-Ggahlggan shamee awil dm guunksht. Put the meat on sticks so it will dry."}
{"headword": "ggahood", "definition": "noun beads on a string, necklace\n-Lu'kwil hoyshga ggahooda hoy hana'ack. The woman is wearing beautiful beads."}
{"headword": "ggaid", "definition": "noun hat\n-Ggal 'weelaeksha ggaidu. My hat is too big."}
{"headword": "ggaida gganaaw", "definition": "noun mushroom\n-Ahlgadee aam naga'tsaaw ggaida gganaaw. Some mushrooms are not good."}
{"headword": "ggaidm boashn", "definition": "noun rimmed hat\n-Ahlgandee anoacka ggaidm boashn hoyn. I don't like the rimmed hat you're wearing."}
{"headword": "ggaidm shgyen", "definition": "noun rain hat\n-Sha 'goa'olsh 'yoo'ock na ggaidm shgyent. The boy forgot his rain hat."}
{"headword": "ggaidm shihoo", "definition": "noun yarn hat\n-Dsabsh n'dse'etsu hailda ggaidm shihoo. My grandmother made many yarn hats."}
{"headword": "ggaidm 'dsagg", "definition": "noun cap\n-Dm 'gilmu ggaidm 'dsagg da nakshu. I'm going to give my husband a cap."}
{"headword": "ggaiggai", "definition": "noun dead tree branch\n-Ama needsn da ggaiggai. Watch out for dead tree branches."}
{"headword": "ggailkshg", "definition": "verb to creep; to sit in protest of moving or going\n-Ggailkshga hlguwoamhlg hla hloonteed. The child crept along when he was angry."}
{"headword": "ggaimggan", "definition": "verb to pry with a lever\n-Shguu mdm kshi ggaimggan 'daa'binshg da ggan. You have to pry the nails out of the wood."}
{"headword": "ggaimgganshk", "definition": "noun oar\n-Giloamdsa 'koa'olda ggaimgganshk. Don't forget the oars."}
{"headword": "ggain", "definition": "noun skunk\n-Lu'kwil ooshga ggain. The skunk is stink."}
{"headword": "ggaklik", "definition": "noun rat, rodent\n-Baasha'nu ndm nee ggaklik. I'm afraid to see a rat."}
{"headword": "ggaksh", "definition": "prefix just started or happened\n-Ggaksh sha'da'ama meelg. The dance just started."}
{"headword": "ggakshwil", "definition": "conjunction that's when, then\n-Hla 'dsilm gawdee gyad 'nee ggakshwil sha'dac'amat. When everyone was in, that's when they started."}
{"headword": "ggakshwil a'aamt", "definition": "verb to get better\n-Ggakshwil a'aamta hana'ack hla wil gigeengwackhla gyad. The woman got better after the people prayed."}
{"headword": "ggal", "definition": "verb; prefix to come, come here; too, also\n-Ggal. Hashacku ndm shilahown. Come here. I want to talk with you."}
{"headword": "ggalaag", "definition": "verb to be cracked; to be crazed\n-Ggalaaga hlgumadm ggaguum da lack kyoack. The seagull egg cracked on the grass."}
{"headword": "ggalaaw", "definition": "noun red cedar tree\n-Ndahl dm wil 'wayy ggalaaw? Where will we find the red cedar trees?"}
{"headword": "ggalbailtg", "definition": "number two boats or canoes\n-Ggalbailtga ckshoa hla badsgt. Two canoes have arrived."}
{"headword": "ggalbash", "definition": "verb to be empty, not there\n-Ggalbasha goack. The basket was empty."}
{"headword": "ggaldm", "definition": "noun container\n-Yoaksha na ggaldm yaawckgn. Wash the container you used for eating."}
{"headword": "ggaldmwa'at", "definition": "noun store\n-Dm kshagyoatga'nj da ggaldmwa'at. I'm going by boat to the store."}
{"headword": "ggaldm'aksh", "definition": "noun bucket, pail, water container\n-Tckayaagwa ggaldm'aksh. Bring the bucket with you."}
{"headword": "ggaldoa", "definition": "noun camp\n-Lu'kwil anoacku ggaldoa gwa'a. I really like this camp."}
{"headword": "ggaldsap", "definition": "noun village\n-Macklackaahla na ggaldsap wil 'waatgu. Metlakatla is the village where I'm from."}
{"headword": "ggaldsock", "definition": "verb to camp\n-Dm ggaldsock'nu shuunta gya'win. I'm going to go camping this summer.\n-Awaa China Town wil ggaldsockm. We went camping at China Town."}
{"headword": "ggaleemksh", "definition": "noun gospel\n-Shmhow na ggaleemksha Shm'oygit ga Lackaga. God's word is the truth."}
{"headword": "ggalgwai'hl", "definition": "noun empty sack\n-Goahl gun ggalgwai'hla gwa'a? Why is this sack empty?"}
{"headword": "ggal haild", "definition": "quantifier too many\n-Ggal hailda gyad da 'dsm boad. There are too many people in the boat."}
{"headword": "ggalipleep", "definition": "noun cannon; thunder\n-Wee howtga hlguwoamhlg hlat tcka'noo ggalipleep. The child cried when she heard the thunder."}
{"headword": "ggalkshaggush", "definition": "verb to jump rope\n-'Naga ggalkshaggusha hlguwoamhlg da gyalck. The child jumped for a long time outside."}
{"headword": "ggalm'algyack", "definition": "noun spokesman\n-Naayu na ggalm'algyacka Shm'oygit? Who is the Chief's spokesperson?"}
{"headword": "ggalooy", "definition": "noun wart\n-Hashacka 'yoota dumt sha 'kotsa ggalooy da an'ont. The man wants to cut the wart off his arm."}
{"headword": "ggalsh", "definition": "noun dried cockles\n-Hashacku ggalsh. I want dried cockles."}
{"headword": "ggalshm", "definition": "interjection come!\n-Ggalshm! Hladm tckoackgm. Come! It's time to eat."}
{"headword": "ggalshm hoa", "definition": "interjection come!\n-Ggalshm hoa! Hladm leemeeym. Come! We're going to sing."}
{"headword": "ggaltsggan", "definition": "number three long objects\n-Ggaltsggan taggan dm geegu ndm ama dsaba guyna. I'm going to buy three planks to fix the street."}
{"headword": "ggaltsggantg", "definition": "number three boats or canoes\n-Ggaltsggantga ckshoa needsu. I see three canoes."}
{"headword": "ggal'dsuu", "definition": "verb to talk, say, claim too much\n-Ggal'dsuu algyacka 'yoota. The man claims too much."}
{"headword": "ggal'kieshuu", "definition": "noun knee\n-Sheepga ggal'kieshuuyu. Ggoadu ggal 'naga da yaayu ashda gi'dseeb. My knee hurts. I think it's because I walked too long yesterday."}
{"headword": "ggal'oa", "definition": "verb to drop, let go\n-Geedsa ggal'oadu ckbeesh awil lu'kwil 'balgiackshgt. I almost dropped the box because it was very heavy.\n-Ggal'oadu noahl. I dropped a plate.\n-Na mungaadu 'wee loaba gwee dowl ggal'oat. I lifted the rock and then dropped it."}
{"headword": "ggal'oash", "definition": "noun stomach\n-Sheepga ggal'oashu. My stomach hurts."}
{"headword": "ggal'tsushg", "definition": "verb to be too small\n-Ggal'tsushga na ggaidn. Your hat is too small.\n-Na geegish nagwaadu 'backsh da ggal'dsooshgd da 'koy. My father bought me pants but they were too small for me."}
{"headword": "ggal'uunck", "definition": "noun Indian box, storage box\n-Ggal'uunck na dee hoy gyad hla 'nag hlat damoatga na wineayat. People used Indian boxes long ago to save their food."}
{"headword": "ggal'waatk", "definition": "verb unlucky; come empty handed\n-Giloa yaan da gwee, ggal'waatgd. He should not go there because he is unlucky."}
{"headword": "ggamckbaickshk", "definition": "noun sawdust\n-Na 'yagayaam da moolaa laa da hailda ggamckbaickshg, da 'nee hoym da lack yuubm. I went down to the sawmill where there was a lot of sawdust and that's what we used on our ground."}
{"headword": "ggamggantk", "definition": "noun door\n-Shga'doosha ggamggantk. Close the door."}
{"headword": "ggamhlabeeshk", "definition": "noun shavings\n-Ggamhlabeeshk hoyu hlan gwal'kn lag. I use shavings to turn the wood."}
{"headword": "ggamwaal", "definition": "noun poor stuff, cheap things\n-Ahlgadee hashacka dm geega ggamwaal. I don't want to buy cheap things."}
{"headword": "ggam'dooshk", "definition": "noun sweepings\n-Dm gwal'ka'nu ggam'dooshk. I'm going to burn the sweepings."}
{"headword": "ggam'do'otsk", "definition": "noun charcoal, coal, soot\n-Ggam'do'otskga hoy gyad hla shagamaashgit. People use charcoal when they paint."}
{"headword": "ggan", "definition": "noun tree, wood\n-Ndm ama haboalda ggan gwee. I'm going to take good care of that tree."}
{"headword": "gganahietg", "definition": "verb to lean against (a wall, firm object)\n-Oa, hla gganahietgu da waaba gwa'a, hla geedsa shonaahlu. Yes, I leaned against this house, when I almost got tired."}
{"headword": "gganaow", "definition": "noun frog\n-Tcka'nooyu gganaow da awaa lack'daa. I heard a frog by the lake."}
{"headword": "gganawulee", "definition": "noun backpack; strap to carry things\n-Gi'dsoan na wil nee gganawulee. I saw the backpack in the back room."}
{"headword": "gganeesh", "definition": "verb to be the youngest male\n-Gganeesht Lobat. Robert is the youngest male."}
{"headword": "gganggan", "definition": "noun forest; pieces of wood\n-Shackdoa gganggan. Gather more pieces of wood."}
{"headword": "ggangwal'ka", "definition": "noun kindling\n-Tcka'nee gganhlaag ggangwal'ka dee 'kotsu. I cut up kindling every morning."}
{"headword": "Gganhaada", "definition": "noun Raven Clan (crest)\n-Gganhaada nagwaads Ruth. Ruther's father is Raven.\n-Gganhaada wil hokshgush nagwaadu. My father's moiety is Raven."}
{"headword": "gganhlaag", "definition": "noun morning\n-Oomhoant nagwaadu ashda gganhlaag. My father went fishing this morning."}
{"headword": "gganhlaan", "definition": "noun wooden body armor\n-Shgu dm hoym gganhlaan da lack ha'liwildoolgit. We need to wear body armor when we go onto the battlefield."}
{"headword": "gganhla'ka'winshk", "definition": "noun clothespin, scissor-like tool\n-'Gwaatga tcka'nee gganhla'ka'winshk. All the clothes pins are gone."}
{"headword": "gganlugoy'pa", "definition": "noun window, light source\n-Dm 'daayu da awaa gganlugoy'pa. I'm going to sit by the window."}
{"headword": "ggantk", "definition": "verb to be dried hard, stiff with cold\n-Geedsa ggantka ggaidu awil lu'kwil gwatka lacka. My hat almost dried hard because the weather was so cold."}
{"headword": "gganwaal", "definition": "noun cheap goods\n-Gway'a wila dsaba gganwaalt. His things look very cheap."}
{"headword": "gganwaay", "definition": "noun oar lock\n-Lu 'ken ggaimgganshk da gganwaay. Put the oar in the oar lock."}
{"headword": "gganyishya'tsa", "definition": "noun suspenders\n-Dm geegu shu gganyishya'tsa da nakshu. I'm going to buy new suspenders for my spouse."}
{"headword": "ggan'dameesh", "definition": "noun marker, pencil\n-Ahl shguuhl ggan'dameesh da 'kwan? Do you have a pencil?"}
{"headword": "ggan'doa", "definition": "noun button, clasp to hold cape on; safety pin\n-Ndsu ggan'doa. Give me the safety pin."}
{"headword": "ggapshil", "definition": "verb to blink, wink\n-Ap ahlgadee ggapshil 'yoota gwee. That man doesn't blink.\n-Na lukhleedaawhl ligigoa da 'dsm 'dsalu dowla ggapshilu. When something goes in my eye, then I blink."}
{"headword": "ggashgaatsg", "definition": "verb to be rough (like sandpaper)\n-Ggashgaatsga na anaashu awil 'tsuu baashk. My skin is rough because of the strong wind."}
{"headword": "ggashgaawt", "definition": "verb to be of a certain size\n-Nda ggashggaw ha'li-tckoackga dm dsabm? How big is the table that we're going to make?"}
{"headword": "ggashggaads", "definition": "noun dog fish\n-Ahl dee 'tsamaa'anee ggashggaads? Do you like the taste of dogfish?"}
{"headword": "ggashishee", "definition": "noun feet\n-Shgaaygshga ggashishee hlgu 'yoota dawil ggusht. The boy's feet were hurt when he jumped."}
{"headword": "ggatgyad", "definition": "verb to be strong (physically or orally)\n-Ap shm lu'kwil ggatgyada 'yoota. The man is really strong.\n-Lu'kwil ggatgyada wila gyoa 'wee 'yoota gwee. That man is very strong at what he's doing."}
{"headword": "ggatgyatga baashg", "definition": "noun gale, strong wind\n-Ggatgyatga baashg ashda gi'dseeb. There was a strong gale yesterday."}
{"headword": "ggawaaym 'tu'utsk", "definition": "noun sword\n-Ggawaaym 'tu'utsga hoy hlaagi gyad hla dildalt. People in the old times used a sword to fight."}
{"headword": "ggawn", "definition": "verb to chew Plural:gganggawn\n-Kwhlee ggawn goa gubn. Completely chew up what you eat.\n(-).Lu'kwil wilaay 'yoota gweet ggawn goa gubed. That man knows how to chew what he eats."}
{"headword": "ggawsh", "definition": "noun hair\n-Nahl en ggadeeshga na ggawshn? Who braided your hair?"}
{"headword": "ggayg", "definition": "noun chest PLURAL: ggaggaygt\n-Sheepga ggaygt. His/her chest hurts."}
{"headword": "ggayneesh", "definition": "noun chum salmon, dog salmon\n-Hailda ggayneesh da awaa Macklackaahla. There's a lot of dog salmon by Metlakatla."}
{"headword": "gga'bala", "definition": "noun gun\n-Hoyu gga'bala hladm goo wunu. I use a gun when I shoot deer."}
{"headword": "gga'bilaash", "definition": "noun larvae\n-Lu doa gga'bilaash da 'dsm 'nhla'naggan. There are mosquito larvae in the barrel."}
{"headword": "gga'dsihlshagya", "definition": "verb to pull down\n-Gga'dsihlshagya 'nakshuuneeshg. Pull down the window."}
{"headword": "gga'dsihl'doosh", "definition": "verb to push down\n-Needsu wil gga'dsihl'doosha hoguwoamhlg na hlmkdeet. I saw the child push his brother down."}
{"headword": "gga'dsihl'oksh", "definition": "verb to fall down\n-Geedsa gga'dsihl'oksha ggan da wil ggal 'balgiackshga maadm. The tree almost fell down because the snow was too heavy."}
{"headword": "gga'dsiyoahl", "definition": "verb to slide (on feet, with a sled)\n-Gga'dsiyoahla hlguwoamhlg da lack daaw. The child slid on the ice."}
{"headword": "gga'eemck", "definition": "noun White man, bearded man\n-Hailda gga'eemck dsoackt da Gitsgaan. There are a lot of Europeans living in Ketchikan.\n-Needsm hailda gga'eemck. We saw a lot of Europeans (Whiteman)."}
{"headword": "gga'gwaa'gw", "definition": "noun low profile, low status, a worthless person\n-Ahlgadee aam dm gga'gwaa'gwn. Don't be a worthless person."}
{"headword": "gga'kai", "definition": "noun wing\n-'Nik'noonga gga'kai ckshgeeg. The eagle has long wings."}
{"headword": "gga'koacksh", "definition": "noun salmonberry bushes\n-Ahlgadee macksha gga'koacksh da gwa'a. The salmon berry bush doesn't grow here."}
{"headword": "gga'kowtg", "definition": "verb to howl like a wolf; to sound in loud tone\n-Gga'kowtga 'yoota hlat tcka'noo gibaaw. The man howled when he heard the wolf."}
{"headword": "gga'kuhl", "definition": "verb to shiver\n-Gga'kuhla'nu hla ckgwatkshu. I shiver when I'm cold."}
{"headword": "ggiehl", "definition": "noun bowl\n-Kshi'nag de hoyu hla lu 'dsaicka wineaya da ggiehlu. I use my middle finger when I lick out my bowl."}
{"headword": "ggiehlam'do'otsk", "definition": "noun iron dish\n-Ggiehlam'do'otsk hoy nakshu hla googt. My wife uses an iron dish when she cooks.\n-Yoaksha ggiehlam'do'otsk. Wash the iron pot."}
{"headword": "ggoab", "definition": "noun waves\n-'Tsuu ggoab da wil gatgyada baashg. There are lots of waves when the wind is strong."}
{"headword": "ggoad", "definition": "noun heart\n-Ama ggoada 'wee 'yoota gwee. That man is very kind."}
{"headword": "ggoash", "definition": "verb to cool, simmer down\n-Aam mdm ggoasha aksh. It's good to cool the water down.\n-Aam mdm ggoasha aksh, ggal gyamgd. It's good to cool the water down, it's too warm."}
{"headword": "ggogg", "definition": "verb to bend forward, bow, stoop\n-Ggoggn da nhluu hahloam giamg. Bow your head under the flag.\n-Hla ggoagga 'wee 'yoota gwee hla gawdee algyackt. That man bowed after he talked."}
{"headword": "ggol", "definition": "verb to come apart, be irreparable; to be strewn loosely Plural:ggolggol\n-Ggol waabsh Dzon. John's house tumbled down.\n-Ggol 'dsilaa awil ggal hultgid. The basket came apart because it was too full."}
{"headword": "ggolee", "definition": "noun hair, scalp\n(-)-Shm 'nuunga ggolee 'wee 'yoota gwee. That man's hair is really long."}
{"headword": "ggol'ge", "definition": "noun yellow berries on muskeg\n-Ha'weenhl needsinee ggol'ge? Haven't you seen the yellow berries on the muskeg?"}
{"headword": "ggontgahl", "definition": "verb to be clear, evident, visible\n-Lu'kwil amookshu da wila how 'yoota gwee da up ahlga ggontgahla wila howd. I really listened to what that man said but it's not clear what he said."}
{"headword": "ggush", "definition": "verb to jump\n-Nee wil ggusha hoan. Look where the fish jumps."}
{"headword": "gibaaw", "definition": "noun wolf\n-Hailda gibaaw da lack'daa gwee. There are many wolves on that island."}
{"headword": "gig", "definition": "noun house fly\n(-)-Lu'kwil hamoolga gig da na 'dsalu. The fly is really bothering my face."}
{"headword": "gigeengwackhl", "definition": "verb to pray\n-Alik dm gigeengwackhlt nagoaga dm sha'daa'amum. Alec will pray before we start."}
{"headword": "gigim'uugg", "definition": "noun blond or reddish hair; horsefly\n-Gigim'uugga hana'acka gwee. That woman has blond hair."}
{"headword": "gigi'oashg", "definition": "verb to be stubborn\n-Gigi'oashga hoguwoamhlg hlat how noat dm yaawcktgt. The child was stubborn when the mother said to eat."}
{"headword": "gigyoaksh", "definition": "noun something that floats\n-Na waaym da wite gwashga da goa 'wee loagsh, aam shga'nag dowla gigyoaksht dowla awaa Ta'gwaan habm. We rowed way over there to get a log, after a while it floated then we went to Metlakatla."}
{"headword": "gigyoatk", "definition": "noun axe, hatchet\n-'Gwatga na gigyoatgu. I lost my hatchet."}
{"headword": "gik", "definition": "prefix again\n-Gik hown. Say it again."}
{"headword": "gilaan", "definition": "noun aft of boat, back end, rear, stern\n-Gilaan dm dee wil hietgn. You will stand in the stern."}
{"headword": "giladse'eds", "definition": "noun dragonfly\n-Lu'kwil 'weelaeksha nagga'dsaaw giladse'eds. Some of the dragon flies are very big."}
{"headword": "gilakyo", "definition": "noun robin\n-Nee wila loa 'guba gilakyo, yagwa sha laaldid. Look what the little robins are doing, they're gathering worms."}
{"headword": "gilhowlee", "definition": "adverb in the woods or forest\n-Wie, gilhowlee wil 'dahla wun. 'Nee dm goym da gganhlaag. We're going to collect berries up in the woods."}
{"headword": "gilksh", "definition": "prefix to be self-inflicted, toward oneself\n-Gilksh amaneedsn, dayat n'dse'etsu da 'koy. Take care of yourself, that's what my grandmother said to me."}
{"headword": "gilksh-shamackshd", "definition": "verb to be willing to die\n-Gilksh-shamacksha nagwaada hlguwoamhlg awil dm didoolsht. The child's father was willing to die so that his child might live."}
{"headword": "gilkshtckal'da'minshg", "definition": "verb to draw, take a picture\n-Hoyshga gilkshtckal'da'minshga dsaba 'yoota. The picture the man made is beautiful."}
{"headword": "gilksh'ietksh", "definition": "verb to repent, be sorry for\n-Gilksh'ietksha hlguwoamhlg awilt oy loab da 'nakshuuneeshg. The child was sorry that he threw a rock at the window."}
{"headword": "giloa", "definition": "verb to stop, not do\n-Giloadsa oyan liploab. Don't throw the rocks."}
{"headword": "gil'aksh", "definition": "verb to give a drink\n-Wie gwinaat. Gil'akshe. Well, fellow. Give me a drink of water."}
{"headword": "ginamaan", "definition": "verb to be left over (food)\n-Hailda goa ginamaant. There are a lot of things left over.\n-Na shagiet wunm ashda 'guulda sha, tckoackgm dowla ginamaan hailda goa dm gubm. We got together one day, we ate and there were a lot of leftovers to eat."}
{"headword": "gina-shawaal", "definition": "verb to be unexpected\n-Gina-shawaal gyad da wil dsoackm. People showed up unexpectedly where we live."}
{"headword": "ginawaal", "definition": "verb to stay behind\n-Ginawaalt Peda awil ggal 'tsuu lacka. Peter stayed behind because the weather was bad."}
{"headword": "gipaig", "definition": "verb to fly, glide in the air Plural: lapaig\n-Ahlga dm gipaiga'nu da sha gya'wn. We're not going to fly today.\n-Ahlga dm gipaiga'nu da Gitsgaan da sha gya'win. We're not going to fly to Ketchikan today."}
{"headword": "Gishbackloa'ds", "definition": "noun People of the Elderberries\n-Hla badsga Gishbackloa'ds da ggaldsabm. The People of the Elderberries have arrived at our village."}
{"headword": "Gish-budwada", "definition": "noun Killer Whale Clan\n-Gish-budwada wil hokshgu. I belong to the Killer Whale Clan."}
{"headword": "gish doa", "definition": "verb to move over\n-Hlimoamee ndm gish doa ha'li'dameesh. Help me move the table over."}
{"headword": "gishihaywaash", "definition": "noun northeast wind\n-Gishiwaashga baashg. There's a northeasterly blowing."}
{"headword": "gishiyaashg", "definition": "noun north wind\n-Ap shm luguuye gishiyaashg wil wuwaalm. The north wind is really blowing where we are."}
{"headword": "gish'daa", "definition": "verb to move over, sit in another place\n-Gish'daan da awaayu. Move over by me."}
{"headword": "gitckawtk", "definition": "adverb some time ago\n-Wite gitckawtk wil dsaga nabeebu. My uncle passed away some time ago."}
{"headword": "Gitdsacklahl", "definition": "noun People of the Shrubs\n-'Woo Gitdsacklahl tcka'neesh 'nuum. People of the Shrubs have invited all of us."}
{"headword": "Gitdseesh", "definition": "noun People of the Salmon (Seal) Traps\n-Lu'kwil aam 'kawtsi dsaba Gitdseesh. People of the Salmon Traps make good ooligan grease."}
{"headword": "Gitlan", "definition": "noun People of Two Passing Canoes; Where the Salmon Spawn; Who sit in the Stern of Canoes\n-Lu'kwil hailda Gitlan. There are a lot of People of Two Passing Canoes."}
{"headword": "Gitnack'angeek", "definition": "noun People of the Mosquitoes\n-Ndahl wil dsoockdu Gitnack'angeek? Where do the people of the Mosquitoes live?"}
{"headword": "gitwaaltk", "definition": "noun enemy intruders, raiders\n-Giloamdsa 'gilm ligigoa da gitwaaltgm gyad. Don't give anything to enemy raiders."}
{"headword": "Gitwilgyots", "definition": "noun People of the (Sea) Kelp\n-Gitwilgyots ndm wil geega laan. I'm going to buy fish eggs from the People of the Kelp."}
{"headword": "Git'ando", "definition": "noun People of the Other Side (Wiers)\n-Ha'wahlgandee tckal'waay Git'ando. I haven't met any People of the Other Side."}
{"headword": "Git'dsilaashu", "definition": "noun People of the Way Inside\n-Wilaay Git'dsilaashu aadmhoan. People of the Way Inside are good fishermen."}
{"headword": "Git'nadoyksh", "definition": "noun People of the Swift Waters\n-Lu'kwil hoyshga dsaba Git'nadoyksh. The work done by the People of the Swift Waters is beautiful."}
{"headword": "giyaaksh", "definition": "adverb out on the water\n-Ahl needsinee boad da wiet giyaaksh? Do you see the boat that's way out on the water?"}
{"headword": "gi'dseeb", "definition": "noun yesterday\n-Nda wila waal lacka ashda gi'dseeb? How was the weather yesterday?"}
{"headword": "gi'dsoan", "definition": "noun back room\n-Gi'dsoan wil shguu ha'dooshg. The broom is in the back room."}
{"headword": "gi'dsoygg", "definition": "noun bow (of boat)\n-'Nuuyu dm 'daam da gi'dsoygg. I'll sit in the bow."}
{"headword": "gi'goahl", "definition": "adverb years ago; long ago\n-Aa'backdu wila leemee hlaa gigyad ashda wite gi'goahl. I remember how the old people used to sing many years ago."}
{"headword": "goa", "definition": "interrogative what?\n-Goahl wilgyedu gwa'a? What color is this?"}
{"headword": "goabackga lacka", "definition": "noun overcast sky\n-Wukdsan en goabacka lacka. The rain clouds have made it an overcast day."}
{"headword": "goabackga sha", "definition": "noun overcast day\n-Anoacku dm hahlalshu da gyalck wil goabacka sha. I like to work outside when the day is overcast."}
{"headword": "goack", "definition": "noun basket\n-Goacka hoy 'gubatguuhlg hla ggashimaayt. The children used small berry baskets to pick berries."}
{"headword": "goadsagid", "definition": "noun container\n-Nda goadsagid dm hoyu da 'kawtsi? Where's the container I'm going to use for the ooligan grease?"}
{"headword": "goamshm", "definition": "noun winter\n(-) Lu'kwil anoacku daayksh hla yaa maadm da goamshm. I really like Indian ice cream when the snow falls in the winter."}
{"headword": "goamtg", "definition": "verb to be soft\n-Goamtga mahluu. The pillow is soft.\n(-)-Lu'kwil goamtga an'on hana'acka gwee. The woman's hand is very soft."}
{"headword": "goaym", "definition": "noun spring (season)\n-Luaam ggoadu hla daawhla goamshm ada hla badsga goaym. I'm happy when the winter leaves and spring arrives."}
{"headword": "goa'opshgn", "definition": "number two long objects\n-Goa'opshgn ggan'dameesh dm 'gilmu da hlguwoamhlg. I'm going to give the child two pencils."}
{"headword": "golksh", "definition": "noun scarf\n-Aam mdm hoy golksh, hailda geega da gyalck. It's good for you to wear a scarf, there are a lot of mosquito's outside."}
{"headword": "goo", "definition": "verb to shoot; to vote by hand or ballot\n-Giloamdsa goo gibaaw. Don't you shoot a wolf."}
{"headword": "gooda'ats", "definition": "noun coat\n-Ndadu gooda'atsn? Where is your coat?"}
{"headword": "gooda'atsm shgyen", "definition": "noun raincoat\n-Ndayu na gooda'atsm shgyenu? Where's my raincoat?"}
{"headword": "gool", "definition": "noun gold\n-'Waaysh Alik gool da lack shga'neesh. Alec found gold on the mountain."}
{"headword": "goomaa", "definition": "noun angel fish, rat fish\n-Naahl en guba goomaa? Who eats rat fish?"}
{"headword": "goowaagg", "definition": "noun elderberry jam\n-Lu'kwil 'tsamaatga goowaagg da lack giamgm anaay. Elderberry jam is very good on warm bread."}
{"headword": "goo'bl", "definition": "number two abstract objects\n-Goo'bl likshgyadm wileelm tgwa hoyu. I use two different kinds of eyeglasses."}
{"headword": "goy", "definition": "verb to go\n-Wie ndahl dm dee goyn? Where are you going?"}
{"headword": "goydiksh", "definition": "verb to arrive\n-Ndahl dm wil goydikshgt Donna May? When is Donna May coming?\n-Na goydiksha 'wee shdeem boad da Ta'gwaan dun nee wila loa gyad. A big steamer came to Metlakatla and I saw what the people did."}
{"headword": "goy'ba", "definition": "verb to be bright\n-Ggal goy'ba laakwsh. The light is too bright.\n(-) Lu'kwil goy'ba laakwsha hoyshm. The light you are using is bright."}
{"headword": "gub", "definition": "verb to eat PLURAL: tckoackg\n-Goadu dm gubn? What are you going to eat?\n-Hladm googs noayu mdm gubt gya'wn. My mother is going to cook and we'll eat now."}
{"headword": "guguul", "definition": "verb to search for\n-Yagwan guguul ma'koacksh. I'm looking for salmon berries."}
{"headword": "gugwalksh", "definition": "verb to be polished, shiny\n-Alu'daa wil gugwalksha gahooda hlgu hana'ack. You can really see how shiny the woman's necklace is."}
{"headword": "gugwnyaa", "definition": "verb to walk toward\n-Hagwil gugwnyaa hash da awaayu. The dog walked slowly toward me."}
{"headword": "guksh", "definition": "verb to jump (of fish)\n-Hashacku ndm 'waay wil gukshga hoan. I want to find where the fish jump."}
{"headword": "gukshg", "definition": "verb to wake up\n-Ahlgadee hashackaa hlguwoamhlg dm gukshgt. The child doesn't want to wake up."}
{"headword": "gushck", "definition": "verb to be bitter\n-Na dsaba hlgu hana'ack goa dm gubm, da ahlgadeet wilaay goahl wila gyoad dowla lu'kwil gushcka gubm. The little girl was cooking what we were going to eat and didn't know what she was doing so what we ate was bitter."}
{"headword": "gushguuds", "definition": "noun sparrow\n(-).Lu'kwil ckshdaamcka wil how gushguuds. The sparrows sound is very loud."}
{"headword": "guudack", "definition": "verb to ask, inquire\n-Ahlgandee wilaayhl goa dm wila gyoayu dun guudacka n'dse'etsu goa dm wila gyoayu. I didn't know what to do so I asked my grandmother what to do."}
{"headword": "guul", "definition": "verb to harvest, reap, pick (of food)\n-Wie dm guul maay sha gya'wn. Hla hailda mikmeegt. Well, we're going to pick berries today. A lot are ripe."}
{"headword": "guulka", "definition": "noun westerly wind\n-Hailda ggoab hla baa guulka. There are a lot of waves when the westerly wind blows."}
{"headword": "guunksh", "definition": "verb to be dry\n-Hladm guunksha na lumaakshu. The clothes will soon be dry.\n-Hla luguunksha ggiehlam'do'otsk. The iron pot has gone dry.\n-Na yoaksha nakshu na hoyayu dowla ahlgandee daackga ndm hoyt. Dsihla guunksht dowla daackgu ndm hoyt. My wife washed my clothes and I couldn't wear them. When they were dry I was able to wear them."}
{"headword": "guunkshm hoan", "definition": "noun dried fish PLURAL: luunkshm hoan\n-Hashackanee guunkshm hoan? Do you want dried fish?"}
{"headword": "guyna", "definition": "noun path, road, trail\n-Yaaka guyna da ggaldsap. Follow the trail to the next village."}
{"headword": "gwaanksh", "definition": "verb to be cooked, done\n-Hla gwaanksha wineaya. The food is done.\n-Hla gwaanksha goa dm gubm aam dowla 'dseen. Our food to eat is cooked so come right in."}
{"headword": "gwaantg", "definition": "verb to touch PLURAL: gwitgwaantg\n-Giloamdsa gwaantga 'nakshuuneeshg. Don't touch the window."}
{"headword": "gwaashg", "definition": "verb to borrow PLURAL: gwishgwaashg\n-Ahlgadee aam dm gwaashgn dish ligit naa. It's not good to borrow from anybody.\n(-).Na 'gwinooy hlgu 'yoota gwee daala da 'koy, hashackt dm gwaashgt da 'koy. The young man asked me for money because he wanted to borrow it from me."}
{"headword": "gwai'hl", "definition": "noun sack\n-Sha hailda gwai'hla gyad, 'nee hoym hla sha hla'ashgm. We have lots of sacks, that's what we use when we gather seaweed."}
{"headword": "gwalg", "definition": "verb to burn\n-Hla gwalga lag. The fire is burning.\n-Na gwalga waaba gwee. That house burned."}
{"headword": "gwalka", "definition": "verb to trim hair by burning ends\n-Ha'wahlgandee nee wil gwalka gyad na ggawsht. I haven't seen people trim their hair by burning the ends."}
{"headword": "gwal'kan", "definition": "verb to turn on (of electricity)\n-Wie hla aam dm gwal'kan laakwsh. Well it's good to the lights on."}
{"headword": "gwan", "definition": "number three fish or flat objects\n-Gwan shgaboo hoan 'gilmsh Peda da 'kam. Peter gave us three fish."}
{"headword": "gwashga", "definition": "adverb in that direction, over there\n-Wie gwashga dm habm. Well, we'll go over there.\n-Gwashga dm wil waalckshm. We're going to walk over there."}
{"headword": "gwashoa", "definition": "noun pig\n-Baasha'nu da gwashoa. I'm afraid of pigs."}
{"headword": "gwatg", "definition": "verb to be cold\n-Gwatga sha. The day is cold.\n-Ggal 'naga waalu dowla gwatga goa dm gubu. I took too long and my food got cold."}
{"headword": "gway'a", "definition": "verb to be poor\n-Gway'a wila dsaba waab. That house is pitiful.\n-Lu'kwil gway'a wila waal hlgu 'yoota gwee. That little boy is doing poorly."}
{"headword": "gwa'a", "definition": "adverb here\n-Ayam gwa'a wil 'daan. Sit right here."}
{"headword": "gwee", "definition": "particle that, there\n-Naa an'on da gwee? Whose hand is that?"}
{"headword": "gweekw", "definition": "noun groundhog\n-Ha'wahlgandee neehl gweekw, 'nee gun ahlgandee wilaayhl goahl dm wila howyu. I've never seen a groundhog, that's why I don't know what to say."}
{"headword": "gwilm ggawdee", "definition": "verb to get ready\n-Wie aam gwilm ggawdeeym. Dm hailda wila gyoam dsidaawhl. Let's get ready. We're going to do a lot of things tonight."}
{"headword": "gwiloan", "definition": "number three people\n-Gwiloan gyad gatgoidikshd. Three people arrived."}
{"headword": "gwinaat", "definition": "noun poor fellow\n-Ahl sheepganee, gwinaat? Are you sick, poor fellow?"}
{"headword": "gwineeshk", "definition": "verb to appear\n-Ahlgadee gwineeshga 'yoota gwee dm hahlalsht. That man didn't appear for work."}
{"headword": "gwinee'dsn", "definition": "verb to show\n-Hashacku ndm gwinee'dsn shu gooda'atsu da 'kwan. I want to show you my new coat."}
{"headword": "gwishgwaash", "definition": "noun blue jay\n-'Daa gwishgwaashg da lack ggan. There's a blue jay in the tree."}
{"headword": "gwishgwashg", "definition": "verb to be blue (in color)\n-Dm geegu gwishgwaashgm ggoda'ats. I'm going to buy a blue coat."}
{"headword": "gwishgwashm an'on", "definition": "noun ring\n-Naahl en dsaba gwishgwashm an'on hoyen? Who made the ring that you're wearing?"}
{"headword": "gwish-halayt", "definition": "noun robe for dancing\n-Hashacksh dup gwee dumt dsaba gwish-halayt. They want to make a robe for dancing."}
{"headword": "gwishmatee", "definition": "noun goat skin coat\n-Dm kshagaadu na gwishmateeyu dsihla 'dsuuhl gwatg. I'm going to get out my mountain goat skin coat when it gets really cold."}
{"headword": "gwish'dseeg", "definition": "noun fawn\n-Hlgu gwish'dseeg hahlyaat da hahlgeeka. There's a little fawn walking on the beach."}
{"headword": "gwish'na'ba'la", "definition": "noun button blanket Plural:gukgwish'na'ba'la\n-Yagwa loo'bishgat da gwish'na'ba'la. He/she is sewing a button blanket."}
{"headword": "gwitgwineeksh", "definition": "noun owl\n-Ahl tckanooyanee gwitgwineeksh? Do you hear the owl?"}
{"headword": "gyab", "definition": "verb to dip, draw water\n-Gyaba aksh dish 'need. Draw water for her.\n-Gyaba aksha awaan dowl 'gilmd da hlguhlgn. Dip that water and give it to your child."}
{"headword": "gyabn", "definition": "verb to come up above the water\n-Gyabn 'wee 'naackhl. The whale came out of the water.\n-Na gyabn 'wee uula da gwashga. The seal came out of the water over there."}
{"headword": "gyad", "definition": "noun people\n-Ndada tckash 'goahl wil goo gyada wun? What part of the year do people shoot deer?"}
{"headword": "gyalck", "definition": "adverb in the open air, outside\n-Gyalck dm habm. Ggal lu giamga 'tsawaab. We'll go outside. It's too warm in the house."}
{"headword": "gyamg", "definition": "noun; verb month; sun, heat; to be hot, warm Plural:lamg\n-Ggalgyamga 'dsm waaba gwa'a. This house is too warm."}
{"headword": "gyamgmdseewsh", "definition": "noun sun\n-Hashacku dm gukshgu nagoacka dm kshagwaantga gyamgmdseewsh. I want to wake up before the sun comes up."}
{"headword": "gyamgm'aatk", "definition": "noun moon\n-Hladm hultga gyamgm'aatk dsadaawhl. The moon will be full tonight."}
{"headword": "gyantee", "definition": "noun sea cucumber\n-Yagwa shagyantee 'guba 'yoota. The young men are gathering sea cucumber."}
{"headword": "gya'galtk", "definition": "verb to roll\n-Mun gya'galtga sha'winshk and lu oyt da 'dsm shdoob. Roll up the paper and throw it in the stove."}
{"headword": "gya'wn", "definition": "adverb now, today\n-Ahlgadee aam lacka da sha gya'wn. The weather is not good today.\n-Dowla gya'win! Right now!"}
{"headword": "gyehlk", "definition": "verb to spear, stab Plural: gyehlgyehlk\n-Gyehlgt Everett hoan da 'kala aksh. Everett speared the fish in the river."}
{"headword": "gyeksh", "definition": "verb to be calm\n-Hla gyeksha baashg gya'win. The wind is calm now.\n-Na oom hoanu ashda 'guulda sha da hu'kwil gyeksha na goyu. I went fishing the other day and it was calm where I went."}
{"headword": "gyelkwsh", "definition": "verb to feel something will happen; admonition\n-Gyelkwshu wil lu'dauckga ggoadn. I feel it when you are sad."}
{"headword": "gyelsh", "definition": "noun mussel\n-Yagwa sha gyelshd. He is picking mussels."}
{"headword": "gyem", "definition": "noun Saskatoon berries\n-Ndahl wil 'waay gyad gyem? Where do people find Saskatoon berries?"}
{"headword": "gyepsh", "definition": "noun; adverb hill, mountain; up high\n-Mun gyepsh wil 'dahla hlgumadm ggagoom. Seagull eggs will be found up high."}
{"headword": "gyeshg", "definition": "verb to be jealous\n(-)-Lu'kwil gyeshgm ggoada hana'ack da shu waabm. That woman is very jealous of our new house."}
{"headword": "gyoash", "definition": "noun flat leaf of kelp\n-Anoacku cksh'waanck da lack gyoash. I like herring eggs on the flat kelp."}
{"headword": "gyuwadun", "definition": "noun horse\n-Ahlga 'dahla gyuwadun da gwa'a, ksha geeka wil 'dahlt. There are no horses here, just down below."}
{"headword": "haackg", "definition": "verb not easy, work hard against odds, suffer PLURAL: hackhaackg\n-Shm haackga da 'koy ndm dsabt. It's not easy for me to do it."}
{"headword": "haad", "definition": "noun intestine\n-Na labiethow na gyadu, dowla haada labiet waald, dsabtda doctor. My intestine was bad and the doctor fixed it."}
{"headword": "haada uula", "definition": "noun seal intestines\n-Anoacka gga'dsaaw gyad haada uula. Some people like the intestine of the seal."}
{"headword": "haahlggan", "definition": "noun wall\n-'Yacka gilkshtckal'damtk da haahlggan. Hang the picture on the wall."}
{"headword": "haash", "definition": "noun fireweed\n-Anoacku wil gyeda haash. I like the color of the fireweed."}
{"headword": "haaya", "definition": "noun wood, rotted\n-Ahlgadee hashacku dm haaya na boadu. I don't want my boat to rot."}
{"headword": "haboal", "definition": "verb to keep, take care of\n-Ama haboald na 'gilm gyad da 'kwan. Take good care of what people give you."}
{"headword": "haboo'yil", "definition": "verb to get things ready\n-Haboo'yil tcka'nee goa dm wa'atm. Get the things ready that we're going to sell."}
{"headword": "hackback", "definition": "noun pocket knife\n-Shguu ndm gee na hackbacku. I need to sharpen my pocket knife."}
{"headword": "hackbayckshg", "definition": "noun saw\n-Wie ndsu hackbayckshg. Give me the saw."}
{"headword": "hackdek", "definition": "noun bow; tool\n-Goahl wilsh hackdek dm hoyu? What tool shall I use?\n-Dm dsabu hackdek ndm gaa wineaya da hlguyu. I'm going to make a bow so I can get food for my family."}
{"headword": "hackshgweekwshg", "definition": "noun instrument with holes; whistle\n(-)-Lu'kwil aam wila how hackshgweekwshg dsabn. The sound of the whistle you made is very good."}
{"headword": "hack'biyaan", "definition": "noun pipe for smoking\n-Gishya'an hack'biyaan. Pass the pipe around."}
{"headword": "hadaay", "definition": "noun steering wheel\n-Labite hlgookshn dm daayu da boad, labite waal na hadaayu. I wasn't able to steer the boat, my steering wheel went out."}
{"headword": "hadahaw", "definition": "verb to like to do, spend time doing\n-Hadahawyu hla lu'bishu. I like to sew."}
{"headword": "hadiksh", "definition": "verb to swim Plural:lahadiksh\n-Lu'kwil hashacku dm hadikshu dsihla shuunt. I really want to swim when summer is here."}
{"headword": "hadsag", "definition": "verb to be fatal\n-Ha'dackgm sheepg wil hadsagt. He died from syphilis."}
{"headword": "hadsikshm gik hawn", "definition": "verb to say again\n-Hadsikshm gik hawn - ggal ckshdaamcka 'dsig'dsig. Say it again - the car was too loud."}
{"headword": "hadsikshm gik waan", "definition": "verb to do again, repeat\n-Hoyshga leemeeyn, hadsikshm gik waan. Your singing is beautiful, do it again."}
{"headword": "hadsm", "definition": "prefix again\n(-)-Hadsm kshidaawhld. She went out again."}
{"headword": "ha-geemgm noahl", "definition": "noun dish cloth\n-Shguu ndm yoaksha noahl. I have to wash the dish towels."}
{"headword": "hageem'ka", "definition": "noun cloth to wipe with\n(-)-Ndsu hageem'ka. Give me the cloth to wipe with."}
{"headword": "haggagietk", "definition": "noun scissors\n-Noayu en dsaba na hoyayu, hoy haggagietk dumt 'kotsa dm hoyt. My mother made my clothes, she used scissors to cut what she used."}
{"headword": "hagwil", "definition": "prefix slowly\n-Hagwil yaa 'yoota awil sheepga ggal'oasht. The man walked slowly because his stomach hurt."}
{"headword": "hagwilhoo", "definition": "noun rope\n-Wie 'dsuu hagwilhoo, 'nee dm hoyu hla oom hoanu. Well, the rope is strong, it's what I use to go fishing."}
{"headword": "hagwil waan", "definition": "prefix to do slowly, slow down\n-Hagwil waan hla yaawckgn. Eat slowly.\n-Ggal 'deelda wila gyoan, hagwil waan. You're doing it too fast, slow down."}
{"headword": "hagwilyaa", "definition": "verb to walk slowly\n-Hagwil yaa 'yoota awil sheepga ggal'oasht. The man walked slowly because his stomach hurt."}
{"headword": "hagwilya'dsa", "definition": "verb to ring bell slowly\n-Hagwilya'dsa hashoicka waab dsuds wil dsaga gyad. The bell rings slowly at the church when someone dies."}
{"headword": "hagwn", "definition": "noun horse mussel\n-Eh! 'Tsamaatga 'guba hagwn. 'Nee guulm hla geeka aksh. Oh boy! The horse mussel tastes very good. That's what we get when the tide is low."}
{"headword": "hagyoaksh", "definition": "noun keel\n-Shgu ndm ama dsaba hagyoaksh. I have to repair the keel."}
{"headword": "hahlalsh", "definition": "verb to work, labor\n-'Tsuu hahlalsha hana'ack hlat shakshil waab. The woman worked hard when she cleaned the house."}
{"headword": "hahldoa", "definition": "verb to put in front of fire\n-Hahldoa loagakshgm hoaya da awaa lag. Put the soaked clothes by the fire."}
{"headword": "hahldock", "definition": "verb to take along the beach\n-Hahldocka ggan da 'kala aksh. Take the wood along the beach."}
{"headword": "hahlgeeka", "definition": "adverb down the beach Plural:hak-hahlgeeka\n-Ndm tckal'waayan da hahlgeeka. I'll meet you on the beach."}
{"headword": "hahlibeeshk", "definition": "noun knife Plural:hakhahlibeeshk\n-Ndsu hahlibeeshk. Dm sha shackanu. Give me the knife. I'm going to sharpen it."}
{"headword": "hahloa", "definition": "noun cloth Plural:hakhahloa\n(-)-Lu'kwil goamtga hahloa gwa'a. This cloth is very soft."}
{"headword": "hahloamboad", "definition": "noun sailboat\n-Dm kshagyoatgu da Ta'gwaan da 'dsm hahloamboad. I am going to Metlakatla by sailboat."}
{"headword": "hahloam gyamg", "definition": "noun flag Plural:hakhahloam gyamg\n-Shguu hahloam gyamg da 'kam. We have a flag."}
{"headword": "hahlwaal", "definition": "adverb along the beach\n-Ama doa ckbeesh da hahlwaal 'kala aksh. Put the boxes nicely along the beach."}
{"headword": "hahlyaa", "definition": "verb to walk along the beach\n-Wiedsa hahlyaa'nm da 'kala aksh. Let's walk along the beach of the river."}
{"headword": "hahlyaagw", "definition": "verb to hold skins toward fire to roast\n-'Tsamaatga hoan na hahlyaagwda gyad da awaa lag. Fish whose skins are roasted by the fire taste good."}
{"headword": "hahow", "definition": "noun what people are saying\n-Hahow gyad hla goidiksha uuah. People are saying that the ooligans have arrived."}
{"headword": "haickal", "definition": "verb to be determined, persistent\n-Dm haickalan mdm wila da'ackhlga goa hashackan. You have to be persistent, then you will get what you want.\n-Haickala hlguwoamhlg hla oom hoant. The child was determined when he went fishing."}
{"headword": "haig", "definition": "noun aroma, smell; spirit\n-Wudi 'biyaan na haigt. They smell like smoke."}
{"headword": "haild", "definition": "quantifier many\n-Wilaayu hailda maay. I know there's lots of fruit."}
{"headword": "hakk", "definition": "noun goose\n-Ha'weenhl backanee yoam hakk? Haven't you tasted roasted goose?"}
{"headword": "hakshm", "definition": "adverb again\n-Hakshm leemeeyn, aam wila howt. Sing again, it sounded good."}
{"headword": "haldaaksh", "definition": "noun ointment, medicine\n-Ama haldaaksha woamsh. Devil's club is good medicine."}
{"headword": "haldaaw", "definition": "verb to treat with medicine\n-Haldaaw wil gwalga an'ont. Treat his hand with medicine where it is burned."}
{"headword": "haldaawgit", "definition": "noun witchcraft\n-Lebaasha gyad da haldaawgit. People are afraid of witchcraft."}
{"headword": "haldm", "definition": "prefix to bring up, lift\n-Haldm gaa likshoack. Bring up the door.\n-Haldm gaa likshoack da awaayu. Bring up the door to me."}
{"headword": "haldmbaa", "definition": "verb to agree to go with; to arise\n-Haldmbaa hana'ack hlat tckanoo boad. The woman got up when she heard the boat.\n-'Kineetgu ashda gganhlaag da haldmbaayu dm hahlalshu. I got up in the morning to go to work."}
{"headword": "haldm'acklg", "definition": "verb to arise, to get up\n-'Wee amhown dish maata - shguu dm haldm'acklgt. Holler at Martha - she has to get up."}
{"headword": "haldm'oy", "definition": "verb to wake up\n-Haldm'oy nakshn, hladm laaltgd da hahlalsht. Wake up your husband, he'll be late for work."}
{"headword": "haleemee", "definition": "noun musical instrument\n-Yagwat shiwilaaykwshgish Kayla haleemee. Kayla is learning to play the piano."}
{"headword": "halhal", "definition": "noun something that spins; toy top\n(-)-Lu'kwil anoacka hlguwoamhlg halhal 'gilumu dish 'need. The child really like the top that I gave her."}
{"headword": "hamoolg", "definition": "noun; verb bothersome thing, nuisance; to be bothered\n-Hamoolgsh malee hla wil ayawa 'yoota. Mary is bothered when the man shouts."}
{"headword": "hana'ack", "definition": "noun girl, lady, woman\n-Ndayu na hlguhlgm hana'ackn? Where is your little girl?"}
{"headword": "hapckdooweew", "definition": "noun horn spoon\n-Hapckdooweew dsaba gyad da ggan, 'nee hoym hla tckoackgm. People made horn spoons out of wood, that's what we use when we eat."}
{"headword": "hapshgoulg", "definition": "noun spoon\n-Yagwa sha hapshgoulgu. I am carving a spoon."}
{"headword": "hapshgoulgm ggan", "definition": "noun wooden spoon\n-Hashacku ndm geega hapshgoulgm ggan dsabn. I want to buy the wooden spoon you made."}
{"headword": "hap'dsee", "definition": "noun comb\n-Shakshen na hap'dseeyn. Clean your comb."}
{"headword": "hash", "definition": "noun dog Plural:hashhaash\n(-) Needsu hash ada doosh. I see a dog and a cat."}
{"headword": "hashack", "definition": "verb to want\n-Hashacku shameeym wun. I want deer meat."}
{"headword": "hashdalksh", "definition": "noun ring finger\n-Ggal geetga hashdalksha hana'ack dumt hoy gwishgwashm an'ont. The woman's ring finger is too swollen to wear her ring."}
{"headword": "hasheepg", "definition": "noun sickness\n-Luwantga ggoadu ndm gidigaa hasheepg. I'm worried that I might catch a sickness."}
{"headword": "hashooshk", "definition": "noun trouble\n-Hashooshga ligi goa waal hlgu 'yoota gwee. Whatever that boy does seems to cause trouble."}
{"headword": "hashoyck", "definition": "noun bell\n-Yedsa hashoyck dsida hashackanee. Ring the bell when you want me."}
{"headword": "hathot'dackg", "definition": "verb to boil\n-Hla hathot'dackga shgoosheed. The potatoes are boiling."}
{"headword": "hawaalt", "definition": "noun arrow, spear, sharp fighting equipment\n-Dsabish Joe hawaalt. Joe made an arrow."}
{"headword": "hawala'awa", "definition": "noun weapon\n-Goahl wilsh hawala'awa dm gaadn? What weapon are you going to take?"}
{"headword": "hawhaw", "definition": "noun lion\n-Ha'weenhl needsinee hawhaw? Haven't you seen a lion?"}
{"headword": "hayaawckg", "definition": "noun fork\n-Anoaggu shga 'naga hayaawckga hoyn. I like the length of the fork you're using."}
{"headword": "hayatsk", "definition": "noun copper shield\n(-).•u'kwil hlu'daka hlaagigyad hayatsk. The old people treasured their copper shields."}
{"headword": "ha'aksh", "definition": "noun dipper to drink with\n-Dee lup shguu ha'akshu. I have my own dipper."}
{"headword": "ha'ashya", "definition": "verb to sneeze\n-Ashguu ha'ashya hlguwoamhlg. The child's sneeze is funny."}
{"headword": "ha'ats", "definition": "noun tree stump\n-Ggal 'weelaeksha ha'ats gwa'a. This stump is too big."}
{"headword": "ha'bish", "definition": "noun cover, top of an object\n-'Gwaatga ha'bisha ggaldm shikopee. The lid to the coffee pot is lost."}
{"headword": "ha'dackg", "definition": "verb to be bad\n-Lu'kwil ha'dackga lacka. The weather is bad.\n-Ha'dackga wila gyoa hlgu 'yoota gwee, baashu goa dm wila walt. That young man is doing something wrong, I'm afraid of what he'll do."}
{"headword": "ha'dackgm sheepg", "definition": "noun syphilis\n-Ahlgadee aam ha'dackgm sheepg. Syphilis is not good.\n-Labite waal 'yoota gwee, 'ken ha'dackgm sheepg dish 'need dowl sheepgt. That man messed up, he got syphilis, and got sick."}
{"headword": "ha'dal", "definition": "noun cedar bark strips for baskets\n-'Gilmsh Dzaak ha'dal dish 'need. Jack gave her cedar bark."}
{"headword": "ha'dooshg", "definition": "noun broom\n-Macka ha'dooshg. Put the broom away."}
{"headword": "ha'dsaick", "definition": "noun index finger\n(-).Na hoyu ha'dsaick ndm wilaay goa dm needsu lack book. I use my index finger to know what I'm seeing on the book. (Turn pages with it.)"}
{"headword": "ha'dsalt", "definition": "noun devil fish\n(-)-Lu'kwil hashacku ndm backa ha'dsalt. I really want to taste devil fish."}
{"headword": "ha'dseekwsha", "definition": "noun wooden bailer for water\n-Ndahl wil shguhl ha'dseekwsha? Where is the wooden brailer?"}
{"headword": "ha'dsinaash", "definition": "verb to have good luck, be lucky\n-Aam dsa ap ha'dsinaasha shuunta gwa'a. It will be nice to have good luck this summer."}
{"headword": "ha'dsiyaan", "definition": "verb to be lucky\n-Ahl ha'dsiyaanee da sha gya'wn? Do you feel lucky today?"}
{"headword": "ha'dsi'uult", "definition": "noun snail\n-Ama nee wila yaan, hailda ha'dsi'uult da gwa'a. Watch where you walk, there are lots of snails here."}
{"headword": "ha'kalaaw", "definition": "noun club for killing slaves, fish or animals\n-Ndsu ha'kalaaw awaan. Give me that seal club."}
{"headword": "ha'kan", "definition": "noun to make it tough for\n(-)Lu'kwil ha'kanm 'yoota hla baaldm dm hlimoamt. The man made it hard onus when we tried to help him."}
{"headword": "ha'kayaan", "definition": "noun wooden war club, wooden slave killer\n-Shuulga ha'kayaan hoy hlaagi gyad. The clubs used by people in the past were dreaded."}
{"headword": "ha'koa", "definition": "noun back\n-'Man ha'koayu. Rub my back."}
{"headword": "ha'li", "definition": "prefix upon\n-Shgu ha'li'daa da awaa 'nakshuneeshg. Put the chair by the window."}
{"headword": "ha'libaashagganshk", "definition": "noun place to dry seaweed\n-Sheeds dm hoym da ha'libaashagganshgm. We're going to use sheets for drying the seaweed."}
{"headword": "ha'lickbaickshg", "definition": "noun sawhorse\n-Na dsaba nagwaadu waab adat hoy ha'lickbaickshg. My father built a house and he used a sawhorse."}
{"headword": "ha'lidal", "definition": "noun battlefield\n-Goayu ha'lidalshm? What are you fighting over?"}
{"headword": "ha'lidsogg", "definition": "noun earth, world\n-Hashacku dm gyeksha ha'lidsogg. I want peace on the earth."}
{"headword": "ha'ligalmeelg", "definition": "noun playground\n-Wie dm dsabm ha'ligalmeelg. Well, we'll fix up the playground."}
{"headword": "ha'liggoad", "definition": "verb to assume, guess, think\n-Ahl 'nee dee ha'liggoadn? Is that what you think too?\n-Ha'liggoadu hladm yaa waash. I think it's going to rain.\n-Ha'li ggoadu ndm goy Ta'gwaan. I think I'm going to go to Metlakatla."}
{"headword": "Ha'li goo'bl Sha", "definition": "noun Tuesday\n-Hla Ha'li goo'bl Sha gya'wn. Today is Tuesday."}
{"headword": "Ha'li Kwshdoonsha Sha", "definition": "noun Friday\n-Hla Ha'li Kwishdoonsha Sha gya'wn. Today is Friday."}
{"headword": "ha'limalshk", "definition": "noun altar, pulpit\n-Lu'kwil anoaggu ha'limalshga dsaba gyad. I really like the altar that the people made."}
{"headword": "ha'linoak", "definition": "noun bed Plural:ha'liaahlg\n-Ha'liggoadu nhluu ha'linoak wil shguu 'dsoacksh. I think the shoes are under the bed."}
{"headword": "Ha'li Shgwaitga Sha", "definition": "noun Sunday\n-Ha'li Shgwaitg dowl ggadsudsm, dowl leemeeym da 'dsm na Waabsh Shm'oygit ga Lackaga. On Sunday we go to church and sing the Lord's house."}
{"headword": "Ha'li tckaalpcka Sha", "definition": "noun Thursday\n-Dm gwindaawhl da Gitsgaan dsihla Ha'li tckaalpcka Sha. I'm going over to Ketchikan on Thursday."}
{"headword": "ha'litckoackg", "definition": "noun dinner table\n-Hailda wineaya da lack ha'litckoackg. There's lots of food on the table."}
{"headword": "ha'litoa", "definition": "noun shelf\n-'Lee shguu sha'winshk da lack ha'litoa. Put your books on the shelf."}
{"headword": "ha'litoamnoahl", "definition": "noun cabinet, dish rack\n-'Dsm waabtckoackga wil shguu ha'litoamnoahl. The cabinet is in the dining room."}
{"headword": "ha'liwaalcksh", "definition": "noun floor\n-Dm 'daayu da lack ha'liwaalcksh I'm going to sit on the floor."}
{"headword": "ha'liwildoolgit", "definition": "noun battleground\n-Ha'wahlgandee nee ha'liwildoolgit shawaadida Viet Nam. I haven't seen the battleground that's called Viet Nam."}
{"headword": "Ha'li yaygga Sha", "definition": "noun Saturday\n-Hla Hali yaygg dowla Gitsgaan habn, dm geegu wineaya. On Saturday we go to Kethikan to buy food."}
{"headword": "ha'li'daa", "definition": "noun chair\n-Ha'li'daa hashacksh noayu. My mother wants a chair."}
{"headword": "ha'li'dameesh", "definition": "noun desk, table\n-'Lee shguu ckbeesh da lack ha'li'dameesh. Put the box on the table."}
{"headword": "ha'li'doygg", "definition": "noun day to greet people\n-Lu amaam ggaggoada gyad da hla ha'li'doygg. People are happy on the day to greet people."}
{"headword": "ha'li'dsul", "definition": "noun equipment for filleting fish; place for filleting fish\n-Lu'kwil ama ha'li'dsulsh maata. Martha made a good place to fillet fish."}
{"headword": "Ha'li 'Guul Sha", "definition": "noun Monday\n-Hla Ha'li 'Guul Sha gwa'a. This is Monday."}
{"headword": "Ha'li 'Gwilee Sha", "definition": "noun Wednesday\n-Ndm tckal'waayn da waab tckoackg dsihla Hali'Gwilee Sha. I'll meet you at the restaurant on Wednesday."}
{"headword": "ha'tsal", "definition": "noun octopus, squid, devil fish\n-Wilaaysh Doreen ai'dsm ha'tsal. Doreen knows how to fry devilfish."}
{"headword": "ha'wahlg", "definition": "verb to be against custom or law, forbidden\n-Ha'wahlgadee badsgt. They haven't arrived yet.\n-Na shguu gga'bala da 'koy dowl ha'wahlga dumt 'gwinoo gyad dumt hoyt. I have a gun but I don't allow anyone to ask to use it."}
{"headword": "ha'weeni", "definition": "verb to wait\n-'Ka ha'weeni, ndm hlimoamn! Wait a minute, I'll help you!"}
{"headword": "hieda", "definition": "noun Haida person\n-'Dsuu hlgu hieda 'yoota gwa'a da'al aam wila Shm'algyackt. This young man is Haida but he speaks good 'TsmSHIAN language."}
{"headword": "hiedmck", "definition": "noun Haida language\n-Dee hashacku ndm wilaay hiedmck. I want to know the Haida language, too."}
{"headword": "hieds", "definition": "verb to send\n-Hiedsihla ckbeesh dish Dzon. Send the box to John."}
{"headword": "hietg", "definition": "verb to stand Plural: macksh\n-Ama hietga ggadsaagg da lack yuub. The cross stands good on the ground."}
{"headword": "hiwaash", "definition": "noun southeast wind\n-Giloamdsa 'goa'olda gooda'atsm shgyan dsihla gwaantga hiwaash. Don't forget your raincoat when the southeast wind starts."}
{"headword": "hlaagi gyad", "definition": "noun olden times, old people\n-Shaggiet waal hlaagi gyad. The old people are meeting together."}
{"headword": "hlacksh", "definition": "noun claw Plural:hlikhlacksh\n-Shuulga hlacksha 'kalmoash. The crab's claws are fearsome."}
{"headword": "hlackshmshee", "definition": "noun toenail\n-Ggal 'nik'nuunga hlackshmsheeyn. Your toenails are too long."}
{"headword": "hlackshm'dsiwaalt", "definition": "noun fingernail\n-Ama'basha wil gyeda hlackshm'dsiwaaltn. Your fingernails are a pretty color."}
{"headword": "hlaggiack", "definition": "noun; verb curved knife for carving; to be bent\n-Shgu ndm geega shu hlaggiack. I have to buy a new carving knife."}
{"headword": "hla tgiyaa sha", "definition": "noun dusk\n(-).Lu'kwil gyeksha wil hla tgiyaa sha. It's peaceful at dusk."}
{"headword": "hla'ashg", "definition": "noun seaweed\n(-).Na dsaba nakshu hla'ashg ashda gi'dseeb da up lu'kwil 'tsamaatgd. My wife made some seaweed yesterday and it tasted real good."}
{"headword": "hla'at", "definition": "noun ball Plural:hlikhlaat\n-Ggal 'weelaeksha hla'ata gwee. That ball is too big."}
{"headword": "hla'kiackshg", "definition": "verb to climb\n-Mun hla'kiackshga hlgu awta da lack ggan. The porcupine climbed up the tree.\n-Na hla'kiackshgu da lackoa waab da geedsa tgeokshe. I climbed up on the roof and almost fell down."}
{"headword": "hla'kods", "definition": "noun rhubarb\n-Aam dm guulda hla'kods da gyalck. Hla meegt. It's time to gather the rhubarb outside. They're ripe."}
{"headword": "hlgaawg", "definition": "noun sister\n-Eh! lu'kwil ama'basha hlgaawgu. Wow! My sister is very pretty."}
{"headword": "hlgookshn", "definition": "verb to be unable, can't Plural: hlackhlgookshn\n(-)Hlgookshu dm hadikshu. I'm not able to swim.\n-Lu'kwil wilaay wila gyoa 'yoota bite hlgooksh'nu ndm hoy'ant. That man knows what he doing and I can't do it like him."}
{"headword": "hlguhlg", "definition": "noun small child\n-Lu'kwil wilgoashga na hlguhlgu. My small child is very intelligent."}
{"headword": "hlguhlgm noahlt", "definition": "noun doll\n-Yagwan dsaba dm na'acka hlguhlgm noahlsh Kayla. I am making a dress for Kayla's doll."}
{"headword": "hlgumad", "definition": "noun egg\n-Hailda hlgumad da ggagoom. The seagull has lots of eggs."}
{"headword": "hlgumadm ggagoom", "definition": "noun seagull egg\n-Hla guul gyad hlgumadm ggagoom. lu'kwil 'tsamaatgt gya'wn. People are looking for seagull eggs. It really tastes good now."}
{"headword": "hlgu shggay", "definition": "noun little finger, pinky\n-Sheepga hlgu shggayu. My little finger hurts."}
{"headword": "hlgutcka'oa", "definition": "noun cousin\n-Hashacku ndm nee hlgutcka'oayu. I want to see my cousin."}
{"headword": "hlguwoamhlg", "definition": "noun child, infant\n-Amaggoada hlguwoamhlga gwee. That little child over there is always friendly."}
{"headword": "hlgu 'yoota", "definition": "noun boy\n-Nagwaada hlgu 'yoota gwee. That is the boy's father."}
{"headword": "hlimoam", "definition": "verb to help\n-Aam hlimoamsh dp gwa'a. ahlgadee shm ggal aamhl wila load. Let's help these. They aren't doing well."}
{"headword": "hli'oan", "definition": "noun Indian bread\n-Eh! Wilaay nakshu dsaba hli'oan. Wow! My wife sure knows how to make Indian bread."}
{"headword": "hlmkdee", "definition": "noun brother\n-Yagwa goo hlmkdeeyu 'tu'itsgm ol. My brother is hunting for black bear."}
{"headword": "hloa", "definition": "verb to be fast, go fast\n-Lu'kwil hloa 'dsig'dsig da lack guyna. The car goes really fast on the road.\n-Lu'kwil hloa boadsh John Leask. John Leask's boat is really fast."}
{"headword": "hload", "definition": "verb to honor, respect\n-Wie aam mdm hloada 'yoota, aam wila howd da 'kam. Well, we should respect the man, what he says is good.\n-Hloadm na waabsh Shm'oygit ga Lackaga. We respect the house of the Lord."}
{"headword": "hloontee", "definition": "verb to be angry Plural:lukhloontee\n-Sha hloontee na shila hahlalshu. My coworker got angry all of a sudden.\n-Na hloontee n'dse'etsu awil ahlgandee dsabhl guyna. My grandmother got mad because I didn't fix the street."}
{"headword": "hlub", "definition": "verb to be deep\n-Hluba aksh dm wil hadikshu. The water is deep where I'm going to swim.\n-Na oom hoanu dowl hluba wil 'ken yeeh. I went fishing and the King Salmon was in deep water."}
{"headword": "hluk'kwdaa'yn", "definition": "noun grandchildren\n-Yagwa shayuu hlgu hluk'kwdaa'yn da 'koy. My little grandchild is hiding from me."}
{"headword": "hlumsh", "definition": "noun in-law\n-Hailda hlumshu gya'wn. I have a lot of in-laws now."}
{"headword": "hoan", "definition": "noun fish, salmon\n-Yagwa guba nagwaadu hoan. My father is eating fish."}
{"headword": "hoaya", "definition": "noun clothing Plural: hakhoaya\n-Hashacku shu hoaya. I want new clothes."}
{"headword": "homhom", "definition": "noun ankle\n-Sheepga homhomu. My ankle hurts."}
{"headword": "hoom", "definition": "verb to smell\n-Hoomu 'biyaan. I smell smoke."}
{"headword": "hoom'tsack", "definition": "verb to kiss\n-Oy hoom'tsack da hlgu teedsa. Throw the teacher a kiss."}
{"headword": "hoo'bl", "definition": "adverb at night\n-Hoo'bl dee wil gakshga na gga'dsaaw gyad. Some people are really awake at night."}
{"headword": "hou'ts", "definition": "noun duck\n-Ha'wahlgan dee nee wil gipaiga hou'ts I haven't seen the ducks fly."}
{"headword": "how", "definition": "noun voice\n-Gakshga hlguwoamhlg hlat tcka'noo na howsh noat. The child woke up when she heard her mother's voice."}
{"headword": "hoy", "definition": "verb to use, wear\n-Hoy bilaan, ggal 'weelaeksha na 'backshn. Wear a belt, your pants are too big."}
{"headword": "hoyack", "definition": "verb to be correct\n-'Hoyacka wila how hana'ack. The woman sounds right.\n(-)Lu'kwil aam wila gyoan. hoyacka hoyen. You're doing real well. What you're using is correct."}
{"headword": "hoyshg", "definition": "verb to be handsome, nice looking, pretty\n-Hoyshga madsiggalay. The flower is beautiful.\n-Hoyshga madsiggalay macksht da awaa waabn. The flowers by your house are beautiful."}
{"headword": "hukdsab", "definition": "noun somebody who can do many things well\n-Needsu shga hukdsabsh Tony. I see how many things Tony can do."}
{"headword": "hultg", "definition": "verb to be full Plural:halhultg\n-Hultga waabu da wineaya. My house is full of food.\n-Na aadm da gwashga, gawdee aadm dowla lu 'kend da lack boad dowla hultga'nm. We went fishing over there, when we were done fishing the boat was full."}
{"headword": "hultga giamg", "definition": "noun full moon\n-Dm gik hultga giamg dsidaawhl. It will be a full moon again tonight."}
{"headword": "ihlay", "definition": "noun blood\n-Ihlay 'dmggowsha doosha gwee. That cat's head is bleeding."}
{"headword": "kboal", "definition": "number ten people\n-Kboal shgaboo gyad dm tckoackgt. Ten people will eat."}
{"headword": "klushmsh", "definition": "noun Nass River\n-Shayaa shgaboo hoan da klushmsh. There are fewer fish in the Nass River."}
{"headword": "kshabatsk", "definition": "verb to stick out\n-Ahlgadee aamhl dm kshabatsga gga'bala da 'newalee. It's not good to have the gun stick out from the backpack."}
{"headword": "kshadsackoatg", "definition": "verb to be naked, nude, without clothing\n-Kshadsack'oatga 'yoota hla hadiksht. They were naked on the beach."}
{"headword": "kshagaa", "definition": "verb to take out\n-Kshagaa loagikshgm goda'ats ada 'yackt. Take out the soaking wet coat and hang it."}
{"headword": "kshagwaantg", "definition": "verb to come out\n-Hashacku dm 'kwihlbaayu hla kshagwaantga giamg. I want to run about when the moon comes out.\n-Ashda giyaatg dowla kshagwaantga 'wee giamg. Last night the big moon came out."}
{"headword": "kshalacklack", "definition": "verb to be born\n-Shuunt wil kshalacklackgu. I was born in the summer.\n-Gganhaada dee wil kshalacklackgn. You were born of the Raven."}
{"headword": "kshashashee", "definition": "verb to be barefooted\n-Kshasha ggashishee 'gubatguuhlg da gyalck. The children were barefooted outside.\n-Kshasha ggashishee 'gubatguuhlg, ahlgadeet da'acklga gyad dumt geega 'dsoacksh. The children were barefooted because the people weren't able to buy shoes."}
{"headword": "ksha'anaash", "definition": "verb to be naked, nude, without clothing\n-Ksha'anaash Hukdsab hla hadiksht. Tony went swimming naked.\n-Ahlgandee neehl wil ksha'anaash gyad hla hadiksht. I haven't seen people go swimming naked."}
{"headword": "ksha'dsal", "definition": "noun half-dried fish\n-Ahl anoackanee ksha'dsal? Do you like half-dried fish?"}
{"headword": "kshda'moash", "definition": "number nine abstract, round or flat objects\n-Kshda'moasha shgaboo noahl dm yoakshm. We're going to wash nine plates."}
{"headword": "kshdm'ashoal", "definition": "number nine people\n-Kshdm'ashoal gyad gwin daawhld da Gitsgaan. Nine people went over to Ketchikan."}
{"headword": "kshdnshoal", "definition": "number five people\n-Ksha kshdnshoal shaboo gyad dm leemeet. Only five people are going to sing."}
{"headword": "kshdsood", "definition": "noun waiter\n-'Tsuu hahlalsha kshdsood da wil loolgita gyad. The waiter worked hard where the people feasted."}
{"headword": "ksheel", "definition": "noun tear, teardrop Plural:ggaksheelt\n-Kshabaa ksheel hal wil shgaaygshgt. Her tears ran when she got hurt.\n-Hla weehowtgu da ksheelu. When I cry the teardrops come out."}
{"headword": "ksheeshg", "definition": "verb to settle for damages done\n-Luamaam ggaggoadm hla wil ksheeshga 'yoota. We were happy when the man settled for the damages."}
{"headword": "kshgoack", "definition": "verb to be first, ahead\n-Kshgoackt Nancy da 'koy. Nancy is first before me.\n-Na sha'apyaa'nu da lack geeka dowl ksgoacka nakshu. I was walking on the beach and my wife was ahead of me."}
{"headword": "kshi'nag", "definition": "noun middle finger\n-Kshi'nag de hoyu hlan lu 'dsaicka wineaya da ggiehlu. I use my middle finger to lick out the bowl."}
{"headword": "kshlushg", "definition": "noun shirt Plural:ggakshlushg\n-Aam 'ka shakshn kshlushgn. 'tsa'tsiksht. Clean your shirt. It's dirty."}
{"headword": "kshlushgm noak", "definition": "noun nightgown\n-Dm hoyu kshlushgm noak dsihla noakee. I'm going to wear a nightgown when I go to bed."}
{"headword": "kshuud", "definition": "noun autumn, fall\n-Dm guuldm hoan dsihla kshuud deehl goamshm. We'll harvest fish in the fall and winter."}
{"headword": "kwdacksh", "definition": "verb to go away from, leave a place\n-Dm kwdackshm ggaldoa. Dm luyeltgm hloula aam lacka. We're going to leave the village. We'll return while the weather's good."}
{"headword": "kwdag", "definition": "verb to shoot (arrow, gun)\n-Ggabackshga'nu hla kwdaga 'yoota. I was startled when the man shot the gun."}
{"headword": "kwdee", "definition": "verb to be hungry Plural:lukwdee\n-Hla kwdeeyu. I'm hungry.\n-Na shaupwaalckshm ashda 'guulda shada dowl lu'kwil kwdeeyu dowla luyeltgm. We went walking the other day and I got hungry so we came home."}
{"headword": "kwdoosh", "definition": "noun knife\n-Giloamdsa 'koa'olda kwdoosh. Don't forget the knife."}
{"headword": "kwhlacksh", "definition": "verb to kick; to press, put weight on\n-Kwhlackshu hla'at da awaa 'yoota gwee. I kicked the ball to the man there."}
{"headword": "kwhlackshhla'at", "definition": "noun football\n-Goahl shm anoacka gyad kwhlackshhla'at? Why do people really like football?"}
{"headword": "kwhleeggiackn", "definition": "verb to scrape, grind to pieces\n-Shu mdm kwhleeggiackn na anaasha wun. You have to really scrape the deer hide."}
{"headword": "kwhlee ggolggol", "definition": "verb to come apart entirely, to be nothing left\n-Kwhlee ggolggol boad da wil 'dsuu baashg. The wind tore the boat apart until it was gone."}
{"headword": "kwhleeyedsg", "definition": "verb to pound\n-'Naga hahlalsht n'dse'etsu hlat kwhleeyedsa hla'ashg. My grandmother worked a long time when she pounded the seaweed."}
{"headword": "kwhlee'ba'gya", "definition": "verb to be dented; to bend, dent badly\n-Kwhlee'ba'gya 'dsig'dsig da wil oksha 'wee loab. The big rock that fell dented the car."}
{"headword": "kwhlee'doosh", "definition": "verb to punch; to knock out\n-Da'apsh en kwhlee'doosht Dan. David knocked Dan out."}
{"headword": "kwhlee'kayaan", "definition": "verb to hit, beat up with a club\n-Kwhlee'kayaan 'wee hoan, hloula didoolsht. Hit the big fish, it's still alive."}
{"headword": "kwhl'aack", "definition": "noun lips\n-Ashguu kwhl'aacka hlguwoamhlg hla hloonteed. The child's lips are funny when he's angry."}
{"headword": "kwshdoonsh", "definition": "number five flat, round or abstract objects\n-Kwshdoonsha mashgm 'na'ba'la dm geegu. I'm going to buy five red buttons."}
{"headword": "kw'dsag", "definition": "noun slingshot\n-Kw'dsag hoysh Kayla hlat goo hla'at. Kayla used a slingshot to shoot the ball."}
{"headword": "kyoagg", "definition": "noun grass\n-Lu'kwil meehoksha kyoagg hla 'kotst. Grass smells really good when it's cut."}
{"headword": "laaksha aksh", "definition": "noun high tide\n-Dm shigyoatgm dsihla laaksha aksh. We will leave at high tide."}
{"headword": "laakwsh", "definition": "noun light\n(-).Lu'kwil hailda laakwsh da lack guyna. There are lots of lights on the street."}
{"headword": "laald", "definition": "noun worm\n-Needsu laald da nhluu loab. I saw a worm under the rock."}
{"headword": "laaltg", "definition": "verb to be slow Plural:ggalaaltg\n-Labite laaltga wila gyoa 'yoota gwee. That man is slow."}
{"headword": "laam", "definition": "noun alcohol\n-Giloamdsa geega laam. Don't buy alcohol."}
{"headword": "laan", "definition": "noun salmon eggs\n-Shm ama goa laan, 'nee dm hoym hla goog hla'ashgm. Fish eggs are really good, that's what we'll use when we cook seaweed."}
{"headword": "laandsa", "definition": "prefix to start\n-Laandsa shaggiet 'koal ggaggoadm. Let's all be of one heart."}
{"headword": "laa'wil", "definition": "verb to wrap up\n-Laa'wil ckbeesh nagoaga mdm hiedst. Wrap up the box before you send it."}
{"headword": "labaalck", "definition": "verb to detest, hate\n-Ahlgadee shguuhl dm labaalcka shila gyadn. You don't have to hate your fellow man.\n-Labite hloontee wila waal 'yoota gwee da labaalcku wila howt. That man was angry and I detested what he was saying."}
{"headword": "labaggietwaal", "definition": "verb to do something wrong, make a mistake\n-Ahlgadee hashacku dm labaggietwaalu. I don't want to do something wrong.\n-Lu'kwil ahlgadee aamhl wila gyoa 'yoota gwee, labitewaalt. That man did not do good, he did something wrong."}
{"headword": "laba'on", "definition": "noun arm muscle\n-'Weelaeksha laba'onsh Alik. Alec has large arm muscles."}
{"headword": "lack", "definition": "prefix on, upon\n-'Lee shguu wush da lack ha'li'dameesh. Put the blanket upon the table."}
{"headword": "lacka", "definition": "noun sky\n-'Kineetgu ashda gganhlaaga dowl lacka wil nee'etsgu ndm nee dsihla waash. When I woke up the other morning and I looked up to the sky to see if it would rain."}
{"headword": "Lackaga", "definition": "noun above, Heavens, weather\n-Ahl tckanooynee goal dm wila waal Lackaga dsigi'dseeb? Have you heard what the weather is going to do tomorrow?"}
{"headword": "lackdee", "definition": "adverb on the hill\n-Needsu wun da lackdee. I can see the deer on the hill."}
{"headword": "Lack-giboo", "definition": "noun Wolf Clan\n-Lack-giboo wil hokshgt nakshu. My husband belongs to the Wolf Clan."}
{"headword": "lack guyna", "definition": "adverb on the road\n-Lu'kwil hloa wila baa 'dsig'dsig a lack guyna. The car is going to fast on the road."}
{"headword": "lackhoo", "definition": "noun sand bar\n-Na 'yagayaam da lackhoo, nayaayu, gwinee'dsn da wil 'ken ha'dsalt, dowlt 'waad da lack loab. My grandfather and I walked down to the sandbar and he showed me where the devilfish was and we found it on the rock."}
{"headword": "Lack-shgeeg", "definition": "noun Eagle Clan\n-Lack-shgeeg wil hokshgu. I belong to the Eagle Clan."}
{"headword": "lackshumaay", "definition": "noun month of picking berries, summertime\n-Yagwa shamaayt. He/she is picking berries."}
{"headword": "lackshuulda", "definition": "noun ocean\n-Baasha'nu hla 'weelaeksha ggoab da lackshuulda. I get afraid when the waves on the ocean are big."}
{"headword": "lack waalee magwa'ala", "definition": "verb to have hard times\n-Tckanooyu wil lack waalee magwa'ala hlaagigyad. I heard that old people had hard times."}
{"headword": "lackyuub", "definition": "adverb on the ground\n-'Lee shguu lag da lackyuub. Lay the firewood on the ground."}
{"headword": "lack'aksh", "definition": "adverb on the water\n-Gyoaksha 'wee ggan a lack'aksh. The tree is floating on the water."}
{"headword": "lack'anaaym uua", "definition": "verb to boil ooligans in a pot\n-Wie dsa dup dsam lack'anaaym uua. Let's boil some ooligans in a pot."}
{"headword": "lack'awsh", "definition": "adverb on the sand\n-Wiedsa sha lagm da lack'awsh. Lets build a fire on the sandy beach."}
{"headword": "lack'daa", "definition": "noun lake\n-Hailda 'ts'uu'uts da lack'daa. 'Nee dm goym. There are a lot of birds on the lake. That's where we're going."}
{"headword": "lack'dsimaay", "definition": "adverb on the barnacles\n-Ama needsn da lack'dsimaay. Be careful on the barnacles."}
{"headword": "lack'oa", "definition": "noun top of\n-'Lee shguu sha'winshg da lack'oa ha'li'dameesh. Put the paper on the table."}
{"headword": "lack'oa waab", "definition": "noun roof\n-Na hla'kiackshgu da lack'oa waabu da goadsa wila waalu, ahlgadee da'ackgu dm tgiyaayu. I climbed on my roof and couldn't do anything, I wasn't able to get down."}
{"headword": "lack'U", "definition": "noun muskeg; upon muskeg\n-Ama needsa wila yaan da lack'U. You have to walk carefully on the muskeg."}
{"headword": "lag", "definition": "noun fire, firewood\n-Wie dsadp shietdoa lag. Let's gather wood."}
{"headword": "lageel", "definition": "noun eyebrow, eyelashes\n-Yagwat 'kockda hana'ack na lageelt. The woman is plucking her eyebrows."}
{"headword": "laggee", "definition": "noun hair-kelp for herring eggs to cling to\n-'Ka anoacku cksh'waanck da lack laggee. I like herring eggs on hair kelp the best."}
{"headword": "laguulgit", "definition": "noun; verb burnt possessions of a dead person; to burn possessions of a dead person\n-'Guul ganootg dm daawhlt nagoacka dm laguulgita gyad. People are supposed to wait one week before they burn."}
{"headword": "lapwail", "definition": "noun frying pan\n-Lu tckalgwalga na lapwailu. My frying pan is burned inside."}
{"headword": "lawaal", "definition": "noun happening\n-Luamaam ggaggoada gyad da lawaalt. The people were happy at the gathering."}
{"headword": "la'uu", "definition": "noun trout\n-Ggal hailda shayb da la'uu, 'nee gn ahlgndee anoackt. There are too many bones in a trout, that's why I don't like it."}
{"headword": "lebilt haaw", "definition": "verb to argue against\n-Lebilt haaw hana'ack hlat tckanoo wil bee'ega hlguhlgt. The woman argued when she heard her child lie."}
{"headword": "leediksh", "definition": "verb to awaken\n-Leedikshgn 'gubatguuhlg. Wake up children.\n-Leedikshga hlguyu dm ggashgoolt gganhlaagagwa'a. My children woke up to go to school this morning."}
{"headword": "leemee", "definition": "noun; verb song; to sing\n-Hla dsudsu dowla leemeeym da Shm'oygit 'dsm lacka. We went to church and sang to God in Heaven."}
{"headword": "leemya'tseshg", "definition": "noun fur animal\n-Hailda leemya'tseshga wil 'kohla 'dsig'dsig. There's a lot of animal fur on the highway."}
{"headword": "leetsg", "definition": "noun; verb grouse; to count\n-Moakshga na shamee leetsg. Grouse meat is white."}
{"headword": "le'wul", "definition": "noun drops of water, water drops\n-'Nawinoa le'wul da lack wileelm tgwayu. The water drops on my eyeglasses are annoying."}
{"headword": "ligeetnaa", "definition": "noun anybody, anyone, anything, somebody, someone, something\n-Ligeetnaa dm ent geega gwa'a. Anyone will buy this."}
{"headword": "liggiwaal", "definition": "noun belongings, possessions, clothing\n-'Gwaatga tcka'nee na liggiwaalsh Peda da 'dsm lag. All of Peter's belongings were lost in the house fire."}
{"headword": "ligi", "definition": "conjunction or\n-'Nuuyu ligit 'nuun dm daawhlt da Gitsgaan. Either you or I will go to Ketchikan."}
{"headword": "likshgyad", "definition": "noun something else, a different thing\n-Likshgyadm ggaldsap wil 'waatgm. We come from a different village."}
{"headword": "likshgyadmgyad", "definition": "noun a different person, someone else\n-Likshgyadmgyad 'daad da awaayu. A different person sat by me."}
{"headword": "likshoack", "definition": "noun door\n-'Kacka likshoack. giamga gyalck. Open the door. It's warm outside."}
{"headword": "liksh'daa", "definition": "noun island\n-Liksh'daa gyalck wil wun shgoosheedm. The island is where we plant potatoes."}
{"headword": "lipgeekhl", "definition": "interjection Buy it yourself!\n-Lipgeekhl. Buy it yourself."}
{"headword": "liphahaw", "definition": "verb to be ineffective\n-Ahlgadee amooksha gyad dish 'need awil liphahawd. Nobody listens to her because she's ineffective."}
{"headword": "liphown!", "definition": "interjection Say it yourself!\n-Liphown na algyacka Shm'oygit ga Lackaga awil dm ggatgyadn. Say the words of God to yourself so you will be strong."}
{"headword": "liplaid", "definition": "noun minister, pastor, preacher, priest\n-Shmhow algyacka liplaid. The pastor preached the truth.\n-Gatgyada amhow liplai da gwa'a. The pastor has a strong voice."}
{"headword": "lipnahow", "definition": "verb to talking to oneself\n-Shiggene'etsga gyad da hana'ack hla lipnahowt. People stared at the woman when she talked to herself."}
{"headword": "lish'yaan", "definition": "noun boil (on the skin); mink\n-Dm 'manu haldaaksh da lish'yaan. I'm going rub medicine on boil.\n-Hailda lish'yaan da nlack yuubu. There are a lot of mink on my trap line."}
{"headword": "loab", "definition": "noun rock, stone Plural:liploab\n-Geedsa sha'okshu da lack loab. I almost fell down on the rock."}
{"headword": "loan", "definition": "noun horse clam\n-Wilaaym wil 'dahla loan. We know where the horse clam can be found."}
{"headword": "loa'ds", "definition": "noun elderberries\n-Dm guuldm loa'ds dsihla dsigi'dseeb. We'll pick elderberries tomorrow."}
{"headword": "loolgit", "definition": "noun feast\n-Dm hoym gwish'na'ba'la dsihla loolgit. We will wear a button blanket when there is a feast."}
{"headword": "loolp", "definition": "noun fish trap\n-Ahlgadeet naa en hoy loolp da sha gya'wn. Nobody uses fish traps today."}
{"headword": "loonda hloadihl", "definition": "verb to put together\n-Yagwat loonda hloadihla taggan awil dmt dsaba guyna. He's putting the planks together because he's making a path."}
{"headword": "loopg", "definition": "verb to sew\n-Hla loopgat noayu shu goda'ats. My mother is sewing a new coat."}
{"headword": "loyg", "definition": "verb to move camp\n-Ggal hailda loygn. You packed too many things with you."}
{"headword": "ludaaltg", "definition": "verb to meet\n-Ndm ludaaltgn da awaa ggaldmwa'at. I will meet you at the store."}
{"headword": "ludaawhla giamg", "definition": "noun afternoon\n-Shoonaahla'nu hla ludaawhla giamg. I am tired in the afternoon."}
{"headword": "ludamdam", "definition": "verb to hug\n-Needsu wil ludamdamcksh Dush hlgu 'yoota. I saw Doris hug the man."}
{"headword": "ludoa", "definition": "verb to be inside\n-Ludoa hoan da 'dsm gwai'hl. Put the fish in the sack."}
{"headword": "ludoahl", "definition": "verb to put inside\n-Ludoahl da 'dsm gi'dsoan. Put it into the closet."}
{"headword": "lugowshga aksh", "definition": "noun low tide\n-Wie hla lugowshga aksh. Aam dm sha ggaboackm. The tide is low. Let's get some cockles."}
{"headword": "lugwaantg", "definition": "noun time for\n-Hla lugwaantga dm wil yaawckga hlguwoamhlg. It's time for the little child to eat."}
{"headword": "luhoa'Nhl", "definition": "verb to fill\n-Luhoa'N oomhl da 'koy? Will you fill the bucket for me?"}
{"headword": "lukhleehoaya", "definition": "noun undergarment\n-Ahl shakshakshga na lukkwhleehoyyan? Are your underclothes clean?"}
{"headword": "lukhleekshlushg", "definition": "noun undershirt\n-Ggal gyamga hlguwoamhlg, 'nee gun ahlgadeet hoy lukhleekshlushg. The child was too warm, that's why he didn't wear an undershirt."}
{"headword": "lukhlee'backsh", "definition": "noun underpants\n-Hoy lukhlee'backsh da nhluu 'backsha dsinan. Wear underpants under your jeans."}
{"headword": "lumaaksh", "definition": "verb to wash clothing or soft material\n-Yagwat lumaaksha lukhleehoyyat. She is washing her undergarments."}
{"headword": "lup na waal", "definition": "verb to fight, compete against each other\n-Lu'kwil lup na waal hlaagi gyad. Our ancestors competed against each other.\n-Lup na waalm hla hla'atm da Town Hall. We compete against each other when we play basketball at the Town Hall."}
{"headword": "luwantg", "definition": "verb to worry\n-Luwantga ggoada hana'ack hla 'gwaatga naksht. The woman worried when her husband was lost."}
{"headword": "luwantgmggoad", "definition": "verb to be worried\n-Luwantgmggoadu hla 'tsuu baashg. I get worried when the wind is strong."}
{"headword": "luyeltg", "definition": "verb to return, turn back\n-Dm luyeltga'nu da awaash noayu. I'm returning to mothers."}
{"headword": "lu'bish", "definition": "verb to sew\n-Yagwat lu'bishga gwish'na'ba'lat. She is sewing on her button blanket."}
{"headword": "lu'dsakya", "definition": "verb to go out (of fire)\n-Hl'loontee hana'ack hla lu'dsakya lag. The woman was angry when the fire went out."}
{"headword": "lu'gen", "definition": "verb to put in\n-Lu'gen ggan'dameesh da 'dsm ckbeesh. Put the pencil in the box."}
{"headword": "lu'kwil", "definition": "verb to be many, very\n(-)-Lu'kwil 'tsimaatga ai'dsm tckow. Fried halibut tastes very good."}
{"headword": "lu'kwil ama ggoad", "definition": "verb to be a kind person\n(-)'Lu'kwil ama ggoadish Meli. Mary is very kind.\n-Lu'kwil ama ggoada 'yoota gwee dat 'gilm daala da 'koy. That man is very kind and he gave me money."}
{"headword": "lu'wai", "definition": "verb to get caught in the act, be found out\n-Lu'wai nakst da wila loat. His wife found out what they were doing."}
{"headword": "lu'wal", "definition": "leak\n-Luwantga ggoada 'yoota hlat nee wil lu'wal ckshoa. The man was worried when he saw that his canoe leaked."}

```jsonl
{"headword": "maackee", "definition": "noun rainbow\n-Gyeksha ggoadu hlan nee maackee. My heart is peaceful when I see as rainbow."}
{"headword": "maadm", "definition": "noun falling snow\n-Hladm yaa maadm. It's going to snow."}
{"headword": "maadm gyekshg", "definition": "noun calm in the weather\n-Dm gwindaawhlm da Gitsgaan dsihla maadm gyekshg. We'll go over to Ketchikan when there's calm weather."}
{"headword": "maash", "definition": "noun bark ( of a tree); leg cramp\n-Maasha asheeyu awil gwatga sha. I have a leg cramp because it's a cold day.\n-Ckdsee na maasha 'wee ggan gwa'a. This tree has thick bark."}
{"headword": "maaw", "definition": "noun chin\n-Babaa maaw hlgu 'yoota. The boy's chin is trembling."}
{"headword": "maay", "definition": "noun berries, fruit\n-Ahl dm shimaaya'nee? Are you going berry picking?"}
{"headword": "maayha gwilhoo", "definition": "noun rope berry, trailing blackberry\n-Macksha maayha gwilhoo da lack 'daa gwee. Trailing blackberries grow on that island over there."}
{"headword": "maaym ggaagg", "definition": "noun raven berries\n-Ahl anoackanee maaym ggaagg? Do you like raven berries?"}
{"headword": "maaym ggalipleeb", "definition": "noun thunder berries\n-Goahl wil gyeda maaym ggalipleeb? What color are thunder berries?"}
{"headword": "maaym ol", "definition": "noun bear berries\n-Ahl needsnee maaym ol? Have you seen bear berries?"}
{"headword": "mackla", "definition": "adverb through a sea channel\n-Hashackt dmt 'waay mackla. He wants to find the sea channel."}
{"headword": "madeeg", "definition": "noun bear, brown bear, grizzly bear\n-Baasha'nu ndm nee hailda madeeg da 'kala aksh. I'm afraid to see lots of bears on the river."}
{"headword": "madsiggalay", "definition": "noun flower\n-Ama'basha wil macksh madsiggalay da na 'dsaa waab. The flower (house plant) is beautiful inside the house"}
{"headword": "madsigga'aam", "definition": "noun medicine plant\n-Dm guuldm madsigga'aam. We'll search for medicine plant."}
{"headword": "maggoab", "definition": "verb to be seasick\n-Maggoaba hlguwoamhlg hla 'tsuu lackaga. We went to Ketchikan one day and my wife got seasick."}
{"headword": "maggoanshga", "definition": "verb to be curious of details, inquire into\n-Wie, maggoanshga gwa'a da 'koy. Well, explain this to me."}
{"headword": "magool", "definition": "noun strawberry\n-Ndahl wil macksha magool? Where do the strawberries grow?"}
{"headword": "magwa'ala", "definition": "noun deep winter, hard times\n-Gwilm ggowdee wineaya awil hladm goidiksha magwa'ala. Get the food stored because deep winter will soon be here."}
{"headword": "mahaaya", "definition": "noun dry rot\n-Hla mahaaya 'wee ggan. The big tree is dry rotting."}
{"headword": "mahl", "definition": "verb to tell\n-Ndm mahlda nagwaadn goa wila gyoan. I'm going to tell your father what you're doing."}
{"headword": "mahluu", "definition": "noun pillow\n-'Lee shguu mahluu da lack ha'linoak Put the pillow on the bed."}
{"headword": "mala", "definition": "verb to hurry, be in a hurry\n-Ggal mala'nu hlan shakshn waab. I was in too big a hurry when I cleaned the house."}
{"headword": "malamwaal", "definition": "verb to hurry while doing something\n-Ahlga aamhl dm malamwaaln dsihla gigeengwackhln. It's not good to hurry when you're praying."}
{"headword": "mala'ka'kuhl", "definition": "verb to run a race against each other\n-Shoonaahla 'yik'yoota hla gawdee mala'ka'kuhlt. The men were tired after they raced against each other."}
{"headword": "malshg", "definition": "noun; verb story, tale; to narrate, tell\n-Dackshm 'daa hlu hana'ack hla yagwa malshga n'dse'etst. The little girl sat still while her grandmother told a story."}
{"headword": "malshgm sha'winshg", "definition": "noun newspaper\n-Geegu malshgm sha'winshg da tcka'nee sha. I buy a newspaper every day."}
{"headword": "malshgm 'tu'itsg", "definition": "noun telephone\n-Ggal ckshdaamcka hashoycka malshgm 'tu'itsga geegu. The bell on the telephone I bought is too loud."}
{"headword": "malwoa", "definition": "noun navy ship, ship of war\n-Needsm malwoa da lackshuulda. We could see a ship of war way out on the ocean."}
{"headword": "manggoahl", "definition": "verb to go up and get\n-Naahl dm en manggoahlt? Who's going to go up and get it?"}
{"headword": "mashg", "definition": "noun red\n-Shm mashga ggowsha hlgu hana'ack. The girl's hair is red.\n-Goahl wilgyedu gwa'a? What color is this?"}
{"headword": "mashgm'ol", "definition": "noun brown bear\n-Yagwa goo hlmkdeeyu mashgm'ol. My brother is hunting for brown bear."}
{"headword": "mat", "definition": "verb to want someone's food\n-Ahlgadee dsoagga hlgu 'yoota hlat mata goa gubu. • The little boy wasn't ashamed when he wanted what I was eating."}
{"headword": "mati", "definition": "noun sheep\n-Hailda mati da sha'neesh. There's lots of sheep on the mountain."}
{"headword": "ma'koacksh", "definition": "noun salmonberry\n-Hla meega ma'koacksh. The salmon berries are ripe."}
{"headword": "ma'oan", "definition": "noun elbow; night pot\n-Gyidi'oksha ma'oanu. I hit my elbow.\n-Sha gatsa ma'oan. Empty the night pot."}
{"headword": "ma'ul", "definition": "verb to faint\n-Ggal 'tsuu gyamg 'nee gun ma'ult. The heat was so hot it made her faint."}
{"headword": "ma'watsa", "definition": "verb to act silly\n-Ma'watsa hlguwoamhlga gwee. That child is acting very silly."}
{"headword": "meeg", "definition": "noun squall\n-'Dsilmbaa gyad hla meega lacka. People ran indoors when the squall came."}
{"headword": "meehoksh", "definition": "verb to be fragrant, smell good Plural:mikmeehoksh\n-Meehoksha madsiggalay da awaa na waabn. The flowers by your house smell good.\n-Na googish Charlie 'wee hoan da up lu'kwil meehoksha wil waalt. Charlie was cooking a big fish and it really smelled good where he was at."}
{"headword": "meelg", "definition": "verb to dance Plural:makmeelg\n-Shila meelgee. Dance with me.\n-Hladm meelga'nu. I am going to dance.\n-Hla gowdee naksha gyad dowla meelg wila waald hladm giloat. After people get married then they dance until the celebration was over."}
{"headword": "meeyoob", "definition": "noun rice\n(-).Lu'Kwil 'tsamaatga meeyoob ada enta hoan. Rice and canned fish really taste good."}
{"headword": "meeyoobm 'Tsmshian", "definition": "noun Indian rice\n-Na gwinee'dsinsh n'dse'etsu goa dm wila guba meyoobm 'Tsmshian, 'nee dsabt da 'kam. My grandmother showed me how to eat Indian rice, that's what she made for us."}
{"headword": "mela goo'bl", "definition": "quantifier both\n-Hoy mela goo'bl an'on. Use both hands."}
{"headword": "meyaan", "definition": "noun Chief, head of\n-Lu'kwil amaggoada Meyaanm. Our Chief is a very kind person."}
{"headword": "me'ish", "definition": "noun milk, woman's breast\n-Ahlgadee 'tsamaatga me'ishm mishmoosh. Cow milk does not taste good."}
{"headword": "mihla", "definition": "quantifier each\n-Gi'lm mihla 'guulda daala da 'gubatguuhlg. Give a dollar to each of the children."}
{"headword": "mihleetg", "definition": "noun green\n-Mihleetga 'yansh. The leaves are green."}
{"headword": "mileed", "definition": "noun steelhead trout\n-Weehowtgt n'dse'ets dat nee mileed 'gilmum dish 'need. My grandmother cried when she saw the steelhead trout I gave her."}
{"headword": "mishmoosh", "definition": "noun bull, cattle, cow\n-Ahlgandee nee mishmoosh da wil dsoackm. I don't see any cows where we live."}
{"headword": "mishoa", "definition": "noun sockeye salmon, red salmon\n-Lu'kwil 'tsamaatga mishoa. Sockeye is very tasty."}
{"headword": "mish'ol", "definition": "noun brown bear\n-Yagwat goo mish'ol. He is hunting for brown bear."}
{"headword": "mitmaatg", "definition": "noun something rotten, unsanitary\n-Ggal gyamga shamee da gyalck, 'nee gun mitmaatgt. The meat got too warm outside, that's why it's rotten."}
{"headword": "mi'tsa 'ka'aam", "definition": "noun licorice root\n-Ahl 'waayanee mi'tsa 'ka'aam? Did you find any licorice root?"}
{"headword": "moaksh", "definition": "noun snow on the ground\n-'Dsuu moaksh hla gukshgu da gganhlaag. There was lots of snow on the ground when I woke up in the morning."}
{"headword": "moakshg", "definition": "noun white\n-Hashacku moakshgm hla'at. I want the white ball."}
{"headword": "moakshgm'ol", "definition": "noun polar bear\n-Yagwa goo hlmkdeeyu da moakshgm'ol. My brother is hunting for polar bear."}
{"headword": "moalksh", "definition": "noun crabapple\n-Ahl dee 'tsamaa'anee moalksh? Do you like crabapples?"}
{"headword": "moalkshack", "definition": "verb to taste sour, citrusy\n(-).Na lu'kwil moalkshacka maay. The berries were very sour."}
{"headword": "moamsh", "definition": "verb to be crazy\n-Moamsha 'yoota gwee. That man is crazy."}
{"headword": "moan", "definition": "noun salt\n-Moan hoy gyad hlat dsaba hoan. People use salt to work on fish."}
{"headword": "moanm hoan", "definition": "noun salted fish\n-Aam shga hailda moanm hoan dsabn. It's good that you did a lot of salted fish.\n-Nayaayu ne en gwinee'dsn goa dm wila gyoayu dm dsaba hoan. Da 'nee wila gyoat, gwinee'dsn da koy, da 'nee shawaadid da gyad, moanm hoan. My grandfather showed me how to salt fish, that's what he did, he showed me, and that's what people call MOAnm hoan."}
{"headword": "moash", "definition": "noun thumb\n-Na sheepga moashu dowla na 'wee 'taabu da yagwan dsaba guyna. My thumb was hurt when I hit it as I worked on the street."}
{"headword": "moashm shee", "definition": "noun big toe\n-Shgaaygshga moashm sheeyu. My big toe is wounded."}
{"headword": "moatg", "definition": "verb to rescue, save Plural:lumoatg\n-Moatga hlguwoamhlg hlgu 'tsu'uts. The child saved the little bird."}
{"headword": "moa'ackg", "definition": "noun a very kind person\n-Anoacka gyad shga moa'ackga liplaid. People like the preacher's kindness."}
{"headword": "moolaa", "definition": "noun sawmill\n-Wie hailda ggan 'kotsa moolaa. The sawmill cuts a lot of wood.\n-Moolaa wil hahlalsha na gga'dsaaw 'yoota. Some of the men work at the sawmill."}
{"headword": "mun", "definition": "prefix upwards\n-Mun ne'etsgm da lacka hla tcka'nooym 'wee gipaiganshg. We looked up at the sky when we heard the big airplane."}
{"headword": "mundockhl", "definition": "verb to bring up\n-Mundockhl da lacka. Bring them upstairs.\n-Mundocka hali'daa da lacka. Bring the chair upstairs."}
{"headword": "mungaa", "definition": "verb to lift up; up towards\n-Hlauda Shm'oygit ga Lackaga ada mungaa gga'an'on. Praise the Lord and raise up your hands."}
{"headword": "mungaahl", "definition": "verb to pick up\n-Mungaahl da lacka. Pick it up and take it upstairs."}
{"headword": "muntckadockhl", "definition": "verb to carry along with other things\n-Ayinshinhl mdm muntckadockhla lapwail ada wineaya? Aren't you going to take the frying pan and the food?"}
{"headword": "munyaa", "definition": "verb to ascend, go up, walk up Plural:mnwaalcksh\n-Ama'pasha wil munyaa giamg. It's beautiful when the sun comes up.\n-Na sheepgu ashda 'guulda sha dowla munyaa hlgugu dumt nee wila waalu. I was sick the other day and my son came to see me."}
{"headword": "mun'doosh", "definition": "verb to push up\n-Baalda hlguwoamhlg dumt mun'doosha 'wee ggan. The little child tried to push up the board."}
{"headword": "naa", "definition": "noun; interrogative breath; who?\n-Naadu en guba hoan? Who is eating fish?"}
{"headword": "naashu", "definition": "noun raspberries\n-Naashu hashacksh n'dse'etsu hla sheepgt. My grandmother wanted raspberries when she was sick."}
{"headword": "naat", "definition": "vocative term of endearment towards a male\n-Nda wila waan, naat, dayat n'dse'etsu dish Lally. How are you, dear one, said my grandmother to Larry."}
{"headword": "naay", "definition": "noun mother\n-Dm geegu anaay dish naayu. I am buying some bread for my mom."}
{"headword": "nacknock", "definition": "noun supernatural being, power\n-Baasha gubatguuhlg da adaawckm nacknock. The children are afraid of stories about supernatural beings."}
{"headword": "nacknockm hana'ack", "definition": "noun clever woman, woman cheater, woman trickster\n-Nacknockm hana'ack dsoackt da liksh'daa gwee. A woman with supernatural powers lives on that island."}
{"headword": "nacknockm 'yood", "definition": "noun cheater, trickster\n-Nacknockm 'yood na nakshsh melee. Mary's husband is a trickster."}
{"headword": "Nadzaheen", "definition": "noun fish camp on Annette Island\n-Nadzaheen wil dsoacku. I live at the fish camp on Annette."}
{"headword": "na gga'dsaaw", "definition": "quantifier a few, some\n-Na gga'dsaaw 'bil'bal dm hoyu. I'm going to use a few of the buttons."}
{"headword": "nagwaadu", "definition": "noun my father\n-Ndadut nagwaadu? Where's my father?"}
{"headword": "nagwaat", "definition": "noun father of\n-Babooda hlguwoamhlg dm wil luyeltga nagwaat. The child waited for her father to return."}
{"headword": "nahaapt", "definition": "noun box cover, lid\n-'Lee shguu nahaapt. Put the lid on."}
{"headword": "naksh", "definition": "noun; verb spouse; to marry\n(-).Lu'kwil aam ggaggoadish Tony deesh Donna May wil gatgoidikshd. Tony and his spouse Donna May are very happy that they arrived."}
{"headword": "nanu", "definition": "verb to misbehave\n-Lu'kwil nanu 'gubatguuhlg da 'dsm waabshgool. The children in the school were misbehaving."}
{"headword": "nashmhowtksh", "definition": "noun; verb something that one believes in; to promise\n-Na mahla 'yoota da 'koy goa dm wila gyoayu. Nashmhowtksht, 'nee wila gyoayu. That man told me what to do and it was true so that's what I did."}
{"headword": "nayaa", "definition": "noun grandfather\n-Hla backgawdee na gganayaatgm. All our grandfathers are gone."}
{"headword": "nayaan", "definition": "noun your grandfather\n-Amookshn da nayaan. Listen to your grandfather."}
{"headword": "nayaat", "definition": "noun his/her grandfather\n-Needsu nayaat da awaa ggaldmwa'at. I saw her grandfather by the store."}
{"headword": "nayaayu", "definition": "noun my grandfather\n-Yagwa goom leetsgut nayaayu. My grandfather is hunting for grouse."}
{"headword": "na'a", "definition": "noun mother\n-Dm geegu anaay dish na'a. I am buying some bread for my mom."}
{"headword": "na'ack", "definition": "noun baby sister; dress, skirt Plural: ggana'ack\n-Lu'kwil taggoada hlgu na'ack. The little baby girl is very content."}
{"headword": "na'dsiksh", "definition": "noun fish tail\n-Sha 'kotsa tcka'nee na'dsiksh. Cut off all of the fish tails."}
{"headword": "na'dum", "definition": "1. verb to draw, write\n-Na'dum na waan da lack sha'winshga gwa'a. Write your name on this paper.\n-Na gi'dsoycka boad na'dum na waat. The name of the boat is written on the bow.\n2. verb to write\n-Na'dumt Father Duncan goa mahldid da 'kam. Father Duncan wrote down everything he said to us."}
{"headword": "na'waan", "definition": "noun what you got; what you have\n-'Gilm na'waan da hlmkdeeyn. Give what you have to your brother."}
{"headword": "nda", "definition": "interrogative go away!; how, when, where\n(-).Ndahl mawil geegdu gooda'ats? Where did you buy your coat?"}
{"headword": "ndada", "definition": "interrogative where?\n-Ahlgandee wilaay ndahl wil shgu shu hla'at geegn. I don't know where the new ball is that you bought."}
{"headword": "ndashda", "definition": "interrogative where?\n-Ndashda wil shguu shu gooda'atsu? Where could my new coat be?"}
{"headword": "nee", "definition": "verb to look at, see\n-Needsu hash ada doosh. I see a dog and a cat."}
{"headword": "Neesh hlagganoosh", "definition": "noun Git Lan Chief\n-Neesh hlagganoosh waa 'wee Shim'oygit. The Chief's name is Neesh hlaggaNOOSH."}
{"headword": "neeyaash", "definition": "noun grandfather of\n-Alik waa neeyaash lobat. Alec is the name of Robert's grandfather."}
{"headword": "ne'etsg", "definition": "verb to look at\n-Ne'etsgut dup gwee da awaa 'dsig'dsig. They were all looking at the car."}
{"headword": "nhluu", "definition": "verb to be under\n-Nhluu hali'daa wil shgu hla'at. The ball is under the chair.\n-Nhluu waabm wil dsoacka 'wee hash. Underneath our house is where that big dog lives."}
{"headword": "Nishgaa", "definition": "noun Nass River people\n-Dsoackt nabeebu da shbaggiet git Nishgaa. My uncle lives among the Nass River People."}
{"headword": "nlag", "definition": "noun fireplace\n-Hladm shagwaldu nlag. I will light the fireplace."}
{"headword": "nlip 'dsabam", "definition": "noun our brothers, our own people\n-Hyda nlip 'dsabam dup gwee. They are like our brothers."}
{"headword": "nloo'bish", "definition": "noun thread\n-Shgu dm geegu moakshgm nloo'bish. I have to buy white thread."}
{"headword": "noa", "definition": "noun mother\n-Dm geegu anaay dish noayu (na'a). I am buying some bread for my mom."}
{"headword": "noahl", "definition": "noun dishes\n-Dm yoakshn noahl. You're going to wash the dishes."}
{"headword": "noak", "definition": "verb to lie down Plural:laahlk\n-Wie dm 'ka noaku, aam shm ama shgwaitgu. Well, I'm going to lay down. I'll have a good rest."}
{"headword": "noo", "definition": "noun halibut hook\n-Nabeebu ent dsaba noo da 'koy ndm gidigaa hoan. My uncle made the halibut hook for me so that I could catch fish."}
{"headword": "noogit", "definition": "noun apparition, ghost, spirit, vision\n-Lu wun noogit da 'dsm loab, daya naga'tsaaw gyad. There are spirits in the cave, that's what some people say."}
{"headword": "nootg", "definition": "verb to get dressed up\n-Shm ama nootgn. Get dressed up.\n-Shm ama nootgn da Ha'li Shgwaitg. Get dressed up on Sunday."}
{"headword": "noo'anshg", "definition": "noun decoration\n-Hla ksha gowdee noo'anshg da tcka'nee ggaldmwa'at. There are no more decorations in the stores."}
{"headword": "nta", "definition": "prefix container\n-Ahlgadee goahl lushguud da nta daalayu. There's nothing in my wallet (container for money)."}
{"headword": "n'neet", "definition": "interjection yes\n-N'neet, wilaayu wila hown. Yes, I know what you are saying."}
{"headword": "n'tse'ets", "definition": "noun grandmother\n-'Tsuu hahlalsha n'dse'etsu hlat guul maay. My grandmother worked hard when she picked berries."}
{"headword": "n'tse'etsu", "definition": "noun my grandmother\n-Hladm kwdackshu na waabsh n'tse'etsu. I'm leaving my grandmother's home.\n-Maata na waash n'tse'etsu. My grandmother's name was Martha."}
{"headword": "oa", "definition": "interjection yes\n-Oa, hashacku gwee. Yes, I want that."}
{"headword": "oa'ash", "definition": "noun female cousin\n-Nda wila waan, oa'ash? How are you, cousin?"}
{"headword": "oa'dsn", "definition": "noun nothingness, spirit\n-Gyelkshu oa'dsn da 'dsm waab. It felt like there was a spirit in the house."}
{"headword": "ock", "definition": "interjection ouch!\n-Ock! sheepga gwee. Ouch! That hurt."}
{"headword": "oksh", "definition": "verb to fall; to hit Plural:ak'oksh\n-Oksha ggan'dameesh. The pencil fell."}
{"headword": "ol", "definition": "noun bear\n-Shuulga ol. Bears are dangerous."}
{"headword": "oo", "definition": "verb to troll\n-Hashacksh nabeebu dm oom hoant. My uncle wants to go trolling."}
{"headword": "ood", "definition": "verb to cook potatoes in sand near fire\n-Wie dsidp ooda shgoosheed. Why don't we cook the potatoes.\n-Yagwa googa n'dse'etsu dowlat ooda shgoosheed. When my grandmother was cooking she cooked it in the sand near the fire."}
{"headword": "oom ggaagg", "definition": "verb to fish for rock cod\n-Wiedsa oom ggaaggm dsihla dsigi'dseeb. Why don't we go fishing for rock cod tomorrow?"}
{"headword": "oomhl", "definition": "noun bucket, pail\n-'Gwaatga na oomhlu. I lost my pail.\n-Gaa oomhl ada gyeba aksh. Get a bucket and get some water."}
{"headword": "oom hoan", "definition": "verb to fish, troll\n-Yagwa oom hoan nabeebu. My uncle is fishing.\n-Yagwa oom hoant nabeebu, hashackt dm 'maga mishoa. My uncle is fishing, he wants to catch sockeye."}
{"headword": "oonkshig", "definition": "noun ashes from a fire\n-Kshi shakshl oonkshig da shdoob. Clean the ashes out of the stove."}
{"headword": "ooshg", "definition": "verb to stink\n-Goahl gun shm ooshga shamee gwee? Why is that meat really stink?"}
{"headword": "ooshgmlaan", "definition": "noun stink eggs\n-Ayin. ahlgadee hashackeehl ooshgmlaan. No. I don't want stink eggs."}
{"headword": "oo'alsh", "definition": "noun great-grandmother\n(-)-Lu'kwil hashacku dm dee oo'alshu. I really want to be a great-grandmother."}
{"headword": "o'yoonsh", "definition": "verb to be generous\n-O'yoonsha n'dse'etsu hlat 'gilm wineaya da 'kam. My grandmother is very generous when she gives us food."}
{"headword": "pdal", "definition": "noun rib\n-Sheepga pdalu hla hietga'nu. My rib hurts when I stand up."}
{"headword": "pdeack", "definition": "noun clan\n-Goahl wilsh pdeack wil hokshgush noan? What is your mother's moiety?"}
{"headword": "phloan", "definition": "noun sea otter\n-Nda shsga 'doackga na anaasha phloan? How expensive is the sea otter skin?"}
{"headword": "plakshkw", "definition": "verb to be beaten up, exhausted, overworked PLURAL: pleeplakshkw\n-Lu'kwil plakwshga'nu da shga 'naga meelgm. I'm really exhausted from dancing so long."}
{"headword": "pukshg", "definition": "verb to spit\n-Giloadsa pukshgn da lack ha'liwaalcksh. Don't spit on the floor."}
{"headword": "p'tsaan", "definition": "noun totem pole\n-'Tsuu hahlalsha hana'ack hlat dsaba p'tsaan. The woman worked real hard when she made the totem pole."}
{"headword": "sha", "definition": "noun cloud, day\n-Gyamga sha hla wil shamaaym. The day was warm when we picked berries."}
{"headword": "sha bee'eg", "definition": "verb to lie, tell a lie\n-Giloa sha bee'egshn. Don't lie."}
{"headword": "shackaicksh-ga", "definition": "verb to cut, saw off\n-Yagwat shackbaicksh-ga ggan. He is sawing off the wood.\n-Na shackbaicksh-ga 'yoota gwee loagsh dowla shalagsht. That man sawed off a log and built a fire."}
{"headword": "shackdoa", "definition": "verb to gather\n-Wie shiet shackdoa lag. 'Nee dm hoym dsidaawhl dsihla gwatk. Well gather the wood. That's what we'll use tonight when it gets cold."}
{"headword": "shacksh oomhoan", "definition": "noun fishing boat\n-Dm kshagyoatgu da Ta'gwaan da 'dsm shacksh oomhoan. I am going to Metlakatla by fishing boat."}
{"headword": "shackul'ka", "definition": "noun toasted seaweed\n-Ayinhl shguhl shackul'ka da 'kwan? Don't you have any toasted seaweed?"}
{"headword": "shadoack", "definition": "verb to remove, to take off (plural)\n-'Deeldm shadoacka 'yoota na gooda'atst deehl na 'dsoacksht hla 'dsilm baat. The man quickly took his coat off when he ran in."}
{"headword": "shadseelksh", "definition": "verb to melt away\n-Ndashnhl dm wil shadseelksha maadm? When will the snow melt away?"}
{"headword": "shagaa", "definition": "verb to remove, take off (singular) PLURAL: shadoack\n-Shagaa na gooda'atsn. Take your coat off."}
{"headword": "shagaksh", "definition": "verb to surprise\n-Shagaksha nabeebu hlat needsu. My uncle was surprised when he saw me."}
{"headword": "shagamaashgit", "definition": "verb to paint\n-Hladm shagamaashgit da waab. They're going to paint the house."}
{"headword": "shageeshk", "definition": "verb to dodge, move out of the way\n-Shageeshgn hlat oy dup gwee hla'at. Move out of the way when they throw the ball."}
{"headword": "shaggagiamg", "definition": "noun sunshine\n-Mahlda malshgm sha'winshg dm shaggagiamg dsigi'dseeb. The newspaper said it will sunshine tomorrow."}
{"headword": "shagiet 'koal", "definition": "verb to be as one\n-Shagiet 'goal ggaggoadm. We are of one heart.\n-Dm ggatgyad'nm dsihla shagiet 'goal ggaggoadm. We will be strong if we are of one heart."}
{"headword": "shaguyna", "definition": "verb to fall down\n-Shaguyna hlguwoamhlg hla baat. The child fell down when he ran."}
{"headword": "sha gya'wn", "definition": "noun today\n-Ahlgadee aam lacka da sha gya'wn. The weather is not good today."}
{"headword": "shagyeksh", "definition": "verb to be calm\n-Na shagyeksha baashg da gganhlaag. The wind was calm in the morning."}
{"headword": "shagyoaksh", "definition": "verb to drift away\n-Geedsa shagyoaksha boad awil gatgyada baashg. The boat almost drifted away because the wind was strong."}
{"headword": "shahleel", "definition": "verb to erase\n-Shahleel na waan. Erase your name.\n-Shahleel na waan da sha'winshga gwa'a. Erase your name from this paper."}
{"headword": "shahloontee", "definition": "verb to get mad all of a sudden\n-Ahlga aam shahloonteeyn. Amooksha gyad da 'kwan ada wilaayd da goa wila hown. It's not good to get angry. People listen to you and they'll know what you're saying."}
{"headword": "shakshg", "definition": "verb to be clean Plural:shikshakshg\n-Shim shikshakshga hoaya hla 'yackt da gyalck. The clothes are really clean when they hang outside.\n-Lu'kwil shakshga waabn. Your house is very clean. Your house is very clean."}
{"headword": "shalagsh", "definition": "verb to build a fire\n-Yagwa dm shalagshga'nu. I'm going to build a fire.\n-Na dm shalagshu ashda 'guulda shada. I was going to build a fire one day."}
{"headword": "shamee", "definition": "noun flesh, meat\n-Shameeym wun dm shi'biyaan'nm. We're going to smoke deer meat."}
{"headword": "shameeym wun", "definition": "noun deer meat\n-Hashacku shameeym wun. I want deer meat."}
{"headword": "shanaahl", "definition": "noun; verb miracle, wonder; to breathe Plural: lushanaahl\n-Lushanaahlga goa nwila gyoan. What you just did was amazing.\n-Kshabuu aksh da lack'oa 'dmgowsha 'naackhl hla shanaahlgt. In order to breathe a whale must blow water out of its head."}
{"headword": "shanaahlg", "definition": "1. verb to be astonished, surprised\n-Shanaahlga goa tcka'nooyu. I was surprised at what I heard.\n2. verb to be amazing\n-Shanaahlga wila dsaba na waabt. The house is built amazingly well."}
{"headword": "shayb", "definition": "noun bones\n-Wa'ackda hasha shaybm wun. The dog buried the deer bone"}
{"headword": "sha'aamdza waan", "definition": "interjection Do your best! Wishing you well!\n-Sha'aamdza waan hla leemeeyn. I wish you well when you sing."}
{"headword": "sha'anaayshk", "definition": "verb to make bread\n-Hladm sha'anaayshgm dish melee. We're going to make some bread for Mary."}
{"headword": "sha'daa", "definition": "verb to begin\n-'Nuuyu dm en sha'daa leemee. I'm going to start the song.\n-Hladm sha'daa'ama ndm dsaba boad. I'm going to start to fix the boat."}
{"headword": "sha'daatg", "definition": "verb to start off\n-Ndahl dm wil sha'daatga oom hoan gyad? When will people start fishing?"}
{"headword": "sha'doosh", "definition": "verb to push\n-Ashguu hlgu hash hlat sha'doosha hla'at. The dog was funny when it pushed the ball."}
{"headword": "sha'dsool'biksh", "definition": "verb to sink below the surface\n-Ayinhl needsnee wil sha'dsool'biksha 'wee 'naackhl? Didn't you see the big while sink below the water?"}
{"headword": "sha'kots", "definition": "verb to cut off, get rid of\n-Na goo 'yoota gwee wun dowlat sha'kots goa dumt 'gilm da 'koy. That man shot a deer and cut off what he's going to give me."}
{"headword": "sha'mn", "definition": "noun spruce\n-Goayu 'ka anoaggn, sha'mn ligi geek? Which do you like better, spruce or hemlock?"}
{"headword": "sha'oyhl", "definition": "verb to throw away\n-Sha'oyhl da gyalck. Throw it outside."}
{"headword": "sha'up yaa", "definition": "verb to take a walk\n-Wiedsa sha'up yaa'nm da 'kala aksh. Let's take a walk along the path."}
{"headword": "sha'winshgm giamg", "definition": "noun calendar\n-Shguuhl sha'winshgm giamg da 'kwan? Do you have a calendar?"}
{"headword": "sha'winshk", "definition": "noun paper\n-'Gilum sha'winshk dish 'need. Give her the paper."}
{"headword": "shbaggiet", "definition": "particle among, between\n-Kshagudsa aksh da shbaggiet loab. Pour out the water among the rocks.\n-Ya'anshga ggan'dameesh da shbaggiet 'gubatguuhlk. Divide the pencils among the children."}
{"headword": "shdatee", "definition": "noun stinging nettles\n-Bite waalu da gga'koacksh dowl gwalga an'onu da shdatee. l was in the bushes and the stinging nettles burned my hand."}
{"headword": "shda'magsh", "definition": "noun snowstorm\n-Lu'kwil 'dsuu shda'magsh ashda gi'dseeb. The snowstorm was fierce yesterday."}
{"headword": "shda'magsha shdoa ggan", "definition": "north north blizzard, snow on north side of tree\n-'Tsuu lacka hla shda 'magsha shdoa ggan. The weather is bad when there's a north blizzard."}
{"headword": "shdeem boadm gilhouli", "definition": "noun train\n-'Daashga hlguwoamhlg hlat nee 'wee shdeem boadm gilhouli. The child clapped when he saw the big train."}
{"headword": "shdoa", "definition": "noun half\n-'Kotsa anaay da 'nashdoat. Cut the bread in half."}
{"headword": "shdool", "definition": "verb to accompany\n-Na shdoolu nakshu dm sha'ap yaat, bite baasht dm 'gwihl 'goalt. I accompanied my wife when she walked, she was afraid to walk alone."}
{"headword": "sheeds", "definition": "noun sheet\n-Goahl wilgyeda sheeds dm geegn? What color sheets are you going to get?"}
{"headword": "sheedsm wush", "definition": "noun flannel blanket, sheet\n-Anoaggu shga gyamga sheedsum wush da goamshm. I like flannel sheets in the winter."}
{"headword": "sheelgit", "definition": "noun eldest one\n-Dsoan dee 'ka sheelgit. John is the eldest."}
{"headword": "sheen", "definition": "verb to get dizzy, drunk\n-Giloa sheen. ahlgadee aamhl wila gyoan. Don't get drunk. What you're doing is not good."}
{"headword": "sheepg", "definition": "verb to be sick; to be hurt Plural:shisheepg\n-Sheepgt noayu. My mother is sick.\n-Na sha'apyaa'nu ashda 'guulda shada da labite sheepga asheeyu. I was walking around one day and my feet really hurt."}
{"headword": "she'ehl", "definition": "prefix to attempt\n-She'ehl aadmhoan hlgu 'yoota. The man tried to fish."}
{"headword": "shga", "definition": "noun herring\n-Shga dee hoy fishman hla oom hoant. Fisherman use herring to fish."}
{"headword": "shgaaygshg", "definition": "verb to be hurt, wounded; to hurt, wound\n-Shgaaygshga asheeyu. My foot hurts.\n-Na Shgaaygshga 'yoota gwee wil tkee oksht. The man hurt himself when he fell down."}
{"headword": "shgaaytg", "definition": "noun darkness\n-Up lu'kwil shgaaytg. It's really dark.\n-Tckalyaa shgaaytg. It's getting darker."}
{"headword": "shgaboo", "definition": "quantifier; verb a few, some; to be a few\n-Nda shgaboo hoan 'gilmd da 'kwan? How many fish did he give you?"}
{"headword": "shgadawhl", "definition": "verb to go across\n-Shgu dm shgadawhlm da Gitsgaan. Dm geegu hoaya. We have to go across to Ketchikan. I have to buy clothes."}
{"headword": "shgalaan", "definition": "noun last one\n-Wie 'nuuyu shgalaan da na dsabm. I was the last one to do it."}
{"headword": "shga'doosh", "definition": "verb to close, shut\n-Lu'kwil baashga gyalck dowla howyu da hlguyu dm shga'doosha likshoack. It was really windy outside so I told my children to shut the door."}
{"headword": "shga'dsuu", "definition": "verb to be ugly\n-Lu'kwil shga'dsuu 'wee ha'li'dameesha gwee. That big table is really ugly.\n-Na painshga 'yoota gwee dowl lu'kwil shga'dsuu wila dsabit. That man painted and it was very ugly."}
{"headword": "shga'nakt", "definition": "noun duration, length (of time, space)\n-Ndahl sha'naga 'dsig'dsign? How long is your vehicle?"}
{"headword": "shga'neesh", "definition": "noun mountain\n-Hailda wun da lack shga'neesh. There are more deer up on the mountain."}
{"headword": "shggan", "definition": "noun woven mat\n-Dm baaldu ndm dsaba shggan. I'm going to try making a woven mat."}
{"headword": "shggan loa'ds", "definition": "noun elderberry bush\n-Yagwa dup guguul shggan loa'ds. We're looking for elderberry bushes."}
{"headword": "shggan moalksh", "definition": "noun crabapple tree\n-Hailda maay da shggan moalksh. There's a lot of fruit on the crabapple tree."}
{"headword": "shgoaksh", "definition": "verb to lack, not to have enough\n-Hla shgoaksha da wineaya. Aam dm sha wunm. We're getting short on food. Let's go get deer."}
{"headword": "shgool", "definition": "noun school\n-Sitka wil shgoolu. I went to school in Sitka."}
{"headword": "shgoosheed", "definition": "noun potatoes\n-Hla gwaanksha shgoosheed. The potatoes are cooked."}
{"headword": "shguu", "definition": "verb to place, put\n-Shguuhl agwee! Put it there!"}
{"headword": "shgwaitg", "definition": "verb to rest Plural:lishgwaitg\n-Ggal 'dsuu hahlalsha n'dse'etsu, aam dm shgwaitgt. My grandmother is working too hard, it's good for her to rest."}
{"headword": "shgyen", "definition": "noun gum, pitch, lead Plural:ggackshgyen\n-Tckal hla'ayga shgyen da na ggawshu. I got gum stuck in my hair."}
{"headword": "shidyaawd", "definition": "verb to exchange, pay back, reciprocate, return\n-Dm shidyaawdu ggaid na geegu. I'm going to return the hat I bought.\n-Na geegu hali'tckoackg adan shidyaawgwd. I bought a table and I returned it."}
{"headword": "shidyoaksh", "definition": "verb to rinse out\n-Ha'wahlgndee shidyoaksha wush. I haven't rinsed out the blanket."}
{"headword": "shiepg", "definition": "verb to be hard\n-Hla shiepga ash. The soapberries are hard.\n-Na dsaba noayu ash dowl ahlgadeet dup gubt. Gowdeet dsabt dowla shiepgt, dowla dup gubt. My mother made some soapberries but we didn't eat it. It got hard after she made it, then we ate it."}
{"headword": "shie'bn", "definition": "verb to harden, to sharpen\n-Shgu ndm shie'bn gigyoatk nagoacka ndm hoyt. I have to sharpen the hatchet before I use it."}
{"headword": "shigeene'etsg", "definition": "verb to stare at\n-Giloa shigeene'etsgn da hana'acka gwee. Don't stare at that woman."}
{"headword": "shiggoatg", "definition": "verb to start thinking about, have an idea about\n-Shiggoatgn da goa dm wuwaalm da sha gya'wn. Think of something that we can do today."}
{"headword": "shihoan", "definition": "verb to gather fish, work on fish Plural: ggashihoan\n-Aam dm wila waal ggaldsab dsihla ggashihoan gyad. The village will do well if the people gather fish."}
{"headword": "shila ndmhow", "definition": "noun compassion\n-Aam dm shila ndmhow shila gigyadm. We should have compassion for all people."}
{"headword": "shilmdock", "definition": "verb to take away\n-Yagwat shilmdocka shu hoya. He's taking away the new clothes."}
{"headword": "shiloonksh", "definition": "verb to dry\n-Shiloonksha wush. Dry the blankets."}
{"headword": "shiloonu", "definition": "noun dry items (clothes, fish)\n-Hashacku ndm shiloonu shamee. I want to dry the meat."}
{"headword": "shilu'aam", "definition": "verb to make happy\n-Shilu'aam ggoadn. Make your heart happy."}
{"headword": "shilu'aamggoad", "definition": "verb to be happy\n-Hla badsga'nu! Shilu'aamggoadn! I'm here! Be happy!\n-Shilu'aamggoadu hlat 'gilm Dson hoan da 'koy. I was happy when John gave me fish."}
{"headword": "shishdsoacksh", "definition": "verb to cohabit, picnic, play camp, have a small party\n-Shishdsoacksha tcka'nee gyad. The whole village went on a picnic.\n(-).Lu'kwil anoaggga 'gubatguuhlg dm shishdsoacktsht. The children really like to play camp."}
{"headword": "shishnankshg", "definition": "verb to act silly, funny\n-Shishnankshga hlgu doosh nlat nee wu'tseen. The little cat acted silly when it saw the mouse.\n-Labite goadsa wila waalu ashda 'guulda shada labite shishnankshga nakshu dowla 'ka yaayu. I didn't know what to do one day, my wife was acting silly then I took a walk."}
{"headword": "shishoosh", "definition": "verb to be small Plural: This is the plural form.\n-Ggal shishoosha na 'dsoackshu. My shoes are too small."}
{"headword": "shish'aacksh", "definition": "verb to laugh; to make laugh Plural: lusha'aacksh\n-Goahl gan shish'aacksh dut Kayla? Why is Kayla laughing?"}
{"headword": "shiwilaaykwsh", "definition": "verb to learn\n-Aam shiwilaaykwsha goa wila how teedsa, dm al lup aam wila loam hla gowdeet. Learn from the teacher, we'll be better for it when it's all done."}
{"headword": "shiwilaay'yamck", "definition": "noun; verb teacher; to teach\n-Hla goydiksha shiwilaay'yamck. The teacher has arrived."}
{"headword": "shi'biyaanshk", "definition": "noun smoked food\n-Hla sha'biyaanshga noayu goa dm gubm hla goamshm. My mother smoked food that we're going to eat in the winter."}
{"headword": "shi'indoyntk", "definition": "noun garden\n-Aam wila macksha galot a shi'indoyntkgu. The carrots are growing well in my garden."}
{"headword": "shmhow", "definition": "verb to tell the truth\n-Shmhow hana'ack hla malshgt da 'kam. She told the truth when she talked to us."}
{"headword": "shmksheeyeds", "definition": "verb to chop out\n-Ha'weenhl ma shmksheeyedst? Haven't you chopped it out yet?"}
{"headword": "shmlag", "definition": "noun open fire\n-'Tsamaatga wineaya googd da shmlag. Food cooked on a open fire tastes good."}
{"headword": "Shm'algyack", "definition": "noun 'TsmSHIAN language (lit. The True Language)\n-Hashacku ndm wilaay Shm'algyack. I want to know Shm'algyack."}
{"headword": "shm'okshdock", "definition": "verb to take out\n-Shm'okshdocka shgoosheed da gyalck. Take the potatoes outside."}
{"headword": "Shm'oygit", "definition": "noun leader, person of high ranking, Chief, Mayor Plural: Shmgyigyad\n-Wie 'nee 'yoota gwee Shm'oygit. Shgu dm hlaud. That man is the Chief. We need to show respect.\n-Shm'oygit en 'gilmd 'koy. The Chief gave it to me."}
{"headword": "Shm'oygit ga Lackaga", "definition": "noun Chief of the Heavens, God\n-Shm'oygit ga Lackaga en 'gilm didoolsha da 'kam. God gives us life.\n-Shm'oygit ga Lackaga en dsaba ha'lidsock. God made the earth."}
{"headword": "shndock", "definition": "verb to carry, take along\n-Shindocka tcka'nee ggan'dameesh. Take along all the pencils\n(-)-'gwihl yaayu da hahl geeka dun shnDocka 'guba ggan. I was walking along the beach and I carried along a little wood."}
{"headword": "shnyaagw", "definition": "verb to hold\n-Ama shnyaagwa hahlibeeshg. Be careful when you hold a knife."}
{"headword": "shoa", "definition": "noun food you take from a meal\n-Ashguu gyad hlat docka shoa. People are humorous when they take food home."}
{"headword": "shoashoa", "definition": "noun rattle for dancing\n(-)-Lu'kwil aam shoashoa dsabn. The rattle you made is very good."}
{"headword": "shoonaahl", "definition": "verb to be tired\n-Shoonaahla'nu da wil yaa waash. I'm tired of the rain.\n-2042 'Naga wil yaa'nu da bite shoonaahla'nu. I walked a long ways and I got tired."}
{"headword": "shu", "definition": "verb to be new\n-Hashacku ndm geega shu ha'li'daa. I want to buy a new chair."}
{"headword": "shugya'wn", "definition": "adverb just now\n-Shu gya'wn hla sha dsaga 'yoota. The man just now died."}
{"headword": "shumacksh", "definition": "noun young people\n-Hla yagwa baalda shumacksh dmt wilaay Shm'algyack. The young people are trying to learn our language."}
{"headword": "shuulg", "definition": "noun; verb middle; something fearful; to be dreaded, fearful\n-Sha ckbaycksha ggan da na shuulgt. Saw the wood in the middle."}
{"headword": "shuulga aatk", "definition": "noun midnight\n-Shgu dm laahlgm nagoaga shuulga aatk. We have to go to bed before midnight."}
{"headword": "shuulga sha", "definition": "noun noon\n-Shuulga sha dm wil shaggiet gowdee gyad. The people will gather at noon."}
{"headword": "shuunsh", "definition": "verb to be blind\n-Shuunsha hlgu 'yoota gwee. That young man is blind.\n-Labite 'gwaa'an hlgu 'yoota daala dowla shuunsht, ahlgadeet da'ackgat dm 'waat. The young man lost his money and he wasn't able to see to find it."}
{"headword": "shuunt", "definition": "noun summer\n-Hla goaym ada hla shuunt. It's spring and summer."}
{"headword": "shuwileen", "definition": "verb to bother, chase, go after, hunt\n-Giloamdsa shuwileen ha hlgaawgn. Don't bother your sister.\n-Na goo wunm ashda 'guulda shada, dowlat shuwileen 'wee gibaaw dowla luyeltgm da wil 'waatgm. We went hunting one day and a wolf bothered us so we returned to where we came from."}
{"headword": "shu'bash", "definition": "noun to be young; young person Plural:shumacksh\n-Lu'kwil shu'basha wila gyoa'yoota gwee. That man is acting very young."}
{"headword": "shwun", "definition": "verb to blow\n-Shwun hana'acka haleemee. The woman blew into the instrument.\n-Aam wila how hana'ack hlat shwun haleemee. The woman sounded good when she blew into the instrument."}
{"headword": "sh'dsoal", "definition": "noun beaver\n-Nee shga 'kwiloa'acka hlgu sh'dsoal. Look how that busy that little beaver is."}
{"headword": "sh'kaancksh", "definition": "noun athlete's foot, toes that have a smell\n-Ooshga sh'kaancksha hlguwoamhlg. The child's toes don't smell good."}
{"headword": "taggan", "definition": "noun plank, lumber\n-Shguu ndm geega taggan. I have to buy some lumber.\n-Ggal dalpga taggan. The lumber is too short."}
{"headword": "ta'apshgn", "definition": "number four long objects\n-Ta'apshgn 'ptsaan da ggaldsapm. There are four totem poles in the village."}
{"headword": "Ta'gwaan", "definition": "noun Taku people; Metlakatla\n-Ta'gwaan shiwaada nagga'dsaaw gyad Macklackaahla. Ta'GWAAN is what some people call Metlakatla.\n-Lu'kwil ama'basha Ta'gwaan hla gowdee shuunt. Metlakatla is very beautiful after the summer."}
{"headword": "tckaalpck", "definition": "number four flat, abstract or round objects\n-Tckaalpcka hla'at 'gilmu dish 'need. I gave him four balls."}
{"headword": "tckaalpckshg", "definition": "number four boats or canoes\n-Tcka'nooyu hla badsga tckaalpckshga ckshoa. I heard that four canoes have arrived."}
{"headword": "tckaamshm", "definition": "noun Raven\n-Ama amooksha 'gubatguuhlg da adaawck dish tckaamshm. The children really listened to the stories about Raven."}
{"headword": "tckadsmpshg", "definition": "noun boiled whole fish\n-Lu'kwil 'tsamaatga tckadsmpshg. The boiled fish is very tasty.\n-Dm tckadsmpshga'nm da waabshgool. We are going to make boiled fish at the school."}
{"headword": "tckalaam", "definition": "verb to be adaptable\n-Tckal'aam 'yoota gwee hla she'ehl googd. That man is adaptable when he tried to cook."}
{"headword": "tckaldakhl", "definition": "verb to tie on (with ribbon, twine)\n-Tckaldakhla hagwilhoo da likshoack. Tie the rope to the door."}
{"headword": "tckaldock", "definition": "verb to take along\n-Tckaldocka tcka'nee wineaya. Take all of the food with you."}
{"headword": "tckalgaa", "definition": "verb to take, carry along\n-Dm tckalgaadu wush awil ckgwatksha'nu. I'll carry along the blanket because I'm cold."}
{"headword": "tckalhokshnhl", "definition": "verb to add to, bring to, tie to\n-Tckalhokshnhla sha'wnshk da haahlggan. Attach the paper to the wall."}
{"headword": "tckalpckdoal", "definition": "number four people\n-Tckalpckdoal gyad lu dsoackt da waaba gwee. Four people are living in that house."}
{"headword": "tckalshagihl", "definition": "verb to bring towards, pull in\n-Ama'basha wil tckalshagihla ggawshn da na 'dsaln. Your hair looks pretty when it's brought toward your face."}
{"headword": "tckalyaa", "definition": "verb to develop, enlarge, expand, grow, increase\n-Tckalyaa baashg. The wind is getting stronger.\n-Tckalyaa shgaboo boada goidikshd da Gitsgaan. The number of boats coming to Ketchikan increased."}
{"headword": "tckal'daabhl", "definition": "verb to nail on\n-Tckal'daabhl da haahlggan. Nail it to the wall."}
{"headword": "tckal'daabit", "definition": "verb to fasten\n-Tckal'daaba likshoack. Fasten the door.\n-Aam dsabn wil tckal'daabn likshoack. You did good fastening the door."}
{"headword": "tckal'dsaab", "definition": "verb to bind against\n-Tckal'dsaaba taggan da ggan. Bind the stick to the small tree.\n-Tckal'dsaaba hagwilhoo da ggan. Bind the rope to the tree."}
{"headword": "tckal'dsa'ba", "definition": "noun; verb sculpture, statue, painting, image; to paint\n-Ndm tckal'dsa'ba na hlguhlgu. I'm going to paint my child."}
{"headword": "tckal'dseeb", "definition": "verb to fasten to, tie on\n-Tckal'dseeba wush da 'newalee. Tie on the blanket to the backpack."}
{"headword": "tckal'oy", "definition": "verb to slam, swing shut\n-Ckshdaamcka wil tckal'oy 'yoota likshoack. The door made a loud sound when the man slammed it shut."}
{"headword": "tckal'waa", "definition": "verb to meet\n-Wie dsa dup tckal'waa gyad da Gitsgaan. Let's meet up with people in Ketchikan."}
{"headword": "tckayaagwihl", "definition": "verb to bring along\n-Tckalyaagwa na gooda'atsn. Bring along your coat.\n-Na lisha'ylm ashda 'guulda shada da tckayaagwa schweetish. We went to a movie the other day and brought along some candy."}
{"headword": "tcka'moa", "definition": "noun body\n-Plakshkw tcka'moayu. My body is exhausted."}
{"headword": "tcka'nee", "definition": "quantifier all\n-Tcka'nee gyad en hlimoamsh melee. All the people are helping Mary."}
{"headword": "tcka'nee goa", "definition": "noun everything\n-Giloamdsa geega tcka'nee goa. Don't buy everything."}
{"headword": "tcka'nee gyad", "definition": "noun everybody\n-Tcka'nee gyad en anoagga leemee. Everybody liked the song."}
{"headword": "tcka'nee mihla 'goald", "definition": "noun everyone\n-Ggalshm, tcka'nee mihla 'goald. Come, everyone."}
{"headword": "tcka'noo", "definition": "verb to hear\n-Tcka'nooym wil 'wee'amhow hlguwoamhlg hla 'dseent. We heard the child cry out as he came in."}
{"headword": "tckow", "definition": "noun halibut\n(-)-Lu'kwil 'tsamaatga tckow. Halibut tastes very good."}
{"headword": "tgi", "definition": "prefix down, downward\n-Dm tgi oyu hla'at. I'm going to throw the ball down."}
{"headword": "tgidaawhl", "definition": "verb to sink\n-Giloamdsa ggal'oa ligigoa da lack'U awil dm tgidaawhlt. Don't drop anything in the muskeg because it will sink."}
{"headword": "tgine'etsg", "definition": "verb to look down\n-Tgine'etsgid da 'wee dee. They looked down the big hill."}
{"headword": "tgiyaa", "definition": "noun; verb dusk; to descend, go down;\n-Hlat tgiyaa giamg. The sun is going down."}
{"headword": "tgi'doosh", "definition": "verb to knead, press down\n-Giloamdsa tgi'doosha hlgu 'yoota awaan. Don't push that boy down."}
{"headword": "tgi'dsoahl", "definition": "verb to slide down\n-Shishaacksha 'gubatguhlg hla tgi'dsoahlt da lack maadm. The children laughed as they slid on the snow."}
{"headword": "tgi'gen", "definition": "verb to put down\n-Tgi'gen 'nakshuuneeshg, ggal 'tsuu baashg. Put down the window, the wind is too strong."}
{"headword": "tgi'oksh", "definition": "verb to fall\n-Tgioksha na ggaidu. My hat fell down.\n-Na hla'giackshgu da lack'oa waabm dowl tgi'okshu. I climbed on our roof and I fell down."}
{"headword": "tgwa", "definition": "noun glass; around the point\n-Hultga 'gwish'gwashm tgwa da lack guyna. The road is full of glass."}
{"headword": "Tgwahahay", "definition": "noun Point Davidson\n-Tgwahahay dm wil ggaldsoackm. Point Davidson is where we'll camp."}
{"headword": "tgwayeltg", "definition": "verb to turn around\n-Tgwayeltga hlgu doosh hlat nee hash. The little cat turned around when it saw the dog."}
{"headword": "ukshbaashg", "definition": "noun offshore wind\n-Gatgyeda ukshbaashg. The offshore wind is strong."}
{"headword": "ukshdawhl", "definition": "verb to go out to sea\n-Wie dm ukshdawhlm dm guul hla'ashg. Well, we're going out to sea to gather seaweed."}
{"headword": "ukshdock", "definition": "verb to take out, unpack\n-Ukshdocka gooda'ats da 'newully ada 'yackt. Take the coat out of the backpack and hang it up."}
{"headword": "ukshdockhl", "definition": "verb to take out\n-Naahl dm en ukshdocka ggalim-shahlea? Who will take out the garbage can?"}
{"headword": "ukshhietg", "definition": "verb to stand near the water; to stand out\n-Ahl needsin wil ukshhietga 'wee ggan da awaa liksh'daa gwee? Did you see where the big tree stands out of the water by that island over there?"}
{"headword": "umsheewa", "definition": "noun driftwood; White person, European\n-Umsheewa'nu. I am a European (White man)."}
{"headword": "Umsheewaamck", "definition": "noun English language\n-Ahlgadeet tcka'noo nayaayu Umshewaamck. My grandfather does not understand English."}
{"headword": "uuah", "definition": "noun ooligan\n-Ndada tckash 'goahl wil aadmuuah gyad? What part of the year do people net ooligans?"}
{"headword": "uuck", "definition": "noun coho salmon\n-Yagwat shakshakshen uuck. He is cleaning coho."}
{"headword": "uula", "definition": "noun seal\n-Wilaayd n'dse'etus dsaba uula dm gubm. My grandmother knew how to cook seal for us to eat."}
{"headword": "uunck", "definition": "noun bentwood box\n-Lu doa hla'ashg da 'dsm uunck. Put the seaweed in the bentwood box."}
{"headword": "waa", "definition": "noun name\n-Goahl waash noan? What is your mother's name?"}
{"headword": "waab", "definition": "noun house\n-Hla shm ama dsaba gyad da na waabm. lu'kwil aam wila dsabt gya'wn. People did a good job on our house. It looks very good now."}
{"headword": "waabshgool", "definition": "noun schoolhouse\n-Ama haboalda 'gubatguuhlg na waabshgoold. Children take good care of their schoolhouse."}
{"headword": "waab shiwilaaykwsha", "definition": "noun school (lit. house of learning)\n-Waab shiwilaaykwsha wil shgool tcka'nee goa wilaayut gya'wn. I went to school and that's what I learned everything that I know now."}
{"headword": "waab tckoackg", "definition": "noun restaurant\n-Lu'kwil anoacku wineaya da waab tckoackga gwee. I really like the food at that restaurant."}
{"headword": "waads", "definition": "noun clock, watch\n-Giloa na waadsu. My watch has stopped."}
{"headword": "waadsm an'on", "definition": "noun wristwatch\n-Lu'kwil anoacku waadsm an'on 'gilm nakshu da 'koy. I really like the wristwatch my husband gave me."}
{"headword": "waalck", "definition": "verb to walk\n-Hailda gyad waalckd da waab dsuds. Lots of people walked to church."}
{"headword": "waash", "definition": "noun rain\n-Dm yilyeltgm dsihla yaa waash. We'll come back when it rains."}
{"headword": "waashm yain", "definition": "noun misty rain\n-Hladm waashm yain dsihla aamshga'nak. It's going to drizzle pretty soon."}
{"headword": "waay", "definition": "verb to paddle, row\n-'Naga waayn, ayinhl shoonaahlanee? You rowed a long ways, aren't you tired?"}
{"headword": "wahl", "definition": "noun yellow cedar\n-Ndahl wil 'dahla wahl? Where will we find yellow cedar?"}
{"headword": "wakyam", "definition": "noun our brothers\n-Shguu dm hlimoamum na wakyam. We must help our brothers."}
{"headword": "wanoack", "definition": "verb to be not enough\n-Wanoacka wineaya da gyad. There's not enough food for everyone."}
{"headword": "wa'at", "definition": "verb to sell\n-Wa'ata na gga'dsaaw hoan. Sell some of the fish."}
{"headword": "weehawtg", "definition": "verb to cry, weep\n-Weehawtga hlguwoamhlga gwa'a. This child is crying.\n-Na dal 'gubatguuhlg ashda 'guulda sha da weehawtga 'goald. The children were fighting one day and one cried."}
{"headword": "wie aam", "definition": "interjection okay\n-Hla 'tsaayanee? Wie aam. You're full? Ok."}
{"headword": "wietdoa", "definition": "adverb far away\n-Wietdoa dm wil loygm. We're going to move camp far away."}
{"headword": "wie wa!", "definition": "interjection alright!; behold!; well now; let's start!; okay!\n-Wie wa! Hladm sha'daatgm. Okay, I'm ready to start.\n-Wie wa! Hladm leemeeym. Okay! We're ready to sing."}
{"headword": "wihlaaycksh", "definition": "noun huckleberry\n-Wineaya shm wihlaayckshm. Wil'laayu wil 'dahla haild. Huckleberries are real food. I know where there are lots."}
{"headword": "wilaay", "definition": "verb to know\n-Aam dm shm ama amookshn da 'yoota gwee. Wilaayd da wila howt. Listen well to that man. He knows what he's talking about."}
{"headword": "wilaayshg", "definition": "noun relative\n-Hailda wilaayshgu. Dm al needsm tcka'nee gyad dsigi'dseeb. I have a lot of relatives. We'll see everyone tomorrow."}
{"headword": "wileel", "definition": "noun eye\n-Sheepga wileelu. My eye is aching."}
{"headword": "wileelm tgwa", "definition": "noun eyeglasses\n-Ahlgadee hashacku ndm hoy wileelm tgwa. I don't want to wear eyeglasses."}
{"headword": "wilgyed", "definition": "noun color\n-Goahl wilgyedu gwa'a? What color is this?"}
{"headword": "wil'nak", "definition": "adverb far away\n-Wil'nak wil dsoacka na gga'dsaaw gyad. Some people live far away."}
{"headword": "wineaya", "definition": "noun food\n-Hailda wineaya da 'kam. We have a lot of food."}
{"headword": "wineaym 'Tsmshian", "definition": "noun Indian food\n-Wie wineaym 'Tsmshian dee lup dsabm. We put up our own Tsmshian Indian food."}
{"headword": "woamsh", "definition": "noun devil's club\n(-).Lu'kwil aam woamsh a na gackshaybt. Devils club is good for her arthritis."}
{"headword": "woanoack", "definition": "noun skunk cabbage\n-Hla 'dahla woanoack. There is the skunk cabbage."}
{"headword": "woapck", "definition": "noun forehead\n-'Kaa woapcka hlguwoamhlg. The little child has a cut on his forehead."}
{"headword": "woon ggawsh", "definition": "noun brain\n-Sheen na woon ggawshu. My brain is dizzy."}
{"headword": "woo'dsee", "definition": "noun caribou, reindeer\n-Ayinhl shguuhl wo'dsee da gwa'a? Are there any caribou in this area?"}
{"headword": "wukdsab", "definition": "verb to be competent, healthy, lucky\n-Needsu shga wuldsabsh Alik. I see how healthy Alec is."}
{"headword": "wuk'dsa'wulsh", "definition": "noun thief\n-Wuk'dsa'wulsh en 'gaal'ga boad. A thief took the boat.\n-Goi'diksha wuk'dsa'wulsh dowlt docka na hoanu. A thief came and took my fish."}
{"headword": "wun", "definition": "noun deer\n-Lu'kwil kwdee'nu da shameeym wun. I'm really hungry for deer meat."}
{"headword": "wush", "definition": "noun blanket Plural:wishwush\n-Yoaksha wusha gwa'a. Wash this blanket."}
{"headword": "wu'tseen", "definition": "noun mouse\n-Yaaka doosha hlgu wu'tseen. The cat followed the mouse."}
{"headword": "yaa", "definition": "verb to walk Plural:waalck\n-Dm yaa'nu da awaash nabeebu. I'm walking to my uncle's."}
{"headword": "yaa moaksh", "definition": "verb to snow\n-Dm yaa moaksh da dsigi'dseeb. It's going to snow tomorrow."}
{"headword": "yaawckg", "definition": "verb to eat\n-Hladm yaawckga'nu. I'm going to eat.\n-Ahlgadee da'ackgu dm yaawckgu, sheepga 'kalmhowyu. I'm not able to eat, my throat is sore."}
{"headword": "yackya'oack", "definition": "verb to sob\n-'Naga yackya'oackga hlguwoamhlg hla gawdee weehowtgt. The child sobbed for a long time after she finished crying."}
{"headword": "yain", "definition": "noun fog\n(-)-Lu'kwil 'dsuu yain a lack'daa. The fog is very thick on the lake."}
{"headword": "yanna gee", "definition": "verb to walk over here\n-Yanna gee dowla gya'wn, dayat nagwaadu, ada luwantga ggoadu. Walk over here right now, my father said, and I was worried."}
{"headword": "ya'an", "definition": "verb to pass around\n-Ya'anshga wineaya, lu'kwil kwdee gyad. Pass the food around, people are very hungry."}
{"headword": "ya'anshg", "definition": "noun distribution\n-Yagwa ya'anshgm liggiwaal loolgidit. The person having the feast is passing out gifts."}
{"headword": "ya'tseshg", "definition": "noun animal\n-Hailda likshgyadm ya'tseshg da liksh'daa. There are lots of different animals on the island."}
{"headword": "yeds", "definition": "verb to break up, chop, club, hit, pound\n-Doulat yedst. Then they chopped it.\n-Yetsga bilhaa dee wil aamt. Abalones are good when they pounded.\n-'Ka 'dsamaa'anu yeds hla'ashg. I like chopped seaweed best."}
{"headword": "yeds hla'ashk", "definition": "noun chopped seaweed\n-Lu'kwil anoaggu yeds hla'ashk. I really like chopped seaweed."}
{"headword": "yeeh", "definition": "noun King salmon, Chinook salmon\n-Eh! 'Wee 'tsamaatga 'wee yeeh na 'gilm gyad da 'kam. Wow! That big King salmon people gave us tastes good."}
{"headword": "yehl", "definition": "noun fish slime\n-Hultga ggaan'onu da yehlm hoan. My hands are full of fish slime."}
{"headword": "yehlg", "definition": "verb to be smooth\n-Yehlga liploab doat da 'kala aksh. The rocks along the river are smooth."}
{"headword": "yoa", "definition": "verb to roast on open fire\n-Wiedsa dup yoa hoan. Let's roast the fish on the open fire."}
{"headword": "yoaksh", "definition": "verb to wash\n-Hladm yoaksha hlguwoamhlg na 'dsalt awil 'dsa'dsiksht. The child is going to wash her face because it's dirty."}
{"headword": "yoo hoosh", "definition": "verb to save for later\n-Yoo hoosha yoam hoan. Save the roasted fish for later."}
{"headword": "yuu", "definition": "verb to hide away\n-Wie yuuee maay. Ggal hailda 'gubatguuhlg dm en gubt. Well, I hide the fruit. There are too many children who will eat it."}
{"headword": "yuub", "definition": "noun earth, ground, land, soil\n-Hailda lish'yaan da nlack yuubu. There are lots of mink on my land."}
{"headword": "'backsh", "definition": "noun pants, trousers Plural:gga'backsh\n-Ndadu 'backsh? Where are the pants?"}
{"headword": "'backsha dsina", "definition": "noun jeans\n-'Backsha dsina na hoym da 'gubatguuhlgm. We wore jeans when we were children.\n-Noashdp shga 'dauckga 'backsha dsina gya'wn. Oh my goodness! Jeans are very expensive now."}
{"headword": "'backshm ggaboack", "definition": "noun corduroy pants\n-Geegish lobat 'backshm ggaboack. Robert bought corduroy pants."}
{"headword": "'bahl'bal", "definition": "verb to misbutton\n-'Bahl'bala gwish'na'ba'la hoy hana'ack.. The robe the woman wore was misbuttoned."}
{"headword": "'bal", "definition": "verb to button up\n-'Bal na gooda'atsn, gwatga gyalck. Button your coat, it's cold outside.\n-'Kacka na gooda'atsn, aam la 'balt. Your coat is open, button it up."}
{"headword": "'balda hahloa", "definition": "noun cotton gloves\n-Na hoyu 'balda hahloa da waab shihoan. I wore cotton gloves at the cannery."}
{"headword": "'balgiackshg", "definition": "verb to be heavy Plural:'bil'balgiackshg\n-'Balgiackshga 'wee loab. The big rock is heavy.\n-Na geegu ha'li'daa dowl ggal 'balgiackshga dm da'ackgu ndm gaad. . I bought a chair and it was too heavy for me to take it."}
{"headword": "'balt", "definition": "noun glove\n-Hoy 'balt da gwatg. Wear gloves when it's cold."}
{"headword": "'bash", "definition": "verb to caulk an opening; to grow\n-'Basha madsiggalay gwee. That flower is grown.\n(-)-Lu'kwil 'dsuu wila 'basha 'yoota gwee. That man really grew."}
{"headword": "'bashee", "definition": "noun diaper\n-Hladm lumaakshish maalee 'bashee. Mary is going to wash the diapers."}
{"headword": "'bashu", "definition": "verb to fart\n-Ooshga 'bashu hash. The dog let out a smelly fart."}
{"headword": "'ba'an", "definition": "verb to break (bread, dried food)\n-'Ba'an anaay. Break the bread.\n-'Ba'an anaay ada gishya'nd da gyad. Break the bread and pass it around to the people."}
{"headword": "'ba'atsa", "definition": "noun kelp, rock weed\n-'Baa'atsa dee hoyu da hla wun shgoosheed. I use kelp for the potatoes."}
{"headword": "'beehl", "definition": "verb to crush, mash\n-'Beehla maay. Crush the berries.\n-'Dsamaatga 'beehlgm shgoosheed. Mashed potatoes taste good."}
{"headword": "'beensh", "definition": "noun wild celery\n-'Tsamaa'anu ndm guul 'beensh. • I like to gather wild celery."}
{"headword": "'bihloashk", "definition": "noun dried seaweed\n-'Doackg ndm 'waay 'bihloashk. It's difficult to find dried seaweed."}
{"headword": "'bilgwa", "definition": "noun chief's headgear; eagle down\n-Gyoaksha 'bilgwa hla meelga gyad. The eagle down was floating in the air when the people danced."}
{"headword": "'bilhow", "definition": "verb to gossip, talk about\n-Goahl 'bilhowda hana'ack awaan? What is that woman talking about?"}
{"headword": "'bish'bash", "definition": "verb to caulk, seal\n-'Bish'basha 'nakshuuneeshg. Seal the windows.\n-Baaldu baashg da 'nakshuuneeshg, shgu ndm 'bish'basht. I feel the wind in the window, I need to seal it."}
{"headword": "'biyaan", "definition": "noun smoke\n-Bishbooshm lag, dowla lu oyt da 'dsm shdoob, dowla'biyaant. We chopped up the wood, put it in the stove and it smoked."}
{"headword": "'daa", "definition": "verb to sit Plural:wun\n-Ndahl dm wil 'daan? Where will you sit?"}
{"headword": "'daashg", "definition": "verb to applaud, clap hands\n-'Daashga hlguwoamhlg hlat nee nagwaatgt. The little child clapped when she saw her father.\n-'Daashga gyad da shga aam wila howshga dup gwee. People clapped because they sounded so good.\n-Na leemee hlgu hana'ack da Town Hall dowl lu'kwil ama'basha dsabt dowla 'daashga gyad. The little girl sang at the Town Hall and she sounded real good so the people clapped."}
{"headword": "'daa'binshg", "definition": "noun nail\n-Hailda 'daa'binshga hoyd hlat dsaba waab. They used a lot of nails to make the house."}
{"headword": "'dackwunsh", "definition": "noun adze\n-'Dackwunsha hoy hlaagigyad hlat dsaba p'tsaant. Years ago our ancestors used to make totem poles."}
{"headword": "'dag", "definition": "noun wind, whirlwind\n-Ayawaa hana'ack hlat nee 'dag. The woman yelled when she saw the whirlwind."}
{"headword": "'dahl", "definition": "verb to smear, spread\n-'Dahla hoan da lack anaay. Smear the fish on the bread."}
{"headword": "'dahla awaan", "definition": "verb to put away\n-'Dahla awaan dsihla gawdeeyn. Put that away when you are done."}
{"headword": "'daish", "definition": "noun arrow\n-Hla ahlgadee naahl en dsabhl 'daish gya'wn. Nobody makes arrows anymore."}
{"headword": "'dameesh", "definition": "verb; noun to write; written material\n-Aba'ackshgu dm badsga 'dameeshn. I'm anxious for your letter to arrive."}
{"headword": "'da'giackshg", "definition": "verb to have too much food in one's throat\n-Ggal hailda gubu dowla 'da'giackshgu. I got too much food in my throat because I ate too much."}
{"headword": "'da'kil", "definition": "verb to fold over\n-'Da'kil sha'winshk adm mackt. Fold the paper and put it away."}
{"headword": "'da'wil", "definition": "noun fish hook\n-Ggal'dsushga 'da'wil hoyn. The fish hook you're using is too small."}
{"headword": "'deebn", "definition": "noun sea lion\n-Nee shga 'weelaeksha 'wee 'deebn. Yagwat guulksha hoan. Look how big that sea lion is. It's looking for fish."}
{"headword": "'deeld", "definition": "verb to do quickly, work fast\n-'Deelda waalsh Magalee hlat dsaba anaay. Mary worked fast when she made the bread.\n-Sha 'deelda wila gyoan, ggal laaltgn. Hurry up with what you're doing, you're too slow."}
{"headword": "'deen", "definition": "noun; verb fish trap; to hurry\n-Hultga na 'deenm. Our fish trap is full.\n-Giloa laaltgn, 'deen! Don't be slow, hurry!"}
{"headword": "'dilgyad", "definition": "verb to serve (food)\n-Naa dm 'dilgyad da waab tckoackg? Who is going to serve at the restaurant?"}
{"headword": "'di'ik", "definition": "noun navel\n-Needsu 'di'ikn. I can see your belly button."}
{"headword": "'dmggowsh", "definition": "noun head\n-Hla sheepga 'dmggowshu, ggal 'dsuu wila gyoayu ashda gi'dseeb. My head hurts because I did so much yesterday."}
{"headword": "'dmggowshm hoan", "definition": "noun fish head\n-'Tsamaatga 'dmggowshm hoan, daya nagga'dsaaw gyad. Fish heads really taste good, that's what some people say."}
{"headword": "'dmlaan", "definition": "noun steersman; stern (of a boat)\n-Ggal 'balgiackshga ckbeesh shguud da 'dmlaan. The box in the stern is too heavy."}
{"headword": "'dmlaanee", "definition": "noun neck\n-Hlmdakhla golksh da 'dmlaaneeyn. Wrap a scarf around your throat."}
{"headword": "'dmmeet", "definition": "noun berries\n(-)-Lu'kwil moalksha 'dmmeet. Those berries are sour."}
{"headword": "'dmwaalgit", "definition": "noun skull\n-'Waaym 'dmwaalgita ol. We found the skull of a bear."}
{"headword": "'dmyaa", "definition": "1. verb to be fast, quick; to go fast\n-'Dmyaa hlgu doosh hlat hoom hoan. The little cat goes fast when it smells fish.\n2. verb to walk to the front\n-Na shila yaagu hlguhlgu dowl ggal 'dmyaa wila gyoat. I was walking with my child and he walked too fast."}
{"headword": "'dm'kie", "definition": "noun shoulder, upper arm\n-Hoyu 'dm'kieyu dm'yagayaayu da geeka dm goyu wun dm backyaayu da awaayu. I used my shoulder to go down the beach to get a deer to carry it up."}
{"headword": "'dm'koa", "definition": "noun backbone\n-'Mun ckaldaawckg da 'dm'koayu awil shgaaygshgt. Rub medicine on my back because it's hurt."}
{"headword": "'doackg", "definition": "verb to be expensive; difficult; challenging; steep; valuable Plural:'dack'doackg\n-Ggal 'doackga waaba gwee. That house is too expensive.\n(-).Na dm geegu automobile dowl ggal 'doackgd dowl giloand. I was going to buy an automobile but it was too expensive so I quit."}
{"headword": "'doagg", "definition": "verb to suck\n-Hloula 'doagga hlguwoamhlg na moasht. The child still sucks his thumb."}
{"headword": "'doo", "definition": "verb to sweep\n-'Doo da nhluu ha'li'dameesh. Sweep under the table."}
{"headword": "'doosh", "definition": "verb to hit, push with fist\n-Giloam 'kwihl 'dooshee ahlga shmal aamhl wila howyu. Don't push me about, I don't feel so good.\n-'Doosha ckbeesha awaan da awaayu. Push that box over here by me."}
{"headword": "'dooshg", "definition": "verb to sweep with branch or broom\n-Ha'weenhl 'dooshgn da 'dsim gi'dsoan? Haven't you swept in the closet?"}
{"headword": "'doyck", "definition": "verb to thank, express appreciation\n-'Doyckshn daahl. Thank you my dear woman."}
{"headword": "'doycksh", "definition": "verb to express appreciation, thank\n-'Gilum gyada hoan da 'koy adan 'doycka 'yoota gwee. People gave me fish and I thanked that man for it."}
{"headword": "'dsaa", "definition": "verb to stab\n-'Dsaayu na 'dsiwaaltu da 'lagg. I stabbed my finger with a needle."}
{"headword": "'dsaab", "definition": "verb to be caught in a bind, tight space\n-'Dsaaba hahloa da shbaggiet loab. The cloth was caught among the rocks.\n-'Dsaaba hagwilhoo. The rope is caught in a bind."}
{"headword": "'dsaay", "definition": "verb to be full; to burp\n-Lu'kwil 'dsaayu gya'win. I'm really full now.\n-Gawdee yaawckckgu da up lu'kwil 'dsaayu. After I ate I was really full."}
{"headword": "'dsab", "definition": "verb to brail, bring above water\n-Hla baa na boadm da geyaaksh, dowla oksh'ken aad, aamshga'nag dowla 'dsabt. hailda hoan da'ackgm. Our boat went out on the water and we let our net go, and after a while we brailed the fish. We were able to catch lots of fish."}
{"headword": "'dsack'dsackg", "definition": "verb itchy\n-'Dsack'dsackga asheeyu. My feet are itchy."}
{"headword": "'dsaick", "definition": "verb to lick\n-'Dsaickda hlguwoamhlga shweedish. The child licked the candy."}
{"headword": "'dsak", "definition": "noun China slippers\n-Ahl anoackanee 'dsak? Do you like china slippers?"}
{"headword": "'dsakya", "definition": "verb to turn off Plural:'dsik'dsakya\n-'Dsakya laakwsh. Turn the light off."}
{"headword": "'dsakyl", "definition": "verb to put out\n-'Dsakyl shdoob nagoacka mdm kwdaksha waab. Put the stove out before you leave the house."}
{"headword": "'dsal", "definition": "noun; verb face; to fillet fish Plural:gga'dsal'dsal\n(-).Lu'kwil mashga na 'dsalt hla dsoackt. His face gets very red when he's ashamed."}
{"headword": "'dsalksh", "definition": "noun whirlpool\n-Ama needsa boad, shuulga 'dalksha gwee. Be careful with the boat, that whirlpool is fearful."}
{"headword": "'dsamtee", "definition": "noun electricity, lightning\n-Ahlgandee nee 'dsamtee. I didn't see the lightening."}
{"headword": "'dsashkw", "definition": "noun lice Plural:'dsack'dsashkw\n-Baasha'nu ndm nee 'dsaskw. I'm afraid to see lice."}
{"headword": "'dsayck", "definition": "verb donate\n-Lu'kwil ama ggaggoada gyad hla 'dsayckt. People are good hearted to donate."}
{"headword": "'dsa'ack", "definition": "noun clam Plural:gga'dsa'dsa'ack\n-Dm aidsdida 'dsa'ack dm gubm. She will fry clams for us to eat."}
{"headword": "'dsa'dsiksh", "definition": "verb to be dirty, dusty, soiled\n(-)'Dsa'dsiksha na 'dsig'dsigu. My car is dirty.\n-Labite waal 'yoota gwee da na boad, bite 'dsa'dsiksha na 'dsawt. That man messed up with his boat, it was dirty inside."}
{"headword": "'dsa'oamtee", "definition": "noun dried meat\n-Lu'kwil 'dsamaatga 'dsa'oamteem shamee dsabn. The dried meat you made is very tasty."}
{"headword": "'dsa'wulsh", "definition": "verb to steal\n-Giloamdsa 'dsa'wulsha ligigoa da ggaldmwa'at. Don't steal anything from the store."}
{"headword": "'dseeb", "definition": "verb to tie\n-'Dseeba na golksha hlgu hana'ack. Tie the little girl's scarf."}
{"headword": "'dseeba hagwilhoo", "definition": "verb to tie a rope\n-'Dseeba hagwilhoo da kwduun ggan gwee. Tie the rope around that tree."}
{"headword": "'dseeka", "definition": "verb to run aground\n-'Dseeka na boads Dson. John's boat ran aground on the beach."}
{"headword": "'dseen", "definition": "verb to come in, enter, go in Plural: lamdsack\n-Na 'dseen giamgm aatk. The moon went in.\n-'Dseen. Hla gwaanksha wineaya. Come in. The food is done.\n-Gwatga gyalck, aam 'dseen da 'dsm gwa'a. It's cold outside, it's good to come in here."}
{"headword": "'dseen giamgm'aatk", "definition": "noun sun or moon eclipse\n-Needsu wil 'dseen giamgm'aatk da giyaatk. I saw the moon eclipse last night."}
{"headword": "'dseen gyamgm'aatk", "definition": "noun moon eclipse\n-Needsu wil 'dseen gyamgm'aatk. I saw the moon eclipse."}
{"headword": "'dsee'bltk", "definition": "verb to burn up\n-Lu 'doackga ggaggoada gyad wil shm 'dsee'bltga waab dzuds. The people were very sad when the church burned all the way down."}
{"headword": "'dsee'dsee", "definition": "noun bone marrow\n-Lu'kwil 'tsamaatga 'dsee'dsee. The bone marrow is very tasty."}
{"headword": "'dsee'g", "definition": "verb to be left by the tide; to leak\n-'Dseega ckshoa. The canoe is leaking.\n-Luwuntga ggoada 'yoota dm 'dsee'ga na boad. The man was worried about his boat leaking."}
{"headword": "'dsee'k", "definition": "noun shells\n-Hailda 'dsee'k 'waayu da hahlgeeka. I found a lot of shells on the beach."}
{"headword": "'dsig'dsig", "definition": "noun car, wagon, vehicle\n-Dm geegu 'dsig'dsig da Gitsgaan. I am going to buy a car in Ketchikan."}
{"headword": "'dsilaa", "definition": "noun basket Plural:'dsuck'dsilaa\n-Lu'kwil hoyshga 'dsilaa dsabsh Magalee. The basket that Margaret made is very beautiful."}
{"headword": "'dsilaay", "definition": "verb to visit\n-Dm 'dsilaayu n'dse'etsu da 'dsm waab sheepg. I'm going to visit my grandmother in the hospital."}
{"headword": "'dsilmbaa", "definition": "noun to run into a house\n-'Dsilmbaa hana'ack hlat nee naksht. The woman ran in when she saw her husband."}
{"headword": "'dsilmgaa", "definition": "verb to take in\n-'Dsilmgaa ha'li'daa dsihla yaa waash. Take the chair in if it rains."}
{"headword": "'dsilmmeelg", "definition": "verb to dance in\n-'Dsilmmeelga'nu awil ap shm lu aamggoadu. I danced in because I was so happy."}
{"headword": "'dsiloom", "definition": "verb to bring food, pack a lunch\n-Meehoksha na 'dsiloomn. Your lunch smells good.\n-Na shaupwaalckshm ashda 'guulda shada, da lup 'dsiloom goa dm gubm. We went for a walk the other day and brought food that to eat."}
{"headword": "'dsimaatk", "definition": "verb to be tasty\n-Lu'kwil 'dsimaatga winea dsabsh noayu. The food that my mother fixes is very tasty."}
{"headword": "'dsimaay", "definition": "noun barnacles; great-great-grandchildren\n-'Lee hultga 'dsimaay da lack loab. There were a lot of barnacles on the rocks."}
{"headword": "'dsiwaalt", "definition": "noun finger\n-Sheepga 'dsiwaalu. My finger hurts."}
{"headword": "'dsiwaand", "definition": "noun end\n-Dm habm na 'dsiwaand guyna. We're going to the end of the road."}
{"headword": "'dsm", "definition": "prefix within\n-Lu shgu 'dsoacksh da 'dsm ckbeesh. Put the shoes within the box."}
{"headword": "'dsmhoan", "definition": "noun red snapper\n-Yagwat shakshakshen 'dsmhoan. He is cleaning red snapper."}
{"headword": "'dsm'an'on", "definition": "noun palm of hand\n-'Woamckga 'dsm'an'Onu. The palm of my hand aches."}
{"headword": "'dsm'dee", "definition": "noun neck, nape\n-Dakhla golksh da 'dsm'deeyn. Tie the scarf around your neck.\n-Hlmdakhla golksh da 'dsm'deeyn. Wrap the scarf around your neck."}
{"headword": "'dsm'kol", "definition": "noun anus\n-Gaapshga hash na 'dsm'kolt. The dog scratched its anus."}
{"headword": "'dsnkbaa", "definition": "verb to run backwards\n-'Dsnkbaa hlguwoamhlg hlat baald dm gidigaa hla'at. The child ran backwards when she tried to catch the ball."}
{"headword": "'dsnkyaa", "definition": "verb to walk backwards\n-'Dsnkyaa 'yoota hlat nee ol. The man walked backwards when he saw the bear."}
{"headword": "'dsnshhood", "definition": "verb run away from\n-'Dsinshhooda hlguwoamhlg hlat needsm. The child ran away from us when he saw us."}
{"headword": "'dsnshloyg", "definition": "verb to stay behind, be left behind\n-Henalee 'dsnshloygd. Henry stayed behind when the people left."}
{"headword": "'dsoacksh", "definition": "noun shoes Plural:gga'dsoacksh\n-Nda wil geega 'dsoackshn? Aam wila dsabit. Where did you buy your shoes? They look good."}
{"headword": "'dsoacksha 'tsawaab", "definition": "noun slippers\n-Lu'kwil anoacku na shu 'dsoacksha 'dsawaabu. I really like my new slippers."}
{"headword": "'dsoackshm hahloa", "definition": "noun tennis shoes\n-Needsu 'dsoackshm hahloa. I saw the tennis shoes."}
{"headword": "'dsoahl", "definition": "verb to slide\n-'Dsoahla hoan da awaayu. Slide the fish over to me."}
{"headword": "'dsuu baashg", "definition": "verb to be very windy\n-Tckalyaa wil 'dsuu baashg. It is getting very windy.\n-Lu'kwil 'dsuu baashg dm waayn da gwashga. There's too much wind to row over there."}
{"headword": "'dum", "definition": "verb to write\n-'Ka ha'weeni, dm 'dumu na waayu. Wait, I'll write my name."}
{"headword": "'gahlgyoa", "definition": "verb to list to one side\n-Luwantga ggoadu da wil 'gahlgyoa boada gwee. I'm worried about the way that boat is listing to one side."}
{"headword": "'galdoal", "definition": "number six people\n-'Galdoalda shgaboo gyad dm mikmeelgt. Six people are going to dance."}
{"headword": "'galyeds", "definition": "verb to hit with a stick or club\n-'Galyedsa 'yoota 'wee uula. The man clubbed the seal."}
{"headword": "'gal'doosh", "definition": "verb to hit with fist, punch\n-Hl'loontee 'yoota adat 'gal'doosha likshoack. The man got angry and hit the door with his fist."}
{"headword": "'gal'oy", "definition": "verb to hit with a thrown object\n-Hl'loontee hlguwoamhlg adat 'gal'oy loab da na waabt. The child got angry and threw a rock at his house."}
{"headword": "'geelg", "definition": "noun feeling of strong taste in throat\n-Labiethow ggaloashu da 'geelgu. My stomach didn't feel good and I had a strong taste in my throat."}
{"headword": "'ge'ets", "definition": "verb to point\n-'Ge'etsga hlguwoamhlg da goa hashackt. The child pointed to what he wanted."}
{"headword": "'ge'etsckan", "definition": "verb to point at, point out\n-'Ge'etsckan da mihleetgm hla'at. Point to the green ball."}
{"headword": "'gidaa", "definition": "noun rake to catch herring in water\n-'Gidaa hoy hlagigyad hlat gidigaa shga. People of long ago used a rake to catch herring in water."}
{"headword": "'gideelt", "definition": "number twenty flat objects\n-'Gideelt shaboo malshgmsha'winshg dm geegu. I'm going to buy twenty newspapers."}
{"headword": "'gilum", "definition": "verb to give, hand to\n-Wie 'gilum hoan dish dp 'need, ggoadu hla kwdeed. Well give them some fish, I think they're hungry"}
{"headword": "'gineetg", "definition": "verb to rise, get up from laying down\n-'Gineetgn! Shgu dm hahlalshn. Get up! You have to work."}
{"headword": "'gipcka", "definition": "prefix all of, the entire\n-'Gipcka 'gwaatga hoan. The entire catch of fish was lost."}
{"headword": "'goahl", "definition": "noun year\n-Nda shgaboo 'goahla hlguwoamhlga gwee? How many years is that child?"}
{"headword": "'goal", "definition": "number one person\n-Ksha 'goalda 'yoota dm leemeet. Only one person will sing.\n-Ksha 'goal goidikshd. Only one person came."}
{"headword": "'goald", "definition": "number six abstract, flat or round objects\n-'Goalda shgaboo hla'at hoy 'gubatguuhlg hla galmeelgt. The children used six balls when they played."}
{"headword": "'gubatguuhlg", "definition": "noun children\n-Aam wila how 'gubatguuhlg hla leemeet. The children sound good when they sing."}
{"headword": "'guul", "definition": "number one abstract or round thing\n-Ayinhl shguuhl gik 'guulda ha'li'daa? Isn't there one more chair?"}
{"headword": "'gwaatg", "definition": "verb to be lost, missing\n-Gwaatga na ggaidu. My hat is lost.\n-'Gwaatga na 'dsoackshu. My shoes are lost.\n-Labite 'gwaatga 'yoota gwee. That man is lost."}
{"headword": "'gwaa'dish", "definition": "verb to miss, be lonesome for\n-'Gwaa'disha ggoadu da 'kwan. I'm lonesome for you."}
{"headword": "'gwaloa'am gyad", "definition": "noun hard working person\n-'Gwaloa'am gyadat Dan. Dan is a very hard working person."}
{"headword": "'gwash", "definition": "verb to break, crack Plural:'gwish'gwash\n-Labite goadsa wila waalu, hla 'gwasha ggoadu. I didn't know what to do, my heart was broken."}
{"headword": "'gweentee", "definition": "noun salmon stomach\n-Naahl en hashacka 'gweentee? Who wants the salmon stomachs?"}
{"headword": "'gwilamacksh", "definition": "noun Hudson Bay tea\n-Na 'gilm n'dse'etsu 'gwilamacksh dm sha deeyu. My grandmother gave me Hudson Bay tea to make tea."}
{"headword": "'gwilee", "definition": "number three abstract or round things\n-'Gwilee daala shga'doackgt. It costs three dollars."}
{"headword": "'gwiloa'ack", "definition": "verb to be industrious, hard working\n-Lu'kwil 'gwiloa'acka hlgu 'yoota gwee da wil hahlalsht. That young man is a hard worker at his job."}
{"headword": "'gwish'gwash", "definition": "verb to be broken\n-'Gwish'gwasha 'nakshuuneeshg. The window is broken.\n-Giloamdsa oyhl hla'at da awaa 'nakshuuneeshg, dm 'gwish'gwasht. Don't throw the ball by the window, it will be broken."}
{"headword": "'gwit'gwaatg", "definition": "verb, plural to be lost\n-'Gwit'gwaatga hlikhla'at. The balls are lost.\n-'Gwit'gwaatga gubatguuhlg hlikhla'at. The children lost the balls."}
{"headword": "'gyaag", "definition": "number one flat object\n-Ksha 'gyaaga hoan ginamaand. There's only one fish left."}
{"headword": "'gyaba wil 'gyap'gyaba 'goahl", "definition": "noun centennial (100 yrs)\n-Hla 'gyaba wil 'gyap'gyaba 'goahl na wil mackshgm da Shu Macklackaahla. It has been over 100 hundred years since we arrived at New Metlakatla."}
{"headword": "'gyag", "definition": "verb to choke, get something caught in the throat\n-Ahlgadee ggawn 'yoota gwee dowla 'gyagt. That man didn't chew good so he choked."}
{"headword": "'gyaickg", "definition": "verb to escape, run away, flee Plural:huut\n-Ahlgadee hashacksh nagwaadu dm ggalmeelgu da gyalck, dowla 'gyaickgu. My father didn't want me to play outside so I ran away.\n-'Gyaickgun du! Run away!"}
{"headword": "'gyap", "definition": "number ten abstract, round or flat objects\n-'Gyap shgaboo daala 'gilmt ndm geega shu 'dsoacksh. He gave me ten dollars to buy new shoes."}
{"headword": "'gynnm", "definition": "particle our own, ours\n-Nlip 'gynnm gga'bala awaan. The guns over there are our own."}
{"headword": "'kaa ggoadn", "definition": "noun compassion\n-Alu'daa wil 'kaa ggoada liplaid. You could see the preacher's compassion."}
{"headword": "'kaal'g", "definition": "verb to steal Plural:ga'gaal'g\n-Giloamdsa 'kaal'ga ligigoa da ggaldmwa'at. Don't steal anything from the store."}
{"headword": "'kabaa", "definition": "verb to be lame\n-'Kabaa hlgu hash. The little dog is lame.\n-Sha oksha 'yoota gwee dowl 'kabaat hla 'kineetgt. That man fell down and he was lame when he got up."}
{"headword": "'kack", "definition": "verb to open\n-'Kacka likshoack. gyamga gyalck. Open the door. It's warm outside."}
{"headword": "'kahl'oksh", "definition": "fall to fall to one side\n-Ha'liggoadu dm 'kahl'oksha ha'li'daa. I think the chair is going to fall over."}
{"headword": "'kala aksh", "definition": "noun creek, river, stream\n-Shayaa shgaboo hoan da 'kala aksh. There are fewer fish in the stream."}
{"headword": "'kalaamsh", "definition": "noun rose, wild rose\n-Hashacku ndm macksha 'kalaamsh da awaa waabu. I want to grow roses by my house."}
{"headword": "'kalmhow", "definition": "noun throat\n-Sheepga 'kalmhawyu. My throat hurts.\n(-).Na sheepga 'kalmhawyu da goa doctor dm needsm goa wila waalu. My throat was sore and we went to the doctor to see what's wrong with me."}
{"headword": "'kalmoash", "definition": "noun crab\n-Hashacku 'kalmoash. I want crab."}
{"headword": "'kamea", "definition": "number one boat or canoe\n-Ksha 'kamea boad needsu hla badsgt. I only see that one boat has arrived."}
{"headword": "'kawtsi", "definition": "noun ooligan grease\n-Hashacku 'kawtsi. I want ooligan grease."}
{"headword": "'kaw'kaaw", "definition": "noun crow\n-Tcka'nee goa guba 'kaw'kaaw. Crows eat everything."}
{"headword": "'ka'at", "definition": "noun cane\n(-).Naahl en dsaba 'ka'atn? Who made your cane?"}
{"headword": "'ka'awts", "definition": "noun labret worn in lip\n-Shuulga wila dsaba 'yoota hlat hoy 'ka'awts. The man looks fearsome when he wears a labret."}
{"headword": "'ka'tsushg", "definition": "verb to be smaller\n-'Ka 'tsushga ckbeesh nadm hoyu. The box I was going to use is smaller."}
{"headword": "'ka 'weelaeksh", "definition": "verb to be bigger\n-'Ka 'weelaeksha na goacku. My basket is bigger.\n-Shgu ndm hoy 'ka 'weelaekshm ckbeesh. I have to use a bigger box."}
{"headword": "'kiewoaksh", "definition": "noun dried fish strips\n(-).Lu'kwil hashacku ndm 'waay 'kiewoaksh. I really want find some dried fish strips.\n-Kshuud dm wil sha 'kiewoakshm. We make dried fish strips in the fall."}
{"headword": "'koa'ol", "definition": "verb forget\n-'Koa'olda hlguwoamhlg na gooda'atst. The child forgot his coat."}
{"headword": "'kots", "definition": "verb to cut, slice Plural:'kots'kots\n-Yagwan 'kotsa shamee. I'm cutting up meat.\n-Na gidigaadu 'wee hoan dowlat 'kots'kots noayu dumt 'gilm da gyad. I caught a fish and my mother cut it up to give to people."}
{"headword": "'kowts", "definition": "noun chin, indentation under the lip\n-Gitwaaltg en hoy 'kowts. Warriors wear a labret."}
{"headword": "'koy", "definition": "pronoun me\n-Wie wa! 'gilum daala da 'koy. Wie baloogu. OK! Give me money. I'm broke."}
{"headword": "'lagg", "definition": "noun needle\n-Gaa 'lagg ada lu'bishn. Get a needle and sew."}
{"headword": "'la 'daa ggoadu", "definition": "verb to have an upset stomach\n-'La 'daa ggoadu hla gowdeen guba shameeym uula. My stomach was upset after I ate the seal meat."}
{"headword": "'leebahla", "definition": "verb to spread\n-'Leebahla wush da lack ha'linoak. Spread the blanket on the bed."}
{"headword": "'leeshguu", "definition": "verb to put on\n-'Leeshguu mahlu da lack ha'linoak. Put the pillow on the bed."}
{"headword": "'leetlumhlk", "definition": "verb to cover\n-Bahla 'leetlumhlk da lack yuub. Cover the ground with the canvas."}
{"headword": "'lee'buul", "definition": "verb to sprinkle on\n-'Lee'buul hla'ashg da lack meyoob. Sprinkle the seaweed on the rice.\n-Na googed noayu dowlat 'lee'buul moan da lack goa dm gubm. When my mother cooked she sprinkled salt on what we were going to eat."}
{"headword": "'lee'dameeshm ggan", "definition": "noun blackboard, chalkboard\n-'Dum na waan da lack 'lee'dameeshm ggan. Write your name on the blackboard."}
{"headword": "'maakwsh", "definition": "noun wet snow\n-Ama nee wila yaan, 'tsuu 'maakwsh da lack guyyna. Be careful walking, there's lots of wet snow on the street."}
{"headword": "'mag", "definition": "verb to fish, catch salmon\n-Hailda 'magm hoanm. We caught lots of fish.\n-Hailda 'magm hoanm da Hemlock. We caught lots of fish at Hemlock."}
{"headword": "'man", "definition": "verb to anoint, grease, massage, oil, rub\n-Aam madm tckal 'man haldaaksh na asheeyn. It's good to rub medicine on your leg."}
{"headword": "'naa", "definition": "noun bait\n-Dm geegu 'naa nagoaga dm oom hoanm. I have to buy my bait before we go fishing."}
{"headword": "'naackhl", "definition": "noun killer whale, whale\n-Shanaahlga shga hailda 'naackhl da wil oom hoanum. It's amazing how many killer whales there are where we fished."}
{"headword": "'naam tckaw", "definition": "noun halibut bait\n-Nda shgaboo 'naam tckaw doat da 'kam? How much halibut bait do we have?"}
{"headword": "'nabaa", "definition": "verb to be soaking wet; to be just born\n-'Nabaa na kshlushgu. My shirt is soaked.\n-'Nabaa na gooda'atsu awil ggal ggadsikshga waash. My coat is soaked because the rain really poured down."}
{"headword": "'nack'noo", "definition": "verb to hear\n-Ayinhl 'nack'nooyn wil 'weeamhow hlguwoamhlg? Didn't you hear the child cry out?"}
{"headword": "'nadalpg", "definition": "verb to approach shore\n-'Nadalpga 'wee 'naackhl da hahl geeka. The whale is coming close to the beach."}
{"headword": "'nahloamshk", "definition": "verb to be hallowed, sacred\n-'Nahloamshga gyad wildoolgit. The graveyard is sacred to the people."}
{"headword": "'nahoa'ya", "definition": "noun tools\n(-)-Lu'kwil anoacku shu 'nahoa'ya geegu. I really like the new tools I bought."}
{"headword": "'nak", "definition": "verb to be long\n(-)-Lu'kwil 'wee 'naga aada 'yoota gwee. That man's seine was very long."}
{"headword": "'nakshuuneeshg", "definition": "noun mirror, window\n-Dm 'daayu da awaa 'nakshuuneeshg. I'm going to sit by the window."}
{"headword": "'nakshuuneeshgm 'dsal", "definition": "noun mirror\n-Giloa hlowla lune'etsgn da 'nakshuuneeshgm 'dsal. Quit looking in the mirror all the time."}
{"headword": "'naphlackhl", "definition": "verb to be tall\n-Du! Nee shga 'naphlackhla hlguwoamhlga gwee! Good grief! See how tall that child is."}
{"headword": "'na shdoa giamg", "definition": "noun half moon\n-Shm 'na shdoa giamg sha gya'wn. It is half moon now."}
{"headword": "'nashee'bnshk", "definition": "noun friend, sweetheart\n-Hladm loayga 'nashee'bnshgu. My friend is moving away."}
{"headword": "'nawinoa", "definition": "verb to be bothersome, annoying\n(-)-Lu'kwil 'nawinoa 'wee hasha gwee. That big dog is very annoying."}
{"headword": "'nayeltg", "definition": "verb to come back out of the woods\n-Hladm 'nayeltgsh dup gwee. They will be coming from the woods soon."}
{"headword": "'nayets", "definition": "verb to break in, break open (with hammer, axe)\n-'Nayetsa likshoack. Break open the door.\n-Na hloontee 'yoota da 'koy dat 'nayetsa likshoacku da 'wee ha'hlibeeshg. The man was mad at me and he hit my door with a big knife."}
{"headword": "'nayoa", "definition": "noun something you use to roast\n-'Tsuwaan ggan dm hoyu hlan 'nayoa shamee. I'm going to use a pointed stick to roast the meat."}
{"headword": "'na'bahloanshg", "definition": "noun ribbon\n-Ama'basha 'na'bahloanshg da na ggawshn. The ribbon in your hair is pretty."}
{"headword": "'na'ba'la", "definition": "noun button Plural:'bil'bal\n-Shgu dm geegu 'na'ba'la. I have to buy a button."}
{"headword": "'na'oomhoan", "definition": "noun place to catch fish\n-Ndahl dm wil 'na'oomhoanm? Where shall we find a place to catch fish?"}
{"headword": "'na'taash", "definition": "noun item worn on a lapel\n-'Na'taasha madsiggalay da gooda'atsn. Put a flower on your coat."}
{"headword": "'needee", "definition": "interrogative right?\n-Hla lugowdee aksh, 'needee? The water is empty, right?"}
{"headword": "'Neehlwaan", "definition": "interjection amen\n-'Neehlwaan, daya gyad hla gawdee gigeengwackhlt. \"Amen,\" that's what people say when they're finished praying."}
{"headword": "'neet", "definition": "pronoun he, she, it\n-Giloamdsa 'gilum daala dish 'neet. Don't give him any money."}
{"headword": "'newalee", "definition": "noun backpack\n-Hashacku shu 'newalee. I want a new backpack."}
{"headword": "'nhla'naggan", "definition": "noun keg, barrel\n-Wie ya'an 'wee 'nhla'naggan da gwa'a. Pass that big wooden barrel over here."}
{"headword": "'nhloamshg", "definition": "verb to be respected, sacred\n-'nHloamshga gyad na Waabsh Shm'oygit ga Lackaga. People respect the house of the Lord."}
{"headword": "'nishuushg", "definition": "noun coffin\n-Lu'kwil hoyshga 'nishguushga gwee. That coffin is very beautiful."}
{"headword": "'noahl", "definition": "noun drum\n-Lu'kwil aam wila how 'noahla dsabn. The drum that you made sounds real good."}
{"headword": "'ntawa'at", "definition": "noun pocket\n-Ggal hultga 'ntawa'ata hlguwoamhlg. The child's pocket is too full."}
{"headword": "'nuk 'nuungm gganggan", "definition": "noun tall trees, trees\n-'Nuk 'nuungm gganggan dm hoy gyad hlat dsaba shu waabshgool. People are going to use tall trees when they build the new school."}
{"headword": "'nuum", "definition": "pronoun we\n-'Nuum dm en googa wineaya dsihla dsigi'dseeb. We're going to cook the food tomorrow."}
{"headword": "'nuun", "definition": "pronoun you\n-'Nuun dm en googa wineaya, 'needee? You are going to cook the food, right?"}
{"headword": "'nuuyu", "definition": "pronoun I\n-'Nuuyu gwa'a hla shagwalga lag. I'm the one who built the fire here."}
{"headword": "'nu'ud'ood", "definition": "verb to forsake\n-Ahlga dmt 'nu'ud'ooda Shm'oygit ga Lackagat 'nuum. God will not forsake us."}
{"headword": "'poo'a", "definition": "verb to fart\n-Ooshga 'poo'a hash. The dog let out a smelly fart."}
{"headword": "'taab", "definition": "verb to hit with, hammer; to hit, tap\n-Ama needsa 'taa'binshg. Be careful with the nail."}
{"headword": "'tapckaad", "definition": "number two fish, animals or flat things\n-'Tapckaada hoan dm geegu. I'm going to buy two fish."}
{"headword": "'tapckadool", "definition": "number two people\n-Ksha 'tapckadool gyad lu 'daad da 'tsm waab tckoackg. Only two people are sitting in the restaurant."}
{"headword": "'tapckaldoal", "definition": "number seven people\n-'Tapckadoal gyad lu 'daad da boad. Seven people are in the boat."}
{"headword": "'tapckoald", "definition": "number seven abstract, round or flat objects\n-'Tapckoalda leemee 'gubatguuhlg da 'dsm waab shgool. Children sang seven times in the school."}
{"headword": "'tsack", "definition": "noun nose\n-Gwa'a na 'tsacku. Here is my nose."}
{"headword": "'tsack'tsackg", "definition": "verb to tickle\n-Tsack'tsackga an'onu. My hand itches."}
{"headword": "'tsamaatg", "definition": "verb to taste good\n-'Tsamaatga ksha'dsal na gubm. The half dried fish we ate tasted good."}
{"headword": "'tsilaashu", "definition": "noun swift rapids, waterfall, gorge, canyon\n-Geedsa tgidaawhla boad da 'tsilaashu. The boat almost went over the waterfall."}
{"headword": "'tsimoo", "definition": "noun ear\n-'Tsack'tsackga 'tsimooyu. My ear tickles."}
{"headword": "'tsiyol'g", "definition": "noun kingfisher\n-Ndahl wil 'waay gyad 'tsiyol'g? Where do people find kingfishers?"}
{"headword": "'tsm aack", "definition": "noun inside of the mouth\n-Geedsa gwalga 'tsm aacku awil ggal giamga aksh. The inside of my mouth almost burned because the water was too hot."}
{"headword": "'tsmloab", "definition": "noun cave\n-Goashinhl ya'tseshg lu wundida 'dsmloaba gwa'a. I wonder what kind of animal lives in this cave."}
{"headword": "'Tsmshian", "definition": "noun Tsimshian\n-'Tsmshian'nu I am a Tsmshian."}
{"headword": "'tsm'tsack", "definition": "noun nostril\n-Goahl gun kshibaa 'tsm'tsacka hlguwoamhlga gwee? Why is that little child's nostril running?"}
{"headword": "'tsm'tsansh", "definition": "noun armpit\n-'Tsuu baa aksh da 'tsm'tsanshu hla luwontga ggoadu. The water really runs from my armpits when I'm worried."}
{"headword": "'tsushg", "definition": "verb to be little, small\n-Lu'kwil 'tsushga 'bil'bal. The button is very small.\n-Hashacka hlgu 'yoota dump hlimoamu dowl ggal 'tsushgt da goa dm wila gyoayu. The little boy wanted to help me but he was too small for what I was going to do."}
{"headword": "'tsu'uts", "definition": "noun bird\n-'Gyaickga hlgu doosh hla gipaigga 'tsu'uts da awaat. The little cat ran away when the bird flew by it."}
{"headword": "'tu'utsg", "definition": "verb to be black\n-'Tu'utsga wil gyeda 'dsig'dsig. The color of the car is black.\n-Yagwa paintga 'yoota gwee boat da 'tu'utsga hoyt. That man is painting the boat and he used black to do it."}
{"headword": "'tu'utsgm maay", "definition": "noun blueberry\n-Wi'laayu wil 'dahla 'tu'utsgm maay. I know where blueberries grow."}
{"headword": "'tu'utsgm ol", "definition": "noun black bear\n-Yagwa goo hlmkdeeyu 'tu'utsgm ol. My brother is hunting for black bear."}
{"headword": "'wa", "definition": "prefix without\n-'Wa 'tsimoo, dayat n'dse'etsu hla ahlgadee amooksha hlguwoamhlg. No ears, that's what my grandmother said when the child didn't listen."}
{"headword": "'waan", "definition": "noun teeth\n-Shikshakshgn na 'waan da tcka'nee sha. Clean your teeth every day."}
{"headword": "'waatg", "definition": "verb to be found; to come from\n-Macklackaahla wil 'waatgu. I come from Metlakatla."}
{"headword": "'waay", "definition": "verb to find\n-'Waayu ama goa. I found something good.\n-'Waayu ama goa da ggaldmwa'at. I found something good at the store."}
{"headword": "'waleemee", "definition": "noun to have no song\n-'Waleemeet Carol. Carol has no song to sing."}
{"headword": "'watsa", "definition": "noun land otter\n-Ha'wahlgandee nee 'watsa da ggaldoa. I haven't seen any land otter at camp."}
{"headword": "'wayoaksh", "definition": "verb to hope, trust\n-'Wayoakshgm Shm'oygit ga Lackaga da 'Need en wilaay goa aamt da 'kam. We trust God that He knows what's best for us."}
{"headword": "'wa'ama ne'ets", "definition": "verb to be careless\n-'Wa'ama ne'etsa hana'acka gwee. That woman is very careless.\n-Giloadsa 'wa'ama ne'etsn. Don't be careless."}
{"headword": "'wa'dsimoo", "definition": "noun someone who never listens\n-'Wa'dsimoo! Dayat n'dse'etsu hla ahlgadee amookshu dish 'need. No ears! That's what my grandmother said when I didn't listen to her."}
{"headword": "'weegyat", "definition": "verb to miss, feel loss of, be lonesome for\n-Lu'kwil 'weegyatga'nu da 'kwan. I'm really lonesome for you."}
{"headword": "'weelaeksh", "definition": "verb to be big\n-Nda shga 'weelaeksha ol needsn? How big was the bear that you saw?\n-Lu'kwil 'weelaeksha 'wee hoan gidi-da'ackga 'yoota gwee. That man caught a very big fish."}
{"headword": "'weelaeksha ggashgaawt", "definition": "verb to be large\n-Lu'kwil 'weelaeksha ggashggaw ggoab. The waves are very big."}
{"headword": "'weelaekshm gyad", "definition": "noun person of high ranking\n-'Weelaekshm gyads Henry. Henry has a high rank."}
{"headword": "'yaagw", "definition": "noun earthquake\n-Ahlgadee hashackee ndm baalda 'yaagw. I don't want to feel an earthquake."}
{"headword": "'yaansh", "definition": "noun gumboots\n-Wilaaysh Malee wil 'dahla hailda 'yaansh. Marie knows where there are a lot of gumboots."}
{"headword": "'yack", "definition": "verb to hang\n-Wie 'yacka hoan. Aam dm sha 'biyaanshgm. Well, hang the fish. We'll smoke it."}
{"headword": "'yansh", "definition": "noun leaf of a tree\n-Hailda 'yansh da ggan gwee. Ggoadu dm hailda maay. There are a lot of leaves on that tree. I think it will have a lot of fruit."}
{"headword": "'yee-kwdal", "definition": "number eight abstract, round or flat objects\n-Hashacku mdm 'lee shgu 'yee-kwdal noahl da lack hali'tckoackg. I want you to put eight plates on the table."}
{"headword": "'ye-kwhladoal", "definition": "number eight people\n-'Ye kwhladoal shgaboo gyad dm gatgoidiksht. There are eight people who are coming."}
{"headword": "'yoo", "definition": "noun bark container to pick berries in\n-'Yoo dm hoyu dsihla dsabu ggoack. I'll use bark for making baskets."}
{"headword": "'yoota", "definition": "noun man Plural:'yik'yoota\n-Eh! Nee 'wee 'yoota gwee. Aam wila nootgt. Wow! Look at that man over there. He's dressed real good."}
{"headword": "'yootishg", "definition": "noun tie; necklace\n-Lu'kwil hoyshga 'yootishga dsabish Magalee. The necklace that Margaret made is very beautiful."}
{"headword": "'yoo'uck", "definition": "noun baby boy\n-Lu'kwil taggoada hlgu 'yoo'uck. The baby boy is very content."}
```