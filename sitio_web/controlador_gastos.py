import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA TABLA GASTOS
class ControladorGastos:

	#Recolecta todos los gastos de un usuario en un intervalo determinado
	def verGastos(self, user_id, fecha_ini, fecha_fin):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)
		cursor.callproc('verGastos', argumentos)
		resultados = cursor.stored_results()
		cursor.close()
		return resultados
		
	#Agrega un nuevo registro a los gastos del usuario
	def agregarGastos(self, user_id, monto, id_categoria, fecha, descripcion):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, monto, id_categoria, fecha, descripcion)
		inserciones = cursor.callproc('agregarGasto', argumentos)
		db.commit()
		cursor.close()
		return inserciones
		
	#Borra un gasto
	def borrarGasto(self, id):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (id,)
		cursor.callproc('borrarGasto', argumentos)
		db.commit()
		cursor.close()
		
	#Modifica los campos de un gasto
	def modificarGasto(self, id, id_categoria, monto, fecha, descripcion):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (id, id_categoria, monto, fecha, descripcion)
		cursor.callproc('modificarGastos', argumentos)
		db.commit()
		cursor.close()
		
	#Recolecta todos los gastos de un usuario en un intervalo determinado, filtrados por categoria
	def verGastosGrafico(self, user_id, fecha_ini, fecha_fin):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)
		cursor.callproc('verGastosGrafico', argumentos)
		resultados = cursor.stored_results()
		cursor.close()
		return resultados