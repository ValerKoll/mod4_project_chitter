-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  username VARCHAR(255),
  password VARCHAR(255)
);
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  content VARCHAR(255),
  time_stamp VARCHAR(255),
  user_id INTEGER
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, username, password) VALUES ('Peter Pan', 'peterpan', 'peter&1234');
INSERT INTO users (name, username, password) VALUES ('Jenny Mill', 'notsoFar', 'docker£1234');
INSERT INTO users (name, username, password) VALUES ('kevin Tosh', 'kevin-90', 'linux456789!');

INSERT INTO posts (title, content, time_stamp, user_id) VALUES ('This is great', 'The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions', '2023-12-09 12:20', 1);
INSERT INTO posts (title, content, time_stamp, user_id) VALUES ('title 2', 'Great answer, and comments highlight that in python not everything behaves the way you need it to, but there-s always convenient ways to make it so. The most convenient way is often importing a purpose-built library', '2023-12-10 13:10', 1);  
INSERT INTO posts (title, content, time_stamp, user_id) VALUES ('My motorbike', 'Always one of the most stylish and fun of the retro scrambler breed, the only let-down for the Fantic Caballero 500 was the meagre performance of its somewhat lumpy single-cylinder engine. This new 700cc twin answers that criticism with more power', '2023-12-13 14:50', 1);
INSERT INTO posts (title, content, time_stamp, user_id) VALUES ('Contact me now for more', 'This new 700 is a follow-up to the original, 2019 500cc single-cylinder version which was already a great starting point given its authentic retro-mod scrambler style, fun handling and decent quality. This new 700 builds on that with extra ', '2023-12-19 11:00', 1);





