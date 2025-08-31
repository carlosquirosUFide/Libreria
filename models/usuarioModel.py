#Importar los módulos
from models.conexion import Conexion


class UsuarioModel:
    def listarUsuarios(self):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_listar_usuarios")
        usuarios = []
        for result in cursor.stored_results():
            usuarios.extend(result.fetchall())
        cursor.close()
        conexionBD.close()
        return usuarios
    
    def buscarUsuario(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_buscar_usuario",[id])
        for result in cursor.stored_results():
            usuario = result.fetchone() 
        cursor.close()
        conexionBD.close()
        return usuario
    
    def crearUsuario(self, nombreUsuario, apellidos, correo,contrasena, idRol):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_crear_usuario', [nombreUsuario, apellidos, correo, contrasena, idRol])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result

    def actualizarUsuario(self, id, nombreUsuario, apellidos, correo, id_rol):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_actualizar_usuario',[id, nombreUsuario, apellidos, correo, id_rol])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def eliminarUsuario(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)

        try:
            cursor.callproc('sp_eliminar_usuario',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        


            


