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
    
    def listarProductosCarrito(self, idUsuario):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True, dictionary=True)
        cursor.callproc("sp_listar_productos_carrito",[idUsuario])
        autores = []
        for result in cursor.stored_results():
            autores.extend(result.fetchall())
        cursor.close()
        conexionBD.close()
        return autores
    
    def eliminarProductoCarrito(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_eliminar_producto_carrito',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def aumentarCantidad(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_aumentar_cantidad_producto',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
        
    def disminuirCantidad(self, id):
        conexionBD = Conexion().abrirBD()
        cursor = conexionBD.cursor(buffered= True)
        try:
            cursor.callproc('sp_disminuir_cantidad_producto',[id])
            conexionBD.commit()
            result = cursor.rowcount
        except:
            result = 0
        finally:
            cursor.close()
            conexionBD.close()
            return result
    
