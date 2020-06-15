import time
from random import randint

class Quicksort:
    def __init__(self,lista):
        self.lista = lista

    @staticmethod    
    def sort (lista):
        if len(lista) <= 1:
            return lista
            
        elemento_igual,elemento_mayor,elemento_menor = [],[],[]
        pivote = lista[randint(0,len(lista)-1)]
        
        for elemento in lista:
            if elemento < pivote:
                elemento_menor.append(elemento)
            elif elemento == pivote:
                elemento_igual.append(elemento)
            else:
                elemento_mayor.append(elemento)
        return Quicksort.sort(elemento_menor) + elemento_igual + Quicksort.sort(elemento_mayor)