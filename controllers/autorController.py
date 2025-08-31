from flask import Blueprint, redirect, url_for, render_template, flash, request
from models.autorModel import AutorModel

autorbp = Blueprint("autor", __name__)

@autorbp.route("/autor/crear", methods = ['GET','POST'])
def crear():
    if request.method == 'POST':
        nombre_autor = request.form['nombre_autor']

        retorno = AutorModel().crearAutor(nombre_autor)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('autor.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo crear el autor", "error"))
            return render_template("/autor/crear.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/autor/crear.html")

@autorbp.route("/autor/", methods=['GET', 'POST'])
def index():
    autores = AutorModel().listarAutores()
    return render_template('/autor/index.html',autores = autores)

@autorbp.route("/autor/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    autor = AutorModel().buscarAutor(id)
    if request.method == 'POST':
        nombre_autor = request.form['nombre_autor']

        retorno = AutorModel().actualizarAutor(id, nombre_autor)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('autor.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo editar el autor", "error"))
            return render_template("/autor/editar.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/autor/editar.html", autor = autor)

@autorbp.route("/autor/detalle/<int:id>")
def detalle(id):
    autor = AutorModel().buscarAutor(id)
    return render_template('/autor/detalle.html',autor = autor)

@autorbp.route('/autor/eliminar/<int:id>', methods=['GET','POST'])
def eliminar(id):
    autor = AutorModel().buscarAutor(id)
    if request.method == 'POST':
        retorno = AutorModel().eliminarAutor(id)

        if retorno > 0:
            flash(("No se pudo eliminar el autor", "error"))
            return redirect(url_for('autor.index'))
        else:
            flash(("No se pudo eliminar el autor", "error"))
            return render_template("/autor/eliminar.html", autor = autor)
    return render_template("/autor/eliminar.html", autor = autor)
    


