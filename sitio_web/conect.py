import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA BASE DE DATOS
class ControladorPrincipal:

	#conexion a la base de datos del sistema
	def conectar(self):
		db= mysql.connector.connect(user='root', password='',
								host='127.0.0.1',
								database='budgetsoft')
		return db 

	
	#Verifica que los datos proporcionados para iniciar sesion son correctos
	def ingresar(self, usuario, password):
		db = self.conectar()
		cursor = db.cursor()
		argumentos = (usuario, password, False)
		resultados = cursor.callproc('verificar_inicio_sesion', argumentos)
		correcto = resultados[2] #indica si los datos proporcionados son correctos
		cursor.close()
		return correcto
	

	#Busca los datos personales del usuario
	def cargar_informacion_usuario(self, usuario): 
		db = self.conectar()
		cursor = db.cursor()
		argumentos = (usuario,)
		cursor.callproc('buscar_datos', argumentos)
		for result in cursor.stored_results():
			resultado = result.fetchall()
		cursor.close()
		return resultado

	
	#Inserta un nuevo usuario en el sistema
	def agregar_usuario(self, usuario, password, nombre, email):
		db = self.conectar()
		cursor = db.cursor()
		argumentos = (self,usuario, password, nombre, email)
		inserciones = cursor.callproc('insertar_usuario', argumentos)
		db.commit()
		cursor.close()
		return inserciones
	
	
	#Modifica los datos del usuario
	def actualizar_datos(self, usuario, password, nombre, email):
		db = self.conectar()
		cursor = db.cursor()
		argumentos = (usuario, password, nombre, email)
		cursor.callproc('modificar_datos', argumentos)
		db.commit()
		cursor.close()
		
	#Recolecta todos los ingresos de un usuario en un intervalo determinado
	def ver_ingresos(self, usuario, fecha_ini, fecha_fin):
		db = self.conectar()
		cursor = db.cursor()
		argumentos = (usuario, fecha_ini, fecha_fin)
		cursor.callproc('buscar_ingresos', argumentos)
		#for result in cursor.stored_results():
			#resultados.append(result.fetchall())
		resultados = cursor.stored_results()
		cursor.close()
		return resultados
