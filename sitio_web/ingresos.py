#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
from conect import * #conexion y funciones con la base de datos

print("Content-Type: text/html\n")

#Variables de la sesion iniciada
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')

#Objeto controlador principal
base_datos = ControladorPrincipal()

#Titulo, estilo y modulo ajax
print("""
	<html>
	<head>
	<title>BUDGETSOFT Ingresos</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
	<script type="text/javascript" src="jquery.min.js"></script> 
	<script type="text/javascript"> 
	function getData(){
        var parametros = {
				"fecha_inicial" : document.getElementById('fecha_inicial').value,
				"fecha_final" : document.getElementById('fecha_final').value,
                "Sesion" : document.getElementById('Sesion').value,
		};
        $.ajax({
                data:  parametros,
                url:   'tabla_ingresos.py',
                type:  'get',
                beforeSend: function ()
				{
                        $("#contenido").html("Procesando, espere por favor...");
                },
                success:  function (response)
				{
                        $("#contenido").html(response);
                }
        });
	}
	</script>
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
print('<li><a href="home.py?Sesion=')
print(sesion + '">Principal</a></li>')		
print('<li><a href="balance.py?Sesion=')
print(sesion + '">Balance</a></li>')
print('<li class="current_page_item"><a href="ingresos.py?Sesion=')
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

#Formulario que recupera los ingresos en un intervalo de tiempo determinado
print("""
	<div id="panel2">
		<h2>Ingresos</h2>
		<form action = ''>
		<b>Desde: </b>
		<input type=date name=fecha_inicial id=fecha_inicial>
		<b> Hasta: </b>
		<input type=date name=fecha_final id=fecha_final>
		<input type=hidden name=Sesion id=Sesion value=
"""
)
print(sesion + '>')		
print("""		
		<input type=button value=Mostrar onClick="getData()"
		</form>
		<div id = contenido></div>
"""
)
		
		
print("""
	</div>
	</body>
    </html>
"""
)