class Factorial:
    def __init__(self,numero):
        self.numero = numero

    @staticmethod
    def factorial (numero):
        if numero == 1:
            return numero
        else:
            try:
                return numero * Factorial.factorial(numero-1)
            except RecursionError:
                print('Ingrese un número mayor o igual a 1')