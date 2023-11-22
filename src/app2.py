from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

con=MySQL(app)

@app.route('/estudiante', methods=['GET'])
def listar_alumnos():
    try:
        cursor=con.connection.cursor()
        sql= "select * from alumno"
        cursor.execute(sql)
        datos=cursor.fetchall()
        listar_alumnos=[]
        for fila in datos:
            alum={'matricula': fila[0], 'nombre':fila[1], 'apaterno':[2], 'amaterno':[3], 'correo': fila[4]}
            listar_alumnos.append(alum)
        return jsonify({'alumnos':listar_alumnos, 'mensaje':'Lista de alumnos'})
    except Exception as ex:
        return jsonify({'mensaje':'error de conexion'})

def pagina_no_encontrada(error):
    return "<h1> PÁGINA NO ENCONTRADA ...</h1>", 404

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run() 
