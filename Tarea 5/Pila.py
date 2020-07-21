class Pila:
    def __init__(self,numero1,numero2,resultado,respuesta1):
        self.numero1=numero1
        self.numero2=numero2
        self.resultado=resultado

    @staticmethod
    def suma(numero1,numero2,resultado):
        resultado_final=""
        longitud1 = len(numero1)
        longitud2 = len(numero2)
        longitud_total=0
        contador=0
        if longitud1>longitud2:
            contador=longitud1
        elif longitud1<longitud2:
            contador=longitud2
        else:
            longitud1=contador
        longitud_total = contador
        for i in range(contador):
            if longitud1>longitud2:
                numTemp1=numero1.pop()
                resultado.append(str(numTemp1))
                longitud_total-=1
                longitud1-=1
            elif longitud1<longitud2:
                numTemp2=numero2.pop()
                resultado.append(str(numTemp2))
                longitud_total-=1
                longitud2-=1
            else:
                numTemp1=numero1.pop()
                numTemp2=numero2.pop()
                int(numTemp1)
                int(numTemp2)
                resTemp = numTemp1 + numTemp2
                resultado.append(str(resTemp))
                longitud_total-=1
        resultado.reverse()
        print(resultado)
        resultado_final=resultado_final.join(resultado)
        return resultado_final