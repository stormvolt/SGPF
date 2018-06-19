#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_gastos import * #conexion y funciones con la tabla gastos
from controlador_categorias import * #conexion y funciones con la tabla categorias

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
	<th>Categoria</th>
	<th>Fecha</th>
	<th>Descripcion</th>
	</tr>
"""
)

#Objeto controlador de la tabla gastos
tabla_gastos = ControladorGastos()

#Objeto controlador de la tabla categorias
tabla_categorias = ControladorCategorias()

#Cargamos la lista de categorias de gastos
categorias_disponibles = tabla_categorias.verCategorias()
nombres_categorias = []
keys_categorias = []
for cursor_categorias in categorias_disponibles:
	cursor = cursor_categorias.fetchall()
	for fila_categoria in cursor:
		keys_categorias.append(fila_categoria[0])
		nombres_categorias.append(fila_categoria[1])

#Buscamos los gastos del usuario
datos = tabla_gastos.verGastos(user_id,fecha_inicial,fecha_final)

fila = 0 #fila de la tabla
#Se imprime la tabla de resultados
for result in datos:
	resultado= result.fetchall()
	for registro in resultado:
		print('<tr>')
		print('<td><input type="number" min="1" id="1' + str(fila) +  '" required value="' + registro[1] + '"></td>')
		#Selector de categorias
		print('<td><select id="2' + str(fila) +  '">')
		for i in range(len(keys_categorias)):
			if( keys_categorias[i]==registro[2] ):
				print('<option value="' + keys_categorias[i] + '" selected>' + nombres_categorias[i] + '</option>')
			else:
				print('<option value="' + keys_categorias[i] + '">' + nombres_categorias[i] + '</option>')		
		print('<td><input type="date" id="4' + str(fila) + '" required value="' + registro[4] + '"></td>')
		print('<td><input type="text" id="5' + str(fila) +  '" required value="' + registro[5] + '"></td>')
		#Boton para borrar registro
		print('<td><form action="gastos.py?Sesion=')
		print(sesion + '" method="post">')
		print('<input type="hidden" name="accion" value="borrar">')
		print('<input type="hidden" name="fecha_inicial" value="' + fecha_inicial +'">')
		print('<input type="hidden" name="fecha_final" value="' + fecha_final +'">')
		print('<input type="hidden" name="registro" value="'+ str(registro[0])+ '">')
		print('<input type="submit" value="Borrar"></form></td>')
		#Formulario para modificar registro
		print('<td><form action="gastos.py?Sesion=')
		print(sesion + '" method="post">')
		print('<input type="hidden" name="accion" value="modificar">')
		print('<input type="hidden" name="fecha_inicial" value="' + fecha_inicial +'">')
		print('<input type="hidden" name="fecha_final" value="' + fecha_final +'">')
		print('<input type="hidden" name="registro" value="'+ registro[0]+ '">')		
		print('<input type="hidden" id="monto' + str(fila)  + '" name="monto" required value="">')		
		print('<input type="hidden" id="id_categoria' + str(fila)  + '" name="id_categoria" required value="">')		
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
	document.getElementById("id_categoria"+fila).value = document.getElementById("2"+fila).value;	
	document.getElementById("fecha"+fila).value = document.getElementById("4"+fila).value;
	document.getElementById("descripcion"+fila).value = document.getElementById("5"+fila).value;
}
</script>
"""
)	