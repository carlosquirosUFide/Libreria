from flask import Blueprint, redirect, url_for, render_template, flash, request
from models.libroModel import LibroModel


homebp = Blueprint("home", __name__)

@homebp.route("/", methods = ['GET','POST'])
def index():
    libros = LibroModel().listarLibros()
    return render_template("/home/index.html", libros = libros)