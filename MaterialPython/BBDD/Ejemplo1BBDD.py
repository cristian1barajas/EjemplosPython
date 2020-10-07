#!/usr/bin/env python
#_*_ coding: utf8 _*_

import sqlite3

miconexion = sqlite3.connect("PrimeraBase") # Creamos la conexión
miCursor = miconexion.cursor() # Crear cursor

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")


"""variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos) # Inserta varios items"""

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()
for producto in variosProductos:
    print(producto)

miconexion.commit()
miconexion.close() # Cerramos la conexión


