# zbior (set) - przechowuje unikalne wartości
# nie zachowuje kolejnosci
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)  # rzutowanie na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()  # tylko słowko set
print(zb2)  # set()

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(25)
zbior.add(33)

print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 25}

# usunięcie eleemntu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 25}

# pop() - usunie pierwszy element
print(zbior.pop())  # 33

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print("Zmmienna:", zmienna)  # Zmmienna: 66
