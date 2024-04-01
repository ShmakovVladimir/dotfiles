a = int(input("Введите число a:"))
b = int(input("Введите число b:"))

print(f"a + b = {a+b}") #сложение
print(f"a - b = {a - b}") #вычитание
print(f"a * b = {a * b}") #умножение
print(f"a / b = {round(a / b, 2)}") #деление(округление используя round)
print(f"a / b = {a / b:.2f}") #деление(тут синтаксис округления внутри f-строки)
print(f"a // b = {a // b}") #целочисленное деление
print(f"a % b = {a % b}") #остаток от деления
print(f"a**b = {a**b}") #возведение в степень

print(f"a < b: {a < b}")
print(f"a <= b: {a < b}")
print(f"a > b: {a < b}")
print(f"a >= b: {a < b}")
print(f"a != b: {a < b}")
print(f"a == b: {a < b}")

