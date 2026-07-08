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
