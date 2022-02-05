from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import MySQLdb.cursors 
import smtplib,ssl


app = Flask(__name__)
app.static_folder = 'static'

app.config['MYSQL_HOST'] = 'localhost'#Host
app.config['MYSQL_USER'] = 'root' #usuario
app.config['MYSQL_PASSWORD'] = '12345' #Contraseña
app.config['MYSQL_DB'] = 'prueba_tecnica' # La base de datos
mysql = MySQL(app) 

def enviar_correo(receiver_email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "codep2022@gmail.com"
    password ="pruebacode"
    message="Bienvenido al Blog de Noticias"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == 'POST':       
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        celular = request.form["celular"]
        comentario = request.form["comentario"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        query = f"""INSERT INTO visitantes (nombre,email ,celular) values('{nombre}','{correo}','{celular}')""" 
        cursor.execute(query) 
        mysql.connection.commit()
        enviar_correo(correo)
    return render_template('index.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0",debug=True)