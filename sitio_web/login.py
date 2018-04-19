#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='budgetsoft')
							  
form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('Usuario','empty')
password = form.getfirst('Password','empty')

cursor=db.cursor()

sql = "SELECT * FROM `usuarios` WHERE `usuario` LIKE '%s' AND `password` LIKE '%s'" % (usuario,password)

cursor.execute(sql)
resultado=cursor.fetchall()
cursor.close()

print ("""
    <!DOCTYPE HTML>
	<html>

	<head>
	<title>BUDGETSOFT Login</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
"""
)    	

if(len(resultado)!=0):
	print('<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=home.py?Sesion=')
	print(usuario + '">') 

	
print ("""	
	</head>

	<body>

	<header id="header">
	<img src = "images/logo.jpg" width="70" height="70" alt="Imagen no encontrada">
	<h1>BUDGETSOFT</h1>
	</header>

	<div id="sidebar">
	<h1>Navegacion</h1>
	<nav id="nav">
		<ul>
			<li><a href="principal.py">Inicio</a></li>
			<li><a href="signup.py">Registrarse</a></li>
			<li class="current_page_item"><a href="login.py">Iniciar sesion</a></li>			
		</ul>
		</nav>
		</div>
		<div id="panel2">
			<h2>Iniciar sesion</h2>
			<form action="login.py" method="post">
			<b>Usuario:</b>
			<input type="text"  name="Usuario"> <br><br>
			<b>Password:</b>
			<input type="password"  name="Password"> <br><br>
			<br>
			<input type="submit" value="Acceder"> <br>
			</form>

"""
)
if(usuario=='empty'):
	print('<br> Ingrese un usuario. <br>')
elif(len(resultado)==0):
	print("""
		<br>Usuario no registrado o datos incorrectos <br>
	"""
	)

		

print ("""
	<br>
	</div>
	</body>
    </html>
"""
)    
