#Importar librerías
from models.conexion import Conexion

class HomeModel:
    def registroUsuario(self, nombreUsuario, apellidos, correo,contrasena):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_registro_usuario', [nombreUsuario, apellidos, correo, contrasena])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        

    def login(self, correo_electronico, contrasena):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_login", [correo_electronico, contrasena])
        usuarios = []
        for result in cursor.stored_results():
            fila = result.fetchone()
            if fila is not None:
                usuarios.append(fila)
        print(usuarios)
        cursor.close()
        conexionBD.close()
        return usuarios
    

    def cambiarContrasena(self, id, nuevaContrasena, contrasenaActual):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_cambiar_contrasena', [id, nuevaContrasena, contrasenaActual])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def buscarUsuarioCorreo(self, correo_electronico):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_buscar_usuario_correo", [correo_electronico])
        usuarios = []
        for result in cursor.stored_results():
            fila = result.fetchone()
            if fila is not None:
                usuarios.append(fila)
        cursor.close()
        conexionBD.close()
        return usuarios
    
    def recuperarAcceso(self, correo_electronico, contrasena):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_recuperar_acceso', [correo_electronico, contrasena])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        

