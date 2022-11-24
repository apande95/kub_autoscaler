CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

CREATE DATABASE userdb;

GRANT ALL PRIVILEGES ON userdb.* TO 'admin'@'localhost';

USE userdb;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    uname VARCHAR(255) NOT NULL,
    password VARCHoAR(255) NOT NULL
);

INSERT INTO user (uname, password) VALUES ('admin1','admin1');
INSERT INTO user (uname, password) VALUES ('admin2','admin2');
INSERT INTO user (uname, password) VALUES ('admin3','admin3');
INSERT INTO user (uname, password) VALUES ('admin4','admin4');
INSERT INTO user (uname, password) VALUES ('admin5','admin5');
INSERT INTO user (uname, password) VALUES ('admin6','admin6');
INSERT INTO user (uname, password) VALUES ('admin7','admin7');
INSERT INTO user (uname, password) VALUES ('admin8','admin8');
INSERT INTO user (uname, password) VALUES ('admin9','admin9');
INSERT INTO user (uname, password) VALUES ('admin10','admin10');
INSERT INTO user (uname, password) VALUES ('admin11','admin11');
INSERT INTO user (uname, password) VALUES ('admin12','admin12');
INSERT INTO user (uname, password) VALUES ('admin13','admin13');
