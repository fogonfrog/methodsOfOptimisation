import math as m

def f(x):
    return x * x - 4 * x +6

a = int(input('vvedite a: '))
b = int(input('vvedite b: '))

eps = 0.5
gam = 0.2
c = (3 - 5 ** (1/2))/2 * (b - a) + a
d = (5 ** (1/2) - 1)/2 * (b - a) + a
fc = f(c)
fd = f(d)
i = 1
print("Итерация = ", i)
print("C = ", c)
print("D = ", d)
print("F(C) = ", fc)
print("F(D) = ", fd)

while abs(a - b)>=eps:
    i +=1
    if fc <= fd:
        b = d
        d = c
        fd = fc
        c = (3 - m.sqrt(5))/2 * (b - a) + a
        fc = f(c)
        print("F(C)<=F(D)")
        print("Итерация = ", i)
        print("B = ",b)
        print("C = ", c)
        print("D = ", d)
        print("F(C) = ", fc)
        print("F(D) = ", fd)
    else:
        a = c
        c = d
        fc = fd
        d = (m.sqrt(5) - 1)/2 * (b - a) + a
        fd = f(d)
        print("F(C)>F(D)")
        print("Итерация = ", i)
        print("A = ",a)
        print("C = ", c)
        print("D = ", d)
        print("F(C) = ", fc)
        print("F(D) = ", fd)
print("Ответ : ",(a + b) / 2)
print("Количество итераций = ",i)
