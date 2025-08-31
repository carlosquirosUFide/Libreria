#Importar los módulos
from models.conexion import Conexion

class LibroModel:
    def listarLibros(self):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_listar_libros")
        libros = []
        for result in cursor.stored_results():
            libros.extend(result.fetchall())
        cursor.close()
        conexionBD.close()
        return libros
    
    def crearLibro(self, precio, cantidad, nombreLibro, id_autor, id_editorial, id_categoria, url_imagen):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_crear_libro', [precio, nombreLibro, cantidad,id_autor,id_editorial, id_categoria, url_imagen])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result

    def actualizarLibro(self, id,  precio, cantidad, nombreLibro, id_autor, id_editorial, id_categoria, url_imagen):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_actualizar_libro',[id, precio, cantidad, nombreLibro, id_autor, id_editorial, id_categoria, url_imagen])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def eliminarLibro(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)

        try:
            cursor.callproc('sp_eliminar_libro',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result


