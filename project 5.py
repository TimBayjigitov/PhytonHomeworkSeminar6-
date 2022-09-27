# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = int(input(inputText))
            if num < 0:
                num *= -1
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

n = InputNumbers('Введите колличество членов последовательности: ')
ls1 = [i for i in range(n)]
result = (list(map(lambda x: -3**(x), [i for i in range(n)])))
print(result)
print([x if i % 2 != 0 else x*-1 for i,x in enumerate(result)])
