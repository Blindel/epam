def send_notification(cursor: mysql.connector.cursor_cext.CMySQLCursor, trig_name: str, t_name: str, t_name2: str):
	"""t_name is the table we are tracking updates from, t_name2 - notifications table """
	cursor.execute(f"""INSERT INTO {t_name2}(table_name, action) 
				VALUES ('{t_name}', 'updated')""")
	
def create_trigger(cursor: mysql.connector.cursor_cext.CMySQLCursor, trig_name: str, t_name: str, t_name2: str):
		"""t_name is the table we are tracking updates from, t_name2 - notification table """
		try:
			cursor.execute(f"""CREATE TRIGGER {trig_name} AFTER UPDATE ON {t_name} 
				 FOR EACH ROW BEGIN INSERT INTO {t_name2}(table_name, action) 
				 VALUES ('{t_name}', 'update'); END;""", )
		except:
			pass
		
def create_notification_table(cursor: mysql.connector.cursor_cext.CMySQLCursor, t_name: str):
    """Creates table containing four columns: id: int (Automatic), col1: table you want to track(VARCHAR(20))"""
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {t_name} ("
    "  id INT(11) AUTO_INCREMENT,"
    f"  table_name VARCHAR(20) NOT NULL,"
    f"  action VARCHAR(20) NOT NULL,"
	f"  PRIMARY KEY (id),"
	"	timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    ");")
	
def pull_values(cursor: mysql.connector.cursor_cext.CMySQLCursor, t_name: str, col: str) -> list:
	"""Returns all values from provided table"""
	cursor.execute(f"""
                   SELECT DISTINCT {col}
                   FROM {t_name}""")
	records = cursor.fetchall()
	return records

