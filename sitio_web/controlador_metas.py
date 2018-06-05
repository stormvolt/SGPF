import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA TABLA METAS
class ControladorMetas:

	#Recolecta todos las metas de un usuario
	def cargarMetas(self, user_id):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id,)
		cursor.callproc('cargarMetas', argumentos)
		resultados = cursor.stored_results()
		cursor.close()
		return resultados
		
	#Agrega un nuevo registro a las metas del usuario
	def agregarMeta(self, user_id, nombre, monto, fecha_ini, fecha_fin, descripcion):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, nombre, monto, fecha_ini, fecha_fin, descripcion)
		inserciones = cursor.callproc('agregarMeta', argumentos)
		db.commit()
		cursor.close()
		return inserciones
		
	#Borra una meta
	def borrarMeta(self, id):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (id,)
		cursor.callproc('borrarMeta', argumentos)
		db.commit()
		cursor.close()
		
	#Modifica los campos de una meta
	def modificarMeta(self, id, nombre, monto, fecha_ini, fecha_fin, descripcion):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (id, nombre, monto, fecha_ini, fecha_fin, descripcion)
		cursor.callproc('modificarMeta', argumentos)
		db.commit()
		cursor.close()