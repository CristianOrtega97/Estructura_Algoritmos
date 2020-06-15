import time

class Quicksort:
    def __init__(self,lista):
        self.lista = lista

    @staticmethod    
    def sort (lista):
        start_time = time.time()
        return ((time.time() - start_time)*1000000)