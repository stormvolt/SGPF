import mysql.connector

#conexion a la base de datos del sistema
def conectar():
	db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='budgetsoft')
	return db 