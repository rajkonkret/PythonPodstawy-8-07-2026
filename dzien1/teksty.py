tekst = "Witaj Świecie"

print(type(tekst))  # <class 'str'>
print(tekst)  # Witaj Świecie

# teksty są niemutowalne
# Return a copy of the string converted to uppercase.
tekst.upper()
print(tekst)  # Witaj Świecie

print(tekst.upper())  # WITAJ ŚWIECIE

tekst_upper = tekst.upper()
print(tekst)  # Witaj Świecie
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

# title()

# Witaj Świecie
# 0123456789....

print(tekst[1])  # i
print(tekst[3])  # a
print(tekst[6])  # Ś

print(tekst.index("Ś"))  # indeks numer 6
print(tekst.index("e"))  # index 9, pierwszy z lewej

print(tekst.count("w"))  # występuje 1 raz
print(tekst.lower().count("w"))  # występuje 2 razy

print(tekst.count("j", 0, 4))  # 0 razy, z prawej strony zbiór otwarty, 0123

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usuwanie bialych znaków , wiodocąch, konczących spacji itp
print(tekst.removesuffix("Świecie").strip())  # "Witaj"
# uzycie slice
print(tekst[3:].removesuffix("Świecie").strip())  # "aj"

encode_s = tekst.encode('utf-8')
print(encode_s)
print(type(encode_s))
# b'Witaj \xc5\x9awiecie'
# <class 'bytes'> typ bajtowy
#  \xc5\x9a literka Ś w kodzie unicode
# \x - dane w sytemie szesnastkowym
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"

print(len(imie))  # długosc danych, 5

# Mam na imię ...
print("Mam na imię" + imie)  # Mam na imięRadek
print("Mam na imię", imie)  # Mam na imię Radek

# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.
print("Mam na imię", imie, sep="ooo")  # Mam na imięoooRadek

# f-string, wstrzykiwanie zmiennej do tekstu
tekst_format = f'Mam na imię {imie}.'
print(tekst_format)  # Mam na imię Radek.

tekst_format = f'\tMam na imię {imie}.\n i lubię pythona.\b'
print(tekst_format)
# \t - tab
# \n - nowa linia
# \b - backspace
# "	  Mam na imię Radek.
#  i lubię pythona"
print(f"Radek \\n")  # Radek \n
print(f'Radek \' \'')  # Radek ' '

starszy = "Witaj %s"  # %s - string
print(starszy % imie)  # Witaj Radek

print("Witaj {}!".format("Radek"))  # Witaj Radek!
print(f"Witaj {"Radek"}!")  # Witaj Radek!

print("""
    Witaj
Radek""")
# "    Witaj
# Radek"
