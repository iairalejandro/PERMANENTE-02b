def insertion_sort(n, e):
    for j in range(len(n)-1):
        if n[j] == e:
            return True
    return False

n = list(range(10000000))
e = int(input("e: "))

import time

t_inicio = time.time()

resultado = insertion_sort(n, e)

t_final = time.time()

print("resultado={}, tiempo={:.4f}".format(resultado, t_final-t_inicio))
