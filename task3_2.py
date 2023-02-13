# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
#  Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = input("Введите число:")
x = int(x)

new_set = set(list)
print(new_set)
for i in range(0, len(new_set)):
    if x > min(new_set) and x < max(new_set):
        
        print(x)
# list = [x for i in list if i > min(list) and i < max(list)]
# print(list[x])
# print(list)
