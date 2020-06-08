class Exponente_Multiplicacion:
    def __init__(self,numero,resultado,exponente):
        self.numero = numero
        self.resultado = resultado
        self.exponente = exponente

    @staticmethod
    def exponente_multiplicacion(numero,resultado,exponente):
        if exponente <= 1:
            print('El resultado de la potencia es: ', resultado)
            return resultado
        else:
            return Exponente_Multiplicacion.exponente_multiplicacion(numero,numero*resultado,exponente-1)