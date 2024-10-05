def tran(a):
    if a == 0:
        return ''
    else:
        return tran(a // 4) + str(a % 4)

num = int(input("Введите десятичное число: "))
quatr = tran(num)
print("Представление числа в четверичной системе счисления: ", quatr)

