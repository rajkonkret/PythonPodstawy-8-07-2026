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
