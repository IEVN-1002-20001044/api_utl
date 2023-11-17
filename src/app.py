

from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

@app.route('/') #esto se conoce como decorador
def index():
    grupo="IEVN1002"
    lista=["IEVN1001", "IEVN1002", "IEVN1003"]
    return render_template('index.html', grupo=grupo, lista=lista)

@app.route('/hola') #nueva ruta
def hola():
    return 'Saludo utl'

@app.route('/user/<string:nombre>') #nueva ruta con metodo string
def user(nombre):
    return 'Saludo {0}'.format(nombre)

@app.route('/user/<int:n1>') #nueva ruta con metodo int
def user1(n1):
    return 'El número es: {}'.format(n1)

@app.route('/user/<int:id>/<string:nom>') #nueva ruta con pase de dos parametros de diferente tipo
def user2(id, nom):
    return 'ID: {0} - NOMBRE: {1}'.format(id, nom) #posición de las variables

@app.route('/suma/<float:n1>/<float:n2>') #suma
def suma(n1, n2):
    return 'La suma es: {}'.format(n1+n2)


@app.route('/alumnos/') #ruta para pag de alumnos
def alumnos():
    return render_template('alumnos.html')

@app.route('/default/') #ruta de dos forma, con y sin parametro que se puede cambiar
@app.route('/rutaigual/<string:dd>')
def default(dd='hanjisung'): #valor por default
    return '<h1>El nombre es: {} </h1>'.format(dd)

if __name__ == "__main__":
    app.run(debug=True) #activar deporación/actualización en tiempo real