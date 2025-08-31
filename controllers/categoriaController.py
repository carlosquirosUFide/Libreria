from flask import Blueprint, redirect, url_for, render_template, flash, request
from models.categoriaModel import CategoriaModel

categoriabp = Blueprint("categoria", __name__)

@categoriabp.route("/categoria/crear", methods = ['GET','POST'])
def crear():
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']

        retorno = CategoriaModel().crearCategoria(nombre_categoria)
        print(retorno)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('categoria.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo crear el categoria", "error"))
            return render_template("/categoria/crear.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/categoria/crear.html")

@categoriabp.route("/categoria/", methods=['GET', 'POST'])
def index():
    categorias = CategoriaModel().listarCategorias()
    return render_template('/categoria/index.html',categorias = categorias)

@categoriabp.route("/categoria/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    categoria = CategoriaModel().buscarCategoria(id)
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']

        retorno = CategoriaModel().actualizarCategoria(id, nombre_categoria)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('categoria.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo editar el categoria", "error"))
            return render_template("/categoria/editar.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/categoria/editar.html", categoria = categoria)

@categoriabp.route("/categoria/detalle/<int:id>")
def detalle(id):
    categoria = CategoriaModel().buscarCategoria(id)
    return render_template('/categoria/detalle.html',categoria = categoria)

@categoriabp.route('/categoria/eliminar/<int:id>', methods=['GET','POST'])
def eliminar(id):
    categoria = CategoriaModel().buscarCategoria(id)
    if request.method == 'POST':
        retorno = CategoriaModel().eliminarCategoria(id)

        if retorno > 0:
            flash(("No se pudo eliminar el categoria", "error"))
            return redirect(url_for('categoria.index'))
        else:
            flash(("No se pudo eliminar el categoria", "error"))
            return render_template("/categoria/eliminar.html", categoria = categoria)
    return render_template("/categoria/eliminar.html", categoria = categoria)
    


