# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
import operator


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = [int(i) for i in input(inputText).split()]
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def FindHalfIndex(list):
    half_index = 0
    count_index = 0
    for i in list:
        count_index+=1
    half_index = math.ceil(count_index/2)
    return half_index



ls1 = InputNumbers('Введите числа списка: ')
ls2 = ls1[::-1]
ls1 = ls1[:FindHalfIndex(ls2)]
ls2 = ls2[:FindHalfIndex(ls2)]
print(list(map(operator.mul, ls1, ls2)))


