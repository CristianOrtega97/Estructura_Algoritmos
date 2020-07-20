from random import randint

class Quicksort:
    def __init__(self,lista_tren):
        self.lista_tren = lista_tren

    @staticmethod    
    def quicksort(lista_tren):
        if len(lista_tren) <= 1:
            return lista_tren
            
        elemento_igual,elemento_mayor,elemento_menor = [],[],[]
        pivote = lista_tren[randint(0,len(lista_tren)-1)]
        
        for elemento in lista_tren:
            if elemento < pivote:
                elemento_menor.append(elemento)
            elif elemento == pivote:
                elemento_igual.append(elemento)
            else:
                elemento_mayor.append(elemento)
        return Quicksort.quicksort(elemento_menor) + elemento_igual + Quicksort.quicksort(elemento_mayor)

    @staticmethod    
    def sort(lista_tren):
        lista_tren.sort()     