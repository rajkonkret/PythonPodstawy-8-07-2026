# funkcja - blok programu, który można uzyc wielokrotnie
# funkcja musi byc najpierw zadeklarowana
# zeby funkcja sie uruchomiła musi zostac wywołąna


a = 6
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # argumenty obowiązkowe
    print(a + b)  # lokalne a, b


def dodaj3(a, b, c=0):  # argumenty z wartością domyślna
    print(a + b + c)


# wywołanie funkcji
dodaj()  # 14

# argumenty po pozycji
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(45, 89)  # 134

dodaj3(45, 78)  # 123
dodaj3(45, 78, 100)  # 223

# argumenty po nazwie
dodaj3(c=100, b=90, a=9)
dodaj3(b=90, a=9)
