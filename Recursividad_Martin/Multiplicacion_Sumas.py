class Multiplicacion_Suma:
    def __init__(self,numero,veces):
        self.numero = numero
        self.veces = veces
    
    @staticmethod
    def multiplicacion_suma(numero,veces):
        if veces == 2:
            return print('El resultado es: ', numero)

        elif veces == 0:
            return print('El resultado es: ', 0) 
        else:
            return Multiplicacion_Suma.multiplicacion_suma(numero + numero,veces-1)