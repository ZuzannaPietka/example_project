# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello, student))


# zadanie 1.2

print('Wpisz swoje imie')
imie = input()
print(type(imie))
print("Hello"+' '+imie)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci).__str__()
print("Liczba studentow wynosi: " + liczba_studentow)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]


for i in studenci:
    print("hello "+i)

# zadanie 1.5

liczba = 3
potega = 4

wynik = 3**4

# oczekiwany rezultat:
# Wynik wynosi: 81
print("Wynik wynosi: "+wynik.__str__())