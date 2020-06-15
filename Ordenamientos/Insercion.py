import time

class Insercion:
    def __init__(self,lista):
        self.lista = lista

    @staticmethod    
    def sort (lista):
        start_time = time.time()
        for i in range(1,len(lista)):
            aux = lista[i]
            indice = i
            while indice > 0 and lista[indice -1] > aux:
                lista[indice] = lista[indice-1]
                indice = indice - 1
            lista[indice] = aux
        return ((time.time() - start_time)*1000000)