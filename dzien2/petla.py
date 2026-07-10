# pętla - mozliwosc wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(30):
    pass  # nic nie rób

print(i)  # 29

for _ in range(15):
    print("Test podłoga")

# prawidłowa nazwa zmiennej
print(_)  # 14

for i in range(5):
    print(i * 2)
    print(i + 2)
# 8
# 6
print("Wyjscie z pętli")  # Wyjscie z pętli
print()

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for i in range(len(lista3)):
    print(lista3[i])
    # 0
    # 2
    # 4
    # 6
    # 8

for c in lista3:  # podstawi kolejne elemnty z listy
    print(c)
# 0
# 2
# 4
# 6
# 8

for c in lista3:
    if c > 4:
        print(c, "wieksza niz 4")
    elif c == 4:
        print("Rowne 4")
    else:
        print("Mniejsze niz 4")
    print(c)  # za kazdym przejsciem pętli

print("Po zakończeniu pętli")

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # (start, stop, krok)
    print(i)

imiona = ['Sylwia', 'Marek', 'Tomek', 'Anna']

for o in imiona:
    print(o)
# Sylwia
# Marek
# Tomek
# Anna

# 0 Sylwia

print(imiona.index("Sylwia"))  # 0
print(imiona[0])
# 0
# Sylwia

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Sylwia') -> a, b
# (1, 'Marek')
# (2, 'Tomek')
# (3, 'Anna')

for i, o in enumerate(imiona):
    print(i, o)
# 0 Sylwia
# 1 Marek
# 2 Tomek
# 3 Anna

imiona = ['Sylwia', 'Marek', 'Tomek', 'Anna']
