from flask import Blueprint, redirect, url_for, render_template, flash, request
from models.libroModel import LibroModel
from models.autorModel import AutorModel
from models.editorialModel import EditorialModel
from models.categoriaModel import CategoriaModel
from werkzeug.utils import secure_filename
import os
import uuid


FOLDER_IMG = 'static/img'


librobp = Blueprint("libro", __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@librobp.route("/libro", methods=['GET', 'POST'])
@librobp.route("/libro/", methods=['GET', 'POST'])
def index():
    libros = LibroModel().listarLibros()
    return render_template('/libro/index.html', libros = libros)


@librobp.route("/libro/crear", methods = ['GET','POST'])
def crear():
    autores = AutorModel().listarAutores()
    editoriales = EditorialModel().listarEditoriales()
    categorias = CategoriaModel().listarCategorias()
    if request.method == 'POST':
        precio = request.form['precio']
        nombre_libro = request.form['nombre_libro']
        cantidad = request.form['cantidad']
        autor = request.form['autor']
        editorial = request.form['editorial']
        categoria = request.form['categoria']
        imagen = request.files['url_imagen']
        url_imagen = None

        if imagen and  allowed_file(imagen.filename):
            filename = secure_filename(imagen.filename)
            unique_filename = str(uuid.uuid4()) + "_" + filename
            url_imagen = f"img/{unique_filename}"
            imagen.save(os.path.join(FOLDER_IMG, unique_filename))


        retorno = LibroModel().crearLibro(precio, nombre_libro, cantidad, autor, editorial, categoria, url_imagen)
        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('libro.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo crear el libro", "error"))
            return render_template("/libro/crear.html",
                                    autores = autores,
                                    editoriales = editoriales,
                                    categorias = categorias)

    # Si es GET, solo mostramos el formulario
    return render_template("/libro/crear.html",
                           autores = autores,
                           editoriales = editoriales,
                           categorias = categorias
                           )

@librobp.route("/libro/detalle/<int:id>")
def detalle(id):
    libro = LibroModel().buscarLibro(id)
    return render_template('/libro/detalle.html',libro = libro)

@librobp.route('/libro/eliminar/<int:id>', methods=['GET','POST'])
def eliminar(id):
    libro = LibroModel().buscarLibro(id)
    if request.method == 'POST':
        retorno = LibroModel().eliminarLibro(id)

        if retorno > 0:
            flash(("No se pudo eliminar el libro", "error"))
            return redirect(url_for('libro.index'))
        else:
            flash(("No se pudo eliminar el libro", "error"))
            return render_template("/libro/eliminar.html", libro = libro)
    return render_template("/libro/eliminar.html", libro = libro)


@librobp.route("/libro/editar/<int:id>", methods = ['GET','POST'])
def editar(id):
    libro = LibroModel().buscarLibro(id)
    autores = AutorModel().listarAutores()
    editoriales = EditorialModel().listarEditoriales()
    categorias = CategoriaModel().listarCategorias()
    if request.method == 'POST':
        precio = request.form['precio']
        nombre_libro = request.form['nombre_libro']
        cantidad = request.form['cantidad']
        autor = request.form['autor']
        editorial = request.form['editorial']
        categoria = request.form['categoria']
        url_imagen = None
        imagen = request.files['url_imagen']
        if imagen and allowed_file(imagen.filename):
            unique_filename = secure_filename(imagen.filename)
            url_imagen = f"img/{unique_filename}"
            imagen.save(os.path.join(FOLDER_IMG, unique_filename))
        retorno = LibroModel().actualizarLibro(id,  precio, cantidad, nombre_libro, autor, editorial, categoria, url_imagen)

        if retorno > 0:
            flash(("Datos guardados correctamente", "success"))
            return redirect(url_for('libro.index'))
        else:
            # Devuelve el template con un mensaje de error opcional
            flash(("No se pudo editar el libro", "error"))
            return render_template("/libro/editar.html",
                                   autores = autores,
                                   editoriales = editoriales,
                                   categorias = categorias,
                                   libro = libro)

    # Si es GET, solo mostramos el formulario
    return render_template("/libro/editar.html", 
                           libro = libro,
                           autores = autores,
                           editoriales = editoriales,
                           categorias = categorias)


