from Funcion_For import *
from Invertir_Frase import *
from Suma import *
from Factorial import *
from Palindromo import *
from Fibonacci import *
from Multiplicacion_Sumas import *
from Division_Restas import *
from Exponente_Multiplicacion import *
from Hanoi import *

respuesta = 1

while respuesta!=0:
    try:
        print('Selecciona una opcion: ')
        print('1.- Factorial')
        print('2.- Sumatoria')
        print('3.- Potencia con Multiplicación')
        print('4.- Multiplicacion con Sumas')
        print('5.- División con Restas')
        print('6.- Potencia con Sumas') 
        print('7.- Palindromo')
        print('8.- Torres de Hanoi')  #Pendiente
        print('9.- Invertir la Frase')
        print('10.- Funcion For')
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
            exponente = int(input('Ingrese el Exponente: '))
            print('El resultado de la potencia es: ',Exponente_Multiplicacion.exponente_multiplicacion(numero,exponente))
        elif respuesta == 4:
            numero = int(input('Ingrese el numero a multiplicar: '))
            veces = int(input('Ingrese el numero de veces a realizar: '))
            print(Multiplicacion_Suma.multiplicacion_suma(numero,veces))        
        elif respuesta == 5:
            numero = int(input('Ingrese el Dividendo: '))
            veces = int(input('Ingrese el Divisor: '))
            print(Division_Restas.division_restas(numero,veces))
        elif respuesta == 6:
            numero = int(input('Ingrese el numero a multiplicar: '))
            veces = int(input('Ingrese el numero de veces a realizar: '))
            veces_exponente = veces
            numero_exponente = Multiplicacion_Suma.multiplicacion_suma(numero,veces)
            print(Exponente_Multiplicacion.exponente_multiplicacion(numero_exponente,veces_exponente))
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
                n = int(input('Ingrese el numero de aros: '))
                inicio = input('¿De que torre parte? ')
                final = input('¿A que torre va? ')
                medio = input('¿Cual sobra? ')
                Hanoi.hanoi(n,inicio,final,medio)
        elif respuesta == 9:
            frase = str(input('Ingrese la frase palíndroma: '))
            frase = list(frase)
            fraseoriginal = list(frase)
            ultima_pos = len(frase)-1  #Ultima posición
            primera_pos = 0   #Primer posicion
            Invertir_Frase.invertir_frases(frase,primera_pos,ultima_pos)
        elif respuesta == 10:
            repeticion = int(input('Ingrese las veces a repetir: '))
            Funcion_For.funcion_for(repeticion)
        elif respuesta == 11:
            numero = int(input('Ingrese el Numero: '))
            print(Fibonacci.fibonacci(numero))
        elif respuesta == 0:
            print('Saliendo de la aplicación')
        else:
            print('Seleccione una opción valida')
    except ValueError:
            print('Ingrese un caracter válido')



