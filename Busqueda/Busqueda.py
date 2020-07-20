class Busqueda:
    def __init__(self,cursor,objetivo,lista):
        self.cursor = cursor
        self.objetivo = objetivo
        self.lista = lista

    @staticmethod    
    def busqueda(cursor,objetivo,lista):
        for i in range(164):
            palabra = ",".join(map(str,cursor[i]))
            if objetivo in palabra:
                palabra = palabra.split()
                lista.append(cursor[i])
        return lista
            