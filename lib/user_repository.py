from lib.user import User

class User_repository():    
    def __init__(self, connection):
        self._connection = connection
    
    def get_users(self):
        rows = self._connection.execute('SELECT * FROM users')
        list_to_return = []
        for row in rows:
            entry = User(row["id"], row["name"], row["username"], row["password"])
            list_to_return.append(entry)
        if len(list_to_return):
            return list_to_return
        
    def add_user(self, user):
        if user.is_valid():
            self._connection.execute('INSERT INTO users (name, username, password) VALUES (%s, %s, %s)', [user.name, user.username, user.password])
            return True
        return False