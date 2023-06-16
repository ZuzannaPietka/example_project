import csv

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def oblicz_wynagrodzenie_netto(self):

        wynagrodzenie_netto = 0.73 * self.wynagrodzenie_brutto
        return wynagrodzenie_netto

    def oblicz_koszt_pracodawcy(self):

        koszt_pracodawcy = self.wynagrodzenie_brutto + 0.248 * self.wynagrodzenie_brutto
        return koszt_pracodawcy


def odczytaj_pracownikow_z_pliku(nazwa_pliku):
    lista_pracownikow = []
    with open(nazwa_pliku, 'r') as plik:
        czytnik_csv = csv.DictReader(plik)
        for wiersz in czytnik_csv:
            imie = wiersz['imie']
            nazwisko = wiersz['nazwisko']
            wynagrodzenie_brutto = float(wiersz['wynagrodzenie_brutto'])
            pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
            lista_pracownikow.append(pracownik)
    return lista_pracownikow


def oblicz_wynagrodzenia_netto(lista_pracownikow):
    wynagrodzenia_netto = []
    for pracownik in lista_pracownikow:
        netto = pracownik.oblicz_wynagrodzenie_netto()
        wynagrodzenia_netto.append((pracownik.imie, pracownik.nazwisko, netto))
    return wynagrodzenia_netto


pracownicy = odczytaj_pracownikow_z_pliku('pracownicy.csv')
wynagrodzenia_netto = oblicz_wynagrodzenia_netto(pracownicy)

for imie, nazwisko, netto in wynagrodzenia_netto:
    print(f"Pracownik: {imie} {nazwisko}, wynagrodzenie netto: {netto} zł")

def oblicz_calkowity_koszt(lista_pracownikow):
    koszt_pracodawcy = 0
    for pracownik in lista_pracownikow:
        koszt_pracodawcy += pracownik.oblicz_koszt_pracodawcy()
    return koszt_pracodawcy


pracownicy = odczytaj_pracownikow_z_pliku('pracownicy.csv')
koszt = oblicz_calkowity_koszt(pracownicy)

print(f"Calkowity koszt pracodawcy: {koszt} zł")
