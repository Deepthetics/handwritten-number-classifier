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


