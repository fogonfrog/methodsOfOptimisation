def func(x):
    return x * x + 4 * x + 6

def fibbon(n):
    if n <= 1:
        return 1
    return fibbon(n-1) + fibbon(n-2)

a = int(input("Введите a = "))
b = int(input("Введите b = "))

eps = 0.5

x = (b - a) / eps
n = 2

while fibbon(n) < x:
    n += 1

print("N = ", n)

yk = a + (b - a) * (fibbon(n) / fibbon(n + 2))
zk = a + (b - a) * (fibbon(n + 1) / fibbon(n + 2))

fyk = func(yk)
fzk = func(zk)

i = 1
print("Итерация = ", i)
print("Yk = ", yk)
print("Zk = ", zk)
print("F(Yk) = ", fyk)
print("F(Zk) = ", fzk)


while abs(a - b) >= eps:
    i += 1
    if (fyk <=  fzk):
        b = zk
        yz = yk
        fyz = fyk
        yk = a + (b - a) * (fibbon(n + 1 - i) / fibbon(n + 3 - i))
        fyk = func(yk)
        print("F(Yk) <= F(Yz)")
        print("Итерация = ", i)
        print("B = ", b)
        print("Yk = ", yk)
        print("Yz = ", zk)
        print("F(Yk) = ", fyk)
        print("F(Yz) = ", fzk)
    else:
        a = yk
        yk = zk
        fyk = fzk
        yz = a + (b - a) * (fibbon(n + 2 - i) / fibbon(n + 3 - i))
        fyz = func(zk)
        print("F(Yk) > F(Yz)")
        print("Итерация = ", i)
        print("A = ", a)
        print("Yk = ", yk)
        print("Yz = ", zk)
        print("F(Yk) = ", fyk)
        print("F(Yz) = ", fzk)

print("Ответ : ", (a + b) / 2)
print("Количество итераций = ", i)
