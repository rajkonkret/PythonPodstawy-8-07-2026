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

print(a, b)
