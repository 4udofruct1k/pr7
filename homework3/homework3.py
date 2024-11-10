def tran(a):
    if a == 0:
        return ''
    else:
        return tran(a // 4) + str(a % 4)

while True:
    num = input("Введите десятичное число: ")
    if num.isdigit():
        break
    else:
        print("Неверный ввод")
quatr = tran(int(num))
print("Представление числа в четверичной системе счисления: ", quatr)
