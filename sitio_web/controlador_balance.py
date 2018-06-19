import mysql.connector

#PERMITE REALIZAR UN BALANCE ENTRE INGRESOS Y GASTOS
class ControladorBalance:

	#Obtiene un balance entre ingresos y gastos en un periodo de tiempo determinado
	def obtenerBalance(self, user_id, fecha_ini, fecha_fin):
		balance = 0		
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)		
		cursor.callproc('verIngresos', argumentos)
		ingresos = cursor.stored_results()
		for result in ingresos:
			resultado = result.fetchall()
			for registro in resultado:
				balance = balance + registro[1]		
		cursor.callproc('verGastos', argumentos)
		gastos = cursor.stored_results()
		for result in gastos:
			resultado = result.fetchall()
			for registro in resultado:
				balance = balance - registro[1]		
		cursor.close()		
		return balance
		
	#Obtiene el total de ingresos en un periodo de tiempo
	def totalIngresos(self, user_id, fecha_ini, fecha_fin):
		total = 0		
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)		
		cursor.callproc('verIngresos', argumentos)
		ingresos = cursor.stored_results()
		for result in ingresos:
			resultado = result.fetchall()
			for registro in resultado:
				total = total + registro[1]		
		cursor.close()		
		return total
		
	#Obtiene el total de ingresos en un periodo de tiempo
	def totalGastos(self, user_id, fecha_ini, fecha_fin):
		total = 0		
		db = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='budgetsoft')
		cursor = db.cursor()
		argumentos = (user_id, fecha_ini, fecha_fin)		
		cursor.callproc('verGastos', argumentos)
		gastos = cursor.stored_results()
		for result in gastos:
			resultado = result.fetchall()
			for registro in resultado:
				total = total + registro[1]		
		cursor.close()		
		return total