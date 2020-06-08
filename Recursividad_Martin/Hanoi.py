class Hanoi:
    def __init__(self,n,inicio,final,medio):
        self.n = n
        self.inicio = inicio
        self.final = final
        self.medio = medio

    @staticmethod
    def hanoi(n,inicio,final,medio):
        if n == 1:
            print("Mover %i de la torre %s a la torre %s" %(n,inicio,final))
        else:
            Hanoi.hanoi(n-1,inicio,medio,final)
            print("Mover %i de la torre %s a la torre %s" %(n,inicio,final))
            Hanoi.hanoi(n-1,medio,final,inicio)