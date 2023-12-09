# Route Design Recipe
## 1. Design the Route Signature



>>>>>> TO BE CONTINUED


```
# albums route
POST /albums
    `title:` string
    `release_year:` int
    `artist_id:` int

GET /artists
    'all' int 1 or 2
  Expected response: 200 (OK)
  Expected response: "Album(Pixies, Rock)\nAlbum(ABBA, Pop)\nAlbum(Taylor Swift, Pop)\nAlbum(Nina Simone, Jazz)\n"
  Expected response: 200 (OK)
  Expected response: "Pixies, ABBA, Taylor Swift, Nina Simone"


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

