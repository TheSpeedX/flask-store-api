import sqlite3
from sqlite3 import Error
database = r"firebase.db"

def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)
def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)
	return conn

def create_user(email,phone,username):
	conn=create_connection(database)
	cur = conn.cursor()
	sql = ''' INSERT INTO user(email,phone,username) VALUES(?,?,?) '''
	try:
		cur.execute(sql, (email,phone,username))
		conn.commit()
		return {"success": True}
	except:
		return {"success": False}
def fetch_data(email=None,phone=None):
	conn=create_connection(database)
	cur = conn.cursor()
	if email:
		cur.execute('''SELECT email,phone,username FROM user WHERE email = ? ; ''', (email,))
	elif phone:
		cur.execute('''SELECT email,phone,username FROM user WHERE phone = ? ; ''', (phone,))
	try:
		data=cur.fetchall()
		return {"email":data[0][0], "phone": data[0][1], "username": data[0][2]}
	except:
		return {"email":"", "phone": "", "username": ""}
def main():
	sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
										id integer PRIMARY KEY,
										email text UNIQUE NOT NULL,
										phone text NOT NULL,
										username text NOT NULL
									); """
	# create a database connection
	conn = create_connection(database)
 
	# create tables
	if conn is not None:
		# create projects table
		create_table(conn, sql_create_user_table)
 
	else:
		print("Error! cannot create the database connection.")

main()