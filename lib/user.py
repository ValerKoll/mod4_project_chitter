class User():
    def __init__(self, id, name, username, password):
        self.id = id   # to implement checks
        self.name = name.strip() # to implement checks
        self.username = self.validate_username(username.strip())
        self.password = self.validate_password(password.strip())
    
    def is_valid(self):
        return all([
            self.id is not None,
            self.name is not None,
            self.username is not None,
            self.password is not None
            ])
    
    def validate_username(self, text_to_check):
        if all([
            len(text_to_check) >= 3,
            len(text_to_check) <= 12,
            not(text_to_check[0].isdigit()),
            self.check_fragmentation(text_to_check)
            ]):
            return text_to_check
        else:
            return None
    
    def validate_password(self, text_to_check):
        if all([
            len(text_to_check) >= 10,
            len(text_to_check) <= 20,
            self.check_fragmentation(text_to_check)
            ]):
            return text_to_check
        return None
    
    def check_fragmentation(self, text_to_check):
        return len(''.join(text_to_check.split())) == len(text_to_check)
         
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.username}, {self.password})"