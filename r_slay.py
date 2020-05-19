import sys
import copy

def metod_gausa(a, b):
    x = []
    n = len(b)
    for i in range(0,n):
        x.append(0)
    for k in range(0, n-1):
        for i in range(k+1, n):
            if (a[k][k]!=0):
                t = a[i][k] / a[k][k]
                b[i] = b[i]- t * b[k]
            for j in range(k, n):
                a[i][j] = a[i][j] - t * a[k][j]
    if a[n-1][n-1]!=0 :
        x[n-1] = b[n-1]/a[n-1][n-1]
    else:
        print('Error: Деление на 0!')
        sys.exit()
    for k in range(n-2, -1, -1):
        summ = 0
        for j in range(k+1, n):
            summ += a[k][j] * x[j]
        x[k] = (b[k] - summ)/a[k][k]
    return x

def obr_mat(x):
    E = []
    n = len(x)
    X = []
    for i in range(n):
        E.append([])
        for j in range(n):
            E[i].append(0)
            if i==j:
                E[i][j] = 1
    for i in range(n):
        X.append(metod_gausa(x, E[i]))
    for i in range(n):
        for j in range(i,n):
            X[i][j] = X[j][i]
    return X

def treh_diagonal(a1, a2, a3, b):
    x = []
    c = []
    d = []
    n = 0
    n = len(a2)
    for i in range(0, n):
        x.append(0)
        c.append(0)
        d.append(0)
    for i in range(0, n):
        if (abs(a2[i]) < (abs(a1[i]) + abs(a3[i])) and (f!=0)):
            print("Warrning: Матрица не удовлетворяет достаточному условию!")
    d[0] =  (-1) * a3[0] / a2[0]
    c[0] = b[0] / a2[0]
    for i in range(1, n-1):
        if (a1[i] * d[i - 1] + a2[i])==0:
            print("Error: Деление на 0!")
            sys.exit()
        d[i] = ((-1) * a3[i]) / (a1[i] * d[i - 1] + a2[i])
        c[i] = (b[i] - a1[i] * c[i - 1])/(a1[i] * d[i - 1] + a2[i])
    x[n-1] = (b[n-1] - a1[n-1] * c[n-2])/(a2[n-1] + a1[n-1] * d[n-2])
    for i in range(n-2, -1, -1):
        x[i] = d[i] * x[i+1] + c[i]
    return x

def LU(a, b):
    lu = []
    n = len(b)
    x = []
    y = []
    for i in range(0, n):
        lu.append([])
        x.append(0)
        y.append(0)
        for j in range(0, n):
            lu[i].append(0)
    for i in range(0, n):
        for j in range(i, n):
            summa = 0
            for k in range(0, i):
                summa += lu[i][k] * lu[k][j]
            lu[i][j] = a[i][j] - summa
            #print(lu[i])
        for j in range(i+1, n):
            summa = 0
            for k in range(0, i):
                summa += lu[j][k] * lu[k][i]
            lu[j][i] = (a[j][i] - summa) / lu[i][i]
    for i in range(0,n):
        if lu[i][i] == 0:
            print('Error: Невозможно разложить матрицу в LU')
        #print(lu[i])
    '''
    #разложение матрицы lu на 2 матрицы
    l = copy.deepcopy(lu)
    u = copy.deepcopy(lu)
    for i in range(0,n):
        l[i][i] = 1
        for j in range(0, n):
            if  i < j:
                l[i][j] = 0
    for i in range(0,n):
        for j in range(0, n):
            if i > j:
                u[i][j] = 0
    print(l)
    print(u)
    '''
    for i in range(0, n):
        summa = 0
        for j in range(0, i+1):
            summa += lu[i][j] * y[j]
        y[i] = (b[i] - summa) 
    #print(y)
    for i in range(n - 1, -1, -1):
        summa = 0
        for j in range(i, n):
            summa += lu[i][j] * x[j]
        x[i] = (y[i] - summa) / lu[i][i]
    return x
