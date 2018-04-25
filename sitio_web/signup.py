#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

#conexion a la base de datos
db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='budgetsoft')
							  
form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('Usuario','empty')
password = form.getfirst('Password','empty')
nombre = form.getfirst('Nombre','empty')
email = form.getfirst('Email','empty')

#Titulo y estilo
print ("""
    <html>
	<head>
	<title>BUDGETSOFT Sign up</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
	</head>
"""
)    	

#Encabezado de pagina
print ("""
	<body>

	<header id="header">
	<img src = "images/logo.jpg" width="70" height="70" alt="Imagen no encontrada">
	<h1>BUDGETSOFT</h1>
	</header>

"""
)

#Barra de navegacion
print ("""
	<div id="sidebar">
	<h1>Navegacion</h1>
	<nav id="nav">
		<ul>
			<li><a href="principal.py">Inicio</a></li>
			<li class="current_page_item"><a href="signup.py">Registrarse</a></li>
			<li><a href="login.py">Iniciar sesion</a></li>			
		</ul>
		</nav>
		</div>
		<div id="panel2">
			<h2>Registrarse</h2>
			<form action="signup.py" method="post">
			<b>Usuario:</b>
			<input type="text"  name="Usuario" required> <br><br>
			<b>Password:</b>
			<input type="password"  name="Password" required> <br><br>
			<b>Nombre:</b>
			<input type="text"  name="Nombre" required> <br><br>
			<b>Email:</b>
			<input type="email"  name="Email" required> <br><br>
			<br>
			<input type="submit" value="Registrarse"> <br>
			</form>			

"""
)

#Verficamos que no exista otro suario igual en la base de datos
cursor=db.cursor()
sql = "SELECT * FROM `usuarios` WHERE `usuario` LIKE '%s'" % (usuario)
cursor.execute(sql)
resultado=cursor.fetchall()
cursor.close()


#Insertamos el nuevo registro, si no es un usuario ya existente
sql2 = "INSERT INTO `usuarios` VALUES (null,'%s','%s','%s','%s')" % (usuario, password, nombre, email)
if(len(resultado)!=0):
	print('Ese ususario ya se halla registrado.')
else:
	if(usuario!='empty'):
		insertar = db.cursor()
		number_of_rows = insertar.execute(sql2)
		if(number_of_rows!=0):
			print('<br> Usuario registrado correctamente. <br>')
		db.commit()
		insertar.close()
		
	else:
		print('<br> Ingrese un usuario. <br>')

		

print ("""	
	<br>
	</div>
	</body>
    </html>
"""
)    
