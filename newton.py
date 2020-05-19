import math as m
import copy

eps1 = 1e-5

delta = 1e-5
#x^4*y^2+2x^2*y+1+y^2-2y+1
def f(x):
    return(x[0] * x[0] + 5 * x[1]*x[1] + x[0] * x[1] + x[0])



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
    s = [0,0]
    print("Matr obr: ")
    print(br[0])
    print(br[1])
    for i in range(2):
        for j in range(2):
            s[i] += br[i][j] * gr[j]
    print("S = ", s)
    for i in range(2):
        x0[i] -= s[i]
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
