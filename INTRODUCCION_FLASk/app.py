#   Importamos los paquetes de flask
from flask import Flask, render_template, request
#importtamos las funciones para generar hashes de contraseñas y verificar contraseñas hasheadas
from werkzeug.security import generate_password_hash, check_password_hash   
#Creamos una instacia de nuestra aplicacion
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_BD'] = 'FlaskBD'
#permite que se recargue automaticamente la pagina cuando se realicen cambios en el codigo
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'mysecretkey'


#Creacion de ruta. La ruta/ es la raiz, sera la que se mostrara cuando el proyecto
@app.route("/")
def home():
    #estamos renderizando el archivo login.html que se encuentra en la carpeta templates
    return render_template("login.html")
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        # Procesar el formulario de registro    
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password_hash = request.form["password_hash"]
        id_rol = request.form["id_rol"]

        password_hashead = generate_password_hash(password_hash).encode('utf-8')  # Convertir a bytes

    return render_template("registro.html")

#Iniciamos el servidor FLASK en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000)