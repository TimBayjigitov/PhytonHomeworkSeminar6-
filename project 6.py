# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            num = list(input(inputText).split())
            is_OK = True
        except ValueError:
            print("это не число, повторите попытку")
    return num

def check_list(list, item):
    count = 0
    for i in range(len(list)):
        if list[i] == item:
            count += 1
            if count == 2:
                return i
    else:
        return -1

ls1 = InputNumbers('Введите текст через пробел: ')
text = input('Введите текст который необходимо найти: ')
print(check_list(ls1,text))
