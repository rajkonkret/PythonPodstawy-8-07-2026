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
