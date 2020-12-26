a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
c = int(input("Введите чиcло 3: "))
r1 = a and b and c and "Heт нулевых значений"
print(r1)
r2 = a or b or c or "Введены все нули!"
print(r2)
if a > (b + c):
    print(a - b - c)
else:
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print("Вася")
if a > 5 or (b == 7 and c == 7):
    print("Петя")