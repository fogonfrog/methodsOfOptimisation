def f(x):
    return x * x - 4 * x +6

a = int(input('vvedite a: '))
b = int(input('vvedite b: '))
eps = 0.5
kol = 0

kol = 1
f1 = f(a)
f2 = f(a + eps * kol)
print("Итерация: ",kol)
print("Fk-1 = ",f1)
print("Fk = ",f2)
while(f1>f2):
    print("FK-1 > Fk")
    f1 = f2
    kol += 1
    f2 = f(a + eps * kol)
    print("Итерация: ",kol)
    print("Fk-1 = ",f1)
    print("Fk = ",f2)
print("FK-1 <= Fk")
print("Точка минимума +-0.5: ",(2 * a + eps * (kol-2) + eps * (kol-1))/2)
print("Значение функции: ", f1)
print("Количество итерация: ", kol)

