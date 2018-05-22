import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA TABLA USUARIO
class ControladorUsuarios:

	#Verifica que los datos proporcionados para iniciar sesion son correctos
	def ingresar(self, usuario, password):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (usuario, password, False)
		resultados = cursor.callproc('ingresar', argumentos)
		correcto = resultados[2] #indica si los datos proporcionados son correctos
		cursor.close()
		return correcto
	

	#Busca los datos personales del usuario
	def requerirInformacionUsuario(self, usuario): 
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (usuario,)
		cursor.callproc('requerirInformacionUsuario', argumentos)
		for result in cursor.stored_results():
			resultado = result.fetchall()
		cursor.close()
		return resultado

	
	#Inserta un nuevo usuario en el sistema
	def agregarUsuario(self, usuario, password, nombre, email):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (self,usuario, password, nombre, email)
		inserciones = cursor.callproc('agregarUsuario', argumentos)
		db.commit()
		cursor.close()
		return inserciones
	
	
	#Modifica los datos del usuario
	def modificarDatos(self, usuario, password, nombre, email):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (usuario, password, nombre, email)
		cursor.callproc('modificarDatos', argumentos)
		db.commit()
		cursor.close()	
	