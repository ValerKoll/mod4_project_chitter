from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()

connection.seed('seeds/chitter_library.sql')

#### temp for testing, to delete
rows = connection.execute('SELECT * FROM users;')
for row in rows:
    print(row)
####