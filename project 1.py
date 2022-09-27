# 1- Определить, присутствует ли в заданном списке строк, некоторое число
ls1 = list(input('Введите строку: ').split())
num = input('Введите число которое нужно найти: ')
result = list(map(lambda x: num in x, ls1))
print(result)


