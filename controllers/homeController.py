from flask import Blueprint, redirect, url_for, render_template, flash, request, session, jsonify
from models.libroModel import LibroModel
from models.homeModel import HomeModel
from models.usuarioModel import UsuarioModel
from models.comunesModel import ComunesModel
from models.carritoModel import CarritoModel


homebp = Blueprint("home", __name__)

@homebp.route("/", methods=['GET', 'POST'])
def index():
    libros = LibroModel().listarLibros()
    return render_template("/home/index.html", libros=libros)

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

@homebp.route('/perfil/<int:id>')
def perfil(id):
     usuario = UsuarioModel().buscarUsuario(id)
     return render_template('/home/perfil.html', usuario = usuario)

@homebp.route('/editarPerfil/<int:id>', methods = ['GET', 'POST'])
def editarPerfil(id):
     
     usuario = UsuarioModel().buscarUsuario(id)

     if request.method == "POST":
          #Extraemos los datos del formulario
          nombre_usuario = request.form['nombre']
          apellidos = request.form['apellidos']
          correo = request.form['correo_electronico']
          idRol = session['id_rol']
          
          #Llamamos al modelo
          retorno = UsuarioModel().actualizarUsuario(id, nombre_usuario, apellidos, correo, idRol)
          if retorno > 0:
               flash("Perfil editado con éxito", 'success')
               return redirect(url_for('home.perfil', id=id))
          else:
               flash('Error en la edición del perfil', 'error')
               return render_template('/home/editarPerfil.html', usuario = usuario)

     return render_template('/home/editarPerfil.html', usuario = usuario)

@homebp.route("/cambiarContrasena", methods = ['GET','POST'])
def cambiarContrasena():
        if request.method == 'POST':
            contrasenaActual = request.form['contrasenaActual']
            nuevaContrasena = request.form['contrasenaNueva']
            confirmacionContrasena = request.form['contrasenaConfirmacion']
            id = session['id_usuario']

            if nuevaContrasena != confirmacionContrasena:
                 flash('Las contraseñas ingresadas no coinciden','error')
                 return render_template('/home/cambiarContrasena.html')
            elif contrasenaActual == nuevaContrasena:
                 flash('Las nueva contraseña ingresada es igual a la contraseña actual','error')
                 return render_template('/home/cambiarContrasena.html')
            else:
               retorno = HomeModel().cambiarContrasena(id, nuevaContrasena, contrasenaActual)
               if retorno > 0:
                    flash(("Datos guardados correctamente", "success"))
                    return redirect(url_for('home.index'))
               else:
                    # Devuelve el template con un mensaje de error opcional
                    flash(("La contraseña actual no es correcta", "error"))
                    return render_template("/home/cambiarContrasena.html")
        return render_template('/home/cambiarContrasena.html')

@homebp.route('/recuperarAcceso', methods = ['POST','GET'])
def recuperarAcceso():
     if request.method == "POST":
          correo = request.form['correo_electronico']
          usuario = HomeModel().buscarUsuarioCorreo(correo)

          if usuario.__len__() > 0:

               contrasena = ComunesModel().generarContrasena()

               html = render_template('/correo/recuperarAcceso.html',
                                   nombre=usuario[0]['nombre']+" "+usuario[0]['apellidos'],
                                   correo=correo,
                                   contrasena=contrasena,
                                   anio = 2025,
                                   empresa = "Librería Nueva Década")

               retorno = HomeModel().recuperarAcceso(correo, contrasena)

               ComunesModel().enviar_correo_html(correo, 'Recuperación Acceso', html)

               if retorno > 0:
                    return redirect(url_for('home.login'))
               else:
                    flash('Error al recuperar acceso')
                    return render_template('/home/recuperarAcceso.html')


          else:
               flash('El correo ingreseado no se encontró en el sistema', 'error')
               return render_template('/home/recuperarAcceso.html')

     return render_template('/home/recuperarAcceso.html')
    
               
          
          
     
          
     