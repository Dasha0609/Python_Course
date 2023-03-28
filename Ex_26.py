def number(N, P):
    if P == 0:
        return 1
    return (N*number(N, P-1))

N = int(input('Pls fill number N: '))
P = int(input('Pls fill number P: '))

print(number(N, P)) 