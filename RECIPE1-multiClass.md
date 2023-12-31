# === CHITTER === 
## Core design
<img src="static/tdd-iceberg.png">

### 1. User request

```
phase1
-------
I can let people know what I am doing
 >> post a message (peep) to chitter
I can see what others are saying
 >> see all peeps in reverse chronological order
I can better appreciate the context of a peep
 >> see the time at which it was made
I can post messages on Chitter as me
 >> sign up for Chitter


phase 2
--------
I can post messages on Chitter as me
 >> log in to Chitter
I can avoid others posting messages on Chitter as me
 >> log out of Chitter

phase 3
-------
I can stay constantly tapped in to the shouty box of Chitter
 >> receive an email if I am tagged in a Peep
```
### 2. Analysis
- post messages adding username
- retrive all messages showing main message and comments with usernames
- and add timestamp too
- add sign up functionality
- using log in and out
- add messaging service (advanced)


### 3. Design the Class System
>...\
>user_repository\
>user\
>post_repository\
>post\
>comment_repository\
>comment\
>...

<img src="static/_diagrams/chitter_diagram_ver01.png">

_excalidraw.com_


```
METHODS:
user_repository
    all
    find
    create
user
    __eq__
    __repr__
post_repository
    all
    find
    create
post
    __eq__
    __repr__
comment_repository
    all
    find
    create
comment
    __eq__
    __repr__
```
.\
.\
.
### 4. Implement code
```python
class user():
    # -> id, name, username, password
    # ACTION: check username lenght >= 3 & <= 12, only alpha chars, and set to be unique. ( it needs implementation with database-query)  
    # ACTION: check valid password=> can contain the chars %&!?,
    #    must be longer than 10 chars and contain at least 1 number

    def is_valid_username():
        # <- username
        # exe: check len >= 3 & <= 12, alphanumeric chars only,
        #       not startitng with a number
        #       call external function to check for uniqueness
        # -> True or False

    def is_valid_password():   # => check password validity
        # <- password
        # exe: check len >= 10 & <= 20, alpha chars + %&!?, 
        #       must have 1+ digit
        # -> True or False

    __eq__   # => for testing only 

    __repr__ # => for testing and CLI printout
#-------------------
class user_repository():
    # -> connection

    def all()
        # <- None
        # exe: fetch all data
        # -> a list of user instances
        pass
    def add()
        # <- 1 user instance
        # exe: add data - 1 entry
        # -> None
        pass
    def update()
        # <- 1 user instance
        # exe: add data - 1 entry
        # -> None
        pass
    def delete()
        # <- 1 user instance
        # exe: delete data - 1 entry
        # -> TRUE/false
        pass
    def find()
        # <- user id
        # exe: fetch data - 1 entry
        # -> 1 instance of user
        pass

#-------------------
class post():
    # -> id, title, content, time_stamp, user_id
    # ACTION: check and trunc content if lenght < 30 adding full stop
            # remove empty spaces from both side
            # CAP first letters of each words
    # ACTION: check and trunc content if lenght <= 200  adding "..."
            # remove empty spaces from both side
            # CAP first letter
    # ACTION: add timestamp

    def format_title():
        # <- title
        # exe: check len <= 30 and modify accordnly
    
    def format_content():
        # <- content
        # exe: check len <= 200 and modify accordnly
    
    def add_timestamp():
        # returns timestamp, for ie:2023-12-23 12:20

    __eq__   # => for testing only

    __repr__ # => for testin and CLI printout

#--------------------------
class post_repository():
    # -> connection

    def all()
        # <- user_id
        # exe: fetch data
        # -> a list of post instances
        pass

    def find()
        # <- post id, user id
        # exe: fetch data - 1 entry
        # -> 1 instance of post (connected to user)
        pass

    def add()
        # <- 1 post instance
        # exe: input data - 1 entry
        # -> None
        pass

#-------------------
class comment():
    # -> id, content, post_id
    # ACTION: check and trunc content if its lenght <= 200 adding "..."
            # remove empty spaces from both side
            # CAP first letter
    
    def format_content():
        # <- comment
        # exe: check len <= 200 and modify accordnly

    __eq__   # => for testing only

    __repr__ # => for testin and CLI printout
#-------------------------
class comment_repository():
    # -> connection

    def all()
        # <- post_id
        # exe: fetch data
        # -> a list of comment instances
        pass
    def find()
        # <- comment id, post_id
        # exe: fetch data - 1 entry
        # -> 1 instance of comment (connected to post)
        pass
    def add()
        # <- 1 comment instance
        # exe: input data - 1 entry
        # -> None
        pass
#-------------------

```

### 5. Testing
>
#### a. Create Examples as Unit Tests

_List of tests of the behaviour of each relevant class at a more granular level of detail._



#### CLASS USER    =======================
```python
"""
given a correct id, name, username and password
returns true and store a correct instance
"""
user = User(1, "Peter Pan", "petpan", "password123")
str(user) # => "User(Peter Pan, trpan, password123)"

"""
given 2 instance of user
returns true if the 2 instances contains same values
"""
user1 = User(1, "Peter Pan", "petpan", "password123")
user2 = User(1, "Peter Pan", "petpan", "password123")
user1 == user2 # => True

"""
given an incorrect username and/or incorrect name and/or incorrect password
returns False or True accordingly
"""
user = User(1, "Peter Pan", "pn", "password123")
user.is_valid  #=> False
user = User(1, "Peter Pan", "peter32", "password32")
user.is_valid  #=> True
user = User(1, "Peter Pan", "peter32", "passw£!?d123")
user.is_valid  #=> True
[...]

"""
give a name or a username with an empty space at the begining or the end
returns username without spaces
"""
user = User(1, "  Peter Pan ", " peter23 ", "password123")
user.name # => "Peter Pan"
user.username  # => "peter23"

"""
given empty name or too short name <3
return None
"""
user = User(1, "", "peter23", "password£123")
user.isvalid #=>false
user = User(1, "Pe", "peter23", "password£123")
user.isvalid #=>false


"""
give an username with an empty space in between 2+ words
check for an input with a single word
returns False
"""
user = User(1, "Peter Pan", " peter 23 ", "password123")
user.is_valid # => False
user = User(1, "Peter Pan", " peter23 ", "password123")
user.is_valid # => True

"""
give an password with:
    wrong chars,
    too short or too long,
    not including special chars without '%','&','!','?',
    not containing at least 1+ digit
returns False
"""
user = User(1, "Peter Pan", "peter23", "pa")
user.is_valid() == False
user = User(1, "Peter Pan", "peter23", "passwordtoolongtoolong")
user.is_valid() == False
user = User(1, "Peter Pan", "peter23", "password123")
user.is_valid() == False
[...]


"""
given an incorrect username and/or incorrect name and/or incorrect password
returns some "error message" accordingly
"""
user = User(1, "Peter Pan", "pn", "password123")
user.generate_errors  #=>  "wrong username input"
user = User(1, "Peter Pan", "peter32", "passwo")
user.generate_errors  #=> "wrong password input"
user = User(1, "Peter Pan", "peter32", "passwordpeter")
user.generate_errors  #=> "wrong password input"
user = User(1, "Peter Pan", "p2", "p2")
user.generate_errors  #=> "wrong username input, wrong password input"
user = User(1, "P2", "p2", "p2")
user.generate_errors  #=> "wrong name input, wrong username input, wrong password input"
[...]


```


#### CLASS USER_REPOSITORY   =======================

```python
"""
calling ALL() 
returns the right list of users
"""
feed library
user_repository = User_repository()
user.all #=>[
#User(1, 'Peter Pan', 'peterpan', 'peter&1234'),
#User(2, 'Jenny Mill', 'notsoFar', 'docker£1234'),
#User(3, 'kevin Tosh', 'kevin-90', 'linux456789!')]


"""
calling FIND()
given an USER ID  
returns instance of 1 user
"""
feed library
user_repository = User_repository()
user.execute id=2 #=>
#User(2, 'Jenny Mill', 'notsoFar', 'docker£1234')
user.execute id=99 #=>
#error

"""
calling ADD()
given 1 instance of user 
check for DB integrity
  check if valid too
"""
user = User(0, "Micheal Bubble", "mike123BUB", "rndnowtv1234")
user_repository.add_user(user) #=> True    IS_VALID!
user_repository.get_users() #=>
#     User(1, 'Peter Pan', 'peterpan', 'peter&1234'),
#     User(2, 'Jenny Mill', 'notsoFar', 'docker£1234'),
#     User(3, 'kevin Tosh', 'kevin-90', 'linux456789!'),
#     User(4, "Micheal Bubble", "mike123BUB", "rndnowtv1234")

"""
calling UPDATE()
given user id
  check if valid too
"""

"""
calling DELETE()
given user id
  check if valid too
"""
```


#### CLASS POST ===================
```python
"""
given a correct id, title, content, user_id,    #note: (timestamp to be added)
returns true and store a correct instance adding timestamp
"""
post = post(1, "My first post", "I knew that too many rings have been left in Middle Earth", 1)
str(post) # => "Post(My First Post, I knew that too many rings have been left in Middle Earth, (current timestamp: 2023-12-23 12:20), 1)"

"""
given an incorret title / content
   correct title and content
returns true and store a correct instance adding timestamp
"""
post = post(1, "My first post", "I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth", 1)
str(post) # => "Post(My First Post, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many rings have been left in Middle Earth, I knew that too many r..., (current timestamp: 2023-12-23 12:20), 1)"
[...]

"""
given empty title and/or empty comment
returns None
"""
post = post(1, "", "I knew that too many rings have been left in Middle Earth", 1)
post.is_valid #=> False
post = post(1, "My first post", "", 1)
post.is_valid #=> False

```


#### CLASS POST_REPOSITORY ===================
```python
"""
calling ALL() 
returns the all list of posts
"""
feed library
post_repository = Post_repository()
post.all #=>[
#Post(1, This is great, The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions, 2023-12-09 12:20, 1)
#Post(1, title 2, Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpose-built library, 2023-12-10 13:10, 1)
#Post(1, My motorbike, Always one of the most stylish and fun of the retro scrambler breed, the only let-down for the Fantic Caballero 500 was the meagre performance of its somewhat lumpy single-cylinder engine. This new 700cc twin answers that criticism with more power, 2023-12-13 14:50, 1)
#Post(1, Contact me now for more, This new 700 is a follow-up to the original, 2019 500cc single-cylinder version which was already a great starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-19 11:00, 1)
#]


"""
calling FIND()
given an USER ID  
returns instance of 1 user
"""
feed library
post_repository = Post_repository()
post_repository.find id=2 #=>
#Post(1, title 2, Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpose-built library, 2023-12-10 13:10, 2)
post_repository.find id=99 #=>
#error

"""
calling ADD()
given 1 instance of user 
check for DB integrity
  check if valid too
"""
post_repository = Post_repository()
post_repository.add #=>0, There never been better time, A new 700 is a follow-up to the original, 2019 500cc starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-21 12:00, 2) #=> True    IS_VALID!
post_repository.all() #=>[
#Post(1, This is great, The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions, 2023-12-09 12:20, 1)
#Post(1, title 2, Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpose-built library, 2023-12-10 13:10, 2)
#Post(1, My motorbike, Always one of the most stylish and fun of the retro scrambler breed, the only let-down for the Fantic Caballero 500 was the meagre performance of its somewhat lumpy single-cylinder engine. This new 700cc twin answers that criticism with more power, 2023-12-13 14:50, 3)
#Post(1, Contact me now for more, This new 700 is a follow-up to the original, 2019 500cc single-cylinder version which was already a great starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-19 11:00, 1)
#Post(1, There never been better time, A new 700 is a follow-up to the original, 2019 500cc starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra, 2023-12-21 12:00, 2)


"""
calling UPDATE()
given user id
  check if valid too
"""
feed library
post_repository = Post_repository()

"""
calling DELETE()
given user id
  check if valid too
"""
feed library
post_repository = Post_repository()

```

===================
```python
CLASS COMMENT

```
===================
```python
CLASS COMMENT_REPOSITORY

```






>>>>>> TO BE CONTINUED


#### b. Create Examples as Integration Tests
_Create tests for the classes being used together in different situations and combinations that reflect the ways in which the system will be used_

```python
"""
When we add two users
We see those users reflected in the tracks list
"""
user_repo = UserRepository()
t = T("Carte Blanche", "Veracocha")
t2 = T("Synaesthesia", "The Thrillseekers")
library.add(t_1)
library.add(t_2)
library.users # => [u_1, u_2]
```


### 6. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

