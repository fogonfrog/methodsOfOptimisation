def func(x):
    return x * x + 4 * x + 6

a = int(input("Введите a = "))
b = int(input("Введите b = "))
eps = 0.5
iter = 0

while abs(b-a) > eps:
    iter += 1
    x = (b + a) / 2
    f1 = func(x - eps)
    f2 = func(x + eps)
    print("Итерация: ", iter)
    print("X = ", f1)
    print("F1 = ", f1)
    print("F2 = ", f2)
    if f1 < f2:
        b = x
        print("F1 < F2")
        print("B = X")
    else:
        a = x
        print("F1 >= F2")
        print("A = X")

print("Точка минимума: ", (a + b) / 2)
print("Количество итераций: ", iter)
