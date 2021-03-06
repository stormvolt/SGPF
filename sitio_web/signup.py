#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_usuarios import * #conexion y funciones con la tabla usuarios

print("Content-Type: text/html\n")

#Variables del formulario Iniciar sesion
form = cgi.FieldStorage() 
usuario = form.getfirst('Usuario','empty')
password = form.getfirst('Password','empty')
password_check = form.getfirst('Password_check','empty')
nombre = form.getfirst('Nombre','empty')
email = form.getfirst('Email','empty')

#Objeto controlador de la tabla de usuarios
tabla_usuarios = ControladorUsuarios()

#Titulo y estilo
print ("""
    <html>
	<head>
	<title>BUDGETSOFT Registrarse</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="formato.css" rel="stylesheet" type="text/css" media="screen">
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
			<input type="text"  name="Usuario" placeholder="Usuario" autofocus required> <br><br>
			<input type="password"  name="Password" placeholder="Password" required> <br><br>
			<input type="password"  name="Password_check" placeholder="Confirmar password" required> <br><br>
			<input type="text"  name="Nombre" placeholder="Nombre" autocomplete="off" required> <br><br>
			<input type="email"  name="Email" placeholder="Email" autocomplete="off" required> <br><br>
			<br>
			<input type="submit" value="Registrarse"> <br>
			</form>
"""
)

#Verficamos que no exista otro usuario igual en la base de datos
datos = tabla_usuarios.requerirInformacionUsuario(usuario)

#Insertamos el nuevo registro, si no es un usuario ya existente
if(len(datos)!=0):
	print('<br> Ese ususario ya se halla registrado. <br>')
else:
	if(usuario!='empty'):
		if(password==password_check):
			num_inserciones = tabla_usuarios.agregarUsuario(usuario,password,nombre,email)
			if(num_inserciones != 0):
				print('<br> Usuario registrado correctamente. <br>')
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
