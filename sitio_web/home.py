#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from conect import * #conexion y funciones con la base de datos

print("Content-Type: text/html\n")

#Variables de la sesion iniciada
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')

#Objeto controlador principal
base_datos = ControladorPrincipal()

#Titulo y estilo
print("""
	<html>
	<head>
	<title>BUDGETSOFT Home</title>
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
	"""
)
print('<li class="current_page_item"><a href="home.py?Sesion=')
print(sesion + '">Inicio</a></li>')		
print('<li><a href="balance.py?Sesion=')
print(sesion + '">Balance</a></li>')
print('<li><a href="ingresos.py?Sesion=')
print(sesion + '">Ingresos</a></li>')
print('<li><a href="gastos.py?Sesion=')
print(sesion + '">Gastos</a></li>')
print('<li><a href="metas.py?Sesion=')
print(sesion + '">Metas</a></li>')
print('<li><a href="cuenta.py?Sesion=')
print(sesion + '">Mi cuenta</a></li>')	
print('<li><a href="login.py">Cerrar sesion</a></li>')
print ("""
		</ul>
		</nav>
		</div>
	"""
)		

#Buscamos el nombre del usuario
datos = base_datos.cargar_informacion_usuario(sesion)
 
 
#Mensaje de bienvenida
print ("""
	
	<div id="panel2">
		<h2>Bienvenido, 
"""
)
print(datos[0][3] + '.</h2>')
		
		
print("""
	</div>
	</body>
    </html>
"""
)  