import time

class Seleccion:
    def __init__(self,lista):
        self.lista = lista

    @staticmethod    
    def sort (lista):
        start_time = time.time()
        for i in range(len(lista)-1):
            menor = i
            for j in range(i+1,len(lista)):
                if lista[j]<lista[menor]:
                    menor = j
                    aux = lista[menor]
                    lista[menor] = lista[i]
                    lista[i] = aux
        return ((time.time() - start_time)*1000000)