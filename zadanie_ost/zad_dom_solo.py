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

# Funkcja znajdz_najwiekszy_element_listy(l) zwraca największy element w liście l.
# Jeśli lista jest pusta, zwraca None.
# W przeciwnym przypadku, rekurencyjnie znajduje największy element reszty listy i porównuje go z pierwszym elementem.

def znajdz_najwiekszy_element_listy(l):
    if not l:  # Sprawdzenie, czy lista jest pusta
        return None
    elif len(l) == 1:  # Warunek zakończenia rekurencji, gdy lista zawiera tylko jeden element
        return l[0]
    else:
        max_reszty = znajdz_najwiekszy_element_listy(l[1:])  # Rekurencyjne znalezienie największego elementu reszty listy
        if l[0] > max_reszty:
            return l[0]
        else:
            return max_reszty

# Przykład użycia:
lista = [3, 7, 2, 9, 4]
wynik = znajdz_najwiekszy_element_listy(lista)
print(wynik)  # Wyświetli 9

# Funkcja silnia(n) zwraca silnię liczby n.
# Dla n = 0 lub n = 1, zwraca 1.
# W przeciwnym przypadku, rekurencyjnie oblicza silnię poprzez mnożenie n przez silnię (n-1).

def silnia(n):
    if n == 0 or n == 1:  # Warunek zakończenia rekurencji dla n = 0 lub n = 1
        return 1
    else:
        return n * silnia(n - 1)

# Przykład użycia:
liczba = 5
wynik = silnia(liczba)
print(wynik)  # Wyświetli 120

# Funkcja fib(n) zwraca n-ty element ciągu Fibonacciego.
# Dla n = 0, zwraca 0.
# Dla n = 1 lub n = 2, zwraca 1.
# W przeciwnym przypadku, rekurencyjnie oblicza n-ty element poprzez sumowanie dwóch poprzednich elementów.

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Przykład użycia:
liczba = 6
wynik = fib(liczba)
print(wynik)  # Wyświetli 8