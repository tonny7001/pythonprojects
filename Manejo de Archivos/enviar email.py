import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox

# 1. Variable para almacenar el correo remitente
remitente = "jorge_mosquera6@hotmail.com"
# 2. Variable para el destinatario del correo
destinatario = "meollo70001@gmail.com"
# 3. Contraseña del correo para iniciar sesión en el servidor (usa una contraseña de aplicación o permite aplicaciones menos seguras)
contrasena = "Tonny/==!2308"
# 4. Asunto del correo
asunto = "Prueba de envío de correo"
# 5. Cuerpo del correo donde va el mensaje
cuerpo = "Hola Mundo"

# 6. Crear mensaje utilizando MIMEText para mayor compatibilidad
mensaje = MIMEText(cuerpo)
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto

try:
    # 7. Configuración del servidor SMTP para Hotmail/Outlook
    server = smtplib.SMTP("smtp.office365.com", 587)  # Hotmail/Outlook usa smtp.office365.com
    server.starttls()
    server.login(remitente, contrasena)
    # 8. Enviar el correo
    server.sendmail(remitente, destinatario, mensaje.as_string())
    server.quit()
    messagebox.showinfo(title="Login", message="Mensaje enviado")
except Exception as e:
    # Mostrar el error en caso de fallo
    messagebox.showerror(title="Error", message=f"Hubo un error al enviar el correo: {e}")
