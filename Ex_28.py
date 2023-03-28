#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

a = int(input('Pls fill number a: '))
b = int(input('Pls fill number b: '))

print(sum(a, b))