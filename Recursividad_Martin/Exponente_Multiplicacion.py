class Exponente_Multiplicacion:
    def __init__(self,numero,exponente):
        self.numero = numero
        self.exponente = exponente

    @staticmethod
    def exponente_multiplicacion(numero,exponente):
        if exponente == 0:
            return 1
        else:
            return numero * Exponente_Multiplicacion.exponente_multiplicacion(numero,exponente-1)