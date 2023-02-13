n = input('Ведите колличество монеток: ')
n = int(n)
min = input('Кол-во перевернутых монеток: ')
min = int(min)
max = input('Кол-во неперевернутых монеток: ')
max = int(max)
if min == 0:
    print(0)
elif min < max:    
    n - max
    print(min)
elif max < min:
     n - min
     print(max)  
else: 
    n / 2      
    print(min)

# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
#  Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = input("Введите число:")
x = int(x)
# max = list[0]
# print(min(list))
new_set = set(list)
print(new_set)
# for i in range(0,len(list)):
#     if list[i] > x:        
#         list.remove([i])
#         print(i)
# list = [i for i in list if i > min(list) and i < max(list)]
# print(list[x])
