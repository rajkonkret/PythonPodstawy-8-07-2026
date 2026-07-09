# zbior (set) - przechowuje unikalne wartości
# nie zachowuje kolejnosci
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>
