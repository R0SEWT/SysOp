#pip install pyodbc
import pyodbc
from decouple import config

# instalar el ODBC Driver 18 for SQL Server
# pyoobc es un paquete que permite la conexión 
# a bases de datos SQL Server usando ODBC

'''
    Conexión a la base de datos de Azure
    Se debe tener instalado el driver de ODBC para SQL Server
    Driver={ODBC Driver 18 for SQL Server};
    Server=tcp:sv-upctronix.database.windows.net,1433;
    Database=Upctronix;
    Uid=rosewt;
    Pwd={your_password_here};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;

'''


def getConexion(config): 
    try:
        server = config('server')
        database = config('database')
        username = config('user') 
        port = config('port')
        password = config('pass')
        driver= config('driver')
    except Exception as e: 
        print("Error al cargar .env: ", e)
    try:
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        print("Conexión exitosa")
        return cnxn
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
        return None

def getCursor(cnxn):
    try:
        cursor = cnxn.cursor()
        print("Cursor creado")
        return cursor
    except Exception as e:
        print("Error al crear el cursor: ", e)
        return None
    

def closeConexion(cnxn):
    try:
        cnxn.close()
        print("Conexión cerrada")
    except Exception as e:
        print("Error al cerrar la conexión: ", e)

def getTable(cursor, table):
    try:
        cursor.execute("SELECT * FROM "+table)
        print(f"Tabla {table} consultada")
        return cursor 
    except Exception as e:
        print("Error al consultar la tabla: ", e)
        return None


'''cnxn = getConexion(config)
cursor = getCursor(cnxn)
cursor = getTable(cursor, "Sexo")
closeConexion(cnxn)
'''