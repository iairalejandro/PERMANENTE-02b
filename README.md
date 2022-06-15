# PERMANENTE-02b

CÓDIGO Nª1:
Hecho por la función INSERTION_SORT donde calcula la cantidad de tiempo de búsqueda en una lista del 1 al 10000000.

1. Muestra junto al mensaje si el número está dentro de la lista, si es el caso imprimira TRUE; caso contrario FALSE.
--------------------------------
    for j in range(len(n)-1):
          if n[j] == e:  
              return True
      return False
--------------------------------
2. "n" sería la variable de la lista, y "e" donde el usuario tendrá que escribir el número que se hallara.
---------------------------
n = list(range(10000000))
e = int(input("e: "))
---------------------------
3. Variables de tiempo, y donde se imprimirá el resultado, y la cantidad de tiempo, en este caso en 4 decimales.
--------------------------------------------------------------------------
import time

t_inicio = time.time()

resultado = insertion_sort(n, e)

t_final = time.time()

print("resultado={}, tiempo={:.4f}".format(resultado, t_final-t_inicio))
--------------------------------------------------------------------------
