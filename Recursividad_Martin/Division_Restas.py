class Division_Restas:
    def __init__(self,numero,veces):
        self.numero = numero
        self.veces = veces

    @staticmethod    
    def division_restas(numero,veces):
        if numero == 0:
            return 0
        else:
            return 1 + Division_Restas.division_restas(numero-veces,veces)