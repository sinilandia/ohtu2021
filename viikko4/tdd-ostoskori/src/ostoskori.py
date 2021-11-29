from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.oliot = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        lkm = 0
        i = 0
        while i < len(self.oliot):
            lkm += self.oliot[i].lukumaara()
            i += 1
        return lkm

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        summa = 0
        i = 0
        while i < len(self.oliot):
            summa += self.oliot[i].hinta()
            i+=1
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen ostoksena koriin
        i = 0
        while i < len(self.oliot):
            if self.oliot[i].tuotteen_nimi() == lisattava.nimi():
                self.oliot[i].muuta_lukumaaraa(1)
                return           
            i += 1
        ostos = Ostos(lisattava)
        self.oliot.append(ostos)    

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        i = 0
        while i < len(self.oliot):
            if self.oliot[i].tuotteen_nimi() == poistettava.nimi():
                self.oliot[i].muuta_lukumaaraa(-1)
                return
            i += 1

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.oliot