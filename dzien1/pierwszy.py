# pep8
import sys

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

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4, default_max_str_digits=4300,
# str_digits_check_threshold=640)


# zmienna - pudełko na dane
# snake_case

# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 67
print(name)  # 67
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = "Radek"
print(name)

name = 90
print(name)
# Radek
# 90

# mypy - analiza statyczna
# pip install mypy - instalacja mypy
# cd dzien1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy-8-07-2026\dzien1> mypy pierwszy.py
# pierwszy.py:50: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:55: error: Name "name" already defined on line 46  [no-redef]
# pierwszy.py:58: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonPodstawy-8-07-2026\dzien1>
