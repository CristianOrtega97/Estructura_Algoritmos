from Suma import *
from Factorial import *
from Division import *
from Palindromo import *
from Fibonacci import *
from Hanoi import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Suma')
        print('2.- Factorial')
        print('3.- División')
        print('4.- Palíndromo')
        print('5.- Fibronacci')
        print('6.- Torres de Hanoi')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            numero = int(input('Ingrese un número: '))
            print(Suma.suma(numero))      
        elif respuesta == 2:
            numero = int(input('Ingrese un número: '))
            print(Factorial.factorial(numero))
        elif respuesta == 3:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Division.division(n,v)         
        elif respuesta == 4:
            frase = str(input('Ingrese la frase palíndroma: '))
            Palindromo.palindromo(frase)
        elif respuesta == 5:
            numero = int(input('Ingrese el numero: '))
            print(Fibonacci.fibonacci(numero))
        elif respuesta == 6:
            uno = int(input('Primer numero: '))
            dos = int(input('Segundo numero: '))
            tres = int(input('Tercer numero: '))
            Hanoi.hanoi(uno,dos,tres)
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



