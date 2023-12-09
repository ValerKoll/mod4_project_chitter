# === CHITTER === 
## core design

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
### 2. Analsys
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

<img src="static/chitter diagram ver 01.png">

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
### 4. Implement code
```python
class user_repository():
    # -> connection

    def all()
        # <- None
        # exe: fetch data
        # -> a list of user instances
        pass
    def find()
        # <- user id
        # exe: fetch data - 1 entry
        # -> 1 instance of user
        pass
    def add()
        # <- 1 user instance
        # exe: input data - 1 entry
        # -> None
        pass
#-------------------
class user():
    # -> id, name, username, password

    __eq__
    __repr__
#-------------------
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
class post():
    # -> id, title, content, time_stamp, user_id

    __eq__
    __repr__
#--------------------------
class comment_repository()
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
class comment():
    # -> id, content, post_id

    __eq__
    __repr__
#-------------------------

```

>>>>>> TO BE CONTINUED

### 5. Testing
#### a. Create Examples as Integration Tests
`==========================`\
_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMple

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

#### b. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

