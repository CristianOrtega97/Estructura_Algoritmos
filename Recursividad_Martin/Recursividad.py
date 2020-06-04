from Suma import *
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
        print('2.- Factorial')
        print('4.- División')
        print('5.- Palíndromo')
        print('6.- Fibronacci')
        print('7.- Torres de Hanoi')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            numero = int(input('Ingrese un número: '))
            print(Suma.suma(numero))      
        elif respuesta == 2:
            numero = int(input('Ingrese un número: '))
            Factorial.factorial(numero)
        elif respuesta == 4:
            n = int(input('Ingrese un número: '))
            v = int(input('Ingrese las veces: '))
            Division.division(n,v)         
        elif respuesta == 5:
            frase = input(str('Ingrese la frase palíndroma: '))
            Palindromo.palindromo(frase)
        elif respuesta == 6:
            numero = input(int('Ingrese el numero: '))
            Fibronacci.fibronacci(numero)
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



