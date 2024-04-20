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
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)

# Se establece la conexión
try:
    cursor = cnxn.cursor() # Pa ejecutar comandos SQL
except Exception as e:
    print("Error al crear el cursor: ", e)

# Consultitas

cursor.execute("SELECT * FROM Sexo")
for row in cursor:
    print(row)