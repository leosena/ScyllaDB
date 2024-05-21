CREATE KEYSPACE teste
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE teste;

CREATE TABLE segmentation (
    person_code INT PRIMARY KEY,
    segmentation_id INT
);

CREATE TABLE people (
    person_code INT PRIMARY KEY,
    person_id UUID
);

CREATE TABLE people_final (
        person_id INT,
        person_code INT,
        segmentation_id INT,
        PRIMARY KEY(person_code)
);

INSERT INTO segmentation (person_code, segmentation_id) VALUES (12345, 1);
INSERT INTO segmentation (person_code, segmentation_id) VALUES (23456, 1);
INSERT INTO segmentation (person_code, segmentation_id) VALUES (42343, 1);


INSERT INTO segmentation (person_code, segmentation_id, person_id) VALUES (54322, 1, uuid());

INSERT INTO people (person_code, person_id) VALUES (12345, uuid());
INSERT INTO people (person_code, person_id) VALUES (23456, uuid());
 