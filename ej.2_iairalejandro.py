def bubblesort(L, e):
    n = len(L)
    for j in n - 1 , e + 1: 
        if L[j] < L[j - 1]:
            L[j] , L[j - 1] 
        return True
    return False

L = list(range(10000000))
e = int(input("e: "))

import time

t_inicio = time.time()

resultado = bubblesort(L, e)

t_final = time.time()

print("resultado={}, tiempo={:.4f}".format(resultado, t_final-t_inicio))
