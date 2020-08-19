-- Users table for admin users

DROP TABLE IF EXISTS blogs;
DROP TABLE IF EXISTS contributors;
DROP TABLE IF EXISTS users;

--TODO make tables collaberate together via blog posts, and contributor posts

-- Users
CREATE TABLE users (
  id bigserial PRIMARY KEY,
  email varchar(100) UNIQUE NOT NULL ,
  password varchar(100) NOT NULL,
);

-- Blog Posts

CREATE TABLE blogPosts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES users (id)
)

-- Contributors

CREATE TABLE contributors (
  id bigserial PRIMARY KEY,
  amount varchar(100) NOT NULL,
  excerpt varchar(500) NOT NULL,
)

CREATE TABLE contributorImages (

  id INT PRIMARY KEY ,
  name TEXT NOT NULL ,
  photo bytea NOT NULL
}
