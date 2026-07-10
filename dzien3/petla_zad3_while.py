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

my_list = [1, 5, 2, 5, 90, 3, 5, 6, 7, 91]

# usunięcie wszystkich 5
while 5 in my_list:
    my_list.remove(5)

print(my_list)  # [1, 2, 90, 3, 6, 7, 91] nie zmieniło kolejnosci

my_list = [1, 5, 2, 5, 90, 3, 5, 6, 7, 91]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 90: None, 3: None, 6: None, 7: None, 91: None}
print(list(dict.fromkeys(my_list)))
# [1, 5, 2, 90, 3, 6, 7, 91] nowa lista, brak duplikatów
