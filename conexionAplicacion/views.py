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
        # DEV NOTE:
        # las tablas estan en databse/tablas (ahi puesde revisar las tablas y los nombres de los campos)
         
        # SELECT name, precio, descripcion FROM Producto
        select = "name, precio, descripcion"  
        from_ = "Producto"
        
        data = q.getTable(config, select, from_) 
        
    except Exception as e:
        print("Error en la consulta: ", e)
        return 'Consulta fallida'
    
    print(f"Data consultada con exito")
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