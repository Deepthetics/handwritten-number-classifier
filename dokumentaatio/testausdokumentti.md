# Testausdokumentti

## Yksikkötestaus
Toistaiseksi automatisoidut yksikkötestit vasta image_processing.py -tiedoston funktioille. Tiedoston distance_measures.py funktioille kirjoitetaan testit heti kun itse funktiot saadaan toimimaan oikein. Tällä hetkellä ne toimivat tiedostetusti hieman väärin. Tiedoston image_plotting.py funktioita ei ole tarkoitus testata automaattisesti, koska ne vastaavat erilaisista plottaustoimenpiteistä eivätkä itse suoraan palauta mitään.

## Manuaalinen testaus
Tiedoston image_plotting.py funktiota plot_image_data pystyy käyttämään manuaalisen testauksen työkaluna havainnoimaan silmämääräisesti, että kuvadatan muunnoksesta vastaava funktio to_binary toimii odotetulla tavalla. Alkuperäisen greyscale-kuvan ja mustavalkoisen muunnoksen voi plotata vierekkäin:

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/conversion.png)

## Testien haarautumakattavuus

![](https://github.com/Deepthetics/tiralabra/blob/main/dokumentaatio/kuvat/tiralabra_coverage_report.png)
