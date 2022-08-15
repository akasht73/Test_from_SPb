# Задание 1

# Оригинальная функция
# def isEven(value):
#     return value % 2 == 0

# Из описания задание не до конца понятно (по крайней мере мне) какая именно функция должна быть написана.
# Поэтому решил представить два варианта решения.
# 1.  "Зеркальная" функция, возвращающяя нечетные числа
def isOdd(value):
    return value % 2 == 1

# 2. "Бинарная" функция, возвращающая четные числа
def isEven_bin(value):
    return value & 1 == 0

# test
print(isOdd(10))
print(isOdd(11))
print(isEven_bin(10))
print(isEven_bin(11))