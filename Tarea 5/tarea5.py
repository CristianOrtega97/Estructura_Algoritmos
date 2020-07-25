from Pila import *

respuesta1=input("Ingrese el primer numero: ")
respuesta2=input("Ingrese el segundo numero: ")
resultado=[]

if "." in respuesta1 and "." in respuesta2:
    lista1=list(respuesta1)
    lista2=list(respuesta2)
    lista_dec1=[]
    lista_dec2=[]
    lista_dec3=[]
    lista_dec4=[]

    for i in range(len(lista1)):
        numero1=lista1.pop()
        if numero1==".":
            break
        else:
            lista_dec1.append(int(numero1))

    for i in range(len(lista1)):
        numero1=lista1.pop()
        if numero1==".":
            break
        else:
            lista_dec2.append(int(numero1))

    for i in range(len(lista2)):
        numero2=lista2.pop()
        if numero2==".":
            break
        else:
            lista_dec3.append(int(numero2))

    for i in range(len(lista2)):
        numero2=lista2.pop()
        if numero2==".":
            break
        else:
            lista_dec4.append(int(numero2))

    lista_dec1.reverse()
    lista_dec2.reverse()
    lista_dec3.reverse()
    lista_dec4.reverse() 
    print(lista_dec1)
    print(lista_dec2)
    print(lista_dec3)
    print(lista_dec4)        
    resultado1=Pila.suma(lista_dec1,lista_dec3,resultado)
    print(resultado1)
    resultado=[]
    resultado2=Pila.suma(lista_dec2,lista_dec4,resultado)
    print(resultado2)
    print("El resultado es: ",resultado2,".",resultado1)

if not "." in respuesta1 and "." not in respuesta2:
    numero1 = [int(x) for x in str(respuesta1)]
    numero2 = [int(x) for x in str(respuesta2)]
    resultado=Pila.suma(numero1,numero2,resultado)
    print("El resultado es: ",resultado)
