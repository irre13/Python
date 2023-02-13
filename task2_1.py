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

