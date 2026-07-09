# instrukcja warunkowa
# instrukcje sterowanie przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu

odp = True

if odp: print("Test")  # Test

if odp:
    # blok programu wykonany gdy warunek True
    print("Test")  # Test

# debugger - pozwala wykonac krok po kroku
# pułapki - miejsce gdzie program się zatrzyma

odp = False

if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"  # True

if odp:
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":
    print("Jestem Radek")  # Jestem Radek

odp = 0
print(bool(0))  # False odp = False

if odp:  # False
    print("Działa")
else:  # wartosc domyslna,
    print("Zero -> False")  # Zero -> False

a = "Radek"
# jezeli długosc tekstu jest wieksza niz 3 wypisac:
# "Dlugośc wynosi: ..., więcej niż 3"

if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, więcej niż 3")
# Długość wynosi: 5, więcej niż 3

n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")
# Długość wynosi: 5, więcej niż 3

# operator morsa, walrus operator
# n = len(a)
# if n > 3:
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")
    # Długość wynosi: 5, więcej niż 3

# pobrac zarobki
# jesli zarobki mniejsze niz 10000 -> podatek 0
# dla pozostałych podaek 90% (0.9)
# wypisac obliczony podatek

# zarobki = int(input("Podaj zrobki: "))
# # 1_000_000
# podatek = 0
# # pierwszy spełbniony -> koniec sprawdzania
# # kolejnosc ma znaczenie
# if zarobki < 10_000:
#     podatek = 0
# # elif zarobki >= 10_000 and zarobki < 40_000:
# # elif 10_000 <= zarobki < 40_000:
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# Podaj zrobki: 15000
# Podatek wynosi: 6000.0 pln.
# podatek 0.2 dla dochodu od 10000 do 39999
# Podaj zrobki: 78000
# Podatek wynosi: 31200.0 pln.

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# napisac zadanie test z...
# trzy patania
# punktacja
# strip(), casefold()

# odp = input("Podaj stolicę Polski")
# punkty = 0
#
# if odp.strip().casefold() == 'Warszawa'.strip().casefold():
#     print("Odpowiedź prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Idż się naucz!")
#
# print("Punkty:", punkty)
# # Podaj stolicę PolskiWarszawa
# # Odpowiedź prawidłowa
# # Punkty: 1
#
# # spam += 1    spam = spam + 1
# # spam -= 1    spam = spam - 1
# # spam *= 1    spam = spam * 1
# # spam /= 1    spam = spam / 1
# # spam %= 1    spam = spam % 1
#
# odp = input("Podaj powierzchnię  Polski w tys km2")  # str
#
# if odp.strip().casefold() == '312'.strip().casefold():
#     print("Odpowiedź prawidłowa")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Idż się naucz!")
#
# print("Punkty:", punkty)
# Podaj powierzchnię  Polski w tys km2312
# Odpowiedź prawidłowa
# Punkty: 2

login = input("Podaj login:")

account_active = True

if login == "uczen":
    password = input("Podaj hasło:")
    if password == "1234":
        if account_active:
            print("Zalogowano poprawnie")
        else:
            print("Konto nieaktywne!")
    else:
        print("Błędna hasło!!!")
else:
    print("Nie ma takiego użytkownika")
# Podaj login:uczen
# Podaj hasło:1234
# Zalogowano poprawnie
