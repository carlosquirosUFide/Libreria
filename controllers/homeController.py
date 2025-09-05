from flask import Blueprint, redirect, url_for, render_template, flash, request, session
from models.libroModel import LibroModel
from models.homeModel import HomeModel


homebp = Blueprint("home", __name__)

@homebp.route("/", methods = ['GET','POST'])
def index():
    libros = LibroModel().listarLibros()
    return render_template("/home/index.html", libros = libros)

@homebp.route("/registro", methods = ['GET','POST'])
def registro():
        if request.method == 'POST':
            nombre_usuario = request.form['nombre_usuario']
            apellidos = request.form['apellidos']
            correo = request.form['correo_electronico']
            contrasena = request.form['contrasena']
            retorno = HomeModel().registroUsuario(nombre_usuario, apellidos, correo, contrasena)
            if retorno > 0:
                flash(("Datos guardados correctamente", "success"))
                return redirect(url_for('home.index'))
            else:
                # Devuelve el template con un mensaje de error opcional
                flash(("No se pudo crear el usuario", "error"))
                return render_template("/home/registro.html")
        return render_template('/home/registro.html')


@homebp.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
         correo = request.form['correo_electronico']
         contrasena = request.form['contrasena']

         retorno = HomeModel().login(correo, contrasena)

         if retorno.__len__()>0:
              flash("Datos ingresados con éxito", 'success')
              session['id_usuario'] = retorno[0]['id']
              session['id_rol'] = int(retorno[0]['id_rol'])
              session['nombre'] = retorno[0]['nombre'] + " " + retorno[0]['apellidos']
              return redirect(url_for('home.index'))
         else:
              flash("Los datos ingresados son incorrectos", 'error')
              return render_template('/home/login.html')
              
              
    # Si es GET, solo mostramos el formulario
    return render_template("/home/login.html")

@homebp.route("/cerrarSesion")
def cerrarSesion():
     session.clear()
     return redirect(url_for('home.index'))