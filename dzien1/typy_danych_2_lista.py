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
