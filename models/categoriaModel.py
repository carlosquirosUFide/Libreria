#Importar librerías
from models.conexion import Conexion

class CategoriaModel:
    def listarCategorias(self):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(dictionary=True)
        cursor.callproc('sp_listar_categorias')
        categorias = []
        for resultado in cursor.stored_results():
            categorias.extend(resultado.fetchall())
        cursor.close()
        conexionBD.close()
        return categorias
    
    def buscarCategoria(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_buscar_categoria",[id])
        for result in cursor.stored_results():
            categoria = result.fetchone() 
        cursor.close()
        conexionBD.close()
        return categoria
    
    def crearCategoria(self, nombreCategoria):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_crear_categoria',[nombreCategoria])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
        return result
    
    def eliminarCategoria(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_eliminar_categoria',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
    def actualizarCategoria(self, id, nombreCategoria):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_actualizar_categoria',[id, nombreCategoria])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result


