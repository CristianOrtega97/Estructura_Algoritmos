import pyodbc

class Connection:
    def __init__(self,conn):
        self.conn = conn

    @staticmethod    
    def read (conn):
        print("Read is completed")
        cursor = conn.cursor()
        cursor.execute("select lineas_nombre,lineas_lineasId,lineas_lineasEstacion from lineas_tren")
        return list(cursor.fetchall())