def f(x):
    return x * x - 4 * x +6

a = int(input('vvedite a: '))
b = int(input('vvedite b: '))

eps = 0.1
gam = 0.00002
kol = 0

while abs(a-b) >= 2*eps:
    kol += 1
    print("Итерация = ",kol)
    c = (a + b - gam) / 2
    print("C = ",c)
    d = (a + b + gam) / 2
    print("D = ",d)
    if (f(c) <= f(d)):
        print("f(c) <= f(d)")
        b = d
        print("B = ",b)
        print("A = ",a)
    else:
        print("f(c) > f(d)")
        a = c
        print("B = ",b)
        print("A = ",a)
print("Ответ : ",(a + b) / 2)
print("Количество итерация = ",kol)
