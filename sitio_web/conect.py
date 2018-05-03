import mysql.connector

#conexion a la base de datos del sistema
def conectar():
	db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='budgetsoft')
	return db 

	
#Verifica que los datos proporcionados para iniciar sesion son correctos
def ingresar(usuario, password):
	db = conectar()
	cursor = db.cursor()
	argumentos = (usuario, password, False)
	resultados = cursor.callproc('verificar_inicio_sesion', argumentos)
	correcto = resultados[2] #indica si los datos proporcionados son correctos
	cursor.close()
	return correcto
	

#Busca los datos personales del usuario
def cargar_informacion_usuario(usuario): 
	db = conectar()
	cursor = db.cursor()
	argumentos = (usuario,)
	cursor.callproc('buscar_datos', argumentos)
	for result in cursor.stored_results():
		resultado = result.fetchall()
	cursor.close()
	return resultado

	
#Inserta un nuevo usuario en el sistema
def agregar_usuario(usuario, password, nombre, email):
	db = conectar()
	cursor = db.cursor()
	argumentos = (usuario, password, nombre, email)
	inserciones = cursor.callproc('insertar_usuario', argumentos)
	db.commit()
	cursor.close()
	return inserciones
	
	
#Modifica los datos del usuario
def actualizar_datos(usuario, password, nombre, email):
	db = conectar()
	cursor = db.cursor()
	argumentos = (usuario, password, nombre, email)
	cursor.callproc('modificar_datos', argumentos)
	db.commit()
	cursor.close()
