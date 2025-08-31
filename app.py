from flask import Flask
from controllers.autorController import autorbp
from controllers.homeController import homebp
from controllers.categoriaController import categoriabp
from controllers.editorialController import editorialbp
from controllers.rolController import rolbp
from controllers.usuarioController import usuariobp

app = Flask(__name__)
app.secret_key = "mi-clave-secreta"

# Registrar controlador (blueprint)
app.register_blueprint(autorbp)
app.register_blueprint(homebp)
app.register_blueprint(categoriabp)
app.register_blueprint(editorialbp)
app.register_blueprint(rolbp)
app.register_blueprint(usuariobp)

if __name__ == "__main__":
    app.run(debug=True)