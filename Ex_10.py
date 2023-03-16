
N = int(input('Pls enter coins qty: '))
head, tail = 0, 0

for i in range(N):
        x = int(input('pls use 1 for heads side coins and 2 for tails side: '))
        if x == 1:
            head += 1

print(('Pls change side for: ', head if head < N // 2 else N - head, ('coins')))
  
    

