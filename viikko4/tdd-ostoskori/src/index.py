from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

def main():
    kori = Ostoskori()
    maito = Tuote("Maito", 3)
    jogurtti = Tuote("Jogurtti", 1)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(jogurtti)
    print("Kori: " + kori.oliot[0].tuotteen_nimi() + "  ")
    print("LKM: " + str(kori.oliot[0].lukumaara()))
    print("Kori: " + kori.oliot[1].tuotteen_nimi())
    print("LKM: " + str(kori.oliot[1].lukumaara()))

if __name__ == "__main__":
    main()
