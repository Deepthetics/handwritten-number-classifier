# Testausdokumentti

## Yksikkötestaus
Tällä hetkellä automatisoidut yksikkötestit calculation_utilities-, distance_measures- ja image_processing-moduulien funktioille sekä osalle knn-moduulin funktioista.  Moduulin image_plotting funktioita ei ole tarkoitus testata automaattisesti, koska ne vastaavat erilaisista plottaustoimenpiteistä eivätkä itse suoraan palauta mitään.

## Manuaalinen testaus
Moduulin image_plotting funktioiden toimintaa on testattu manuaalisesti. Kyseisen moduulin funktiota plot_two_images pystyy käyttämään manuaalisen testauksen työkaluna havainnoimaan silmämääräisesti, että kuvadatan muunnoksesta vastaava funktio to_binary toimii odotetulla tavalla. Alkuperäisen greyscale-kuvan ja mustavalkoisen muunnoksen voi plotata vierekkäin:

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/conversion.png)

## Testien haarautumakattavuus

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/coverage_report.png)
