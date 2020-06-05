class Palindromo:
    def __init__(self,frase,primera_pos,ultima_pos):
        self.frase = frase
        self.primera_pos = primera_pos
        self.ultima_pos = ultima_pos

    @staticmethod
    def palindromo(frase,primera_pos,ultima_pos):
        if primera_pos == ultima_pos:
            return True
        elif primera_pos == ultima_pos+1:
            return True
        else: 
            aux1 = frase[primera_pos]
            aux2 = frase[ultima_pos]
            frase[primera_pos] = aux2
            frase[ultima_pos] = aux1
            return Palindromo.palindromo(frase, primera_pos + 1,ultima_pos-1)