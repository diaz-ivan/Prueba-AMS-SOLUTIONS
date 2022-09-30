import sqlite3
from datetime import datetime, timedelta

conexion = sqlite3.connect("Ejercicio1.db")
cursor = conexion.cursor()

#Mostrar una fila de un libro
def mostrar_valor():

        id_libro = int(input("Ingrese el ID del libro: "))
        cursor.execute("SELECT * FROM Libros WHERE LibroID={}".format(id_libro))
        datos = cursor.fetchall()

        conexion.close()
        print(datos)


#Actulizar precio del libro y fecha de edición
def costoUpdate(id_libro):

        nuevoPrecio = int(input("Ingrese el nuevo precio: "))
        fecha = input("Ingerese la fecha de edición (DD/MM/YYYY): ")

        fechaEdicion = datetime.strptime(fecha, '%d/%m/%Y').date()

        sql = '''UPDATE Libros SET Costo={} ,FechaEdicion="{}" WHERE LibroID={}'''.format(nuevoPrecio, fechaEdicion, id_libro)

        cursor.execute(sql)

        print("¡¡Cambios actualizados con éxito!!")

        conexion.commit()

        backupCosto(id_libro)

def backupCosto(id_libro):

        datos = cursor.execute('''SELECT * FROM Libros WHERE LibroID={}'''.format(id_libro))
        for dato in datos:
            dato=dato
        precio = dato[5]

        if precio > 3:

                id_libro = dato[0]
                fechaCambio = datetime.now().date()
                #fechaHoy = fechaCambio.strftime("%d-%m-%Y")

                cursor.execute('''INSERT or IGNORE INTO HistoricoCostos (LibroID, FechaCambio) VALUES ({},{})'''.format(id_libro, fechaCambio))
                print("¡¡Backup realizado con éxito!!")
                conexion.commit()
                conversionPesetas(dato[5], id_libro)

def conversionPesetas(costo,id_libro):

        pesetas = int(costo*166)

        fecha = cursor.execute('''SELECT FechaEdicion FROM Libros WHERE LibroID={}'''.format(id_libro))
        for fechaEdicion in fecha:
                fechaEdicion=fechaEdicion

        mesActual = datetime.today()
        anoAnterior = [mesActual.year] + [mesActual.month]
        anoAnterior = tuple(anoAnterior)

        if (anoAnterior) == (fechaEdicion) and costo == 5:

                cursor.execute('''UPDATE HistoricoCostos SET CostoPesetas={},  WHERE LibroID={}'''.format(pesetas, id_libro))

                conexion.commit()
                conexion.close()
        else:
                conexion.close()





#mostrar_valor()

costoUpdate(10)

#backupCosto(2)
