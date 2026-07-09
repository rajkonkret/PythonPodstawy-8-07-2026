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

# operacje na zbiorach
zbior_2 = {667, 11, 14, 44, 12.34, 18, 52, 667, 62, 99}

# suma zbiorów - tworzy nowy zbió
print(zbior | zbior_2)  # {99, 777, 11, 44, 12.34, 14, 18, 52, 22, 25, 667, 62}
print(zbior.union(zbior_2))  # {99, 777, 11, 44, 12.34, 14, 18, 52, 22, 25, 667, 62}

# część wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {777, 22, 25}
print(zbior.difference(zbior_2))  # {777, 22, 25}
print(zbior_2.difference(zbior))  # {99, 12.34, 14, 52, 667, 62}
