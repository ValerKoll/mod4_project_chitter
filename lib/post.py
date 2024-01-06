from datetime import datetime

class Post():
    def __init__(self, id, title, content, user_id, time_stamp=None):
        self.id = id
        self.title = self.validate_title(title.strip())
        self.content = self.validate_content(content.strip())
        self.time_stamp = self.add_timestamp(time_stamp)
        self.user_id = user_id

    def is_valid(self):
        return all([
            self.id is not None,
            self.title is not None,
            self.content is not None,
            self.time_stamp is not None,
            self.user_id is not None
            ])
    
    def validate_title(self, text_to_check):
        if len(text_to_check) >= 3:
            return self.format_title(text_to_check)
        return None
    
    def validate_content(self, text_to_check):
        if len(text_to_check) >= 3:
            return self.format_content(text_to_check)
        return None
    
    # trunc content to 200 letters
    def format_title(self, text_to_convert):
        text_to_return = text_to_convert.title()
        if len(text_to_return) > 30:
            text_to_return = text_to_return[:29]
        return text_to_return
        
    # trunc content to 200 letters
    def format_content(self, text_to_convert):
        text_to_return = text_to_convert[0].capitalize() + text_to_convert[1:]
        if len(text_to_return) > 200:
            text_to_return = text_to_return[:199] + "..."
        return text_to_return
    
    # returns the instance value if not None
    #   otherwise set the current timestamp, for ie:2023-12-23 12:20
    def add_timestamp(self, time_stamp):
        if not(time_stamp):
            now = datetime.now()
            return now.strftime('%Y-%m-%d %H:%M')
        return time_stamp
        
    def __eq__(self, other):   # => for testing only
        return self.__dict__ == other.__dict__
    
    def __repr__(self): # => for testing and CLI printout
        return f"Post({self.id}, {self.title}, {self.content}, {self.user_id}, {self.time_stamp})"
    