from flask import Blueprint, redirect, url_for, render_template, flash, request, session, jsonify
from models.carritoModel import CarritoModel
from models.libroModel import LibroModel

carritobp = Blueprint("carrito", __name__)

@carritobp.route("/carrito/", methods=['GET', 'POST'])
def index():
    idUsuario = session['id_usuario']
    carrito = CarritoModel().listarProductosCarrito(idUsuario)
    return render_template('/carrito/index.html',carrito = carrito)

@carritobp.route("/carrito/agregarProductos", methods = ['POST'])
def agregar():
    libros = LibroModel().listarLibros()
    if request.method == "POST":
        if session.get('id_usuario') is None:
            # Si es AJAX, devolver JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({"success": False, "message": "Debe iniciar sesión para agregar productos al carrito"}), 401
            else:
                flash("Debe iniciar sesión para agregar productos al carrito", 'error')
                return render_template("/home/index.html", libros=libros)

        idUsuario = session['id_usuario']
        idLibro = request.form['id_libro']
        cantidad = request.form['cantidad']
        monto = request.form['monto']

        retorno = CarritoModel().agregarProductos(idUsuario, idLibro, monto, cantidad)

        if retorno > 0:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({"success": True, "message": "Producto agregado al carrito"})
            else:
                return render_template("/home/index.html", libros=libros)
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({"success": False, "message": "Error al agregar productos al carrito"}), 400
            else:
                flash("Error al agregar productos al carrito", "error")
                return render_template("/home/index.html", libros=libros)


@carritobp.route('/carrito/eliminar/<id>')
def eliminar(id):
    retorno = CarritoModel().eliminarProductoCarrito(id)
    if retorno > 0:
        return redirect(url_for('carrito.index'))
    else:
        flash("No se ha podido eliminar el producto del carrito", 'error')
        return redirect(url_for('carrito.index'))

@carritobp.route('/carrito/aumentar-cantidad/<id>')
def aumentarCantidad(id):
    retorno = CarritoModel().aumentarCantidad(id)

    if retorno > 0:
        return redirect(url_for('carrito.index'))
    else:
        flash("No se ha podido eliminar el producto del carrito", 'error')
        return redirect(url_for('carrito.index'))
    
@carritobp.route('/carrito/disminuir-cantidad/<id>')
def disminuirCantidad(id):
    retorno = CarritoModel().disminuirCantidad(id)

    if retorno > 0:
        return redirect(url_for('carrito.index'))
    else:
        flash("No se ha podido eliminar el producto del carrito", 'error')
        return redirect(url_for('carrito.index'))
    