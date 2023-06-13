from datetime import date

class Mieszkanie:
    def __init__(self, miasto, ulica, numer, metraz, pokoje, cena, rok_budowy, pietro):
        self.miasto = miasto
        self.ulica = ulica
        self.numer = numer
        self.metraz = metraz
        self.pokoje = pokoje
        self.cena = cena
        self.rok_budowy = rok_budowy
        self.pietro = pietro

    def __str__(self):
        return f"Mieszkanie znajduje się w {self.miasto}, na ulicy {self.ulica} {self.numer}. " \
               f"Ma powierzchnię {self.metraz} m², {self.pokoje} pokoje. " \
               f"Cena wynosi {self.cena} zł. " \
               f"Zostało zbudowane w roku {self.rok_budowy}, znajduje się na {self.pietro} piętrze."

    def oblicz_cene_na_metr(self):
        cena_na_metr = self.cena / self.metraz
        return cena_na_metr

    def czy_drogie(self):
        if self.oblicz_cene_na_metr() > 15000:
            return "To mieszkanie jest za drogie."
        else:
            return "To mieszkanie jest tanie."

    def przelicz_cene_za_mkw(self):
        cena_za_mkw = self.cena / self.metraz
        return cena_za_mkw

    def zmien_cene(self, nowa_cena):
        self.cena = nowa_cena

    def pokaz_lokalizacje(self):
        return f"Lokalizacja mieszkania: {self.miasto}, {self.ulica} {self.numer}"

    def oblicz_wiek_mieszkania(self):
        dzisiejsza_data = date.today()
        wiek = dzisiejsza_data.year - self.rok_budowy
        return wiek


mieszkanie_1 = Mieszkanie("Poznan", "Towarowa", "10", 80, 3, 250000, 2005, 2)
print(mieszkanie_1)
print(mieszkanie_1.oblicz_cene_na_metr())
print(mieszkanie_1.czy_drogie())
print("Cena za metr kwadratowy wynosi " + str(mieszkanie_1.oblicz_cene_na_metr()) + " zł.")
print(mieszkanie_1.pokaz_lokalizacje())
print("Mieszkanie ma " + str(mieszkanie_1.oblicz_wiek_mieszkania()) + " lat(a).")
