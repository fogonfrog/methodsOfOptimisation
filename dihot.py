def fun(x):
    return x * x * x * x - 8 * x * x + 8 * x + 1

def dihot(a, b, c):
    print("Метод дихотомии")
    eps = 0.00001
    iter = 0
    while abs(b-a) > eps:
        ++iter
        x = (a + b) / 2
        f1 = fun(x - eps)
        f2 = fun(x + eps)
        if c*f1 < c * f2:
            b = x
        else:
            a = x
    x = (b + a) / 2
    return x, fun(x)

a = int(input("Введите a = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))
print(dihot(a, b, c))