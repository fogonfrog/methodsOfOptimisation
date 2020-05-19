def fib(n):
    if n <= 1:
        return 1
    return fib(n-1)+ fib(n-2)

def f(x):
    return x * x - 4 * x +6

a = float(input('vvedite a: '))
b = float(input('vvedite b: '))

eps = 0.5
gam = 0.2
kol = 0

x = (b - a) / eps
n = 2

while fib(n) < x:
    n+=1

print("N = ",n)
c = a + (b - a)*(fib(n) / fib(n + 2))
d = a + (b - a)*(fib(n + 1) / fib(n + 2))
fc = f(c)
fd = f(d)
i = 1
print("Итерация = ", i)
print("C = ", c)
print("D = ", d)
print("F(C) = ", fc)
print("F(D) = ", fd)


while abs(a - b) >= eps:
    i += 1
    if (fc<=fd):
        b = d
        d = c
        fd = fc
        c = a + (b - a)*(fib(n + 1 - i) / fib(n + 3 - i))
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
        d = a + (b - a)*(fib(n + 2 - i) / fib(n + 3 - i))
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
