class Division_Restas:
    def __init__(self,numero,resta,veces):
        self.numero = numero
        self.resta = resta
        self.veces = veces

    @staticmethod    
    def division_restas(numero,resta,veces):
        if numero < resta:
            return print('El resultado de la división es: ',veces)
        else:
            return Division_Restas.division_restas(numero-resta,resta,veces+1)