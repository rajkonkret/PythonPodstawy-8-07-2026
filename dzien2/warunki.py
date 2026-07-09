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


