from Suma import *
from Resta import *
from Factorial import *
from Division import *
from Palindromo import *
from Fibonacci import *
from Multiplicacion_Sumas import *
from Division_Restas import *
from Exponente_Multiplicacion import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Factorial')
        print('4.- Division')
        print('5.- Palíndromo')
        print('6.- Fibronacci')
        print('7.- Multiplicación con Sumas') 
        print('8.- Division con Restas')
        print('9.- Potencia con Multiplicaciones')
        print('10.- ')
        print('11.- Torres de Hanoi')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            numero = int(input('Ingrese un número: '))
            print(Suma.suma(numero))
        elif respuesta == 2:
            numero = int(input('Ingrese un número: '))
            print(Resta.resta(numero))
        elif respuesta == 3:
            numero = int(input('Ingrese un número: '))
            print(Division.division(numero))      
        elif respuesta == 4:
            numero = int(input('Ingrese un número: '))
            print(Factorial.factorial(numero))        
        elif respuesta == 5:
            frase = str(input('Ingrese la frase palíndroma: '))
            fraseoriginal = frase.replace(" ","")
            frase = frase.replace(" ","")
            frase = list(frase)
            fraseoriginal = list(fraseoriginal)
            ultima_pos = len(frase)-1  #Ultima posición
            primera_pos = 0   #Primer posicion
            Palindromo.palindromo(frase,primera_pos,ultima_pos)
            if (frase == fraseoriginal):
                print('La frase es Palindromo')
            else:
                print('La frase no es Palindromo')
        elif respuesta == 6:
            numero = int(input('Ingrese el numero: '))
            print(Fibonacci.fibonacci(numero))
        elif respuesta == 7:
            numero = int(input('Ingrese el numero a multiplicar: '))
            veces = int(input('Ingrese el numero de veces a realizar: '))
            Multiplicacion_Suma.multiplicacion_suma(numero,veces)
        elif respuesta == 8:
            numero = int(input('Ingrese el Dividendo: '))
            resta = int(input('Ingrese el Divisor: '))
            veces = 0
            Division_Restas.division_restas(numero,resta,veces)
        elif respuesta == 9:
            numero = int(input('Ingrese el Numero: '))
            exponente = int(input('Ingrese el Exponente: '))-1
            resultado = numero
            Exponente_Multiplicacion.exponente_multiplicacion(numero,resultado,exponente)
        elif respuesta == 10:
            #Investigar jijiji
            pass
        elif respuesta == 11:
            #Torres de Hanoi
            pass
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



