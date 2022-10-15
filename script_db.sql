-- Database creation
CREATE DATABASE app_flask_db;
use app_flask_db;

-- Table creation
CREATE TABLE the_article(
    id INTEGER PRIMARY KEY,
    title VARCHAR(50),
    body VARCHAR(600),
    author VARCHAR(50),
    created_date DATE
);
