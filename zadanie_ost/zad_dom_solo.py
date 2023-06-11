#1
# Funkcja suma_listy(l) zwraca sumę wszystkich elementów w liście l.
# Jeśli lista jest pusta, zwraca 0.
# W przeciwnym przypadku, dodaje pierwszy element listy do sumy reszty listy.

def suma_listy(l):
    if not l:  # Sprawdzenie, czy lista jest pusta
        return 0
    else:
        return l[0] + suma_listy(l[1:])

# Przykład użycia:
lista = [3, 9, 8, 1, 2]
wynik = suma_listy(lista)
print(wynik)  # Wyświetli 23

