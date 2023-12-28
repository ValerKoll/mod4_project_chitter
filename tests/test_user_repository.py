from lib.user_repository import User_repository
from lib.user import User

"""
calling ALL() 
returns the right list of users
"""
def test_returns_list_of_users(db_connection):
    db_connection.seed("seeds/chitter_library.sql")
    user_repository = User_repository(db_connection)
    
    expected = [
        User(1, 'Peter Pan', 'peterpan', 'peter&1234'),
        User(2, 'Jenny Mill', 'notsoFar', 'docker£1234'),
        User(3, 'kevin Tosh', 'kevin-90', 'linux456789!')
        ]
    result = user_repository.get_users() 
    assert result == expected

"""
calling ADD()
given 1 instance of user 
check for DB integrity
  check if valid too
"""
def test_add_1_user_and_check_db(db_connection):
    db_connection.seed("seeds/chitter_library.sql")
    user_repository = User_repository(db_connection)
    user = User(0, "Micheal Bubble", "mike123BUB", "rndnowtv1234")
    
    result = user_repository.add_user(user)
    expected = True
    assert result == expected
    
    expected = [
    User(1, 'Peter Pan', 'peterpan', 'peter&1234'),
    User(2, 'Jenny Mill', 'notsoFar', 'docker£1234'),
    User(3, 'kevin Tosh', 'kevin-90', 'linux456789!'),
    User(4, "Micheal Bubble", "mike123BUB", "rndnowtv1234")
    ]
    result = user_repository.get_users() 
    assert result == expected
    
"""
given an incorrect username and/or incorrect name and/or incorrect password
returns some "error message" accordingly
"""
def test_check_error_messages(db_connection):
    db_connection.seed("seeds/chitter_library.sql")
    user_repository = User_repository(db_connection)
    user = User(0, "Peter Pan", "pn", "password123")
    
    result = user_repository.add_user(user)
    expected = False
    assert result == expected
    
    result = ', '.join(user.errors)
    expected = "wrong username input"
    assert result == expected
    
    
    #result = user_repository.add_user(User(1, "Peter Pan", "peter32", #"passwo"))
    #expected = "wrong password input"
    #assert expected == result
    #
    #result = user_repository.add_user(User(1, "Peter Pan", "peter32", #"passwordpeter"))
    #expected =  "wrong password input"
    #assert expected == result
    #
    #result = user_repository.add_user(User(1, "Peter Pan", "p2", "p2"))
    #expected = "wrong username input, wrong password input"
    #assert expected == result
    #
    #result = user_repository.add_user(User(1, "P2", "p2", "p2"))
    #expected = "wrong name input, wrong username input, wrong password input"
    #assert expected == result