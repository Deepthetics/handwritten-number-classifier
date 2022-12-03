# Toteutusdokumentti

## Ohjelman rakenne

Ohjelmakoodi on jaettu seuraaviin moduuleihin:

image_processing.py: Sisältää kuvadatan käsittelyyn käytettävät funktiot

image_plotting.py: Sisältää kuvadatan plottaamiseen käytettävät funktiot

distance_measures.py: Sisältää eri etäisyyksien laskemiseen käytettävät funktiot

knn.py: Sisältää k-NN-menetelmään liittyvät funktiot

## Ohjelman toiminta

Yksittäisiä testidatan kuvia pystyy luokittelemaan k-NN-menetelmällä ja luokittelusta on mahdollista plotata seuraavanlaista dataa:
![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/classification.png)

Useampia testidatan kuvia on mahdollista luokitella kerralla valitulla etäisyysfunktiolla. Luokittelusta voidaan laskea luokitteluvirhe ja tulostaa seuraavanlainen yhteenveto
![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/tiralabra_output.png)

## Käyttöliittymä

Ohjelmalla ei ole vielä kunnollista käyttöliittymää vaan sitä täytyy käyttää suorittamalla tiedosto index.py ja muokkaamalla sieltä tehtäviä funktiokutsuja.
