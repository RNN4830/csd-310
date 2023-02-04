

/* Rachel Nelson
 02/04/2023
 Module 6.2 Assignment */

-- drop database user if exists
DROP USER IF EXISTS 'movies_user'@'localhost';


-- create movies_user and grant them all privileges to the movies database
CREATE USER 'movies_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'popcorn';

-- grant all privileges to the movies database to user movies_user on localhost
GRANT ALL PRIVILEGES ON movies.* TO 'movies_user'@'localhost';


CREATE TABLE imdb (
    imdb_id INT NOT NULL AUTO_INCREMENT,
    rating INT NOT NULL,
    film_id INT NOT NULL,
    PRIMARY KEY (imdb_id)
);

INSERT INTO imdb(rating, film_id)
VALUES('8', (SELECT film_id FROM film WHERE film_name = 'Gladiator'));
