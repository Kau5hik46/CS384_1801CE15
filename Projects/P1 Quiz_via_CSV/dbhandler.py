import sqlite3

class dbhandler():
	def __init__(self, dbname):
		self.database_name = dbname
		self.connection = sqlite3.connect(self.database_name)

	def create_table(self, name):
		scrpit = '''CREATE TABLE '''+ str(name) +'''
         (NAME TEXT NOT NULL,
         ROLL TEXT PRIMARY KEY NOT NULL,
         PASSWORD TEXT NOT NULL,
         WHATSAPP TEXT NOT NULL);'''
		self.connection.execute(scrpit)

	def insert(self, table_name, index_list, values):
		index = ','.join(index_list)
		index = '(' + index + ')'
		values = ','.join(values)
		values = '(' + values + ')'
		scrpit = "INSERT INTO " + str(table_name)+ " " + index + " \
      VALUES " + values
		print(scrpit)
		self.connection.execute(scrpit);

	def.select(self, table_name, index_list):
		


if __name__ == '__main__':
	db = dbhandler("test.db")
	db.create_table("project1_registration")
	db.insert("project1_registration", ["NAME", "ROLL", "PASSWORD", "WHATSAPP"], ["'KAUSHIK'", "'1801CE15'", "'ABCD'", "'9542687186'"])
	db.connection.close()