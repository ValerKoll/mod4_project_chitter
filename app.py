from lib.database_connection import DatabaseConnection
from flask import Flask, request

app = Flask(__name__)

connection = DatabaseConnection()
connection.connect()

connection.seed('seeds/chitter_library.sql')

#### temp for testing, to delete
rows = connection.execute('SELECT * FROM users;')
for row in rows:
    print(row)
####