from flask import Blueprint, render_template
from decouple import config
import pyodbc
import consulta as q

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/productos') 
def consulta():
    try:
        cnxn = q.getConexion(config)
        cursor = q.getCursor(cnxn)
        data = cursor.execute("Select name, precio, descripcion from Producto")
        print(f"Data: {data}")
        q.closeConexion(cnxn)#convertir a string para que pueda ser retornado
        
    except Exception as e:
        print("Error en la consulta: ", e)
        return 'Consulta fallida'
    return render_template('productos.html', productos=data)

@views.route("/sign-in")
def conectarse():
    return render_template('sign-in.html')

@views.route("/log-in")
def registro():
    return render_template('log-in.html')


@views.route("/contactanos")
def contacto():
    return render_template("contacto.html")