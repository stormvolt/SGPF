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
password_check = form.getfirst('Password_check','empty')
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
"""
)


#Formulario de registro
print ("""
		<div id="panel2">
			<h2>Registrarse</h2>
			<form action="signup.py" method="post">
			<input type="text"  name="Usuario" placeholder="Usuario" required> <br><br>
			<input type="password"  name="Password" placeholder="Password" required> <br><br>
			<input type="password"  name="Password_check" placeholder="Confirmar password" required> <br><br>
			<input type="text"  name="Nombre" placeholder="Nombre" required> <br><br>
			<input type="email"  name="Email" placeholder="Email" required> <br><br>
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
	print('<br> Ese ususario ya se halla registrado. <br>')
else:
	if(usuario!='empty'):
		if(password==password_check):
			insertar = db.cursor()
			number_of_rows = insertar.execute(sql2)
			if(number_of_rows!=0):
				print('<br> Usuario registrado correctamente. <br>')
			db.commit()
			insertar.close()
		else:
			print('<br> Los passwords ingresados no coinciden. <br>')		
	else:
		print('<br> Ingrese un usuario. <br>')

		

print ("""	
	<br>
	</div>
	</body>
    </html>
"""
)    
