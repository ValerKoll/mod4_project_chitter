from lib.user import User

class User_repository():    
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        list_to_return = []
        for row in rows:
            entry = User(row["id"], row["name"], row["username"], row["passcode"])
            list_to_return.append(entry)
        if len(list_to_return):
            return list_to_return
    
    def find(self, username, password):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE (username = %s AND passcode = %s)", [username, password]
            )
        #'SELECT * from users WHERE username = %s AND password = %s', [username, password]
        # TODOs: Implement error checks insted of IF
        if rows:
            row = rows[0]
            user = User(row['id'], row['name'], row['username'], row['passcode'])
            if user.is_valid():
                return (True, user)
            return (False, 'Stored values not valid')
        return (False, "User not found")
    
    def add(self, id, name, username, password):
        user = User(id, name, username, password)
        if user.is_valid():
            self._connection.execute('INSERT INTO users (name, username, passcode) VALUES (%s, %s, %s)', [user.name, user.username, user.password])
            return (True, user)
        return (False, user.errors)
    
    def create(self, user):
        pass
    
    def delete(self, user_id):
        pass
    
    # use: account login form  -->> retrive user id 
    def login(self, id_to_match):
        return self.find(id_to_match)