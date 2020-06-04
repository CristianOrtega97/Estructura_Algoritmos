from Suma import *
from Factorial import *
from Palindromo import *
from Fibonacci import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Suma')
        print('2.- Factorial')
        print('3.- Palíndromo')
        print('4.- Fibronacci')
        print('5.- Torres de Hanoi')
        print('0.- Salir')
        respuesta = int(input('Respuesta: '))

        if respuesta == 1:
            numero = int(input('Ingrese un número: '))
            print(Suma.suma(numero))      
        elif respuesta == 2:
            numero = int(input('Ingrese un número: '))
            print(Factorial.factorial(numero))        
        elif respuesta == 3:
            frase = str(input('Ingrese la frase palíndroma: '))
            frase = frase.replace(" ","")
            ultima_pos = len(frase)-1  #Ultima posición
            primera_pos = 0   #Primer posicion
            Palindromo.palindromo(frase,primera_pos,ultima_pos)
        elif respuesta == 4:
            numero = int(input('Ingrese el numero: '))
            print(Fibonacci.fibonacci(numero))
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



