import math as m

def func(x):
    return x * x + 4 * x + 6

a = int(input("Введите a = "))
b = int(input("Введите b = "))

eps = 0.5
l = 0.2
k = 0

y0 = a + 0.38196 * (b - a)
z0 = a + b - y0

fyk = func(y0)
fzk = func(z0)
i = 1

print("Итерация = ", i)
print("Y0 = ", y0)
print("Z0 = ", z0)
print("F(Yk) = ", fyk)
print("F(Zk) = ", fzk)

while abs(a - b) >= eps:
    i += 1
    if fyk <= fzk:
        b = z0
        z0 = y0
        fzk = fyk
        y0 = a + 0.38196 * (b - a)
        fyk = func(y0)
        print("F(Yk) <= F(Zk)")
        print("Итерация = ", i)
        print("B = ", b)
        print("Y0 = ", y0)
        print("Z0 = ", z0)
        print("F(Yk) = ", fyk)
        print("F(Zk) = ", fzk)
    else:
        a = y0
        y0 = z0
        fyk = fzk
        d = 0.38196 * (b - a) + a
        fzk = func(z0)
        print("F(Yk) > F(Zk)")
        print("Итерация = ", i)
        print("A = ", a)
        print("Y0 = ", y0)
        print("Z0 = ", z0)
        print("F(Yk) = ", fyk)
        print("F(Zk) = ", fzk)

print("Ответ : ", (a + b) / 2)
print("Количество итераций = ", i)
