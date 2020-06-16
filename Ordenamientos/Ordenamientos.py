from Burbuja import *
from Seleccion import *
from Quicksort import *
from Insercion import *
import random
import time

tiempo_burbuja = 0.0
tiempo_seleccion = 0.0
tiempo_insercion = 0.0
tiempo_quicksort = 0.0

print('El resultado con: 1000 datos:')
random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(1000)]
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(1000)]
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(1000)]
start_time = time.time()
Quicksort.sort(lista)
tiempo = (time.time() - start_time)*1000000
print('El tiempo de Quicksort es: ',tiempo,' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(1000)]
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')




print('El resultado con: 10000 datos:')
random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(10000)]
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(10000)]
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(10000)]
start_time = time.time()
Quicksort.sort(lista)
tiempo = (time.time() - start_time)*1000000
print('El tiempo de Quicksort es: ',tiempo,' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(10000)]
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')




print('El resultado con: 20000 datos:')
random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(20000)]
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(20000)]
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(20000)]
start_time = time.time()
Quicksort.sort(lista)
tiempo = (time.time() - start_time)*1000000
print('El tiempo de Quicksort es: ',tiempo,' micro segundos')

random.seed(3)
lista = [random.randrange(1, 100, 1) for i in range(20000)]
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')