#Importar librerías
from models.conexion import Conexion

class RolModel:
    def listarRoles(self):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(dictionary=True)
        cursor.callproc('sp_listar_roles')
        roles = []
        for resultado in cursor.stored_results():
            roles.extend(resultado.fetchall())
        cursor.close()
        conexionBD.close()
        return roles
    
    def buscarRol(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_buscar_rol",[id])
        for result in cursor.stored_results():
            rol = result.fetchone() 
        cursor.close()
        conexionBD.close()
        return rol
    
    def crearRol(self, nombreRol):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_crear_rol',[nombreRol])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
        return result
    
    def eliminarRol(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_eliminar_rol',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
    def actualizarRol(self, id, nombreRol):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_actualizar_rol',[id, nombreRol])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result


