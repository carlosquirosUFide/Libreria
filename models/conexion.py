#Importación de Módulos
from mysql import connector

#Clase Conexión
class Conexion:
    #Método para conectarse con la base de datos.
    def abrirBD(self):
        result = connector.connect(
            host = "localhost",
            user = "root",
            passwd = "lm1030.A",
            database = "libreria")
        return result
            
