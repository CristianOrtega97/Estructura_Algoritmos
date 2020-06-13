class Multiplicacion_Suma:
    def __init__(self,numero,veces):
        self.numero = numero
        self.veces = veces
    
    @staticmethod
    def multiplicacion_suma(numero,veces):
        if veces == 0:
            return 0
        else:
            return numero + Multiplicacion_Suma.multiplicacion_suma(numero,veces-1)