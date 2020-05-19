from r_slay import metod_gausa

def F(x1, x2, l):
    return x1 * x1 + 5 * x2 * x2 + x1 * x2 + x1 + l * (2 * x1 + 3 * x2 - 1)


def Fpr(x1, x2):
    return 2 * x1 + 3 * x2 - 1

n = 3
m = 2
eps = 1e-8
delta = [[1, 1, 2],[1,10,3],[2,3,0]]
beta = [-1,0,1]
print("Matr = ", delta)
print("Вектор для поиска решения по методу Гаусса = ", beta)
x = metod_gausa(delta, beta)
x1 = x[0]
x2 = x[1]
l = x[2]

op = [[0,0],[0,0]]
op[0][0] = (F(x1 + eps, x2, l) - 2 * F(x1, x2, l) + F(x1 - eps, x2, l)) / (eps * eps)
op[0][1] = (F(x1 + eps, x2 + eps, l) - F(x1, x2 + eps, l) - F(x1 + eps, x2, l) + F(x1, x2, l)) / (eps * eps)
op[1][0] = (F(x1, x2, l) - F(x1, x2 - eps, l) - F(x1 - eps, x2, l) + F(x1 - eps, x2 - eps, l)) / (eps * eps)
op[1][1] = (F(x1, x2 + eps, l) - 2 * F(x1, x2, l) + F(x1, x2 - eps, l)) / (eps * eps)

res = op[0][0] * op[1][1] - op[1][0] * op[0][1]

if res < 0:
    print("Точка максимума: ", x1, " , ", x2, " , ", l)
    print("Значение функции:", F(x1,x2,l))
else:
    print("Точка минимума: ", x1, " , ", x2, " , ", l)
    print("Значение функции:", F(x1,x2,l))
