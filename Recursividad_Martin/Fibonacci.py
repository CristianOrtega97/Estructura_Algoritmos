class Fibonacci:
    def __init__(self,numero):
        self.numero = numero

    @staticmethod
    def fibonacci(numero):
        if numero == 0:
            return numero
        elif numero == 1:
            return numero
        else:
            return Fibonacci.fibonacci(numero -1) + Fibonacci.fibonacci(numero-2)