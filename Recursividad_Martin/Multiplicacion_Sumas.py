class Multiplicacion_Suma:
    def __init__(self,numero,resultado,veces):
        self.numero = numero
        self.resultado = resultado
        self.veces = veces
    
    @staticmethod
    def multiplicacion_suma(numero,resultado,veces):
        if veces == 0:
            print('El resultado de la multiplicacion es: ', resultado)
            return resultado
        else:
            return Multiplicacion_Suma.multiplicacion_suma(numero,numero+resultado,veces-1)