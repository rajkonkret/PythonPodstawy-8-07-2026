# funkcja - blok programu, który można uzyc wielokrotnie
# funkcja musi byc najpierw zadeklarowana
# zeby funkcja sie uruchomiła musi zostac wywołąna


a = 6
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # argumenty obowiązkowe
    print(a + b)  # lokalne a, b


def dodaj3(a, b, c=0):  # argumenty z wartością domyślna
    print(a + b + c)


# wywołanie funkcji
dodaj()  # 14

# argumenty po pozycji
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(45, 89)  # 134

dodaj3(45, 78)  # 123
dodaj3(45, 78, 100)  # 223

# argumenty po nazwie
dodaj3(c=100, b=90, a=9)
dodaj3(b=90, a=9)

# mieszane
dodaj3(1, b=34, c=89)
dodaj3(1, 34, c=89)

# dodaj3(a=90, 3, 4)  # SyntaxError: positional argument follows keyword argument

print(50 * "-")
wyn = dodaj3(1, 2, 3)
print(wyn)  # None


# funkcje zwracające wynik
def odejmij(a=0, b=0, c=0):
    return a - b - c  # zwraca wynik


print(odejmij(4, 5, 6))  # -7
wyn = odejmij(5, 90)
print(wyn)  # -85

# funkcje lambda
# skrócony zapis funkcje
# zwraca wynik

odejmi4 = lambda a, b, c=0: a - b - c
wyn = odejmi4(4, 9)
print(wyn)  # -5

# mapowanie danych
lista = [6, 9, 10]

l1 = []
for i in lista:
    l1.append(i * 1.1)
print(l1)  # [6.6000000000000005, 9.9, 11.0]

print([i * 1.1 for i in lista])  # [6.6000000000000005, 9.9, 11.0]

# map(), filter(), reduce()
#  funkcje wyzszego rzedu - wymagaja funkcji jako argumentu
# lambda jako funkcja anonimowa
print(f"Użycie map(): {list(map(lambda x: x * 1.1, lista))}")
# Użycie map(): [6.6000000000000005, 9.9, 11.0]
print(f"Użycie map(): {list(map(lambda x: x * 1.25, lista))}")
# Użycie map(): [7.5, 11.25, 12.5]

print(f"Użycie filter(): {list(filter(lambda x: x > 5, lista))}")
# Użycie filter(): [6, 9, 10]
