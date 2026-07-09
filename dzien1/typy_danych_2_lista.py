# kolekcja

# lista - przechowuje dowolna ilosc danych, róznego typu na raz
# zachowuje kolejnosc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Zenek")
lista.append("Anna")
lista.append("Karolina")
print(lista)
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Karolina']

print(len(lista))  # długosc 6

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Karolina']
#     0        1        2        3        4         5

print(lista[1])
print(lista[3])
print(lista[5])
# Tomek
# Zenek
# Karolina

# print(lista[10])  # IndexError: list index out of range

# ostatni element
print(lista[5])  # Karolina
print(lista[len(lista) - 1])  # Karolina
print(lista[-1])  # Karolina
print(lista[-2])  # Anna
print(lista[-3])  # Zenek

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Karolina']
#     0        1        2        3        4         5
#     -6       -5       -4       -3      -2        -1

# slicowanie - fragment listy
print(lista[0:3])  # 012, ['Radek', 'Tomek', 'Marek']
print(lista[:3])  # 012, ['Radek', 'Tomek', 'Marek']

print(lista[2:])  # ['Marek', 'Zenek', 'Anna', 'Karolina'], z ostatnim wlącznie
print(lista[2:5])  # ['Marek', 'Zenek', 'Anna'], bez ostatniego

print(lista[2:10])  # ['Marek', 'Zenek', 'Anna', 'Karolina']
print(lista[12:26])  # []

print(lista[:])
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Karolina']

# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Karolina']
#     0        1        2        3        4         5
#     -6       -5       -4       -3      -2        -1

print(lista[-2:0])  # [] [4:0]
print(lista[0:-2])  # [0:4],['Radek', 'Tomek', 'Marek', 'Zenek']

# od 0 do 14
# range()
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(lista_15[::-1])
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(1, 15, 2)))  # [1, 3, 5, 7, 9, 11, 13]

tablice = [[1, 2], [3, 4]]
# numpy - tablice/macierze, pandas

print(lista)  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Anna', 'Karolina']

# podmiana elementu
lista[2] = "Sylwia"
print(lista)  # ['Radek', 'Tomek', 'Sylwia', 'Zenek', 'Anna', 'Karolina']

# dopisanie na konkretnym indexie
lista.insert(1, "Kamil")
print(lista)
# ['Radek', 'Kamil', 'Tomek', 'Sylwia', 'Zenek', 'Anna', 'Karolina']

lista.append("Radek")
print(lista)
# ['Radek', 'Kamil', 'Tomek', 'Sylwia', 'Zenek', 'Anna', 'Karolina', 'Radek']

# usunięcie z listy, pierwszy z lewej
lista.remove("Radek")
print(lista)
# ['Kamil', 'Tomek', 'Sylwia', 'Zenek', 'Anna', 'Karolina', 'Radek']

# usunięcie po indeksie
print(lista.pop(3))  # Zenek
print(lista)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna', 'Karolina', 'Radek']

print(lista.pop(-1))  # Radek

print(lista)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna', 'Karolina']
print(lista.pop())  # Karolina - usunie ostatni

# sprawdzenie indexu elementu
print(lista.index("Sylwia"))  # indeks numer 2

a = 1
b = 3
a = b
print(f"{a=}, {b=}")  # a=3, b=3

b = 9
print(f"{a=}, {b=}")  # a=3, b=9

lista2 = lista  # kopia adresu listy

lista_copy = lista.copy()  # kopia elementów listy

print(lista2)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna']
print(lista)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna']
print(lista_copy)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna']

lista.clear()  # kasuje wszystkie leemnty z listy
print(lista2)  # []
print(lista)  # []
print(lista_copy)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna']

# id() - adres elementu
print(id(lista2))  # 1877624541120
print(id(lista))  # 1877624541120
print(id(lista_copy))  # 1877626698176

liczby = [54, 999, 12.34, 34, 567, 999]
print(liczby)  # [54, 999, 12.34, 34, 567, 999]

liczby.sort()
print(liczby)  # [12.34, 34, 54, 567, 999, 999]

liczby.append("A")  # dodanie elementu na koncu listy
print(liczby)  # [12.34, 34, 54, 567, 999, 999, 'A']

# liczby.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)  # ['Kamil', 'Tomek', 'Sylwia', 'Anna']
lista_copy.sort()
print(lista_copy)  # ['Anna', 'Kamil', 'Sylwia', 'Tomek']

lista_copy.sort(reverse=True)
print(lista_copy)  # ['Tomek', 'Sylwia', 'Kamil', 'Anna']

lista_copy.append("Tomek")
print(lista_copy)  # ['Tomek', 'Sylwia', 'Kamil', 'Anna', 'Tomek']

lista_copy.reverse()  # odwracanie bez sortowania
print(lista_copy)
# ['Tomek', 'Anna', 'Kamil', 'Sylwia', 'Tomek']

print(liczby)  # [12.34, 34, 54, 567, 999, 999, 'A']
print(liczby[0:3])  # [12.34, 34, 54]
liczby[3] = 666
print(liczby[-1])  # A
print(liczby)  # [12.34, 34, 54, 666, 999, 999, 'A']

tekst = "Pyth on."

lista = [tekst]
print(lista)  # ['Pyth on.']

# rozpakowanie sekwencji
lista_tekst = list(tekst)
print(lista_tekst)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

# split()  - rozbijanie tekstu po znaku

krotka = tuple(lista_copy)
print(type(krotka))
print(krotka)  # <class 'tuple'>
# ('Tomek', 'Anna', 'Kamil', 'Sylwia', 'Tomek')
