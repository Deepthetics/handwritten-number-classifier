# Testausdokumentti

## Yksikkötestaus
Tällä hetkellä automatisoidut yksikkötestit calculation_utilities-, distance_measures- ja image_processing-moduulien funktioille knn-moduulin funktioille. Moduulien image_plotting ja ui funktioita ei ole tarkoitus testata automaattisesti, koska ne vastaavat erilaisista plottaustoimenpiteistä sekä käyttöliittymästä eivätkä itse suoraan palauta mitään.

Testit pystyy toistamaan ajamalla projektin juuressa komennon:

```bash
pytest src
```

## Yksikkötestien haarautumakattavuus

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/coverage.png)

## Manuaalinen testaus
Moduulin image_plotting funktioiden toimintaa on testattu manuaalisesti. Kyseisen moduulin funktiota plot_two_images pystyy käyttämään manuaalisen testauksen työkaluna havainnoimaan silmämääräisesti, että kuvadatan muunnoksesta vastaava funktio to_binary toimii odotetulla tavalla. Alkuperäisen greyscale-kuvan ja mustavalkoisen muunnoksen voi plotata vierekkäin:

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/conversion.png)

## Luokittelualgoritmin empiirinen testaus

Empiirisen testauksen tuloksien tulkinnassa täytyy ottaa huomioon, että testauksessa on käytetty suhteellisen pientä osaa testidatasta. Luotettavammat tulokset vaatisivat testidatan laajempaa käyttöä. Ajankäytöllisistä syistä on empiiristä testausta on tehty 100:n kuvan otoksella testidatasta.

### Harjoitusdatan määrä

On melko ilmeistä, että harjoitusdatan määrän kasvattaminen pienentää luokitteluvirhettä. Harjoitusdatan määrän vaikutusta luokitteluvirheeseen testattiin silti tarkemmin seuraavilla parametreilla:

- harjoitusdata: x

- testidata: kuvat 0-99

- k: 5

- etäisyysmitta: D22

Tuloksista huomataan, että harjoitusdatan määrän kasvattaminen vaikuttaa merkittävästi luokitteluvirheeseen. Harjoitusdatan määrän kasvattaminen yli 10000:n kuvan ei kuitenkaan enää vaikuta luokitteluvirheeseen sitä pienentävästi ainakaan kyseisillä parametreilla.

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/training_data_size.png)

### Etäisyysmittojen vertailu

Testatut etäisyysmitat on määritelty artikkelissa https://ieeexplore.ieee.org/document/576361. Etäisyysmitalla D23 mod tarkoitetaan artikkelissa määriteltyä etäisyysmittaa D23, mutta osakaavassa d6 ei kerrota skalaarilla 1/N.

Etäisyysmittojen (D22, D23, D23 mod) vertailussa luokitteluvirheen suhteen käytettiin seuraavia parametreja:

- harjoitusdata: kuvat 0-9999

- testidata: kuvat 0-99

- k: 5

Tuloksista huomataan, että parhaimpaan tulokseen päästiin etäisyysmitalla D22, mikä oli olettavaakin etäisyysmittoja käsittelevän artikkelin perusteella.

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/distance_measure.png)

- D22: 4%

- D23: 6%

- D23 mod: 5%

Parhaimpaan tulokseen päästiin siis etäisyysmitalla D22, mikä oli olettavaakin etäisyysmittoja käsittelevän artikkelin https://ieeexplore.ieee.org/document/576361 perusteella.

### k:n arvo

...
