

from Conexion import *


class CClientes: #Escribimos la clase con CC (CClientes) para no confundir Class clientes con Clientes.py

    def mostrarClientes():

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute ("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado

        except mysql.connector.Error as error:
            print("Error al mostrar los datos {}".format(error))

    def ingresarClientes(nombres,apellidos,sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values (null,%s,%s,%s);" # el símbolo '%s' es un marcador de posición que será reemplazado por una cadena de caracteres
            valores = (nombres,apellidos,sexo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificarClientes(idUsuario,nombres,apellidos,sexo):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = ("UPDATE usuarios SET usuarios.nombres= %s,usuarios.apellidos = %s,usuarios.sexo = %swhere usuarios.id = %s ;")
            valores = (nombres,apellidos,sexo,idUsuario)
            # para poder ejecutar la conexión tenemos que dar la orden que dariamos en la bd y los valores a modificar
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount, "Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos {}".format(error))


    def eliminarClientes(idUsuario):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = ("Delete from usuarios where usuarios.id = %s ;")
            #Para poder eliminar los clientes tenemos que eliminar una tupla,np una lista, por lo cual el siguiente código se muuestra con la coma al final (valores = (idUsuario,))
            valores = (idUsuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount, "Registro eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos {}".format(error))


