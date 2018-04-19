#!C:\Python27\python
print("Content-Type: text/html\n")

print("""
	<html>
	<head>
	<title>BUDGETSOFT</title>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" >
	<link href="estilo.css" rel="stylesheet" type="text/css" media="screen">
	</head>	

	<body>

	<header id="header">
	<img src = "images/logo.jpg" width="70" height="70" alt="Imagen no encontrada">
	<h1>BUDGETSOFT</h1>
	</header>

	<div id="sidebar">
	<h1>Navegacion</h1>
	<nav id="nav">
	<ul>
		<li class="current_page_item"><a href="principal.py">Inicio</a></li>
		<li><a href="signup.py">Registrarse</a></li>
		<li><a href="login.py">Iniciar sesion</a></li>		
	</ul>
	</nav>
	</div>
	
	<div id="panel2">
		<h2>Inicio</h2>
		<img src = "images/inicio.jpg" width="50%" height="50%" alt="Imagen no encontrada">
		<br>
		BudgetSoft es una aplicacion que brinda a las personas la oportunidad de controlar mejor sus gastos e ingresos. De esta forma,les permite mejorar el rendimiento de sus ganacias y avanzar hacia sus metas.<br>
		<br>
	</div>
	</body>
    </html>
"""
)  