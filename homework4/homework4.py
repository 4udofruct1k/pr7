while True:
    a = input("Введите целое a: ")
    if a.isdigit():
        break
    else:
        print("Неверный ввод")
while True:
    b = input("Введите целое b: ")
    if b.isdigit():
        break
    else:
        print("Неверный ввод")
while True:
    c = input("Введите целое c: ")
    if c.isdigit():
        break
    else:
        print("Неверный ввод")
if b != 0:
    x = int(a)/int(b) - 2*int(c)
    print("Результат уравнения X = a/b - 2*c =", x)
