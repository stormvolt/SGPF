import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA TABLA INGRESOS
class ControladorIngresos:

	#Recolecta todos los ingresos de un usuario en un intervalo determinado
	def verIngresos(self, user_id, fecha_ini, fecha_fin):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)
		cursor.callproc('verIngresos', argumentos)
		resultados = cursor.stored_results()
		cursor.close()
		return resultados
		
	#Agrega un nuevo registro a los ingresos del usuario
	def agregarIngreso(self, user_id, monto, fecha, descripcion):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)
		inserciones = cursor.callproc('agregarIngreso', argumentos)
		db.commit()
		cursor.close()
		return inserciones
		
	def borrarIngreso(self, id):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (id)
		inserciones = cursor.callproc('borrarIngreso', argumentos)
		db.commit()
		cursor.close()
		
	def modificarIngreso(self, id, monto, fecha, descripcion):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (id, monto, fecha, descripcion)
		cursor.callproc('modificarIngreso', argumentos)
		db.commit()
		cursor.close()