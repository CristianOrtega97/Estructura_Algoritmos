class Palindromo:
    def __init__(self,frase,primera_pos,ultima_pos):
        self.frase = frase
        self.primera_pos = primera_pos
        self.ultima_pos = ultima_pos

    @staticmethod
    def palindromo(frase,primera_pos,ultima_pos):
        if len(frase) < 1:
            return True
        else: 
            return "Nada"