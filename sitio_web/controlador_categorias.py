import mysql.connector

#ACTUA COMO INTERMEDIARIO PARA LLAMAR A LAS FUNCIONES DE LA TABLA CATEGORIAS
class ControladorCategorias:
	
	#Despliega todas las categorias
	def verCategorias(self):
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		cursor.callproc('verCategorias')
		resultados = cursor.stored_results()
		cursor.close()
		return resultados

