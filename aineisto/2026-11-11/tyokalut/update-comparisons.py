from pathlib import Path

path = Path('paimio-valtuusto-11-11-2026.html')
html = path.read_text(encoding='utf-8')
addition = r'''
// Vertailuluvut: kokousaineisto 8.11.2026; lukutavan täydennys 9.11.2026.
const comparisons={
43:{note:'Menettelyasia: ei uutta talouslukua tai vuosittaista maksua.',rows:[['Päätösvaltaisuuden raja','Vähintään 24 valtuutettua','Vähintään 24 kokouksessa 11.11.','Rajaan ei esitetä muutosta']]},
44:{note:'Kokouskohtainen valinta; ei vuosittaista talousvertailua.',rows:[['Tarkastajat','Tämän kokouksen tarkastajia ei ole vielä valittu','Sami Lehto ja Mikko Lindberg','Kaksi tarkastajaa tähän kokoukseen'],['Nähtävilläolo','Aineistossa kaksi eri ajankohtaa','16. tai 17.11.2026','Päivä on vahvistettava; ei numerollinen vuosimuutos']]},
45:{note:'Nykyinen vertailupohja on talousarviokirjan TA2026, jossa ovat muutokset 23.9.2026 asti. Se ei ole vuoden 2026 toteuma eikä sisällä vielä kokouksen § 52:n ehdotuksia. Lainakanta on erikseen merkitty ennusteeksi. Luvut ovat pyöristettyjä; erotukset laskettu näkyvistä luvuista.',source:[['Talousarvio · s. 13–20, 91 ja 102',budget]],rows:[
['Toimintakate','−35,840 milj. € · TA2026','−36,117 milj. € · TA2027','277 000 € heikompi'],
['Toimintatuotot, sisäiset + ulkoiset','12,646 milj. € · TA2026','12,027 milj. € · TA2027','−619 000 €'],
['Toimintakulut, sisäiset + ulkoiset','48,486 milj. € · TA2026','48,145 milj. € · TA2027','−341 000 €'],
['Henkilöstökulut','24,544 milj. € · TA2026','24,153 milj. € · TA2027','−391 000 €'],
['Verotulot yhteensä','26,900 milj. € · TA2026','28,365 milj. € · TA2027','+1,465 milj. €'],
['Kunnallisverotulo','22,800 milj. € · TA2026','24,050 milj. € · TA2027','+1,250 milj. €; § 52:ssa 2026-arvioksi ehdotetaan 23,060 milj. €'],
['Kiinteistöverotulo','2,700 milj. € · TA2026','2,600 milj. € · TA2027','−100 000 €; § 52:ssa 2026-arvioksi ehdotetaan 2,515 milj. €'],
['Yhteisöverotulo','1,400 milj. € · TA2026','1,715 milj. € · TA2027','+315 000 €; § 52:ssa 2026-arvioksi ehdotetaan 1,580 milj. €'],
['Valtionosuudet','11,276 milj. € · TA2026','10,897 milj. € · TA2027','noin −379 000 €; § 52:n jälkeen vertailu muuttuu'],
['Vuosikate','2,100 milj. € · tuloslaskelman TA2026','3,039 milj. € · TA2027','+939 000 €; rahoituslaskelman 2026-luku poikkeaa'],
['Poistot ja arvonalennukset','3,494 milj. € · TA2026','3,890 milj. € · TA2027','+396 000 €'],
['Tilikauden yli-/alijäämä','−1,310 milj. € · TA2026','−0,767 milj. € · TA2027','543 000 € pienempi alijäämä'],
['Vuosikate suhteessa poistoihin','noin 60 % · TA2026','noin 78 % · TA2027','noin +18 prosenttiyksikköä; oma laskelma'],
['Korkokulut','1,100 milj. € · TA2026','1,100 milj. € · TA2027','Ei muutosta'],
['Muut rahoitustuotot','423 000 € · TA2026','553 000 € · TA2027','+130 000 € · pyöristetyt luvut'],
['Nettoinvestoinnit','4,184 milj. € · TA2026','0,878 milj. € · TA2027','−3,306 milj. €; 2026 lisäinvestointiesitys erikseen § 52'],
['Lainakannan vuosimuutos','+3,313 milj. € · 2026 ennuste, s. 102','−2,187 milj. € · TA2027','Velan kasvu vaihtuu vähenemiseksi; muutos −5,500 milj. €'],
['Lainakanta 31.12.','71,925 milj. € · 2026 ennuste','69,738 milj. € · TA2027','−2,187 milj. €; viimeisin toteumatieto 30.9.2026 on 71,2 milj. €'],
['Lainaa / asukas','6 365 € · 2026 ennuste','6 144 € · 2027 arvio','−221 €/asukas'],
['Asukasluku 31.12.','11 300 · 2026 ennuste','11 350 · 2027 arvio','+50; viimeisin toteuma 30.9.2026 on 11 256'],
['Suunnittelukauden ulkopuoliset hanketarpeet','Aiempi vertailukelpoinen kokonaissumma ei ilmene aineistosta','25,905 milj. € tarpeita nykyisessä kirjassa','Ei vuosimeno eikä uusi määräraha; vuosimuutosta ei voi laskea']
]},
46:{note:'Vuoden 2026 veroprosentti on voimassa oleva prosentti. Vuoden 2026 tulokertymät ovat eri laskentavaiheita, eivät toteutuneita koko vuoden tuloja.',source:[['Veroluvut · s. 89 ja 91',budget],['Vuoden 2026 muutosesitys',pdf('2026768-10-43330')]],rows:[
['Tuloveroprosentti','8,20 % · vuonna 2026','8,20 % · ehdotus 2027','0,00 prosenttiyksikköä · ennallaan'],
['Kunnallisverotulo / budjettivertailu','22,800 milj. € · nykyinen TA2026','24,050 milj. € · TA2027','+1,250 milj. € / noin +5,5 %'],
['Kunnallisverotulo / päivitetty 2026-arvio','23,060 milj. € · § 52:n ehdotus vuodelle 2026','24,050 milj. € · TA2027','+990 000 € / noin +4,3 %'],
['Vaihtoehtolaskelma: +0,10 prosenttiyksikköä','8,20 % · voimassa','8,30 % olisi vaihtoehto, ei päätösehdotus','Kirjan tuottoarvio +270 000 € ensimmäisenä vuonna; myöhemmin noin +310 000 €/v']
]},
47:{note:'Kaikki prosentit ovat esittelyn vuoden 2026 voimassa olevia prosentteja ja vuoden 2027 ehdotuksia. Prosenttiyksikkö on kahden veroprosentin erotus. Verotuotto esitetään erikseen, koska prosentti ja kertymä ovat eri asioita.',source:[['Vuoden 2026 prosentit ja 2027 ehdotus',itemUrl(47)],['Verotuottoarviot · s. 91',budget]],rows:[
['Yleinen vero, rakennukset','1,10 % · 2026','1,10 % · 2027','0,00 prosenttiyksikköä · ennallaan'],
['Yleinen vero, maapohja','1,30 % · 2026','1,30 % · 2027','0,00 prosenttiyksikköä · ennallaan'],
['Vakituinen asuinrakennus','0,45 % · 2026','0,45 % · 2027','0,00 prosenttiyksikköä · ennallaan'],
['Muut asuinrakennukset','1,20 % · 2026','1,20 % · 2027','0,00 prosenttiyksikköä · ennallaan'],
['Rakentamattomat rakennuspaikat','3,00 % · 2026','3,00 % · 2027','0,00 prosenttiyksikköä · ennallaan'],
['Voimalaitokset','3,10 % · 2026','3,10 % · 2027','0,00 prosenttiyksikköä · ennallaan'],
['Yleishyödylliset yhteisöt','Ei erillistä prosenttia · 2026','Ei erillistä prosenttia · 2027','Ei muutosta; ei yleistä verovapautusta'],
['Kiinteistöverotuotto / budjettivertailu','2,700 milj. € · nykyinen TA2026','2,600 milj. € · TA2027','−100 000 €'],
['Kiinteistöverotuotto / päivitetty 2026-arvio','2,515 milj. € · § 52:n ehdotus vuodelle 2026','2,600 milj. € · TA2027','+85 000 €; prosentit eivät silti muutu']
]},
48:{note:'Nykyinen tarkoittaa ennen uutta hyväksymistä sovellettavaa sopimusta. Vanhaa täydellistä sopimusta ei ole tässä liitekokonaisuudessa; kaikkien ehtojen muutosta ei voi varmistaa uuden tekstin perusteella.',source:[['Uusi yhteistoimintasopimus',pdf('2026768-6-43307')],['Vanhan mallin kuvaus · liite 3',pdf('2026768-7-43312')]],rows:[
['Vastuukunta','Turku · nykyinen järjestely','Turku · päivitetty sopimus','Ei vastuukunnan vaihtoa'],
['Maksuosuuksien laskentapohja','Vuoden 2025 rahoituksesta määritetyt kiinteät osuudet; käytössä vuoden 2026 loppuun','Vuosittain päivittyvät osuudet 1.1.2027 alkaen · tarkemmin § 49','Kiinteästä vuosittain päivittyvään'],
['Paimion maksuosuus euroina','Vertailukelpoinen nykyinen sopimusmaksu ei ilmene liitteistä','Uusi Paimio-kohtainen maksu ei ilmene liitteistä','Euromuutosta ei voi laskea'],
['Lautakunnan paikat','Nykyisen sopimuksen paikkalukua ei ole tarkistettu erillisestä vanhasta sopimuksesta','Uudessa tekstissä 13: Turku 6, muut 7; itäisillä kunnilla 2','Uuden tekstin lukua ei tässä väitetä paikkamäärän muutokseksi'],
['Laskutus ja irtisanominen','Vanhojen ehtojen täsmällinen vertailu puuttuu','Uudessa tekstissä laskutus 4 kertaa/v; irtisanomisilmoitus vähintään 18 kk ennen päättymistä','Ehtojen muutos varmistettava vanhasta sopimuksesta']
]},
49:{note:'Vanhan kustannustenjakomallin vertailu perustuu uuden liitteen 3 nimenomaiseen kuvaukseen vanhasta sopimuksesta. Henkilöstön ja paikallisten ICT-kulujen tarkkoja kokonaislukuja ei julkaistu tässä sopimusasiassa.',source:[['Viranomaistehtävien pääsopimus',pdf('2026768-7-43308')],['Maksuosuusmallien vertailu · liite 3',pdf('2026768-7-43312')]],rows:[
['Paimion toiminta-alue','Paimio ja Sauvo · nykyinen toiminta','Paimio ja Sauvo · uusi sopimus','Ei toiminta-alueen vaihtoa'],
['Kiinteiden osuuksien suunniteltu käyttö','Vanhan sopimuksen mukaan vuoden 2027 loppuun','Kiinteät osuudet vain vuoden 2026 loppuun','Vuosittainen päivitys alkaa vuotta aiemmin'],
['Vuosittaisen laskennan painot','Vanhan mallin euromäärät ja kunnittaiset osuudet eivät sisälly julkaistuun aineistoon','Työikäiset 44,78 %, laaja työttömyys 44,78 %, vieraskieliset 10,44 %','Vanhojen ja uusien Paimio-osuuksien erotus puuttuu'],
['Harkinnanvaraisten tukien määrärahat','Paimion nykyinen tukikohtainen enimmäismäärä ei ilmene sopimusliitteistä','Uusi malli: kunta asettaa vuotuisen määrärahan, ylitys vaatii erillistä sopimista','Uusi euromäärä ei ole päätettävänä tässä sopimuksessa'],
['Tietoturvaloukkauksen ilmoitusaika','Vanhan sopimuksen määräaika ei sisälly vertailuaineistoon','Uudessa liitteessä viimeistään 24 h tiedonsaannista','Ei osoitettua muutosta; uusi velvoitetaso on tiedossa'],
['Oma uravalmennus','Ostopalveluun varattua 2027 määrärahaa leikataan valmistelussa 20 000 €','Apilassa omaa tuotantoa; yhteishankintavelvoite säilyy','20 000 € on muutos 2027 valmistelussa, ei osoitettu säästö 2026 toteumaan']
]},
50:{note:'Omistusta verrataan tilanteeseen ennen kauppaa ja kaupan toteuduttua. Myyntitulo on kertaluonteinen, palvelumeno vuosittainen. Hankintahintaa tai alkuperäistä sijoitusta ei pidä sekoittaa nykyiseen kirjanpito- tai markkina-arvoon.',source:[['Kaupan esittely',itemUrl(50)],['Julkinen kauppakirja',pdf('2026768-8-43325')],['Palvelumäärärahan valmistelu · s. 1',memo]],rows:[
['Paimion osakkeet','19 osaketta · ennen kauppaa','0 osaketta · jos kaikki myydään','−19 osaketta'],
['Paimion omistusosuus','14,62 % · ennen kauppaa','0 % · kaupan jälkeen','−14,62 prosenttiyksikköä'],
['Paimion alkuperäinen sijoitus','51 000 € vuonna 2018: osakemerkintä + SVOP','Kiinteä hinta laskelmani mukaan noin 73 077 €','Eri erät: nykyinen kirjanpitoarvo ja myyntivoitto eivät ilmene julkisesta aineistosta'],
['Koko osakekannan kauppahinta','Nykyistä riippumatonta markkina-arvoa ei ole julkaistu','Kiinteä 500 000 € + lisähinta enintään 250 000 €','Hinnan käypyyttä ei voi päätellä ilman arvonmääritystä'],
['Paimion mahdollinen lisähinta','Ei nykyistä lisähintasaamista tästä toteutumattomasta kaupasta','Enintään noin 36 538 € · laskelma 19/130-osuudella','Ehdollinen, ei varma tulo; laskentaliite puuttuu'],
['Taloushallinnon palvelumääräraha','2026 vertailukelpoinen palvelusopimuksen vuosihinta ei ilmene aineistosta','2027 valmistelussa 204 000 € → 194 000 €','−10 000 € valmistelun sisällä; 2026–2027 muutos puuttuu'],
['Kuntalaina yhtiölle, kaikki myyjät','182 395,58 € · kauppakirjan lainamäärä','Takaisinmaksu tai sopimuksen mukainen hinnan oikaisu','Paimion oma lainaosuus ja nettovaikutus varmistettava'],
['Kilpailu- ja rekrytointikielto','Aiemman vastaavan kiellon kesto ei ilmene aineistosta','Kilpailukielto 5 vuotta, rekrytointikielto 4 vuotta','Kauppaan liittyviä rajoituksia; ei vuosimenoa'],
['Sidosyksikköomistuksen raja','Paimion omistus nyt 14,62 %','Uusi lakiraja 10 %; pääsääntöinen soveltaminen 1.7.2027','Paimio ylittää rajan nyt 4,62 prosenttiyksiköllä; kaupan jälkeen ei omistusta']
]},
51:{note:'Tämä koskee Kiinteistökuntayhtymän tarkastusta, ei Paimion kaupungin omaa tilintarkastussopimusta.',rows:[
['Tilintarkastussopimuksen tila','Edellinen sopimuskausi on esittelyn mukaan päättynyt','BDO Audiator Oy tilikaudelle 2026 + tarkastuslautakunnan sihteerityö','Vuoden 2026 valinta ratkaistaan nyt'],
['Tarkastuksen vuosihinta','Nykyinen / edellinen hinta ei ilmene julkisesta aineistosta','Uusi hinta ei ilmene; mainittu sopimusluonnos puuttuu','Hintamuutosta ei voi laskea']
]},
52:{note:'Saman vuoden 2026 muutosesitys: vasemmalla nykyinen talousarvio, keskellä kokouksessa ehdotettu uusi määrä. Kumpikaan sarake ei ole toteuma. Erotukset ovat liitteen mukaisia.',source:[['Talousarviomuutokset 2026 · 1 s.',pdf('2026768-10-43330')]],rows:[
['Tilintarkastuksen toimintamenot','38 194 €','48 194 €','+10 000 €'],
['Konsernijohdon ja hallinnon toimintatuotot','522 700 €','372 700 €','−150 000 €'],
['Kunnallisvero','22 800 000 €','23 060 000 €','+260 000 €'],
['Kiinteistövero','2 700 000 €','2 515 000 €','−185 000 €'],
['Yhteisövero','1 400 000 €','1 580 000 €','+180 000 €'],
['Verot yhteensä','26 900 000 €','27 155 000 €','+255 000 €'],
['Peruspalvelujen valtionosuus','7 193 200 €','7 252 000 €','+58 800 €'],
['Verotuloihin perustuva valtionosuuksien tasaus','2 893 500 €','2 846 000 €','−47 500 €'],
['Opetus- ja kulttuuritoimen valtionosuus','436 000 €','278 400 €','−157 600 €'],
['Veromenetysten korvaus','753 000 €','704 000 €','−49 000 €'],
['Valtionosuudet yhteensä','11 275 700 €','11 080 400 €','−195 300 €'],
['Tilikauden alijäämä / laskennallinen yhteisvaikutus','1 309 709 € · nykyinen TA2026 tuloslaskelmassa','1 410 009 € · jos vain nämä muutokset lisätään','Alijäämä kasvaa 100 300 €; oma laskelma, ei toteumaennuste'],
['Talonrakennuksen investointimenot','3 030 000 €','3 500 000 €','+470 000 €'],
['Julkisen käyttöomaisuuden investointimenot','960 000 €','810 000 €','−150 000 €'],
['Näiden kahden investointiryhmän menot yhteensä','3 990 000 €','4 310 000 €','+320 000 €; ei koko kaupungin investointisummaa'],
['Seisakkeiden ratasuunnittelun varaus','150 000 € · TA2026','0 € · muutosehdotus','−150 000 €; sisältyy yllä julkiseen käyttöomaisuuteen']
]},
53:{note:'Suunnitelma koskee vuosia 2026–2030. Alla oleva numeerinen nykytila ja lähiajan tavoite tulevat saman kokouksen talousarviokirjan EN2026- ja TA2027-sarakkeista; ne eivät ole tämän hyvinvointisuunnitelman erikseen vahvistettuja 2030-tavoitteita. EN = ennuste, ei lopullinen toteuma.',source:[['Hyvinvointisuunnitelma',pdf('2026768-11-43331')],['Hyvinvoinnin toimintaluvut · s. 61 ja 69–70',budget]],rows:[
['Avoin nuorisotyö, käyntejä','7 000 · EN2026','7 000 · TA2027','Ennallaan'],
['Kesäleirit ja retket, osallistujia','444 · EN2026','444 · TA2027','Ennallaan'],
['Etsivän nuorisotyön tavoittamat','41 · EN2026','44 · TA2027','+3'],
['Koulunuorisotyön osallistujamäärä, kirjan mittari','11 500 · EN2026','11 500 · TA2027','Ennallaan; ei välttämättä eri henkilöiden määrä'],
['PaHaMa, osallistujia','450 · EN2026','700 · TA2027','+250'],
['Uimahallin kävijämäärä','82 000 · EN2026','82 000 · TA2027','Ennallaan'],
['Liikuntaneuvonnan osallistujat','30 · EN2026','30 · TA2027','Ennallaan'],
['Kirjaston aukiolotunnit','4 500 · EN2026','4 500 · TA2027','Ei lisäystä budjettimittarissa; henkilöstölliset palveluajat eri asia'],
['Kirjaston henkilötyövuodet','6,20 · EN2026','5,40 · TA2027','−0,80 htv'],
['Koulunuorisotyön rahoitus','Hankerahoitteinen toiminta vuonna 2026','Hankerahoitus 30.11.2027 asti; joulukuu budjetoitu','Pysyvä jatko 2028 alkaen vielä ratkaisematta'],
['Maksujen korotukset: Ankkalampi, kortit, leirit ym.','Nykyisiä palvelukohtaisia hinnastoja ei ole näissä liitteissä','Lisätuloksi tavoitellaan yhteensä 19 400 € vuonna 2027','Yksittäistä vanhaa ja uutta hintaa tai korotusprosenttia ei voi laskea'],
['Suunnitelman varsinaiset 2030-mittarit','Kattavat lähtöarvot eivät sisälly suunnitelmaan','Useille mittareille ei numeerista 2030-tavoitetta','Lähtö- ja tavoitetasot täydennettävä']
]},
54:{note:'Tässä verrataan samaa yhdeksän kuukauden jaksoa 1.1.–30.9.2025 ja 1.1.–30.9.2026. Kokonaisen vuoden talousarvio ei ole suoraan vertailukelpoinen yhdeksän kuukauden toteumaan. Rahamäärien erotukset lasketaan julkaistuista taulukkoluvuista; yhden euron pyöristyseroja voi syntyä.',source:[['Tuloslaskelma 1–9/2026 ja 1–9/2025',pdf('2026768-12-43037')]],numeric:[
['Myyntituotot',3052972,2994695],['Maksutuotot',549283,577200],['Tuet ja avustukset',731855,574363],['Muut tuotot',4528017,5035299],['Toimintatuotot, sisäiset + ulkoiset',8862127,9181558],
['Henkilöstökulut, menojen määrä',17629145,18015253],['Palvelujen ostot, menojen määrä',9651169,9540512],['Aineet ja tarvikkeet, menojen määrä',2302961,2234627],['Avustukset, menojen määrä',967518,1233887],['Muut toimintakulut, menojen määrä',3581226,4247484],['Toimintakulut, sisäiset + ulkoiset',34132019,35271763],
['Toimintakate',-25269892,-26090205],['Kunnallisvero',15808705,17276256],['Kiinteistövero',2031180,1958176],['Yhteisövero',1083471,1258468],['Verot yhteensä',18923356,20492899],['Valtionosuudet',8051228,8304001],
['Korkotuotot',224690,222919],['Muut rahoitustuotot',418825,418375],['Korkokulut, menojen määrä',347715,528966],['Muut rahoituskulut, menojen määrä',4739,5112],['Vuosikate',1995752,2813912],['Poistot + satunnaiset, kulujen määrä',2497747,2715918],['Tilinpäätössiirrot',63046,63046],['Yli-/alijäämä',-438949,161039],['Ulkoiset toimintatuotot',4447907,4108345],['Ulkoiset toimintakulut, menojen määrä',29717800,30198551]
],rows:[
['Lainakanta: eri ajankohtien toteumat','68,612 milj. € · 31.12.2025','noin 71,2 milj. € · 30.9.2026','noin +2,6 milj. €; ei vuosien välinen 9 kk -vertailu'],
['Asukasluku: eri ajankohtien toteumat','11 278 · 31.12.2025','11 256 · 30.9.2026','−22 asukasta'],
['Kassavarat: aineiston eri ajankohdat','1,0 milj. € · 31.12.2025','2,9 milj. € · heinäkuun loppu 2026','+1,9 milj. €; syyskuun kassaluku puuttuu'],
['Vuoden 2026 tulosarvio vs. 2025 tilinpäätös','−1,918 milj. € · koko vuoden 2025 toteuma','Valmistelijan ehdollinen arvio: 2026 alijäämä alle 1 milj. €','Ei varma toteuma eikä täsmällinen uusi ennuste']
]},
55:{note:'Avoin menettelykohta, ei julkaistuja talouslukuja.',rows:[['Asioiden sisältö','Ei yksilöityjä kiireellisiä asioita tarkistusaineistossa','Mahdolliset asiat selviävät kokouksessa','Talousvaikutusta tai muutosta ei voi vielä laskea']]},
56:{note:'Avoin aloitteiden vastaanottokohta, ei julkaistuja talouslukuja.',rows:[['Aloitteiden sisältö','Ei yksilöityjä aloitteita tarkistusaineistossa','Kokouksessa jätettävät aloitteet','Ei automaattisesti uutta määrärahaa tai palvelupäätöstä']]}
};
const resourceComparisons=[
['Sivistyspalvelujen hallinnon henkilöstö','6,5 · EN2026','6 · TA2027','−0,5; kirjan henkilöstömäärämittari'],
['Päiväkotien hoito- ja kasvatushenkilöstö','102 · EN2026','95 · TA2027','−7; kirjan henkilöstömäärämittari'],
['Perhepäivähoidon ja ryhmisten henkilöstö','14 · EN2026','12 · TA2027','−2; kirjan henkilöstömäärämittari'],
['Varhaiskasvatuksen lapset, syyskuu','582 · EN2026','561 · TA2027','−21 lasta'],
['Kaupungin päiväkotien lapset','393 · EN2026','360 · TA2027','−33 lasta'],
['Yksityisten päiväkotien lapset','148 · EN2026','160 · TA2027','+12 lasta'],
['Palvelusetelin saajat, kirjan mittari','160 · EN2026','170 · TA2027','+10'],
['Varhaiskasvatuksen palvelusetelimääräraha','2,1 milj. € · TA2026','2,2 milj. € · TA2027','+100 000 €'],
['Preitilän päiväkoti','Toiminnassa vuonna 2026','Määrärahat 31.7.2027 asti','Esitys ennakoi toiminnan päättymistä 1.8.2027; erillinen päätös'],
['Käenpesän varahoitoyksikkö','Nykyinen varahoitoyksikkö','Toiminta päättyisi 31.7.2027','Uusi varahoitojärjestely; säästön kuvaus ristiriitainen'],
['Vistan koulunkäynninohjaajat','Nykyinen kokonaismäärä ei ilmene aineistosta','Kuusi vähemmän','−6 ohjaajaa; 93 600 € säästö vuonna 2027'],
['Luokanopettajat','Nykyinen kokonaismäärä ei ilmene aineistosta','Yksi vähemmän elokuusta 2027','−1; 27 000 € säästö, sama erä esiintyy tekstissä kahdesti'],
['Aloittavat ensimmäiset luokat','Nykyinen vastaava luokkamäärä ei ilmene aineistosta','Kuusi ryhmää syksyllä 2027','Tarkka 2026–2027 ryhmämäärän erotus ei varmistettavissa'],
['Yläkoulun ryhmävertailu','Kahdeksan keväällä 2026 päättänyttä 9. luokkaa','Seitsemän aloittavaa 7. luokkaa syksyllä 2027','Eri vuosiluokat; ei saman ikäluokan 8 → 7 -muutos'],
['Lukion erityisopettajaresurssi','Vähennystä edeltävää tarkkaa resurssia ei ilmoiteta tässä kohdassa','0,5 erityisopettajan resurssi','25 000 € säästö; aikaisempaa määrää ei oleteta'],
['Kirjaston henkilötyövuodet','6,20 · EN2026','5,40 · TA2027','−0,80 htv'],
['Kirjaston lainausmäärä','263 000 · EN2026','276 900 · TA2027','+13 900 lainaa'],
['Kirjaston lukutaitotyön osallistujat','2 500 · EN2026','2 200 · TA2027','−300'],
['Kirjaston aukiolotunnit','4 500 · EN2026','4 500 · TA2027','Ennallaan; ei sama kuin henkilöstöllinen palveluaika'],
['Infran määräaikainen työpanos','Kokonaistyöpanos ei ilmene aineistosta','Työpanosta vähennetään 2,38 htv','−2,38 htv'],
['Infran kausityöpanos','Kokonaistyöpanos ei ilmene aineistosta','Lisäksi vähennetään 1,0 htv','−1,0 htv; tekstin mukaan yllä olevan lisäksi'],
['Kiinteistökunnossapidon henkilöstövaje','Yhden htv:n vajaus jatkunut vuodesta 2024','Sama vajaus sisältyy TA2027:ään','Ei uusi yhden htv:n vähennys vuodesta 2026'],
['Leikkikentät','18 · EN2026','16 · TA2027','−2'],
['Aurauskierrokset','14 · EN2026','14 · TA2027','Ennallaan; todellinen tarve riippuu säästä'],
['Kiinteistöjen määrä','101 · EN2026','98 · TA2027','−3 rakennusta'],
['Vesi-, sähkö- ja kaukolämpökulut','1 516 600 € · EN2026','1 599 650 € · TA2027','+83 050 €'],
['Tilintarkastuspäivät, kaupungin oma tarkastus','33 · EN2026','24 · TA2027','−9 päivää; ei § 51:n kuntayhtymäsopimus'],
['Työttömyysprosentti','7,9 % · EN2026','7,0 % · TA2027 tavoite','−0,9 prosenttiyksikköä'],
['Työttömyysturvan rahoitus, toimintataulukko','861 000 € · EN2026','861 000 € · TA2027','Taulukossa ennallaan; muistio pitää tavoitetta 2026 maksuja pienempänä → ristiriita'],
['Vapaa-aikapalvelujen lisätulot','Vertailukelpoinen palvelukohtainen hinnasto puuttuu','Tavoite +19 400 €','Korotus ei ole 19 400 € jokaisessa palvelussa; kokonaistavoite'],
['Asukasbudjetoinnin määräraha','Vuoden 2026 vastaava kokonaisvaraus ei ilmene tarkistetusta kohdasta','20 000 € vuonna 2027 Unto Vainion rahastosta','Vuosimuutos puuttuu; rahoituslähde ilmoitettu'],
['Lautakuntien esityksen tasapainotus','−1 695 760 € · lautakuntien 2027 esitysten alijäämä','−767 285 € · kaupunginjohtajan 2027 esitys','928 475 € parannus saman valmisteluvuoden sisällä'],
['Kevan tasausmaksuarvio','560 023 € · toukokuun arvio vuodelle 2027','299 885 € · lokakuun arvio vuodelle 2027','−260 138 €; ei vuoden 2026 toteumaan verrattu säästö']
];
const sectorComparisons=[
['Konsernijohto ja hallintopalvelut',2461,2582],['Maaseutupalvelut',51,53],['Työvoimapalvelut',1954,2377],['Sivistyspalvelujen hallinto',567,520],['Varhaiskasvatus',10533,10237],['Perusopetus',14441,14783],['Toisen asteen koulutus',2077,2146],['Kirjasto ja kulttuuri',785,762],['Paimion opisto',761,738],['Vapaa-aikapalvelut',1790,1653],['Tekninen hallinto',370,340],['Infrapalvelut',1425,1480],['Ympäristöpalvelut',827,781]
];
const groupComparisons=[
['Yrityskiinteistöjen omavaraisuus','6,00 % · kirjan 2026-luku','6,00 % · vuoden 2027 tavoite','Ennallaan; ei vahvistettu vuoden 2026 tilinpäätös'],
['Yrityskiinteistöjen liikevaihto','396 000 € · kirjan 2026-luku','323 000 € · vuoden 2027 tavoite','−73 000 €'],
['Palvelukeskussäätiön omavaraisuus','0,76 % · kirjan 2026-luku','1,38 % · vuoden 2027 tavoite','+0,62 prosenttiyksikköä'],
['Palvelukeskussäätiön liikevaihto','1 215 000 € · kirjan 2026-luku','1 268 000 € · vuoden 2027 tavoite','+53 000 €'],
['Lämpökeskuksen liikevoitto','769 000 € · kirjan 2026-luku','758 000 € · vuoden 2027 tavoite','−11 000 €'],
['Vesihuollon omavaraisuus','31,9 % · kirjan 2026-luku','32,4 % · vuoden 2027 tavoite','+0,5 prosenttiyksikköä'],
['Lyyli Tuomolan säätiön liikevoitto','−66 000 € · kirjan 2026-luku','−59 000 € · vuoden 2027 tavoite','Tappio pienenee 7 000 €']
];
const euro=new Intl.NumberFormat('fi-FI',{maximumFractionDigits:0});
const fmtEuro=n=>euro.format(n)+' €';
const deltaEuro=n=>(n>0?'+':'')+fmtEuro(n);
function compareRows(i){const c=comparisons[i.n];return [...(c.numeric||[]).map(([label,old,now])=>[label,fmtEuro(old)+' · 1–9/2025',fmtEuro(now)+' · 1–9/2026',deltaEuro(now-old)]),...(c.rows||[])];}
function comparison(i){const c=comparisons[i.n];const headers=i.n===54?['Mittari','Vertailutilanne','Nykyinen toteuma / tieto','Muutos']:i.n===52?['Erä','Nykyinen TA2026','Ehdotettu uusi TA2026','Muutos']:['Mittari','Nyt / vertailupohja','Esitys / seuraava tilanne','Muutos'];return `<section class="block comparison"><div class="block-label">Nykytilanne → esitys</div><p class="small">${escape(c.note)}</p>${table(headers,compareRows(i))}<div class="sources" style="margin-top:13px">${(c.source||[['Asian esittely',itemUrl(i.n)]]).map(([n,u])=>link(n,u)).join('')}</div></section>`;}
function budgetComparisons(){return `<details><summary>Palvelujen nettomenot · 2026 → 2027</summary><p class="small">1 000 euroa, sisäiset ja ulkoiset erät. Menojen ja tulojen erotus esitetään tässä nettomenona ilman miinusmerkkiä. Erotukset laskettu pyöristetyistä luvuista. Kiinteistöpalvelujen positiivista sisäistä toimintakatetta ei sekoiteta näihin nettomenoihin.</p>${table(['Palvelu','TA2026','TA2027','Muutos, 1 000 €'],sectorComparisons.map(([n,a,b])=>[n,euro.format(a),euro.format(b),(b-a>0?'+':'')+euro.format(b-a)]))}${link('Talousarviokirja · s. 13–14',budget)}</details><details><summary>Henkilöstö, palvelumäärät ja säästöjen lähtötasot</summary><p class="small">Henkilöstömäärä, henkilötyövuodet ja rahamääräinen säästö ovat eri mittareita. Jos vanhaa kokonaismäärää ei ole kerrottu, sitä ei ole päätelty vähennyksestä.</p>${table(['Mittari','Nyt / vertailupohja','Esitys / tavoite','Muutos'],resourceComparisons)}${link('Talousarviokirja',budget)} ${link('Kaupunginjohtajakäsittelyn muistio',memo)}</details><details><summary>Konsernin luvut · 2026 → 2027</summary><p class="small">Lähde: talousarviokirjan konsernitavoitteet, s. 104–111. Vuoden 2026 saraketta ei esitetä vahvistettuna tilinpäätöksenä.</p>${table(['Mittari','Kirjan 2026-luku','Vuoden 2027 tavoite','Muutos'],groupComparisons)}${link('Konsernitavoitteet',budget)}</details>`;}
'''
assert 'const comparisons=' not in html
html = html.replace('const checked=new Set();', addition+'\nconst checked=new Set();', 1)
needle='${list(i.facts)}${extras(i)}'
assert html.count(needle)==1
html=html.replace(needle,'${list(i.facts)}${extras(i)}')
needle='<section class="block"><div class="block-label">01 / Todettu ja päätösehdotus</div>'
assert html.count(needle)==1
html=html.replace(needle,'${comparison(i)}'+needle,1)
needle="function extras(i){if(i.extra==='budget')return `"
assert html.count(needle)==1
html=html.replace(needle,needle+'${budgetComparisons()}',1)
# Replace the secondary future-only table with a baseline column, retaining future plans.
old="table(['Erä','2027','2028','2029'],[['Toimintakate, milj. €','−36,117','−36,515','−37,278'],['Verotulot, milj. €','28,365','29,300','30,400'],['Valtionosuudet, milj. €','10,897','10,897','10,897'],['Vuosikate, milj. €','3,039','3,574','noin 3,811'],['Poistot, milj. €','3,890','3,890','3,890'],['Yli-/alijäämä, 1 000 €','−767','−232','noin +5'],['Nettoinvestoinnit, milj. €','0,878','1,716','1,346'],['Velan muutos, milj. €','−2,187','−2,123','−2,623'],['Velka 31.12., milj. €','69,738','67,615','64,992']],'financial')"
new="table(['Erä','TA2026*','2027','2028','2029'],[['Toimintakate, milj. €','−35,840','−36,117','−36,515','−37,278'],['Verotulot, milj. €','26,900','28,365','29,300','30,400'],['Valtionosuudet, milj. €','11,276','10,897','10,897','10,897'],['Vuosikate, milj. €','2,100','3,039','3,574','noin 3,811'],['Poistot, milj. €','3,494','3,890','3,890','3,890'],['Yli-/alijäämä, 1 000 €','−1 310','−767','−232','noin +5'],['Nettoinvestoinnit, milj. €','4,184','0,878','1,716','1,346'],['Velan muutos, milj. €','+3,313 (EN)','−2,187','−2,123','−2,623'],['Velka 31.12., milj. €','71,925 (EN)','69,738','67,615','64,992']],'financial')"
assert old in html
html=html.replace(old,new,1)
html=html.replace('Pyöristetyt luvut kirjan s. 15–20 ja 102.','* TA2026 sisältää muutokset 23.9.2026 asti, ei § 52:n ehdotuksia. EN = vuoden 2026 ennuste. Pyöristetyt luvut kirjan s. 15–20 ja 102.',1)
# The full comparisons replace duplicate short tables, avoiding two subtly different presentations.
start=html.index("if(i.extra==='tax')return table(")
end=html.index("if(i.extra==='attachments')",start)
html=html[:start]+"if(i.extra==='tax')return '';\n"+html[end:]
start=html.index("if(i.extra==='changes')return table(")
end=html.index("function item()",start)
html=html[:start]+"if(i.extra==='changes')return '';return '';}\n"+html[end:]
# Place current comparators directly on the overview cards as well.
html=html.replace('Vuosikate kattaa noin 78 % poistoista.</p></div>','TA2026: −1,31 milj. € → 2027: −0,77 milj. €. Alijäämä pienenee noin 0,54 milj. €.</p></div>',1)
html=html.replace('Rahoituslaskelma; velka vuoden lopussa 69,74 milj. €.','2026 ennuste: velka +3,31 milj. € → 2027: −2,19 milj. €. Lainakanta 71,93 → 69,74 milj. €.',1)
html=html.replace('Karkeita tarvearvioita, eivät uusia määrärahoja.','Nykyinen karkea tarvearvio, ei vuosimeno. Aiempi vertailukelpoinen kokonaissumma puuttuu.',1)
html=html.replace('<section class="section"><h3>Neljä asiaa, joihin tarttua</h3>', '<div class="note"><strong>Mitä ”nyt” tarkoittaa?</strong> TA2026 = nykyinen talousarvio, EN2026 = ennuste, toteuma = toteutunut rajattu ajanjakso. § 52:ssa verrataan saman vuoden vanhaa ja ehdotettua uutta budjettia. Vertailun ajankohta on aina merkitty; puuttuvaa lähtölukua ei ole arvioitu.</div><section class="section"><h3>Neljä asiaa, joihin tarttua</h3>',1)
html=html.replace('Faktat, oma arvio ja kokouskysymykset on erotettu toisistaan.','Jokaisessa asiassa näet ensin nykytilanteen, ehdotuksen ja muutoksen. Faktat, oma arvio ja kokouskysymykset on erotettu toisistaan.',1)
# Searches include the new comparison tables.
old="[i.n,i.title,i.tag,...i.facts,i.assessment,...i.risks,...i.questions].join(' ')"
assert old in html
html=html.replace(old,"[i.n,i.title,i.tag,...i.facts,i.assessment,...i.risks,...i.questions,JSON.stringify(comparisons[i.n])].join(' ')",1)
html=html.replace('Valtuutetun valmistautumisaineisto · 8.11.2026 ·','Valtuutetun valmistautumisaineisto · Lähdeaineisto 8.11.2026, vertailut täydennetty 9.11.2026 ·',1)
path.write_text(html,encoding='utf-8')
print('Päivitetty:',path.name)
