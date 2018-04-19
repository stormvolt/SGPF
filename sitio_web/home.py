#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='budgetsoft')
							  
form = cgi.FieldStorage() # se instancia solo una vez
sesion = form.getfirst('Sesion','empty')

print("""
	<html>
	<head>
	<title>BUDGETSOFT Home</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
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
		<li class="current_page_item"><a href="home.py?Sesion=
"""
) 

print(sesion + '">Inicio</a></li>')		

cursor=db.cursor()
sql = "SELECT * FROM `usuarios` WHERE `usuario` LIKE '%s'"  %  (sesion)
cursor.execute(sql)
resultado=cursor.fetchall()


print("""
		<li><a href="login.py">Balance</a></li>
		<li><a href="login.py">Ingresos</a></li>
		<li><a href="login.py">Egresos</a></li>
		<li><a href="login.py">Configuracion</a></li>
		<li><a href="login.py">Cerrar sesion</a></li>
	</ul>
	</nav>
	</div>
	
	<div id="panel2">
		<h2>Bienvenido, 
"""
) 

print(resultado[0][3] + '.</h2>')
		
		
print("""
	</div>
	</body>
    </html>
"""
)  