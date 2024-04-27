from email.message import EmailMessage
import smtplib


def send_email(config, rem, dest, asunto, cuerpo):
    try:
        smtp_user = config["SMTP_USER"]
        smtp_pass = config["SMTP_PASS"]
    except Exception as e:
        print(f"Error de al leer las claves SMTP: {e}")
        return False

    # inicializacion del email
    try:
        email = EmailMessage()
        email["From"] = rem
        email["To"] = dest
        email["Subject"] = asunto
        email.set_content(cuerpo)
    except Exception as e:
        print(f"Error al inicializar el Email: {e}")
        return False

    # Autentificacion y conexion
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass) 
    except Exception as e:
        print(f"Error al autentificar y conectar al servidor: {e}")
        return False

    # Envio del mensaje
    try:
        server.send_message(email)
        server.quit
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
        return False

    return True
    

