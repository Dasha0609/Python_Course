N = int(input("Pls enter array length: "))
print("Pls enter array's elemnt(s):")
lst = [int(input()) for i in range(N)] 
x = int(input("Pls enter X: ")) 

dif=[abs(lst[i]-x) for i in range(len(lst))]
print(lst[dif.index(min(dif))])
