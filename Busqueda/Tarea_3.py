import pyodbc
from Quicksort import *
from Connection import *
import numpy
from Busqueda import *

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-9RE9NR7;"
    "Database=Tarea3;"
    "Trusted_Connection=yes;"
)

cursor = Connection.read(conn)
Quicksort.sort(cursor)

objetivo = input("Ingresar Valor a Buscar: ")
lista = []
lista = Busqueda.busqueda(cursor,objetivo,lista)
if not lista:
    print("No existe ninguna coincidencia")

if lista:
    print("Coincidencias: ")
    print("")
    print(lista)

