from Pila import *

respuesta1=input("Ingrese el primer numero: ")
respuesta2=input("Ingrese el segundo numero: ")
resultado=[]
numero1 = [int(x) for x in str(respuesta1)]
numero2 = [int(x) for x in str(respuesta2)]

resultado=Pila.suma(numero1,numero2,resultado)
print(resultado)