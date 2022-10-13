-- Database creation
CREATE DATABASE app_flask_db;
use app_flask_db;

-- Table creation
CREATE TABLE the_article(
    id INTEGER PRIMARY KEY,
    body VARCHAR(300),
    author VARCHAR(50),
    created_date DATETIME
);
