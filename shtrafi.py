import copy
import math as m
def f(x,r):
    return(x[0] * x[0] + 5 * x[1]*x[1] + x[0] * x[1] + x[0] + r * (2 * x[0]+3 * x[1]-1)**2)

def norma(x):
    return(m.sqrt(x[0] * x[0] + x[1] * x[1]))


def newton(x0, a, b):
    delta = 1e-5
    gr = [(f([x0[0] + delta, x0[1]], r ) - f([x0[0] - delta, x0[1]], r)) / (2 * delta),
    (f([x0[0], x0[1] + delta],r) - f([x0[0], x0[1] - delta],r)) / (2 * delta)]
    hesse = [[0,0],[0,0]]
    br = [[0,0],[0,0]]
    hesse[0][0] = (f([x0[0] + delta, x0[1]], r) - 2 * f(x0, r) + f([x0[0] - delta, x0[1]], r)) / (delta * delta)
    hesse[0][1] = (f([x0[0] + delta, x0[1] + delta], r) - f([x0[0], x0[1] + delta], r) - f([x0[0] + delta, x0[1]], r) + f(x0, r)) / (delta * delta)
    hesse[1][0] = (f(x0, r) - f([x0[0],x0[1] - delta], r) - f([x0[0] - delta, x0[1]], r) + f([x0[0] - delta, x0[1] - delta], r)) / (delta * delta)
    hesse[1][1] = (f([x0[0], x0[1] + delta], r) - 2 * f(x0, r) + f([x0[0], x0[1] - delta], r)) / (delta * delta)
    opr = (hesse[0][0] * hesse[1][1]) - (hesse[0][1] * hesse[1][0])
    if opr == 0:
        return [0, 0]
    else:
        br[0][0] = hesse[1][1] / opr
        br[0][1] = -hesse[1][0] / opr
        br[1][0] = -hesse[0][1] / opr
        br[1][1] = hesse[0][0] / opr
    s = [0,0]
    for i in range(2):
        for j in range(2):
            s[i] += br[i][j] * gr[j]
    for i in range(2):
        x0[i] -= s[i]   
    return x0, gr

eps1 = 1e-5
eps = 1e-5
x0 = [1,1]
r = 1
beta = 5
i = 0
while r * (2 * x0[0] + 3 * x0[1]-1)**2 > eps:
    print("r * (2 * X1 + 3 * X2-1)^2 > eps")
    i+=1
    a = -1
    b = 1
    x = copy.deepcopy(x0)
    x0, gr = newton(x0, a, b)
    srav = [0,0]
    while (abs(gr[0]) > eps1 and abs(gr[1])>eps1 and srav[0]>eps1 and srav[1]>eps1):
        x = copy.deepcopy(x0)
        x0, gr = newton(x0, a, b)
    print("Итерация: ",i)
    print("X0, X1 =", x0)
    r = beta * r
    print("r = ", r)
print("r * (2 * X1 + 3 * X2-1)^2 <= eps")
print("X0, X1 =", x0)
print("Итераций: ", i)
print("Значение в т. условного минимума: ", f(x0,r))
