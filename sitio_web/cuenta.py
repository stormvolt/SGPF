#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_usuarios import * #conexion y funciones con la tabla usuarios

print("Content-Type: text/html\n")

#Variables del formulario Modificar datos
form = cgi.FieldStorage()
sesion = form.getfirst('Sesion','empty')
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
	<title>BUDGETSOFT Mi cuenta</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="formato.css" rel="stylesheet" type="text/css" media="screen">
	</head>
"""
)

#Se ejecuta la actualizacion de datos
if(password!='empty'):
	if(password==password_check):
		tabla_usuarios.modificarDatos(sesion, password, nombre, email)
	else:
		print('Los passwords ingresados no coinciden.')
	

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
print('<li><a href="home.py?Sesion=')
print(sesion + '">Principal</a></li>')		
print('<li><a href="balance.py?Sesion=')
print(sesion + '">Balance</a></li>')
print('<li><a href="ingresos.py?Sesion=')
print(sesion + '">Ingresos</a></li>')
print('<li><a href="gastos.py?Sesion=')
print(sesion + '">Gastos</a></li>')
print('<li><a href="metas.py?Sesion=')
print(sesion + '">Metas</a></li>')
print('<li class="current_page_item"><a href="cuenta.py?Sesion=')
print(sesion + '">Mi cuenta</a></li>')	
print('<li><a href="login.py">Cerrar sesion</a></li>')
print ("""
		</ul>
		</nav>
	</div>
	"""
)

#Recuperamos los datos del usuario
datos = tabla_usuarios.requerirInformacionUsuario(sesion)
    	
#Formulario de edicion de datos
print ("""
		<div id="panel2">
			<h2>Mis datos</h2>
		"""
)
print('<form action="cuenta.py?Sesion=')
print(sesion + '" method="post">')
print('<TABLE BORDER=0>')
print('<TR>')
print('<TD><b>Usuario:</b><T/D>')
print('<TD><input type="text"  name="Usuario" disabled required value=')
print(datos[0][1] + '></TD>')
print('</TR>')
print('<TR>')
print('<TD><b>Password:</b></TD>')
print('<TD><input type="password"  name="Password" required value=')
print(datos[0][2] + '></TD>')
print('</TR>')
print('<TR>')
print('<TD><b>Confirmar Password:</b></TD>')
print('<TD><input type="password"  name="Password_check" placeholder="Confirmar password" required value="')
print(datos[0][2] +  '"></TD>')
print('</TR>')
print('<TR>')
print('<TD><b>Nombre:</b></TD>')
print('<TD><input type="text"  name="Nombre" required value="')
print(datos[0][3] +  '"></TD>')
print('</TR>')
print('<TR>')
print('<TD><b>Email:</b></TD>')
print('<TD><input type="email"  name="Email" required value=')
print(datos[0][4] + '></TD>')
print('</TR>')
print('</TABLE>')				
print ("""
			
			<br>
			<input type="submit" value="Guardar cambios"> <br>
			</form>			

"""
)

#Mensajes de verificacion
if(password!='empty'):
	if(password!=password_check):
		print('<br> Los passwords ingresados no coinciden. <br>')
	else:
		print('<br> Datos actualizados. <br>')
		

print ("""	
	<br>
	</div>
	</body>
    </html>
"""
)