# while - pętlqa sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

print(50 * "-")

licznik = 0
while licznik < 10:
    licznik += 1
    print("komunikat 3 !!")

while True:
    print(f"""
1. Dodawnie
5. Koniec""")
    odp = input("Wybierz opcje menu: ")

    if odp == '5':
        break
