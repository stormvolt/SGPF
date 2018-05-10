#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from conect import * #conexion y funciones con la base de datos

print("Content-Type: text/html\n")

#Variables de la sesion iniciada
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')
fecha_inicial = form.getfirst('fecha_inicial','empty')
fecha_final = form.getfirst('fecha_final','empty')

#Encabezado generico
print("""
	<html>
	<head>
	<title>CGI script! Python</title
	</head>
	</body>
"""
)


print ("""
	<br>
	<table border=1>
	<tr>
	<th>Monto</th>
	<th>Fecha</th>
	<th>Descripcion</th>
	</tr>
"""
)

#Objeto controlador principal
base_datos = ControladorPrincipal()

#Buscamos los ingresos del usuario
datos = base_datos.ver_ingresos(sesion,fecha_inicial,fecha_final)

for result in datos:
	resultado= result.fetchall()
	for registro in resultado:
		print ('<tr><td>'+str(registro[0])+'</td><td>'+str(registro[1])+'</td><td>'+str(registro[2]))


    
print ("""
	</table>
"""
)