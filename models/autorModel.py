#Importar los módulos
from models.conexion import Conexion

class AutorModel:
    def listarAutores(self):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_listar_autores")
        autores = []
        for result in cursor.stored_results():
            autores.extend(result.fetchall())
        cursor.close()
        conexionBD.close()
        return autores
    
    def buscarAutor(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_buscar_autor",[id])
        for result in cursor.stored_results():
            autor = result.fetchone() 
        cursor.close()
        conexionBD.close()
        return autor
    
    def crearAutor(self, nombreAutor):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_crear_autor', [nombreAutor])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result

    def actualizarAutor(self, id, nombreAutor):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_actualizar_autor',[id, nombreAutor])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def eliminarAutor(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)

        try:
            cursor.callproc('sp_eliminar_autor',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result


