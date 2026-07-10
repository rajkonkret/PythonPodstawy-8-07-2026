import random

"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # od 1 do 100

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # 0.9491859510930893 od 0 do 0.99999999
print(random.random() * 9)  # 7.323289348995436 od 0 do 8.99999999

lista = [67, 45, 32, 68, 90, 42, 49]
# ctrl alt l
print(lista[random.randrange(len(lista))])  # 45
