class Resta:
    def __init__(self,numero):
        self.numero = numero

    @staticmethod
    def resta(numero):
        if numero == 1:
            return numero
        else:
            try:
                return numero - Resta.resta(numero-1)
            except RecursionError:
                print('Ingrese un número mayor o igual a 1')