from Suma import *
from Resta import *
from Factorial import *
from Division import *
from Palindromo import *
from Fibronacci import *
from Hanoi import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Factorial')
        print('4.- División')
        print('5.- Palíndromo')
        print('6.- Fibronacci')
        print('7.- Torres de Hanoi')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Suma.suma(n,v)
        elif respuesta == 2:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Resta.resta(n,v)      
        elif respuesta == 3:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Factorial.factorial(n,v)
        elif respuesta == 4:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Division.division(n,v)         
        elif respuesta == 5:
            frase = input(str('Ingrese la frase palíndroma: '))
            Palindromo.palindromo(frase)
        elif respuesta == 6:
            n = input(int('Ingrese el numero: '))
            Fibronacci.fibronacci(n)
        elif respuesta == 7:
            uno = input(int('Primer numero: '))
            dos = input(int('Segundo numero: '))
            tres = input(int('Tercer numero: '))
            Hanoi.hanoi(uno,dos,tres)
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



