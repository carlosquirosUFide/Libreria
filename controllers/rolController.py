from flask import Blueprint, redirect, url_for, render_template, flash, request
from models.rolModel import RolModel

rolbp = Blueprint("rol", __name__)

@rolbp.route("/rol/crear", methods = ['GET','POST'])
def crear():
    if request.method == 'POST':
        nombre_rol = request.form['nombre_rol']

        retorno = RolModel().crearRol(nombre_rol)
        print(retorno)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('rol.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo crear el rol", "error"))
            return render_template("/rol/crear.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/rol/crear.html")

@rolbp.route("/rol/", methods=['GET', 'POST'])
def index():
    roles = RolModel().listarRoles()
    return render_template('/rol/index.html',roles = roles)

@rolbp.route("/rol/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    rol = RolModel().buscarRol(id)
    if request.method == 'POST':
        nombre_rol = request.form['nombre_rol']

        retorno = RolModel().actualizarRol(id, nombre_rol)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('rol.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo editar el rol", "error"))
            return render_template("/rol/editar.html")

    # Si es GET, solo mostramos el formulario
    return render_template("/rol/editar.html", rol = rol)

@rolbp.route("/rol/detalle/<int:id>")
def detalle(id):
    rol = RolModel().buscarRol(id)
    return render_template('/rol/detalle.html',rol = rol)

@rolbp.route('/rol/eliminar/<int:id>', methods=['GET','POST'])
def eliminar(id):
    rol = RolModel().buscarRol(id)
    if request.method == 'POST':
        retorno = RolModel().eliminarRol(id)

        if retorno > 0:
            flash(("No se pudo eliminar el rol", "error"))
            return redirect(url_for('rol.index'))
        else:
            flash(("No se pudo eliminar el rol", "error"))
            return render_template("/rol/eliminar.html", rol = rol)
    return render_template("/rol/eliminar.html", rol = rol)
    


