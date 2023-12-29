# Route Design Recipe

CRUD\
create  (i.e.  add_users())\
read    (i.e.  get_users(), find_user())\
update  (i.e.  update_user())\
delete  (i.e.  delete_user())\
.

### 1. Design the Routes

```
# retrive all users
GET /users
  Expected response: 200 (OK)
  Expected response: "User(1, 'Peter Pan', 'peterpan', 'peter&1234')\nUser(2, 'Jenny Mill', 'notsoFar', 'docker£1234')\nUser(3, 'kevin Tosh', 'kevin-90', 'linux456789!')"

# add 1 user
POST /users
    `name` string
    `username` int
    `password` int
  Expected response: 200 (OK)
  Expected response: ''
```

### 2. Implement Signature
```python
#########   USERS ROUTE   ##########
@app.route('/users', methods=['GET'])
  request.args['']   #return value for ..?id=1  ---> ['id']

@app.route('/users', methods=['POST'])
  request.form['name', 'username', 'password']
####################################
```

>>>>>> TO BE CONTINUED



## 2. Create Examples as Tests
```python
"""
given: Voyage & 2022 & 2
 action: 1.add new entry to albums
         2.read all the albums' entries
 returns: 200 (OK)
          updated list of albums
"""
POST /albums
    title=Voyage
    release_year=2022
    artist_id=2
  Expected response: 200 (OK)
  Expected response: "Voyage, 2022, 2"

"""
given: Voyage & 2022 & null
 action: 1.DON'T add new entry to albums
         2.read all the albums' entries
 returns: 400 (BAD_REQUEST)
          A NOT updated list of albums
"""
POST /albums
    title=Voyage
    release_year=2022
    #artist_id=2
  Expected response: 400
  Expected response: "Voyage, 2022, 2"


"""
given: all=1 or 2
 action: 1.read all the artists' entries
 returns: 200 (OK)
          a list of artists
"""
GET /artists
    'all' int 1 or 2
  Expected response: 200 (OK)
  Expected response: "Album(Pixies, Rock)\nAlbum(ABBA, Pop)\nAlbum(Taylor Swift, Pop)\nAlbum(Nina Simone, Jazz)\n"
  Expected response: 200 (OK)
  Expected response: "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
given: name=Wild nothing & genre=Indie
  action: 1.add 1 entry to the artists table
          2.read all the artists' entries using GET
 returns: 200 (OK)
          a list of artists
"""

POST /artists
    'name' string 
    'genre' string
  Expected response: 200 (OK)
  Expected response: ''

GET /artists
    'all' int = 2
  Expected response: 200 (OK)
  Expected response: "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"



```

## 3. Test-drive the Route

see test_artists.py

