#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import datetime
from controlador_usuarios import * #conexion y funciones con la tabla usuarios
from controlador_balance import * #para calcular balances entre ingresos y gastos

print("Content-Type: text/html\n")

#Variables de la sesion iniciada
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')

#Objeto controlador de la tabla de usuarios
tabla_usuarios = ControladorUsuarios()

#Obtenemos el nombre y el id del usuario
datos = tabla_usuarios.requerirInformacionUsuario(sesion)
id_usuario = datos[0][0]
nombre = datos[0][3]

#Objeto controlador del balance
mi_balance = ControladorBalance()

#Se toma la fecha de hoy
hoy = datetime.datetime.now()
hoy = hoy.isoformat()
mes = hoy[:7]
hoy = hoy[:10] 

#Titulo y estilo
print("""
	<html>
	<head>
	<title>BUDGETSOFT Principal</title>
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
print(sesion + '">Principal</a></li>')		
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

#Mensaje de bienvenida
print ("""
	
	<div id="panel2">
		<h2>Bienvenido, 
"""
)
print(nombre + '.</h2>')

#Se muestra el balance de este mes
print('<br>')
print('<TABLE BORDER=0>')
print('<tr><th>Balance del mes</th></tr>')	
print('<tr><td>')
print(mi_balance.obtenerBalance(id_usuario,mes + '-01',hoy))		
print('</td></tr>')
		
print("""
	</div>
	</body>
    </html>
"""
)  