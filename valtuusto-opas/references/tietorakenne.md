# Kokoustietojen JSON

Kirjoita UTF-8-koodattu JSON. Esimerkin nimet, luvut ja osoitteet ovat kuvitteellisia. Korvaa ne tarkistetuilla tiedoilla ja lisää jokainen pykälä esityslistan järjestyksessä.

Katso [esityslistan perustiedot](../examples/esityslista-esimerkki.json) ja [täytetty kokous-JSON](../examples/kokous-esimerkki.json). Perustiedoista voi luoda täytettävän luonnoksen skriptillä `scripts/prepare_meeting.py`. Se kopioi pykälät ja linkit ja jättää analyysin kentät täytettäviksi.

- `meeting.time` ja `meeting.venue` ovat valinnaisia. `meeting.sources` voi sisältää koko oppaan yhteisiä lähteitä ja säädöslinkkejä. Valinnainen `meeting.home` on paluulinkin osoite oppaiden luetteloon, esimerkiksi `"../index.html"`, kun opas tallennetaan repon `oppaat`-kansioon. Ilman sitä paluulinkkiä ei näytetä. Valinnainen `meeting.contact` on sähköpostiosoite, johon lukija voi ilmoittaa virheistä; se näkyy tilannekuvan tekoälyhuomautuksessa.
- `overview.stats`, `overview.highlights`, `overview.sources` ja `overview.comparisonNote` ovat valinnaisia. Nostoissa ja tarkennuksissa `n` viittaa olemassa olevaan pykälään.
- Jokaisella pykälällä on `facts`, `risks` ja `questions` tekstilistoina. Tyhjä lista sopii, jos riskiä tai kysymystä ei noussut. `critical` on valinnainen huomion merkki. `sources` sisältää pykälän muut lähteet.
- Jokaisella pykälällä on `comparison.note`. Jos vertailtavaa lukua ei ole, selitä syy siinä. `rows` voi silloin puuttua. Oletuksena jokainen rivi sisältää neljä solua. `headers` voi korvata oletusotsikot esimerkiksi toteumavertailussa.
- `attachments` listaa liitteet ja alaliitteet. Käytä kuvaavaa tilaa, esimerkiksi **Luettu**, **Osin peitetty**, **Linkki puuttuu** tai **Linkitetty, jäi lukematta**. Jätä `url` pois vain, kun osoitetta ei ole. Kerro olennainen liitteen sisältö tai saatavuuden syy kentässä `summary`.
- `details` on valinnainen lista taitettavia erittelyjä. Kukin osio sisältää `title` ja tarvittaessa `text`, `sources` tai taulukon `headers` ja `rows`.
- Kaikki `sources`-kentät ovat `[nimi, URL]`-pareja. Käytä suoria https-osoitteita, kun sellaisia on. Lisää sivunumero linkin nimeen, vaikka PDF:n sivuankkuri ei toimisi kaikissa selaimissa.
