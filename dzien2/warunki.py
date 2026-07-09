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

odp = "Radek"

if odp:
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":
    print("Jestem Radek")  # Jestem Radek
