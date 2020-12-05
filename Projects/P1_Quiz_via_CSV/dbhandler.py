import sqlite3

class dbhandler():
	def __init__(self, dbname, table_name = None, index_tuples = None):
		self.database_name = dbname
		self.connection = sqlite3.connect(self.database_name)
		try:
			self.create_table(table_name, index_tuples)
		except:
			pass

	def create_table(self, name, index_tuple_list):
		self.index_list = [x[0] for x in index_tuple_list]
		index = [' '.join(x) for x in index_tuple_list]
		index = ','.join(index)
		index = '(' + index + ')'
		scrpit = '''CREATE TABLE '''+ str(name) + str(index)
		try:
			self.connection.execute(scrpit)
			self.connection.commit()
		except sqlite3.OperationalError:
			pass
		return name

	def insert(self, table_name, values_old, select_val = None, select_by = 'ROLL'):
		index = self.index_list
		index = ','.join(index)
		index = '(' + index + ')'
		values = values_old
		values = [x.strip() for x in values]
		values = ["'"+x.strip("'")+"'" for x in values]
		values = ','.join(values)
		values = '(' + values + ')'
		scrpit = "INSERT INTO " + str(table_name)+ " " + index + " \
      VALUES " + values
		try:
			self.connection.execute(scrpit)
			self.connection.commit()
		except sqlite3.IntegrityError:
			pass
		if select_val != None:
			return self.select(table_name, select_val, select_by)
		else:
			return self.select(table_name, values_old[1], select_by)

	def select(self, table_name, select_val, select_by = 'ROLL'):
		index = self.index_list
		select_val = select_val.strip("'")
		select_val = "'" +select_val + "'"
		index = ','.join(index)
		scrpit = "SELECT "+ str(index) + " FROM "  + str(table_name) + " where " + str(select_by) + " = " + str(select_val)
		selected = self.connection.execute(scrpit);
		return selected.fetchone()

	def update(self, table_name, column, new_value, select_val, select_by = 'ROLL'):
		if select_by not in self.index_list:
			return None
		new_value.strip("'")
		new_value = "'" + str(new_value) + "'"
		select_val.strip("'")
		select_val = "'" + str(select_val) + "'"
		scrpit = "UPDATE "+str(table_name)+" set "+str(column)+" = " + new_value + " where " + str(select_by) + " = " + str(select_val)
		self.connection.execute(scrpit)
		self.connection.commit()
		return self.select(table_name, select_val, select_by)

if __name__ == "__main__":
	database_name = "project1_quiz_cs384.db"
	# db = dbhandler(database_name, "Quiz_wise_marks", [("ROLL","TEXT", "PRIMARY KEY","NOT NULL"), ("QUIZ", "TEXT", "NOT NULL"), ("TOTAL", "TEXT", "NOT NULL")])
	# print(db.select("Quiz_wise_marks", 'KK'))
