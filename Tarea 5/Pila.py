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
            diferencia = longitud1 - longitud2
        elif longitud1<longitud2:
            num_aux=numero2
            numero2=numero1
            numero1=num_aux
            long_aux=longitud2
            longitud2=longitud1
            longitud1=long_aux
            contador=longitud1
            diferencia = longitud1 - longitud2
            longitud_total = contador
        else:
            contador=longitud1
            diferencia=0
        longitud_total = contador
        for i in range(contador):
            if diferencia != 0:
                if longitud1>longitud2:
                    if longitud2!=0:
                        numTemp1 = numero1.pop()
                        numTemp2 = numero2.pop()
                        numTemp1=int(numTemp1)
                        numTemp2=int(numTemp2)
                        resTemp = numTemp1 + numTemp2
                        if resTemp>=9:
                            resTemp = [int(x) for x in str(resTemp)]
                            numTemp1=resTemp.pop()
                            numTemp2=resTemp.pop()
                            int(numTemp1)
                            int(numTemp2)
                            if longitud1!=0:
                                aux=numero1.pop()
                                numTemp2+=aux
                                numero1.append(str(numTemp2))
                                resultado.append(str(numTemp1))
                                longitud1-=1
                                longitud2-=1
                            else:
                                for i in range(longitud1):
                                    numTemp1 = numero1.pop()
                                    resultado.append(str(numTemp1)) 
                                    longitud1-=1
                                    longitud2-=1     
                        else:
                            resultado.append(str(resTemp))
                            longitud1-=1
                            longitud2-=1
                    elif longitud2==0 and longitud1>0:
                        resTemp=numero1.pop()
                        resultado.append(str(resTemp))
                        longitud1-=1
                else:
                    resTemp=numero1.pop()
                    resultado.append(str(resTemp))
                    longitud1-=1
            else:
                numTemp1 = numero1.pop()
                numTemp2 = numero2.pop()
                numTemp1=int(numTemp1)
                numTemp2=int(numTemp2)
                resTemp = numTemp1 + numTemp2
                if resTemp>9:
                    if longitud1!=0:
                        resTemp = [int(x) for x in str(resTemp)]
                        numTemp1=resTemp.pop()
                        int(numTemp1)
                        aux=numero1.pop()
                        numTemp2+=aux
                        numero1.append(str(numTemp2))
                        resultado.append(str(numTemp1))
                        longitud1-=1
                        longitud2-=1
                    else:
                        resultado.append(str(resTemp))  
                        longitud1-=1
                        longitud2-=1
                else:
                    resultado.append(str(resTemp))  
                    longitud1-=1
                    longitud2-=1                          
        resultado.reverse()
        print(resultado)
        resultado_final=resultado_final.join(resultado)
        return resultado_final