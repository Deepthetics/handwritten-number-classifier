# Viikkoraportti 3

Tällä viikolla on tehty:
- viime viikolla toimimattomat yksikkötestit korjattu
- harmaasävyskaalaiset kuvat muunnettu mustavalkoisiksi ja tämä muunnettu kuvadata talletettu tiedostoihin, jotta pitkän aikaa kestävää muunnosta ei tarvitse suorittaa uudelleen
- perehdytty tarkemmin käytettävien etäisyysmittojen laskemiseen

Ohjelma on edistynyt:
- luotu toiminnallisuudet kuvadatan plottaamiseen ja kuvien välisten etäisyyksien laskemiseen eri etäisyysmitoilla

Opittu:
- kuvadatan plottaamisen toteuttamisesta

Epäselvyydet ja vaikeudet:

Ennen edellisen palautuksen deadlinea oli ongelma etäisyyden laskemisen kanssa, koska luin artikkelin notaatiosta väärin yhden yksityiskohdan, mutta tämä on käsittääkseni nyt korjattu. Hieman edelleen hämmentää etäisyysmittaa D22 käyttäessä funktion f2 tarpeellisuus. Ainakin näiden samankokoisten kuvien etäisyyksiä laskettaessa saan aina d(A,B)=d(B,A), jonka vuoksi max(d(A,B), d(B,A)) on triviaali toimenpide. Ja koska d(A,B)=d(B,A), niin riittäisi laskea vain d(A,B) käyttäen osakaavaa d6. Jos näin ei kuuluisi olla, niin siinä tapauksessa etäisyyden laskemisessa on edelleen jotain väärin.

Onko sovellukselle tarkoitus luoda jonkinlainen käyttöliittymä ja jos on niin tarvitseeko sen olla graafinen vai riittääkö tekstikäyttöliittymä?

Seuraavaksi:
- ensi viikolla olisi tarkoitus varmistua siitä, että etäisyyksien laskeminen on varmasti toteutettu oikein
- tämän jälkeen on tarkoitus toteuttaa toiminnallisuudet testidatan kuvien luokitteluun k:n lähimmän naapurin menetelmällä ja päästä testamaan menetelmää käytännössä

Työhön käytetty aika tällä viikolla: 11 tuntia.
