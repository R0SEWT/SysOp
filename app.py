from flask import Flask
import consulta as q
from decouple import config
import pyodbc

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/consulta') 
def consulta():
    try:
        cnxn = q.getConexion(config)
        cursor = q.getCursor(cnxn)
        cursor = q.getTable(cursor, "Sexo")
        data = cursor.fetchall()
        print(f"Data: {data}")
        q.closeConexion(cnxn)
        return str(data) #convertir a string para que pueda ser retornado
        
    except Exception as e:
        print("Error en la consulta: ", e)
        return 'Consulta fallida'
