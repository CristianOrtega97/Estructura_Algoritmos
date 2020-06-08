class Funcion_For:
    def __init__(self,repeticion):
        self.repeticion = repeticion

    @staticmethod
    def funcion_for(repeticion):
        if repeticion == 0:
            pass

        else:
            print('Recursividad')
            return Funcion_For.funcion_for(repeticion-1)