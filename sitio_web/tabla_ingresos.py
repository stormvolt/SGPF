#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_ingresos import * #conexion y funciones con la tabla ingresos

print("Content-Type: text/html\n")

#Parametros de la busqueda
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')
user_id = form.getfirst('user_id','empty')
fecha_inicial = form.getfirst('fecha_inicial','empty')
fecha_final = form.getfirst('fecha_final','empty')

#Encabezado generico
print("""
	<html>
	<head>
	<title>CGI script! Python</title>
	</head>
	</body>
"""
)

#Tabla de resultados
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

#Objeto controlador de la tabla ingresos
tabla_ingresos = ControladorIngresos()


#Buscamos los ingresos del usuario
datos = tabla_ingresos.verIngresos(user_id,fecha_inicial,fecha_final)

fila = 0 #fila de la tabla
#Se imprime la tabla de resultados
for result in datos:
	resultado= result.fetchall()
	for registro in resultado:
		print('<tr>')
		print('<td><input type="number" min="1" id="1' + str(fila) +  '" required value="'+registro[1]+'"></td>')
		print('<td><input type="date" id="2' + str(fila) + '" required value="'+registro[2]+'"></td>')
		print('<td><input type="text" id="3' + str(fila) +  '" required value="'+registro[3]+'"></td>')
		#Boton para borrar registro
		print('<td><form action="ingresos.py?Sesion=')
		print(sesion + '" method="post">')
		print('<input type="hidden" name="accion" value="borrar">')
		print('<input type="hidden" name="fecha_inicial" value="' + fecha_inicial +'">')
		print('<input type="hidden" name="fecha_final" value="' + fecha_final +'">')
		print('<input type="hidden" name="registro" value="'+ registro[0]+ '">')
		print('<input type="submit" value="Borrar"></form></td>')
		#Formulario para modificar registro
		print('<td><form action="ingresos.py?Sesion=')
		print(sesion + '" method="post">')
		print('<input type="hidden" name="accion" value="modificar">')
		print('<input type="hidden" name="fecha_inicial" value="' + fecha_inicial +'">')
		print('<input type="hidden" name="fecha_final" value="' + fecha_final +'">')
		print('<input type="hidden" name="registro" value="'+ registro[0] + '">')		
		print('<input type="hidden" id="monto' + str(fila)  + '" name="monto" required value="">')
		print('<input type="hidden" id="fecha' + str(fila)  + '" name="fecha" required value="">')
		print('<input type="hidden" id="descripcion' + str(fila)  + '" name="descripcion" required value="">')		
		print('<input type="submit" onclick="actualizar('+ str(fila) +')" value="Modificar"></form></td>')
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
	document.getElementById("monto"+fila).value = document.getElementById("1"+fila).value;
	document.getElementById("fecha"+fila).value = document.getElementById("2"+fila).value;
	document.getElementById("descripcion"+fila).value = document.getElementById("3"+fila).value;
}
</script>
"""
)	