class Suma:
    def __init__(self,numero):
        self.numero = numero

    @staticmethod
    def suma(numero):
        if numero == 1:
            return numero
        else:
            try:
                return numero + Suma.suma(numero-1)
            except RecursionError:
                print('Ingrese un número mayor o igual a 1')