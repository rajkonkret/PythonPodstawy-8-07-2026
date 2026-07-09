# krotka - kolekcja niemutowalna (tylko do odczytu)
# pozwala efektywniej zarządzać pamięcią

tupla_imiona = "Zenek", "Tomek", 'Marek', "Ania"
print(type(tupla_imiona))  # <class 'tuple'>

# tupla_liczby = (43, 45, 22.34, 11, 200)
tupla_liczby = 43, 45, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 45, 22.34, 11, 200)

# tupla jednoelemntową
tupla_jeden = (45,)  # pep8 zaleca nawias
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))  # <class 'tuple'>

# tupla_liczby[0] = 123
# TypeError: 'tuple' object does not support item assignment

# usunięcie całej krotki
del tupla_liczby
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona)
print(tupla_imiona.index("Zenek"))  # indeks 0
print(tupla_imiona.count("Zenek"))  # występuje 1 raz

print(len(tupla_imiona))  # liczba elementów: 4

tup = 1, 2

# a  -  pierwszy
# b = drugi element

a = tup[0]
b = tup[1]

# rozpakowanie krotki
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

# zamiana wartosci zmiennych miejscami
a, b = b, a
print(a, b)  # 2 1

print(tupla_imiona)
# ('Zenek', 'Tomek', 'Marek', 'Ania')

# name1, name2,
# name1, name2, name3 = tupla_imiona
# ValueError: too many values to unpack (expected 3, got 4)

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Zenek Tomek ['Marek', 'Ania']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Zenek ['Tomek', 'Marek'] Ania

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Zenek', 'Tomek'] Marek Ania

# sorted() - sortowwanie
print(sorted(tupla_imiona))  # ['Ania', 'Marek', 'Tomek', 'Zenek']
print(tupla_imiona)  # ('Zenek', 'Tomek', 'Marek', 'Ania') - nie zmienia oryginału

sortowane = sorted(tupla_imiona)
print(sortowane)  # ['Ania', 'Marek', 'Tomek', 'Zenek']

lista = list(tupla_imiona)
print(lista)  # ['Zenek', 'Tomek', 'Marek', 'Ania']
