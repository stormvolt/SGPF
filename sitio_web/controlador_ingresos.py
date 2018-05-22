import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA TABLA INGRESOS
class ControladorIngresos:

	#Recolecta todos los ingresos de un usuario en un intervalo determinado
	def verIngresos(self, usuario, fecha_ini, fecha_fin):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (usuario, fecha_ini, fecha_fin)
		cursor.callproc('verIngresos', argumentos)
		resultados = cursor.stored_results()
		cursor.close()
		return resultados
