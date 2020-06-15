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

lista = [random.randrange(1, 100, 1) for i in range(1000)]

print('El resultado con: 1000 datos:')
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')
start_time = time.time()
Quicksort.sort(lista)
tiempo = (time.time() - start_time)*1000000
print('El tiempo de Quicksort es: ',tiempo,' micro segundos')
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')

lista = [random.randrange(1, 10000, 1) for i in range(10000)]

print('El resultado con: 10000 datos:')
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')
start_time = time.time()
Quicksort.sort(lista)
tiempo = (time.time() - start_time)*1000000
print('El tiempo de Quicksort es: ',tiempo,' micro segundos')
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')

lista = [random.randrange(1, 20000, 1) for i in range(20000)]

print('El resultado con: 20000 datos:')
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')
start_time = time.time()
Quicksort.sort(lista)
tiempo = (time.time() - start_time)*1000000
print('El tiempo de Quicksort es: ',tiempo,' micro segundos')
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')