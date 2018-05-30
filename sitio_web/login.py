#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_usuarios import * #conexion y funciones con la base de datos

print("Content-Type: text/html\n")

#Variables del formulario Iniciar sesion							  
form = cgi.FieldStorage() 
usuario = form.getfirst('Usuario','empty')
password = form.getfirst('Password','empty')

#Objeto controlador de la tabla de usuarios
tabla_usuarios = ControladorUsuarios()

#Se autentifican los datos proporcionados
validar = tabla_usuarios.ingresar(usuario, password)

#Titulo y estilo
print ("""
    <html>
	<head>
	<title>BUDGETSOFT Iniciar sesion</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
	</head>
"""
)    	

#Iniciar sesion
if (validar):
	print('<META HTTP-EQUIV="REFRESH" CONTENT="0;URL=home.py?Sesion=')
	print(usuario + '">') 

	
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
			<li><a href="signup.py">Registrarse</a></li>
			<li class="current_page_item"><a href="login.py">Iniciar sesion</a></li>			
		</ul>
		</nav>
		</div>
	"""
)
    	
#Panel de inicio de sesion
print ("""
		<div id="panel2">
			<h2>Iniciar sesion</h2>
			<form action="login.py" method="post">
			<input type="text"  name="Usuario" placeholder="Usuario" autocomplete="off" autofocus required> <br><br>
			<input type="password"  name="Password" placeholder="Password" required> <br><br>
			<br>
			<input type="submit" value="Acceder"> <br>
			</form>

"""
)

#comprobamos si se ingreso un usuario valido
if(usuario=='empty'):
	print('<br> Ingrese un usuario. <br>')
elif(not validar):
	print("""
		<br>Datos incorrectos <br>
	"""
	)		

print ("""
	<br>
	</div>
	</body>
    </html>
"""
)    
