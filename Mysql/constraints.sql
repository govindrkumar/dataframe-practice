USE TQData;
CREATE TABLE IF NOT EXISTS Class12
(
    Rollno INT PRIMARY KEY,
    NAME VARCHAR(20) NOT NULL,
    AGE INT DEFAULT 10,
    AADHARNO BIGINT UNIQUE KEY,
    CITY VARCHAR(20)
);

DESCRIBE Class12;

--Insert single row
INSERT INTO Class12
VALUES(101,"Don",12,2345672345,"Kota");

--Insert multiple rows
INSERT INTO Class12
VALUES (102, 'Suman', 12, 6785123434, 'Kota'),
(103, 'Radha', 12, 2312234563, 'SialKota'),
(104, 'Komal', 13, 5678901234, 'Patna');

--Unique can be null too
SELECT * FROM Class12;
SELECT AGE,Rollno FROM Class12;

-- Insert into specific column
INSERT INTO Class12 (Rollno, NAME) 
VALUES (107, "Govind");

--Insert Null Values
INSERT INTO Class12 VALUES (108, 'Raman', 12, NULL, null);

--DAte and time
ALTER TABLE Class12
ADD DOB DATE;

ALTER TABLE Class12 
ADD EntryTime  TIME;

SELECT * FROM Class12;
