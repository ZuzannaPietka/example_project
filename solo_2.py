class Mieszkanie:
    def __init__(self, miasto, ulica, numer, metraz, pokoje, cena):
        self.miasto = miasto
        self.ulica = ulica
        self.numer = numer
        self.metraz = metraz
        self.pokoje = pokoje
        self.cena = cena

    def __str__(self):
        return f"Mieszkanie znajduje się w {self.miasto}, na ulicy {self.ulica} {self.numer}. " \
               f"Ma powierzchnię {self.metraz} m², {self.pokoje} pokoje. " \
               f"Cena wynosi {self.cena} zł."

    def oblicz_cene_na_metr(self):
        cena_na_metr = self.cena / self.metraz
        return cena_na_metr

    def czy_drogie(self):
        if self.cena > 1000000:
            return "Drogie"
        else:
            return "Taniutkie"



mieszkanie_1 = Mieszkanie("Poznan", "Towarowa", "10", 80, 3, 250000)
print(mieszkanie_1)
print(mieszkanie_1.oblicz_cene_na_metr())
print(mieszkanie_1.czy_drogie())




