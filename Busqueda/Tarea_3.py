import pyodbc
from Quicksort import *
from Connection import *
import numpy

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-9RE9NR7;"
    "Database=Tarea3;"
    "Trusted_Connection=yes;"
)

cursor = Connection.read(conn)

lista=[('la paz', 1,15),('Escultura',1,26)]
Quicksort.sort(lista)
print(lista)

Quicksort.sort(cursor)
print(cursor)