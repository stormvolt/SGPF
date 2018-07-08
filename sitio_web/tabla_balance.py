#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from controlador_balance import * #para calcular balances entre ingresos y gastos
from controlador_gastos import * #para la grafica de gastos por categoria

print("Content-Type: text/html\n")

#Parametros de la busqueda
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')
user_id = form.getfirst('user_id','empty')
fecha_inicial = form.getfirst('fecha_inicial','empty')
fecha_final = form.getfirst('fecha_final','empty')

#Objeto controlador del balance
mi_balance = ControladorBalance()

#Objeto controlador de la tabla gastos
tabla_gastos = ControladorGastos()

print("""
<html>
<head>
<title>CGI script! Python</title>
<script src="zingchart.min.js"></script>
<link href="formato.css" rel="stylesheet" type="text/css" media="screen">
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
<div id ='grafico_categorias'>
<h3>Gastos por categoria</h3>
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
  
  var myConfig = {
  type: "bar",
  "legend": {
                "layout": "x3",
                "overflow": "page",
                "alpha": 0.05,
                "shadow": false,
                "align":"center",
                "adjust-layout":true,
                "marker": {
                    "type": "circle",
                    "border-color": "none",
                    "size": "10px"
                },
                "border-width": 0,
                "maxItems": 3,
                "toggle-action": "hide",
                "pageOn": {
                    "backgroundColor": "#000",
                    "size": "10px",
                    "alpha": 0.65
                },
                "pageOff": {
                    "backgroundColor": "#7E7E7E",
                    "size": "10px",
                    "alpha": 0.65
                },
                "pageStatus": {
                    "color": "black"
                }
            },
  series: [  
"""
)

#Buscamos los gastos del usuario
datos = tabla_gastos.verGastosGrafico(user_id,fecha_inicial,fecha_final)

#graficamos los gastos por categoria
for result in datos:
	resultado= result.fetchall()
	for registro in resultado:
		print('{')
		print('values:[' + registro[1] + '],')
		print('"text": "' + registro[0] + '"')
		print('},')

print("""
		
  ]
};
  
  zingchart.render({ 
    id:'grafico',
    data:chartData,
    height:300,
    width:300
  });
  
  zingchart.render({ 
	id : 'grafico_categorias', 
	data : myConfig, 
	height: "300", 
	width: "400" 
	});
  
</script>
""")

("""
</body>
</html>
"""
)