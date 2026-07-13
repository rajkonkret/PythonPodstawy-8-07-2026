
from itertools import zip_longest




imiona = ["Radek", "Tomek", "Agata", "Marek", "Anna"]
wiek = [44, 56, 23, 34]

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x000002C2C685B380> iterator

# for item in zipped:
#     print(item)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 34)
# ('Anna', None)

print(40 * "-")

# tylko raz możemy odczytać dane z iteratora
# for o, w in zipped:
#     print(o, w)
# ----------------------------------------
# Radek 44
# Tomek 56
# Agata 23
# Marek 34
# Anna None

lista_zipped = list(zipped)
print(lista_zipped)
for o, w in lista_zipped:
    print(o, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 34
# Anna None
