# 2- Найти сумму чисел списка стоящих на нечетной позиции

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = [int(i) for i in input(inputText).split()]
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

ls = InputNumbers('Введите числа: ')
print(ls)
print(sum(list(filter(lambda x: x%2, ls))))
