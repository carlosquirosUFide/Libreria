import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

class ComunesModel:
    def enviar_correo_html(self, destinatario, asunto, html_contenido):
        # Configuración del servidor SMTP (ejemplo con Gmail)
        smtp_host = "smtp.gmail.com"
        smtp_port = 587
        remitente = "carlosquiros21@gmail.com"
        contrasena = "tumo ubpy wrre ufln"  # Usa una contraseña de aplicación, no la normal
        try:
            # Crear mensaje
            mensaje = MIMEMultipart("alternative")
            mensaje["From"] = remitente
            mensaje["To"] = destinatario
            mensaje["Subject"] = asunto

            # Adjuntar contenido en HTML
            mensaje.attach(MIMEText(html_contenido, "html"))

            # Conectar al servidor SMTP
            servidor = smtplib.SMTP(smtp_host, smtp_port)
            servidor.starttls()
            servidor.login(remitente, contrasena)
            servidor.sendmail(remitente, destinatario, mensaje.as_string())
            servidor.quit()

            print("Correo enviado exitosamente ✅")
        except Exception as e:
            print(f"Error al enviar correo: {e}")

    def generarContrasena(self):
        # Números del 1 al 10 en texto (porque "10" ocupa 2 dígitos)
        numeros = [str(i) for i in range(1, 11)]
        letras = list(string.ascii_lowercase)  # de 'a' a 'z'
        
        # Unir números y letras
        caracteres = numeros + letras
        
        # Escoger 8 caracteres aleatorios
        contrasena = ''.join(random.choice(caracteres) for _ in range(8))
        return contrasena
