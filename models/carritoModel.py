from models.conexion import Conexion

class CarritoModel:
    def agregarProductos(self, idUsuario, idProducto, monto, cantidad):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_agregar_productos_carritos',[idUsuario, idProducto, monto, cantidad])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
        return result
    
