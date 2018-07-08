#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_usuarios import * #conexion y funciones con la tabla usuarios
from controlador_metas import * #conexion y funciones con la tabla metas
from controlador_balance import * #para calcular balances entre ingresos y gastos

print("Content-Type: text/html\n")

#Variables de la sesion iniciada
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')
nombre = form.getfirst('nombre','empty')
monto = form.getfirst('monto','empty')
fecha_inicial = form.getfirst('fecha_inicial','empty')
fecha_final = form.getfirst('fecha_final','empty')
accion = form.getfirst('accion','empty') #define si se agrega, modifica o borra un registro
registro = form.getfirst('registro','empty')

#Objeto controlador de la tabla de usuarios
tabla_usuarios = ControladorUsuarios()

#Objeto controlador de la tabla ingresos
tabla_metas = ControladorMetas()

#Objeto controlador del balance
mi_balance = ControladorBalance()

#Obtenemos el id del usuario
user_id = tabla_usuarios.requerirInformacionUsuario(sesion)[0][0]

#Insertamos el nuevo registro
if(accion=='insertar'):
	tabla_metas.agregarMeta(user_id, nombre, monto, fecha_inicial, fecha_final)
#Borrar el registro
elif(accion=='borrar'):
	tabla_metas.borrarMeta(registro)
#Modificar registro	
elif(accion=='modificar'):
	tabla_metas.modificarMeta(registro, nombre, monto, fecha_inicial, fecha_final)

#Titulo, estilo
print("""
	<html>
	<head>
	<title>BUDGETSOFT Metas</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
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
print('<li><a href="home.py?Sesion=')
print(sesion + '">Principal</a></li>')		
print('<li><a href="balance.py?Sesion=')
print(sesion + '">Balance</a></li>')
print('<li><a href="ingresos.py?Sesion=')
print(sesion + '">Ingresos</a></li>')
print('<li><a href="gastos.py?Sesion=')
print(sesion + '">Gastos</a></li>')
print('<li  class="current_page_item"><a href="metas.py?Sesion=')
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

#Metas del usuyario
print("""
	<div id="panel2">
		<h2>Metas</h2>
		
"""
)

#Tabla de resultados
print ("""	
	<br>
	<table border=1>
	<tr>
	<th>Nombre</th>
	<th>Monto</th>
	<th>Inicio</th>
	<th>Final</th>
	<th>Progreso</th>
	</tr>
"""
)

#Buscamos las metas del usuario
datos = tabla_metas.cargarMetas(user_id)

#Esta variable almacena el balance calculado en el intervalo de tiempo de cada meta
balance = 0

fila = 0 #fila de la tabla
#Se imprime la tabla de resultados
for result in datos:
	resultado= result.fetchall()
	for registro in resultado:
		print('<tr>')
		print('<td><input type="text" id="1' + str(fila) +  '" required value="'+registro[1]+'"></td>')
		print('<td><input type="number" min="1" step=".01" id="2' + str(fila) +  '" required value="'+registro[2]+'"></td>')
		print('<td><input type="date" id="3' + str(fila) + '" required value="'+registro[3]+'"></td>')
		print('<td><input type="date" id="4' + str(fila) + '" required value="'+registro[4]+'"></td>')
		#progreso de la meta
		balance = mi_balance.obtenerBalance(user_id,registro[3],registro[4])
		print('<td><progress value="' + str(balance) + '" max="' + registro[2] + '"</td>')
		#Boton para borrar registro
		print('<td><form action="metas.py?Sesion=')
		print(sesion + '" method="post">')
		print('<input type="hidden" name="accion" value="borrar">')
		print('<input type="hidden" name="registro" value="'+ registro[0]+ '">')
		print('<input type="submit" value="Borrar"></form></td>')
		#Formulario para modificar registro
		print('<td><form action="metas.py?Sesion=')
		print(sesion + '" method="post">')
		print('<input type="hidden" name="accion" value="modificar">')
		print('<input type="hidden" name="registro" value="'+ registro[0] + '">')
		print('<input type="hidden" id="nombre' + str(fila)  + '" name="nombre" required value="">')		
		print('<input type="hidden" id="monto' + str(fila)  + '" name="monto" required value="">')
		print('<input type="hidden" id="fecha_inicial' + str(fila)  + '" name="fecha_inicial" required value="">')
		print('<input type="hidden" id="fecha_final' + str(fila)  + '" name="fecha_final" required value="">')
		print('<input type="submit" onclick="actualizar('+ str(fila) +')" value="Editar"></form></td>')
		print('</tr>')		
		fila = fila + 1
		
    
print ("""
	</table>
"""
)

#Lee los campos de su formulario para la modificacion de registros
print ("""
<script>
function actualizar(fila)
{
	document.getElementById("nombre"+fila).value = document.getElementById("1"+fila).value;
	document.getElementById("monto"+fila).value = document.getElementById("2"+fila).value;
	document.getElementById("fecha_inicial"+fila).value = document.getElementById("3"+fila).value;
	document.getElementById("fecha_final"+fila).value = document.getElementById("4"+fila).value;
}
</script>
"""
)

#Formulario para agregar metas
print('<br><br><br>')		
print('<h2>Agregar meta:</h2>')
print('<form name="agregarMeta" action="metas.py?Sesion=')
print(sesion + '" method="post">')
print('<input type="hidden" name="accion" value="insertar">')
print('<TABLE BORDER=0>')
print('<TR>')
print('<TD><input type="text"  name="nombre" placeholder="Nombre" autocomplete="off" required></TD> ')
print('<TD><input type="number"  name="monto" placeholder="Monto" min="1" step=".01" autocomplete="off" required></TD> ')
print('<TD><input type="date"  name="fecha_inicial" required></TD>')
print('<TD><input type="date"  name="fecha_final" required></TD>')
print('<TD><input type="submit" value="Agregar meta"></TD>')
print('</form>')
print('</TR>')
print('</TABLE>')

print("""
	</div>
	
	</body>
    </html>
"""
)