# Toteutusdokumentti

## Ohjelman rakenne

Ohjelmakoodi on jaettu seuraaviin moduuleihin:

calculation_utlities.py: Sisältää laskennan apuvälineinä käytettävät funktiot

distance_measures.py: Sisältää eri etäisyysmitoilla etäisyyksien laskemiseen käytettävät funktiot

image_plotting.py: Sisältää kuvadatan plottaamiseen käytettävät funktiot

image_processing.py: Sisältää kuvadatan käsittelyyn käytettävät funktiot

knn.py: Sisältää k-NN-menetelmään liittyvät funktiot

## Ohjelman toiminta

Testidatan kuvia pystyy luokittelemaan k-NN-menetelmällä. Käyetettävä harjoitusdata, testidatan luokiteltavat kuvat, k-NN-menetelmässä käytettävä k:n arvo ja etäisyysmitta on mahdollista valita. Ohjelma tulostaa luokiteltujen kuvien ennustetut luokat, todelliset luokat sekä luokitteluvirheen.

Luokitteluista on myös mahdollista plotata seuraavanlainen esitys:

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/classification.png)

Ohjelmalla on yksinkertainen tekstikäyttöliittymä, joka näyttää seuraavanlaiselta:

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/tiralabra_ui.png)

## Suorituskyky ja O-analyysi

Alkuperäiset kuvat ovat harmaasävyisiä ja kuvien välisten etäisyyksien laskemista varten ne täytyy muuttaa mustavalkoisiksi. Harjoitusdatassa on 60000 kuvaa ja testidatassa 10000 kuvaa. Kuvien resoluutio on 28x28. Jotta kuvat saadaan muutettua mustavalkoisiksi, täytyy läpikäydä (60000 + 10000) * 28 * 28 = 54880000 pikseliä. Tämä on aikaavievä operaatio ja sen vuoksi kuvat ovat etukäteen muutettu mustavalkoisiksi ja talletettu tässä muodossa tiedostoon ohjelman käytettäväksi.

Jos luokittelussa käytettävän harjoitusdatan kuvien tai testidatasta luokiteltavien kuvien määrää kasvatetaan, kasvaa luokittelun aikavaativuus lineaarisesti O(n), kun n vastaa harjoitusdatassa olevien kuvien tai testidatasta luokiteltavien kuvien määrää.

Käytettävien kuvien resoluutio vaikuttaa luokittelun aikavaativuuteen merkittävästi. Kuvien välisten etäisyyksien laskemisen aikavaativuus kasvaa neliöllisesti O(n<sup>2</sup>), kun n vastaa käytettävää resoluutiota nxn.

Etäisyyksien laskemista on optimoitu luomalla tietorakenne, joka sisältää jokaista 28x28-resoluutioisen kuvan pikseliä kohden listan, joka sisältää kaikkien muiden pikselien koordinaatit järjestyksessä lähimmästä kauimmaiseen. Kun lasketaan pisteen ja pistejoukon välistä pienintä etäisyyttä, päästään kyseistä tietorakennetta käyttämällä keskimäärin samaan aikavaativuuteen, mutta pienemmällä vakiokertoimella. Kun luokiteltavien kuvien määrä kasvaa, saadaan keskimäärin parempi suorityskyky, jonka huomaa ohjelmaa käyttäessä. 

Jotta voidaan selvittää k lähintä naapuria jokaista luokiteltavaa kuvaa kohden, täytyy harjoitusdatan kuvat järjestää etäisyyksien mukaan pienimmästä suurimpaan. Tähän voidaan käyttää minimikekoa tai järjestämisalgoritmia. Kummassakin tapauksessa aikavaativuus on n log n, kun n vastaa harjoitusdatan kuvien määrää.

## Puutteet ja parannusehdotukset

Ohjelmakoodissa joudutaan välillä tekemään datatyyppien muunnoksia pandas- ja numpy-kirjastojen objektien välillä. Tämä monimutkaistaa ohjelmakoodia hieman, koska kaikki toiminnallisuus olisi ollut mahdollista toteuttaa pelkästään numpy:a käyttämällä, vaikka pandas-kirjaston käyttö paikoin vähentääkin kirjoitettavan koodin määrää.

Useamman luokittelun plottaaminen olisi käyttäjäystävällisempää sisällyttää samaan ikkunaan. Tällä hetkellä jokainen yksittäinen luokittelu plotataan omaan ikkunaansa.
