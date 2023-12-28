from datetime import datetime
from lib.post import Post


"""
given a correct id, title, content, user_id , #note: (timestamp to be added)
returns true and store a correct instance adding timestamp
"""
def test_given_right_parameters_return_right_string():
    post = Post(1, "My First Post", "I knew that too many rings have been left in Middle Earth", 1)
    now = datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M")
    assert str(post) == f"Post(1, My First Post, I knew that too many rings have been left in Middle Earth, {time_stamp}, 1)"

"""
give 2 instance of user
returns true if the 2 instances contains same values
"""
def test_give_2_instances_compare_result():
    post1 = Post(1, "My First Post", "I knew that too many rings have been left in Middle Earth", 1)
    post2 = Post(1, "My First Post", "I knew that too many rings have been left in Middle Earth", 1)
    assert (post1 == post2) == True

"""
given an incorret title / content
   correct title and content
returns true and store a correct instance adding timestamp
"""
def test_given_wrong_parameters_return_formated_string():
    # given title all small cap + 1 space
    now = datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M")
    post = Post(1, " my first post", "i knew that too many rings have been left in Middle Earth", 1)
    assert str(post) == f"Post(1, My First Post, I knew that too many rings have been left in Middle Earth, {time_stamp}, 1)"
    # given a too long title return 29chars
    post = Post(1, "My first post and very long title", "I knew that too many rings have been left in Middle Earth", 1)
    assert str(post) == f"Post(1, My First Post And Very Long T, I knew that too many rings have been left in Middle Earth, {time_stamp}, 1)"
    #given a too long content trunc to 200 chars adding ...
    post = Post(1, "my first post", "I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth", 1)
    assert str(post) == f"Post(1, My First Post, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many r..., {time_stamp}, 1)"
    
"""
given empty title and/or empty comment
returns None
"""
def test_empty_title_empty_content():
    post = Post(1, "", "I knew that too many rings have been left in Middle Earth", 1)
    assert post.is_valid() == False
    post = Post(1, "My first post", "", 1)
    assert post.is_valid() == False
    post = Post(1, "My3", "Co3", 1)
    assert post.is_valid() == True