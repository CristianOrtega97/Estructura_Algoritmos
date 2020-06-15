import time

class Quicksort:
    def __init__(self,lista):
        self.lista = lista

    @staticmethod    
    def sort (lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista.pop()
        elemento_mayor = []
        elemento_menor = []
        
        for elemento in lista:
            if elemento > pivote:
                elemento_mayor.append(elemento)
            else:
                elemento_menor.append(elemento_menor)
        return Quicksort.sort(elemento_menor) + [pivote] + Quicksort.sort(elemento_mayor)