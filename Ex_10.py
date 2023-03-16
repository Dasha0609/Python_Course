"""На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть"""




N = int(input('Pls enter coins qty: '))
head, tail = 0, 0

for i in range(N):
        x = int(input('pls use 1 for heads side coins and 2 for tails side: '))
        if x == 1:
            head += 1
        else:
            tail += 1  

print(f'Pls change side for: ', head if head < tail else tail, 'coins')

#print(('Pls change side for: ', head if head < N // 2 else N - head, ('coins')))
  
    

