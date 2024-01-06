# Route Design Recipe

CRUD\
create  (i.e.  add_users())\
read    (i.e.  get_users(), find_user())\
update  (i.e.  update_user())\
delete  (i.e.  delete_user())\
.

### 1. Setting the app flow
```
HOME PAGE
  LOGIN PAGE
```
### 2. Routes Design

 action       |ROUTE                      | url
--------------|---------------------------|--------------
   home page  |GET '/'                    |   'index.html'
   login      |GET '/account/login'       |   'account.html'
   register   |GET '/account/register'    |   'account.html'
   loggingIn  |POST '/user/login'         | '' --> 'index.html'
   registering|POST '/user/register'      | '' --> 'index.html'
   logout     |GET '/account/logout'      | '' -->  'index.html'
   sort_posts |GET '/<home_page_section>' |   'index.html'


```
# main page - no logged in
GET '/'
  arguments: None
  return MAIN PAGE showing:
    list of recent posts
    options to navigate
    link for login or username+logout 
  
  TESTS:
    Expected response: 200 (OK)
    expect(title) == 'Home Page' 
```
```
# log in page
GET '/account/<section>'
  arguments: None
  return account.html, sections [LOGIN PAGE, REGISTER PAGE]
    LOGIN PAGE showing:
      form --> POST '/user/login'   data=form data + set username
      cancel ---> GET '/'
    REGISTER PAGE showing:
      form --> POST '/user/register'    data=form data + set username
      cancel ---> GET '/'
  
  TESTS:
    Expected response: 200 (OK)
    expect(title) == 'Please Login' or expect(title) == 'Register' 

```
```
# ....page 
POST '/'
  Expected response: 200 (OK)
  Expected response: 

```


### 3. Implement Signature
```python
#########   HOME PAGE ROUTES   ######
@app.route('/', methods=['GET'])

#########   USERS ROUTE   ##########
@app.route('/users', methods=['GET'])

@app.route('/users', methods=['POST'])
####################################
```





## 4. Create Examples as Tests
```python
"""
Action:     GET request to '/'
Arguments:  None
Result:    200 (OK)
          'main - nologin'
"""
def test_main_page_nologin(web_client):
  response = web_client.get("/")
  response.status_code == 200
  #assert response.data.decode("utf-8") == "main - nologin"
  

>>>>>> TO BE CONTINUED



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

## . Test-drive the Route

see test_artists.py

