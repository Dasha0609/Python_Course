N = int(input("Размер массива: "))
print("Элементы массива:")
lst = [int(input()) for i in range(N)] 
x = int(input("Число x: ")) 

inc = 0
for i in lst:
    if i == x:
        inc += 1
print(inc)
