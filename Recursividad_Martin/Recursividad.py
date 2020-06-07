from Funcion_For import *
from Suma import *
from Factorial import *
from Palindromo import *
from Fibonacci import *
from Multiplicacion_Sumas import *
from Division_Restas import *
from Exponente_Multiplicacion import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Factorial')
        print('2.- Sumatoria')
        print('3.- Potencia con Multiplicación')
        print('4.- Multiplicacion con Sumas')
        print('5.- División con Restas')
        print('6.- Potencia con Sumas') #Pendiente
        print('7.- Palindromo') 
        print('8.- ')  #Pendiente
        print('9.- ')  #Pendiente
        print('10.- Funcion For') #Pendiente
        print('11.- Fibonacci')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            numero = int(input('Ingrese un número: '))
            print(Factorial.factorial(numero))  
        elif respuesta == 2:
            numero = int(input('Ingrese un número: '))
            print(Suma.suma(numero))
        elif respuesta == 3:
            numero = int(input('Ingrese el Numero: '))
            exponente = int(input('Ingrese el Exponente: '))-1
            resultado = numero
            Exponente_Multiplicacion.exponente_multiplicacion(numero,resultado,exponente) 
        elif respuesta == 4:
            numero = int(input('Ingrese el numero a multiplicar: '))
            veces = int(input('Ingrese el numero de veces a realizar: '))
            Multiplicacion_Suma.multiplicacion_suma(numero,veces)          
        elif respuesta == 5:
            numero = int(input('Ingrese el Dividendo: '))
            resta = int(input('Ingrese el Divisor: '))
            veces = 0
            Division_Restas.division_restas(numero,resta,veces)
        elif respuesta == 6:
            pass
        elif respuesta == 7:
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
        elif respuesta == 8:
            pass
        elif respuesta == 9:
            pass
        elif respuesta == 10:
            #Investigar jijiji
            pass
        elif respuesta == 11:
            numero = int(input('Ingrese el Numero: '))
            print(Fibonacci.fibonacci(numero))
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



