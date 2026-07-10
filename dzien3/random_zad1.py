import random
from random import randrange

"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # od 1 do 100

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.9491859510930893 od 0 do 0.99999999
print(random.random() * 9)  # 7.323289348995436 od 0 do 8.99999999

lista = [67, 45, 32, 68, 90, 42, 49]
# ctrl alt l
print(lista[random.randrange(len(lista))])  # 45

print(random.choice(lista))  # losuje element z kolekcji, 90

lista_kul = list(range(1, 50))  # od 1 do 49

for _ in range(6):  # od 0 do 5
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    print(kula)
# 26
# 35
# 4
# 38
# 29
# 6

print(random.choices(lista_kul, k=6))  # [34, 17, 20, 2, 30, 2] z powtórzeniami

print(random.sample(lista_kul, k=6))  # [30, 11, 24, 5, 4, 31], bez powtórzen
print(sorted(random.sample(lista_kul, k=6)))  # [4, 13, 27, 33, 41, 46]
#
