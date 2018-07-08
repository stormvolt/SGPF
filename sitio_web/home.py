#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import datetime
from controlador_usuarios import * #conexion y funciones con la tabla usuarios
from controlador_balance import * #para calcular balances entre ingresos y gastos
from controlador_gastos import * #conexion y funciones con la tabla gastos

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
	<script src="zingchart.min.js"></script>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilos_grafico.css" rel="stylesheet" type="text/css" media="screen">
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


#Grafico de pie
print("""
<br>
<div id="grafico">
	<h2>Balance del mes</h2>		
""")
#Se muestra el balance de este mes
print('<br>')
print('<TABLE BORDER=0>')
print('<tr><th>Balance del mes</th></tr>')	
print('<tr><td>')
print(mi_balance.obtenerBalance(id_usuario,mes + '-01',hoy))		
print('</td></tr>')
print('</table>')
print('</div>')


#Se muestran los gastos del dia
print ("""
	<div id='tabla_resultados'>
	<h2>Gastos de hoy</h2>
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
#Buscamos los gastos del usuario
datos = tabla_gastos.verGastos(id_usuario,hoy,hoy)

#Se imprime la tabla de resultados
for result in datos:
	resultado= result.fetchall()
	for registro in resultado:
		print('<tr>')
		print('<td>' + registro[1] + '</td>')
		print('<td>' + registro[3] + '</td>')
		print('<td>' + registro[4] + '</td>')
		print('<td>' + registro[5] + '</td>')
		print('</tr>')
print('</table>')
print('</div>')

#Funcion que grafica el grafico de pie
print("""
</div>
<script>
  var chartData={
	"gui": {
		behaviors: [
		{
			id: 'DownloadPDF',
			enabled: 'none'
		},
		{
			id: 'Reload',
			enabled: 'none'
		},
		{
			id: 'ViewSource',
			enabled: 'none'
		},
		{
			id: 'SaveAsImagePNG',
			enabled: 'none'
		},
		{
			id: 'Print',
			enabled: 'none'
		},
		{
			id: 'DownloadSVG',
			enabled: 'none'
		}
		]
	},
	"legend": {},
    "type":"ring",  // Specify your chart type here.
    "series":[  // Insert your series data here.
"""
)
print ('{ "values": ['+str(mi_balance.totalIngresos(id_usuario,mes + '-01',hoy))+'], "text":"ingresos", "backgroundColor":"#084B8A"},')
print('{ "values": ['+str(mi_balance.totalGastos(id_usuario,mes + '-01',hoy))+'], "text":"gastos", "backgroundColor":"#99CC33"}')
print ("""
    ]
  };
  zingchart.render({ // Render Method[3]
    id:'grafico',
    data:chartData,
    height:300,
    width:300
  });
</script>
</body>
</html>
"""
)
 