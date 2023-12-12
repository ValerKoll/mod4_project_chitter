class User():
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name.strip()
        self.username = username.strip()
        self.password = password
    
    def is_valid_username(self):
        if all([
            len(self.username) >= 3,
            len(self.username) <= 12,
            not(self.username[0].isdigit())
            ]):
            return True
        else:
            return False
    
    def is_valid_password(self):
        if len(''.join(self.username.split())) == len(self.username):
            return True
        return False
         
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.username}, {self.password})"