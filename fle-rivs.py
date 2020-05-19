import math as m
import copy

eps1 = 1e-8
delta = 1e-8

def f(x):
    return(x[0] * x[0] + 5 * x[1] * x[1] + x[1] * x[0] + x[0])

def g(t, x, y):
    result = [x[0] - t * y[0], x[1] - t * y[1]]
    return result

def norma(x):
    return(m.sqrt(x[0] * x[0] + x[1] * x[1]))

def beta(x, y):
    summ = 0
    for i in range(2):
        summ+=x[i]*y[i]
    summ = summ / (norma(y) ** 2)
    return summ

def naisk_spusk(x0, xpred,a ,b, d, k):
    print("Итерация = ", k)
    gr = [(f([x0[0]+delta,x0[1]])-f([x0[0]-delta,x0[1]])) / (2 * delta),
    (f([x0[0],x0[1]+delta])-f([x0[0],x0[1]-delta])) / (2 * delta)]
    if k!=0:
        gr1 = [(f([xpred[0]+delta,xpred[1]])-f([xpred[0]-delta,xpred[1]])) / (2 * delta),
        (f([xpred[0],xpred[1]+delta])-f([xpred[0],xpred[1]-delta])) / (2 * delta)]
        n = norma(gr1)
        gr1 = [i / n for i in gr1]
        print("Предыдущий grad нормированная = ", gr1)
    n = norma(gr)
    gr = [i / n for i in gr]
    print("grad нормированный = ", gr)
    t = [b - (2 * (b - a)) / (1 + m.sqrt(5)), a + (2 * (b - a)) / (1 + m.sqrt(5))]
    if k!=0:
        for i in range(2):
            d[i] = -gr[i] + beta(gr, gr1) * d[i]
    else:
        d = [-(f([x0[0]+delta,x0[1]])-f([x0[0]-delta,x0[1]])) / (2 * delta),
            -(f([x0[0],x0[1]+delta])-f([x0[0],x0[1]-delta])) / (2 * delta)]
    d1 = norma(d)
    d = [i / d1 for i in d]
    print("D нормированный = ",d)
    while abs(b-a) > 2 * eps1:
        f1 = f(g(t[0], x0, d))
        f2 = f(g(t[1], x0, d))
        if f1>=f2:
            a = t[0]
            t[0] = t[1]
            t[1] = a + (2 * (b - a)) / (1 + m.sqrt(5))
        else:
            b = t[1]
            t[1] = t[0]
            t[0] = b - (2 * (b - a)) / (1 + m.sqrt(5))
    l = (t[0]+t[1])/2
    print("L найденная методом золотого сейчения = ",l)
    for i in range(2):
        x0[i] -= l * d[i]
    return x0,xpred, gr, d 

a = -1
b = 1
x0 = [1,1]
d = []
x = copy.deepcopy(x0)
k = 0
x0,xk1, gr, d = naisk_spusk(x0,x, a, b, d, k)
print("X = ", x0)
print("F(X) = ", f(x0))
srav = [0,0]
for i in range(2):
    srav[i] = abs(x[i]-x0[i])
while (abs(gr[0]) > eps1 and abs(gr[1])>eps1 and srav[0]>eps1 and srav[1]>eps1):
    k+=1
    x = copy.deepcopy(x0)
    x0,xk1, gr,d = naisk_spusk(x0, xk1, a, b, d, k )
    print("X = ",x0)
    print("F(X) = ",f(x0))
    for i in range(2):
        srav[i] = abs(x[i]-x0[i])

print("X = ", x0)
print("F(X) = ", f(x0))
