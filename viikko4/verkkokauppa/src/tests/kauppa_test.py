import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self._pankki_mock = Mock()
        self._viitegeneraattori_mock = Mock()
        self._varasto_mock = Mock()
        # alustetaan kauppa
        self._kauppa = Kauppa(self._varasto_mock, self._pankki_mock, self._viitegeneraattori_mock)

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return  5
            if  tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "jogurtti", 1)

        # otetaan toteutukset käyttöön
        self._varasto_mock.saldo.side_effect = varasto_saldo
        self._varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.return_value = 42
        
        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kutsutaan_tilisiirto_oikeilla_argumenteilla(self):
        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self._kauppa._kaupan_tili, 5)

    def test_kaksi_eri_tuotetta_ja_oikein_tilisiirto(self):
        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.return_value = 42

        self._kauppa.aloita_asiointi()

        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(2)

        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self._kauppa._kaupan_tili, 6)

    def test_kaksi_samaa_tuotetta_ja_tilisiirto_oikein(self):
        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.return_value = 42
        
        self._kauppa.aloita_asiointi()

        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(1)

        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self._kauppa._kaupan_tili, 10)

    def test_yksi_tuote_varastossa_toinen_tuote_loppu_ja_tilisiirto_oikein(self):
        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.return_value = 42
        
        self._kauppa.aloita_asiointi()

        self._kauppa.lisaa_koriin(1)
        self._kauppa.lisaa_koriin(3)

        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self._kauppa._kaupan_tili, 5)

    def test_aloita_asiointi_nollaa_edelliset_ostokset(self):
        # palautetaan aina arvo 42
        self._viitegeneraattori_mock.uusi.return_value = 42
        
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.aloita_asiointi()
        self._kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", self._kauppa._kaupan_tili, 0)

    def test_uusi_viite_jokaiselle_maksutapahtumalle(self):
        # määritellään että metodi palauttaa ensimmäisellä kutsulla 1, toisella 2 ja kolmannella 3
        self._viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # ensimmäinen viite
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", self._kauppa._kaupan_tili, 5)
    
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # toinen viite
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 2, "12345", self._kauppa._kaupan_tili, 5)
    
        self._kauppa.aloita_asiointi()
        self._kauppa.lisaa_koriin(1)
        self._kauppa.tilimaksu("pekka", "12345")

        # kolmas viite
        self._pankki_mock.tilisiirto.assert_called_with("pekka", 3, "12345", self._kauppa._kaupan_tili, 5)
    

