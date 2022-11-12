# Viikkoraportti 2

Tällä viikolla on tehty:
- perehdytty MNIST-datasettiin, käytettäviin etäisyysmittoihin ja niiden laskukaavoihin, k:n lähimmän naapurin menetelmään sekä projektissa käytettävien kirjastojen dokumentaatioihin
- alustettu projektin riippuvuuksien hallinta, testikattavuuden kerääminen ja ohjelmakoodin laadun staattinen analyysi
- aloitettu yksikkötestaaminen ja konfiguroitu testaamista, jotta ulkoisten kirjastojen tietorakenteita olisi mahdollista testata (vielä vaiheessa)

Ohjelma on edistynyt:
- luotu toiminnallisuudet datan tiedostoista lukemiseen, sen jatkokäsittelyyn ja kuvadatan muuntamiseen harmaasävykuvista mustavalkoisiksi kuviksi

Opittu:
- etäisyysmitoista
- k:n lähimmän naapurin menetelmästä
- eri tavoista muuntaa harmaasävykuvia mustavalkoisiksi

Epäselvyydet ja vaikeudet:

Harjoitusdatassa on 60000 kuvaa ja näiden muuntaminen mustavalkoisiksi kesti todella kauan, koska laskin, että yksittäisiä arvoja on läpi käytävänä yli 47 miljoonaa. Oletan, että k:n lähimmän naapurin menetelmää käytettäessä ja etäisyyksiä laskettaessa ei ole mahdollista käyttää näin suurta määrää harjoitusdataa, jos halutaan luokitella useampia testidatan kuvia nopeasti. Eli hieman epäselvyyttä sen suhteen, kuinka suurta osaa harjoitusdatasta voisi ja olisi tarkoituksenmukaista käyttää? Testien konfigurointi tuotti myös hieman vaikeuksia, mutta luulen selviäväni niistä.

Seuraavaksi:
- ensi viikolla on tarkoitus toteuttaa vähintään käytettävien etäisyyksien laskeminen mustavalkoisten kuvien välillä sekä saada konfiguroitu testaus, jotta tarvittavien testien luominen on mahdollista
- tämän jälkeen on tarkotus toteuttaa k:n lähimmän naapurin menetelmään perustuva luokittelu sekä testata tätä testidataan
