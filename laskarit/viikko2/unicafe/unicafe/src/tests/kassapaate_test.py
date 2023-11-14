import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_lahtotiedot_oikein_alustuksessa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_myytyjen_lounaiden_lukumaara_oikein_alustuksessa(self):
        self.assertEqual(self.kassapaate.myytyja_lounaita(), 0)

    def test_edullisen_lounaan_osto_kateisella_lisaa_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_maukkaan_lounaan_osto_kateisella_lisaa_saldoa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_edullisen_lounaan_osto_kateisella_lisaa_myytyja_lounaita(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.myytyja_lounaita(), 1)

    def test_maukkaan_lounaan_osto_kateisella_lisaa_myytyja_lounaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.myytyja_lounaita(), 1)

    def test_jos_raha_ei_riita_edulliseen_myyntimaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.myytyja_lounaita(), 0)

    def test_jos_raha_ei_riita_maukkaaseen_myyntimaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.myytyja_lounaita(), 0)

    def test_jos_raha_ei_riita_edulliseen_kassan_saldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_kassassa_oleva_rahamaara_ei_muutu_jos_osto_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_korttimaksu_onnistuu_(self):
        if self.maksukortti.saldo >= 400:
            self.maksukortti.ota_rahaa(400)
            return True
        else:
            return False
