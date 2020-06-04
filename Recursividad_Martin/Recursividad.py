from Factorial import *
from Palindromo import *
from Fibronacci import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Factorial')
        print('2.- Palíndromo')
        print('3.- Fibronacci')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Factorial.factorial(n,v)
        elif respuesta == 2:
            frase = input(str('Ingrese la frase palíndroma: '))
            Palindromo.palindromo(frase)
        elif respuesta == 3:
            n = input(int('Ingrese el numero: '))
            Fibronacci.fibronacci(n)
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



