#Importar los módulos
from models.conexion import Conexion

class EditorialModel:
    def listarEditoriales(self):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_listar_editoriales")
        editoriales = []
        for result in cursor.stored_results():
            editoriales.extend(result.fetchall())
        cursor.close()
        conexionBD.close()
        return editoriales
    
    def buscarEditorial(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_buscar_editorial",[id])
        for result in cursor.stored_results():
            editorial = result.fetchone() 
        cursor.close()
        conexionBD.close()
        return editorial
    
    def crearEditorial(self, nombreEditorial):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_crear_editorial', [nombreEditorial])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result

    def actualizarEditorial(self, id, nombreEditorial):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)
        try:
            cursor.callproc('sp_actualizar_editorial',[id, nombreEditorial])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def eliminarEditorial(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered=True)

        try:
            cursor.callproc('sp_eliminar_editorial',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        

result = EditorialModel().eliminarEditorial(1)
print(result)

