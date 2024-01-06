from lib.post_repository import Post_repository
from lib.post import Post

"""
calling ALL() 
returns the all list of posts
"""
def test_returns_list_of_all_posts(db_connection):
    db_connection.seed("seeds/chitter_library.sql")
    post_repository = Post_repository(db_connection)
    
    result = post_repository.all()
    expected = [
        Post(1, 'This is great', 'The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions', 1, '2023-12-09 12:20'),
        Post(2, 'title 2', 'Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpo...', 2, '2023-12-10 13:10'),
        Post(3, 'My motorbike', 'Always one of the most stylish and fun of the retro scrambler breed, the only let-down for the Fantic Caballero 500 was the meagre performance of its somewhat lumpy single-cylinder engine. This new 7...', 3, '2023-12-13 14:50'),
        Post(4, 'Contact me now for more', 'This new 700 is a follow-up to the original, 2019 500cc single-cylinder version which was already a great starting point given its authentic retro-mod scrambler style, fun handling and decent quality...', 1, '2023-12-19 11:00')
        ]
    assert expected == result



        # "Post(1, This is great, The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions, 2023-12-09 12:20, 1)",
        # "Post(1, title 2, Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpose-built library, 2023-12-10 13:10, 1)",
        # "Post(1, My motorbike, Always one of the most stylish and fun of the retro scrambler breed, the only let-down for the Fantic Caballero 500 was the meagre performance of its somewhat lumpy single-cylinder engine. This new 700cc twin answers that criticism with more power, 2023-12-13 14:50, 1)",
        # "Post(1, Contact me now for more, This new 700 is a follow-up to the original, 2019 500cc single-cylinder version which was already a great starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-19 11:00, 1)"
        
"""
calling FIND()
given an USER ID  
returns instance of 1 user
"""
def test_given_post_id_return_post(db_connection):
    db_connection.seed("seeds/chitter_library.sql")
    post_repository = Post_repository(db_connection)
    
    post_id = 2
    result = post_repository.find(post_id)
    expected = True
    assert expected == result[0]
    expected = "Post(2, Title 2, Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpo..., 2, 2023-12-10 13:10)"
    assert expected == str(result[1])
    
    # post_repository.find id=99 #=>
    post_id = 99
    #result = post_repository.find(post_id)   
    # #error

"""
calling ADD()
given 1 instance of user 
check for DB integrity
  check if valid too
"""
def test_add_1_user_and_check_db(db_connection):
    db_connection.seed("seeds/chitter_library.sql")
    post_repository = Post_repository(db_connection)
    # post_repository.add #=>0, There never been better time, A new 700 is a follow-up to the original, 2019 500cc starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-21 12:00, 2) #=> True    IS_VALID!
    # post_repository.all() #=>[
    #Post(1, This is great, The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions, 2023-12-09 12:20, 1)
    #Post(1, title 2, Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpose-built library, 2023-12-10 13:10, 2)
    #Post(1, My motorbike, Always one of the most stylish and fun of the retro scrambler breed, the only let-down for the Fantic Caballero 500 was the meagre performance of its somewhat lumpy single-cylinder engine. This new 700cc twin answers that criticism with more power, 2023-12-13 14:50, 3)
    #Post(1, Contact me now for more, This new 700 is a follow-up to the original, 2019 500cc single-cylinder version which was already a great starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-19 11:00, 1)
    #Post(1, There never been better time, A new 700 is a follow-up to the original, 2019 500cc starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-21 12:00, 2)
