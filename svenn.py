def f(x):
    return x * x - 4 * x +6

h = 0.2
x = 0
xpred = x
x1 = x + h
k = 1
print("H = ", h)
print("K = ", k)
print("Xk = ", x)
print("Xk+1 = ", x1)
print("F(Xk) = ",f(x))
print("F(Xk+1) = ",f(x1))
if (f(x) < f(x1)):
    print("f(x) < f(x1)")
    h = -h
    print("H = ", h)
    x1 = x + h
    print("Xk+1 = ", x1)
    print("F(Xk+1) = ",f(x1))

while f(x1)<f(x):
    k += 1
    xpred = x
    x = x1
    h = 2 * h
    x1 = x + h
    print("H = ", h)
    print("K = ", k)
    print("Xk = ", x)
    print("Xk+1 = ", x1)
    print("F(Xk) = ",f(x))
    print("F(Xk+1) = ",f(x1))

print("A = ", xpred)
print("B = ", x1)
