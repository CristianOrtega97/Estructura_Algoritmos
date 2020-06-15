from Burbuja import *
from Seleccion import *
from Quicksort import *
from Insercion import *
import random

tiempo_burbuja = 0.0
tiempo_seleccion = 0.0
tiempo_insercion = 0.0
tiempo_quicksort = 0.0

lista = [random.randrange(1, 100, 1) for i in range(100000000000000)]

print('El resultado con: 1000 datos:')
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')
print('El tiempo de Selección es: ',Seleccion.sort(lista),' micro segundos')
print('El tiempo de Quicksort es: ',Quicksort.sort(lista),' micro segundos')
print('El tiempo de Inserción es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')

"""
lista = [random.randrange(1, 10000, 1) for i in range(10000)]

print('El resultado con: 10000 datos:')
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')
print('El tiempo de Seleccion es: ',Seleccion.sort(lista),' micro segundos')
print('El tiempo de Quicksort es: ',Quicksort.sort(lista),' micro segundos')
print('El tiempo de Insercion es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ')

lista = [random.randrange(1, 20000, 1) for i in range(20000)]

print('El resultado con: 10000 datos:')
print('El tiempo de Burbuja es: ',Burbuja.sort(lista),' micro segundos')
print('El tiempo de Seleccion es: ',Seleccion.sort(lista),' micro segundos')
print('El tiempo de Quicksort es: ',Quicksort.sort(lista),' micro segundos')
print('El tiempo de Insercion es: ',Insercion.sort(lista),' micro segundos')
print(' ')
print(' ')
print(' ') """