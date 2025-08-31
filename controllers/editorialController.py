from flask import Blueprint, redirect, url_for, render_template, flash, request
from models.editorialModel import EditorialModel

editorialbp = Blueprint("editorial", __name__)

@editorialbp.route("/editorial/crear", methods = ['GET','POST'])
def crear():
    if request.method == 'POST':
        nombre_editorial = request.form['nombre_editorial']

        retorno = EditorialModel().crearEditorial(nombre_editorial)
        print(retorno)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('editorial.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo crear el editorial", "error"))
            return render_template("/editorial/crear.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/editorial/crear.html")

@editorialbp.route("/editorial/", methods=['GET', 'POST'])
def index():
    editoriales = EditorialModel().listarEditoriales()
    return render_template('/editorial/index.html',editoriales = editoriales)

@editorialbp.route("/editorial/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    editorial = EditorialModel().buscarEditorial(id)
    if request.method == 'POST':
        nombre_editorial = request.form['nombre_editorial']

        retorno = EditorialModel().actualizarEditorial(id, nombre_editorial)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('editorial.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo editar el editorial", "error"))
            return render_template("/editorial/editar.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/editorial/editar.html", editorial = editorial)

@editorialbp.route("/editorial/detalle/<int:id>")
def detalle(id):
    editorial = EditorialModel().buscarEditorial(id)
    return render_template('/editorial/detalle.html',editorial = editorial)

@editorialbp.route('/editorial/eliminar/<int:id>', methods=['GET','POST'])
def eliminar(id):
    editorial = EditorialModel().buscarEditorial(id)
    if request.method == 'POST':
        retorno = EditorialModel().eliminarEditorial(id)

        if retorno > 0:
            flash(("No se pudo eliminar el editorial", "error"))
            return redirect(url_for('editorial.index'))
        else:
            flash(("No se pudo eliminar el editorial", "error"))
            return render_template("/editorial/eliminar.html", editorial = editorial)
    return render_template("/editorial/eliminar.html", editorial = editorial)
    


