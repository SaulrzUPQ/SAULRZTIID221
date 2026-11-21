from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la conexión
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'dbflask'
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

 
@app.route("/")
def home():
    return render_template("login.html")


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apaterno = request.form["apaterno"]
        amaterno = request.form["amaterno"]
        correo = request.form["correo"]
        password = request.form["password"]
        id_rol = request.form["id_rol"]
        password_hasheada = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE correo = %s", (correo,))

        if cursor.fetchone():
            cursor.close()
            flash("Ese correo ya está registrado")
            return render_template("login.html")

        cursor.execute(
            """INSERT INTO usuarios
               (nombre, apaterno, amaterno, correo, password, id_rol)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (nombre, apaterno, amaterno, correo, password_hasheada, id_rol)
        )
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for("home"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form["correo"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()
        sql = """
            SELECT
                usuarios.id,
                usuarios.nombre,
                usuarios.apaterno,
                usuarios.amaterno,
                usuarios.correo,
                usuarios.password,
                roles.nombre
            FROM usuarios
            INNER JOIN roles
                ON usuarios.id_rol = roles.id_rol
            WHERE usuarios.correo = %s
        """
        cursor.execute(sql, (correo,))
        usuario = cursor.fetchone()
        cursor.close()

        # usuario[5] es el hash de la contraseña
        if usuario and check_password_hash(usuario[5], password):
            session["id_ususario"] = usuario[0]
            session["nombre"] = usuario[1]
            session["rol"] = usuario[6]
            if session["rol"] == "Administrador":
                return redirect(url_for("Admin"))  # cambia por tu página principal
            return redirect(url_for("usurio"))

        return render_template("login.html")

    #ruta de admin
    @app.route ("/admin")
    def admin ():
        "si no hay session activa lo manda a login"
        return redirect (url_for("login"))
        if session.get("rol") != " Administrador":
            return "Acceso denegado"
        return render_template(
            "administrador.html",
            nombre=session["nombre"])
        

if __name__ == "__main__":
    app.run(port=5000, debug=True)