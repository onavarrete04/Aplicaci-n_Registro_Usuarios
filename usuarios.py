# Base de datos, motor mysql 

import mysql.connector

class Usuario:

    def abrir(self):
        conexion = mysql.connector.connect(host="localhost",
                                           user="root",
                                           passwd = "on7760284",
                                           database="bd2")
        return conexion
    def añadir_usuario(self,datos):
        cone = self.abrir()
        miCursor = cone.cursor()
        
        sql="insert into usuarios(nombre, nacionalidad, estancia, producto) values (%s,%s,%s,%s)"
            
        miCursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def ver_usuario(self,datos):
        cone = self.abrir()
        miCursor = cone.cursor()
        sql = "select nombre, nacionalidad, estancia, producto from usuarios where codigo = (%s)"
        miCursor.execute(sql,datos)
        consulta = miCursor.fetchall()
        
        cone.close()
        return consulta

    def recuperar_todo(self):
        cone = self.abrir()
        miCursor = cone.cursor()
        sql = "select * from usuarios"
        miCursor.execute(sql)
        consulta = miCursor.fetchall()
        
        cone.close()
        return consulta

    def borrar_usuario(self,datos):
        cone = self.abrir()
        miCursor = cone.cursor()
        sql = "delete from usuarios where codigo = %s"
        miCursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def modificar_usuario(self,datos):
        cone = self.abrir()
        miCursor = cone.cursor()
        sql = "update usuarios set nombre=%s, nacionalidad=%s, estancia =%s, producto=%s  where codigo=%s"
        miCursor.execute(sql,datos)
        respuesta = miCursor.rowcount
        cone.commit()
        cone.close()

        return respuesta



"""

use bd2; 

create table `usuarios`(
    `codigo` int primary key auto_increment,
    `nombre` varchar(30),
    `nacionalidad` varchar(30),
    `estancia` int,
    `producto` varchar(30)
)

"""
