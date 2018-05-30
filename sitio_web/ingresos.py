#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import datetime
from controlador_usuarios import * #conexion y funciones con la tabla usuarios
from controlador_ingresos import * #conexion y funciones con la tabla ingresos

print("Content-Type: text/html\n")

#Variables de la sesion iniciada
form = cgi.FieldStorage() 
sesion = form.getfirst('Sesion','empty')
fecha = form.getfirst('fecha','empty')
monto = form.getfirst('monto','empty')
descripcion = form.getfirst('descripcion','empty')
fecha_inicial = form.getfirst('fecha_inicial','empty')
fecha_final = form.getfirst('fecha_final','empty')
accion = form.getfirst('accion','empty') #define si se agrega, modifica o borra un registro
registro = form.getfirst('registro','empty')

#Objeto controlador de la tabla de usuarios
tabla_usuarios = ControladorUsuarios()

#Objeto controlador de la tabla ingresos
tabla_ingresos = ControladorIngresos()

id_usuario = tabla_usuarios.requerirInformacionUsuario(sesion)[0][0]

#Insertamos el nuevo registro
if(accion=='insertar'):
	tabla_ingresos.agregarIngreso(id_usuario, monto, fecha, descripcion)
#Borrar el registro
elif(accion=='borrar'):
	tabla_ingresos.borrarIngreso(registro)
#Modificar registro	
elif(accion=='modificar'):
	tabla_ingresos.modificarIngreso(registro, monto, fecha, descripcion)

#Titulo, estilo
print("""
	<html>
	<head>
	<title>BUDGETSOFT Ingresos</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
"""
)    	

#Modulo ajax
print ("""
	<script type="text/javascript" src="jquery.min.js"></script> 
	<script type="text/javascript"> 
	function getData(){
        var parametros = {
				"fecha_inicial" : document.getElementById('fecha_inicial').value,
				"fecha_final" : document.getElementById('fecha_final').value,
"""
)    	

#Enviamos el id del usuario
print('"user_id" : ' + str(id_usuario) + ',')

#Modulo ajax
print ("""
		};
        $.ajax({
                data:  parametros,
				
"""
)
print('url:   "tabla_ingresos.py?Sesion=' + sesion + '",')
print ("""
                
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
	<body onload="getData()">
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
		
"""
)

#Se toma la fecha de hoy
hoy = datetime.datetime.now()
hoy = hoy.isoformat()
mes = hoy[:7]
hoy = hoy[:10] 

#Por defecto se buscan los gastos de este mes
print('<b>Desde: </b>')
if(fecha_inicial!='empty'):
	print('<input type=date name=fecha_inicial id=fecha_inicial value="' + fecha_inicial + '">')
else:
	print('<input type=date name=fecha_inicial id=fecha_inicial value="' + mes + '-01' + '">')
print('<b> Hasta: </b>')
if(fecha_final!='empty'):
	print('<input type=date name=fecha_final id=fecha_final value="' + fecha_final + '">')
else:
	print('<input type=date name=fecha_final id=fecha_final value="' + hoy + '">')		
print("""		
		<input type=button value=Mostrar onClick="getData()"
		</form>
		<div id = contenido></div>
		
"""
)

#Formulario para agregar ingresos
print('<br><br><br><br>')		
print('<h2>Agregar ingreso:</h2>')
print('<form name="agregarIngreso" action="ingresos.py?Sesion=')
print(sesion + '" method="post">')
print('<input type="hidden" name="accion" value="insertar">')
print('<TABLE BORDER=0>')
print('<TR>')
print('<TD><input type="number"  name="monto" placeholder="Monto" min="1" autocomplete="off" required></TD> ')
print('<TD><input type="date"  name="fecha" required value="' + hoy + '"></TD> ')
print('<TD><input type="text"  name="descripcion" placeholder="Descripcion" size="50" required></TD> ')
print('<TD><input type="submit" value="Agregar ingreso"></TD>')
print('</form>')
print('</TR>')
print('</TABLE>')

print("""
	</div>
	
	</body>
    </html>
"""
)