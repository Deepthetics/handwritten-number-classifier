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

Olen mielestäni toteuttanut etäisyyksien laskemisen oikein etäisyysmittoja käsittelävän artikkelin pohjalta, mutta testatessani etäisyyden laskemista esim. mitalla D22, saan etäisyydeksi aina arvon 0. Jokin virhe toteutuksessa luultavasti on, mutta en sellaista useiden tarkistuksienkaan jälkeen vielä löytänyt. Vaikuttaisi siltä, että osakaavaa d6 vastaava funktio palauttaa aina arvon 0, koska sen laskema summa on vain summa nollia, koska min(d(a, b)) saa aina arvon nolla, kun b in B kaikilla a in A. Tästä johtuen funktio f2 palauttaa aina arvon 0, jolloin myös D22 palauttaa aina arvon 0...

Seuraavaksi:
- ensi viikolla olisi tarkoitus varmistua siitä, että etäisyyksien laskeminen on varmasti toteutettu oikein
- tämän jälkeen on tarkoitus toteuttaa toiminnallisuudet testidatan kuvien luokitteluun k:n lähimmän naapurin menetelmällä ja päästä testamaan menetelmää käytännössä

Työhön käytetty aika tällä viikolla: 11 tuntia.
