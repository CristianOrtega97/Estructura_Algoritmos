import time

class Burbuja:
    def __init__(self,lista):
        self.lista = lista

    @staticmethod    
    def sort (lista):
        start_time = time.time()
        print(str(lista))
        for i in range(len(lista)-1):
            for j in range(len(lista)-1):
                if lista[j] > lista[j+1]:
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux         
        return ((time.time() - start_time)*1000000)