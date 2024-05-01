from flask import Blueprint, render_template, jsonify, request, session, flash
from decouple import config
import consulta as q
import re

views = Blueprint('views', __name__)

def validar_correo(correo):
    # Expresión regular para validar un correo electrónico
    patron = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron, correo):
        return True
    else:
        return False

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/productos') 
def consulta():
    try:
        select = "id, name, precio, descripcion, img"  
        from_ = "Producto"
        data = q.getTable(config, select, from_)

    except Exception as e:
        print("Error en la consulta: ", e)
        return 'Consulta fallida'
    return render_template('productos.html', productos=data)

@views.route("/contactanos")
def contacto():
    return render_template("contacto.html")


@views.route("/comprar", methods=['POST'])
def comprar():

    if 'usuario' not in session:
        flash("Inicia sesión para poder realizar una compra", category="error")
        return jsonify({'mensaje': 'Usuario no autenticado'}), 401

    productos = request.json['ids']

    cnxn = q.getConexion(config)
    cursor = q.getCursor(cnxn)

    ids_str = ','.join(productos)

    sql = f"SELECT name, precio, descripcion, img FROM producto WHERE id IN ({ids_str})"

    cursor.execute(sql)
    data = cursor.fetchall()
    
    # data son los productos
    # session['email'] es el correo
    flash("Compra realizada con exito", category="success")
    return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    









@views.route("/sign-in")
def registro():
    return render_template('sign-in.html')

@views.route("/log-in")
def logeo():
    return render_template('log-in.html')

@views.route("/envioRegistroUsuario", methods=['POST'])
def registroUsuario():
    cnxn = q.getConexion(config)
    cursor = q.getCursor(cnxn)

    datosUsuario = request.json
    
    nombre = datosUsuario['nombre']
    email = datosUsuario['email']
    password = datosUsuario['password']

    error = False
    if not validar_correo(email):
        flash("Correo invalido", category='error')
        error = True
    if nombre == "":
        flash("Completa tu nombre", category='error')
        error = True
    if password == "":
        flash("Completa tu contraseña", category='error')
        error = True
    if error:
        return jsonify({'mensaje': 'Registro invalido'}), 401
    
    sql = "INSERT INTO Cliente (full_name, email, contra) VALUES (?, ?, ?)"
    try:
        cursor.execute(sql, (nombre, email, password))
        cnxn.commit()
    except Exception as e:
        flash('Error al crear usuario', category='error')
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401
    finally:
        q.closeConexion(cnxn)

    
    flash("Registro realizado con exito", category='success')
    return jsonify({'mensaje': 'Registro realizado con exito'}), 200
    

@views.route("/autentificacion", methods=['POST'])
def autentificacion():    
    cnxn = q.getConexion(config)
    cursor = q.getCursor(cnxn)

    datosLogeo = request.json

    email = datosLogeo['email']
    password = datosLogeo['password']

    sql = "SELECT full_name FROM cliente WHERE email = ? AND contra = ?"
    try:
        cursor.execute(sql, (email, password))
        usuario = cursor.fetchone()
    except Exception as e:
        print("error")
    finally:
        q.closeConexion(cnxn)

    if usuario:
        session['email'] = email
        session['usuario'] = usuario[0] 
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    else:
        flash('Credenciales incorrectas', category='error')
        return jsonify({'mensaje': 'Credenciales incorrectas'}), 401
    
@views.route("/log-out", methods=['POST'])
def cerrar():
    session.clear()
    return '',204