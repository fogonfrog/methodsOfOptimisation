def func(x):
    return x * x + 4 * x + 6

a = int(input("Введите a = "))
b = int(input("Введите b = "))
eps = 0.5
iter = 0

iter = 1
func1 = func(a)
xi = a + eps * iter
func2 = func(xi)

print("Итерация: ", iter)
print("F(a) = ", func1)
print("F(xi) = ", func2)

while(func1 > func2):
    iter += 1
    print("F(xi-1) > F(xi)")
    func1 = func2
    xi = a + eps * iter
    func2 = func(xi)
    print("Итерация: ", iter)
    print("F(xi-1) = ", func1)
    print("F(xi) = ", func2)

print("F(xi-1) <= F(i)")
print("Точка минимума +-0.5: ", (2 * a + eps * (iter - 2) + eps * (iter - 1)) / 2)
print("Значение функции: ", func1)
print("Количество итераций: ", iter)

