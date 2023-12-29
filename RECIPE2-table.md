# Database/Tables Design Recipe


### 1. Extract nouns from the user request

```
(from RECIPE1 Analysis)
- post messages adding username
- retrive all messages showing main message and comments with usernames
- and add timestamp too
- add sign up functionality
- using log in and out
- add messaging service (advanced)
```


```
Nouns:
>>>  users, posts, comments, time,
>>>  sign up, log in, log out, send emails

```

### 2. Set DB names, Table Names and Fields

Database: chitter_library <br>
Database: chitter_library_test <br>


| table `users`   | Properties             | data  type |
| --------------- | ---------------------- |------------|
|                 | `id`                   | SERIAL     |
|                 | `name`                 | VARCHAR    |
|                 | `username`             | VARCHAR    |
|                 | `password`             | VARCHAR    |

| table `posts`   | Properties             | data  type |
| --------------- | ---------------------- |------------|
|                 | `id`                   | SERIAL     |
|                 | `title`                | VARCHAR    |
|                 | `comment`              | VARCHAR    |
|                 | `time_stamp`           | VARCHAR    |
|                 | `user_id`              | INTEGER    |

[...]



[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).



### 3. Deploy the SQL

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  username VARCHAR(255),
  password VARCHAR(255)
);
INSERT INTO users (name, username, password) VALUES (, );

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  content VARCHAR(255)
  time_stamp VARCHAR(255)
  user_id INTEGER
);
INSERT INTO posts (title, content, time_stamp, user_id) VALUES (, );  # DATE ='YYYY-MM-DD HH:MM'

```
>>>>>> TO BE CONTINUED

### 5. create the table

```bash
psql -h 127.0.0.1 chitter_library < chitter_library.sql
psql -h 127.0.0.1 chitter_library_test < chitter_library.sql
```
## 6. seed the table (if needs) 

"""
call seed('file.sql')
"""