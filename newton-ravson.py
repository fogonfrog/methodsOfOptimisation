import math as m
import copy

eps1 = 1e-3

delta = 1e-5

def f(x):
    return(x[0] * x[0] + 5 * x[1] * x[1] + x[1] * x[0] + x[0])

def g(t, x, y):
    result = [x[0] - t * y[0], x[1] - t * y[1]]
    return result

def norma(x):
    return(m.sqrt(x[0] * x[0] + x[1] * x[1]))

def newton(x0, a, b):
    gr = [(f([x0[0] + delta, x0[1]]) - f([x0[0] - delta, x0[1]])) / (2 * delta),
    (f([x0[0], x0[1] + delta]) - f([x0[0], x0[1] - delta])) / (2 * delta)]
    print("grad = ", gr)
    hesse = [[0,0],[0,0]]
    br = [[0,0],[0,0]]
    hesse[0][0] = (f([x0[0] + delta, x0[1]]) - 2 * f(x0) + f([x0[0] - delta, x0[1]])) / (delta * delta)
    hesse[0][1] = (f([x0[0] + delta, x0[1] + delta]) - f([x0[0], x0[1] + delta]) - f([x0[0] + delta, x0[1]]) + f(x0)) / (delta * delta)
    hesse[1][0] = (f(x0) - f([x0[0],x0[1] - delta]) - f([x0[0] - delta, x0[1]]) + f([x0[0] - delta, x0[1] - delta])) / (delta * delta)
    hesse[1][1] = (f([x0[0], x0[1] + delta]) - 2 * f(x0) + f([x0[0], x0[1] - delta])) / (delta * delta)
    opr = (hesse[0][0] * hesse[1][1]) - (hesse[0][1] * hesse[1][0])
    print("Matr: ")
    print(hesse[0])
    print(hesse[1])
    print("Det = ", opr)
    if opr == 0:
        print("opr = 0")
        return [0, 0]
    else:
        br[0][0] = hesse[1][1] / opr
        br[0][1] = -hesse[1][0] / opr
        br[1][0] = -hesse[0][1] / opr
        br[1][1] = hesse[0][0] / opr
    print("Matr obr: ")
    print(br[0])
    print(br[1])
    s = [0,0]
    for i in range(2):
        for j in range(2):
            s[i] += br[i][j] * gr[j]
    print("S = ", s)
    t = [b - (2 * (b - a)) / (1 + m.sqrt(5)), a + (2 * (b - a)) / (1 + m.sqrt(5))]
    while abs(b - a) > 2 * eps1:
        f1 = f(g(t[0], x0, gr))
        f2 = f(g(t[1], x0, gr))
        if f1>=f2:
            a = t[0]
            t[0] = t[1]
            t[1] = a + (2 * (b - a)) / (1 + m.sqrt(5))
        else:
            b = t[1]
            t[1] = t[0]
            t[0] = b - (2 * (b - a)) / (1 + m.sqrt(5))
    l = (t[1] + t[0]) / 2
    print("L найденная методом золотого сейчения = ",l)
    for i in range(2):
        x0[i] -= l * s[i]
    n = norma(gr)
    gr = [i / n for i in gr]
    return x0, gr

a = -1
b = 1
x0 = [1,1]
x = copy.deepcopy(x0)
k = 0
print("Итерация = ",k)
x0, gr = newton(x0, a, b)
print("X = ",x0)
print("F(X)", f(x0))
srav = [0,0]
for i in range(2):
    srav[i] = abs(x[i]-x0[i])
while (abs(gr[0]) > eps1 and abs(gr[1])>eps1 and srav[0]>eps1 and srav[1]>eps1):
    k+=1
    print("Итерация = ",k)
    x = copy.deepcopy(x0)
    x0, gr = newton(x0, a, b)
    print("X = ",x0)
    print("F(X)", f(x0))
    for i in range(2):
        srav[i] = abs(x[i]-x0[i])
