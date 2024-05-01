from flask import Blueprint, render_template, jsonify, request, session, flash
from decouple import config
import consulta as q
import send_mails as sm
import pyodbc
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

    # TODO: enviar un correo con los productos comprados
    usuario = session['usuario']
    email = session['email']
    cuerpo = f"Estimado {usuario} ha comprado los siguientes productos: \n"
    cuerpo += "Precio\t\tProducto\n"
    amout = 0
    for producto in data:
        cuerpo += f"{producto[1]}\t\t{producto[2]}\n"
        amout += producto[1]
    cuerpo += f"Total: {amout}\n"
    cuerpo += "Gracias por su compra\n"
    

    print(cuerpo)
    sm.send_email(config, email, "UPCtronix agradece tu compra", cuerpo)

    # TODO: guardar la compra en la base de datos
    
    
    # data son los productos comprados
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
    
    sql = "INSERT INTO Cliente (full_name, email, contrasena) VALUES (?, ?, ?)" # esto es un ejemplo, no se debe guardar la contraseña en texto plano
    # luego de hacer el registro, se debe redirigir al usuario a la página de logeo
    try:
        cursor.execute(sql, (nombre, email, password)) #luego de hacer el registro, se debe redirigir al usuario a la página de logeo
        cnxn.commit() # se debe hacer commit para guardar los cambios en la base de datos
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
    print(f"logenadose {datosLogeo}")

    email = datosLogeo['email']
    password = datosLogeo['password']

    sql = "SELECT full_name FROM cliente WHERE email = ? AND contrasena = ?"
    try:
        cursor.execute(sql, (email, password)) 
        usuario = cursor.fetchone() # fetchone() obtiene la primera fila de la consulta
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