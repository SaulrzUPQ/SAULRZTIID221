#LIBRERIAS
from tkinter import INSERT
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["Templates_AUTO_RELOAD"]= True

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'crud_albums'

app.secret_key = 'mysecretkey'
mysql = MySQL(app)


@app.route("/")
def index(): 

    con = mysql.connection.cursor()
    con.execute("SELECT * FROM tb_albums")
    conPeliculas = con.fetchall()
    print(conPeliculas)
    return render_template("index.html",listPeliculas = listPeliculas)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        director = request.form['txtDirector']
        anio = request.form['txtAnio']
        print(titulo, director, anio)


        con= mysql.connection.cursor()
        con.execute('INSERT INTO tb_albums (titulo, director, anio) VALUES (%s, %s, %s)', (titulo, director, anio))
        mysql.connection.commit()

    flash('los datos llegaron correctamente')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)


        
