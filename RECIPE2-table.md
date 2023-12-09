# Database/Tables Design Recipe





>>>>>> TO BE CONTINUED

Database: ... <br>
Database: ..._test <br>

## 1. Extract nouns from the user stories or specification

```
User: "I want insert a new entry in the table albums"
```

```
>>> Nouns:
>>>  album, title, release year
```

## 2. Set Table Name and Columns

| table `albums`        | Properties              |
| --------------------- | ----------------------- |
|                       | `title`                 |
|                       | `release year`          |
|                       | `artist_id`             |




## 3. column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

id: SERIAL
title: VARCHAR(255)
release_year: int
artist_id: int



## 4. SQL

```sql
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  release_year INTEGER
  artist_id INTEGER
);

```

## 5. table (if needs)

```bash
psql -h 127.0.0.1 database_name < music_library2.sql
```
## 6. seed the table (if needs) 

"""
call seed('file.sql')
"""