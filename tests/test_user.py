from lib.user import User


"""
give a correct id, name, username and password
returns true and store a correct instance
"""
def test_give_right_parameters():
    user = User(1, "Peter Pan", "petpan", "password123")
    assert str(user) == "User(1, Peter Pan, petpan, password123)"

"""
give 2 instance of user
returns true if the 2 instances contains same values
"""
def test_give_2_instances_compare_result():
    user1 = User(1, "Peter Pan", "petpan", "password123")
    user2 = User(1, "Peter Pan", "petpan", "password123")
    assert (user1 == user2) == True

"""
give an incorrect username and/or incorrect name and/or incorrect password
returns False or True accordingly
"""
def test_incorrent_values():
    # check (len >= 3 & <= 12), (alphanumeric chars only), (later stage: unique)
    #
    #too short
    user = User(1, "Peter Pan", "pn", "password123")
    assert user.is_valid_username()  == False
    #start with 1 digit 
    user = User(1, "Peter Pan", "1eter32", "password32")
    assert user.is_valid_username()  == False
    #correct input
    user = User(1, "Peter Pan", "peter32", "passw£!?d123")
    assert user.is_valid_username()  == True
    #too long
    user = User(1, "Peter Pan", "peter32morethan12", "passw£!?d123")
    assert user.is_valid_username()  == False

"""
give a name or a username with an empty space at the begining or the end
returns username without spaces
"""
def test_remove_empty_spaces():
    user = User(1, "  Peter Pan ", " peter23 ", "password123")
    assert user.name  == "Peter Pan"
    assert user.username  == "peter23"

"""
give an username with an empty space in between 2+ words
check for an input with a single word
returns False
"""
def test_remove_empty_spaces():
    # peter _space_ 23 not be accepted
    user = User(1, "Peter Pan", " peter 23 ", "password123")
    assert user.is_valid_password()  == False
    # peter23 with not space ==> ok
    user = User(1, "Peter Pan", " peter23 ", "password123")
    assert user.is_valid_password()  == True

"""
give an username with:
    wrong chars,
    too short or too long,
    including special chars without '%','&','!','?',
    not containing at least 1+ digit
returns False
"""



"""
give an incorrect username and/or incorrect name and/or incorrect password
returns an "error message" accordingly
"""
# user = User(1, "Peter Pan", "pn", "password123")
# user.generate_errors  #=> username too short
# user = User(1, "Peter Pan", "peter32", "passwo")
# user.generate_errors  #=> password too short
# user = User(1, "Peter Pan", "peter32", "passwordpeter")
# user.generate_errors  #=> incorrect password
# [...]