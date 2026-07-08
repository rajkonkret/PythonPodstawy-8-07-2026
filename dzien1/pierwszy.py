# pep8

print('Hello World')
print()
print()

print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonPodstawy-8-07-2026\dzien1\pierwszy.py", line 10
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
#
# Process finished with exit code 1

print("Dalszy ciąg programu")  # Dalszy ciąg programu
# ctrl alt l - formatowanie

print(type("Radek"))  # sprawdzanie typów, <class 'str'> - typ tekstowych
print("39" + "14")  # 3914 - łaczy teksty (konkatenacja)

print(39)  # 39
print(type(39))  # <class 'int'> liczby całkowite
# print(39 + "14")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# rzutowanie
print(int("39") + int(40))  # 79
print(str(39) + str("14"))  # 3914

print(5 * "4")  # 44444
