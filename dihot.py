def func(x):
    return x * x + 4 * x + 6

a = int(input("Введите a = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))

print("Метод дихотомии")
eps = 0.1
iter = 0

while abs(b-a) >= eps:
    iter += 1
    print("Итерация = ", iter)
    x = (a + b) / 2
    f1 = func(x - eps)
    f2 = func(x + eps)
    if c * f1 < c * f2:
        b = x
    else:
        a = x
x = (b + a) / 2


print(x, func(x))