from flask import Blueprint, redirect, url_for, render_template, flash, request, render_template_string
from models.usuarioModel import UsuarioModel
from models.rolModel import RolModel
from models.comunesModel import ComunesModel


usuariobp = Blueprint("usuario", __name__)

@usuariobp.route("/usuario/crear", methods = ['GET','POST'])
def crear():

    roles = RolModel().listarRoles()
    if request.method == 'POST':
        nombre_usuario = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo_electronico']
        contrasena = ComunesModel().generarContrasena()
        idRol = request.form['rol']
        retorno = UsuarioModel().crearUsuario(nombre_usuario, apellidos, correo, contrasena, idRol)

        html = render_template(
            "creacionUsuario.html",
            nombre=nombre_usuario+" "+apellidos,
            correo=correo,
            contrasena=contrasena,
            anio = 2025,
            empresa = "Librería Nueva Década"
        )

        # Ahora html ya tiene el nombre reemplazado
        ComunesModel().enviar_correo_html(
            destinatario= correo,
            asunto="Creación de Cuenta en el Sistema de Librería Nueva Década",
            html_contenido=html
        )

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('usuario.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo crear el usuario", "error"))
            return render_template("/usuario/crear.html", roles = roles)

    # Si es GET, solo mostramos el formulario
    return render_template("/usuario/crear.html", roles = roles)

@usuariobp.route("/usuario/", methods=['GET', 'POST'])
def index():
    usuarios = UsuarioModel().listarUsuarios()
    return render_template('/usuario/index.html',usuarios = usuarios)

@usuariobp.route("/usuario/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    roles = RolModel().listarRoles()
    usuario = UsuarioModel().buscarUsuario(id)
    if request.method == 'POST':

        nombre_usuario = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo_electronico']
        idRol = request.form['rol']

        retorno = UsuarioModel().actualizarUsuario(id, nombre_usuario, apellidos, correo, idRol)
        print(retorno)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('usuario.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo editar el usuario", "error"))
            return render_template("/usuario/editar.html", usuario = usuario, roles = roles)

    # Si es GET, solo mostramos el formulario
    return render_template("/usuario/editar.html", usuario = usuario, roles = roles)

@usuariobp.route("/usuario/detalle/<int:id>")
def detalle(id):
    usuario = UsuarioModel().buscarUsuario(id)
    return render_template('/usuario/detalle.html',usuario = usuario)

@usuariobp.route('/usuario/eliminar/<int:id>', methods=['GET','POST'])
def eliminar(id):
    usuario = UsuarioModel().buscarUsuario(id)
    roles = RolModel().listarRoles()
    if request.method == 'POST':
        retorno = UsuarioModel().eliminarUsuario(id)

        if retorno > 0:
            flash(("Usuario Eliminado con Éxito", "success"))
            return redirect(url_for('usuario.index'))
        else:
            flash(("No se pudo eliminar el usuario", "error"))
            return render_template("/usuario/eliminar.html", usuario = usuario, roles = roles)
    return render_template("/usuario/eliminar.html", usuario = usuario, roles = roles)
    


