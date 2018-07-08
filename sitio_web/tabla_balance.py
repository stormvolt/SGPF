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

#Objeto controlador del balance
mi_balance = ControladorBalance()

print("""
<html>
<head>
<title>CGI script! Python</title>
<script src="zingchart.min.js"></script>
<link href="estilos_grafico.css" rel="stylesheet" type="text/css" media="screen">
</head>
<body>
"""
)

#Tabla de resultados
print ("""
	<br>
	<div id ='grafico'>
	<table border=1>
	<tr>
	<th>Balance</th>
	</tr>
"""
)
#Se imprime el resultado en pantalla
print('<tr><td>')
print(mi_balance.obtenerBalance(user_id,fecha_inicial,fecha_final))		
print('</td></tr>')		

#Grafico de pie
print("""
</table>
<br><br><br>	
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
print ('{ "values": ['+str(mi_balance.totalIngresos(user_id,fecha_inicial,fecha_final))+'], "text":"ingresos", "backgroundColor":"#084B8A"},')
print('{ "values": ['+str(mi_balance.totalGastos(user_id,fecha_inicial,fecha_final))+'], "text":"gastos", "backgroundColor":"#99CC33"}')
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