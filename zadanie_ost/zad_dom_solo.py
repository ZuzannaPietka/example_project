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

#2
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

#3
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

#4
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

#5
# rozwiązanie sudoku 4x4
def print_board(board):
    for i in range(4):
        if i % 2 == 0 and i != 0:
            print("- - - - - - - - -")
        for j in range(4):
            if j % 2 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, row, col):
    # Sprawdź wiersz
    for i in range(4):
        if board[row][i] == num:
            return False

    # Sprawdź kolumnę
    for i in range(4):
        if board[i][col] == num:
            return False

    # Sprawdź podkwadrat 2x2
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 5):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


# Przykładowa plansza Sudoku 4x4 (0 oznacza puste pole)
board = [
    [0, 2, 0, 0],
    [0, 0, 3, 0],
    [7, 0, 0, 0],
    [0, 0, 0, 0]
]

print("Przed rozwiązaniem:")
print_board(board)
print("\nPo rozwiązaniu:")
if solve_sudoku(board):
    print_board(board)
else:
    print("Nie znaleziono rozwiązania.")










