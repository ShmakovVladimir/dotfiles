x = int(input("Введите число x:  "))
y = int(input("Введите число y:  "))
z = int(input("Введите число z:  "))


numerator = ((x**5 + 7) / (6 * y))**(1/3) 
denominator = 7 - z % y
result = round(numerator / denominator, 2)
print("Результат f = ", result)
