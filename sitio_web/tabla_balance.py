#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_balance import * #para calcular balances entre ingresos y gastos

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
	<title>CGI script! Python</title
	</head>
	</body>
"""
)

#Tabla de resultados
print ("""
	<br>
	<table border=1>
	<tr>
	<th>Balance</th>
	</tr>
"""
)

#Objeto controlador del balance
mi_balance = ControladorBalance()

#Se imprime el resultado en pantalla
print('<tr><td>')
print(mi_balance.obtenerBalance(user_id,fecha_inicial,fecha_final))		
print('</td></tr>')		
    
print ("""
	</table>
"""
)