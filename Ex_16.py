N = int(input("Pls enter array length: "))
print("Pls enter arraya's elemnt(s):")
lst = [int(input()) for i in range(N)] 
x = int(input("Pls enter X: ")) 

inc = 0
for i in lst:
    if i == x:
        inc += 1
print(inc)
