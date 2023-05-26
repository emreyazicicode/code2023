/* comment
Columns:
	id	int AI PK   AI = Auto_incrment (automatically increments!!, 1,2,3,4,5)
	firstname	varchar(45)  NN
	lastname	varchar(45)  NN
	gender	enum('female','male') NN
	dob	date 
	email	varchar(45)
	address	varchar(100)
*/

/*
USE `code`;
Switching to database
Makes the "database" active
*/
INSERT INTO `student`  
(`firstname`, `lastname`, `gender`) VALUES ('Ahmet', 'YILMAZ', 'male');



/* Reserved keywords: from to 
FLIGHT --> flightnumber, from, to, user, create, as, after, account, left
*/


/* Insert an item to student table with columns firstname,
   lastname and gender with values 'Ahmet', 'YILMAZ', 'male'.
 */

/*
	NOTE: SQL Statements (codes) can be splitted into multiple lines!!
    NOTE: Every SQL statement must have ";" semicolon at the end.
    NOTE: SQL Syntax is similar in Sql server, Mysql, Oracle, Postgresql
    NOTE: For the names, use ` where necessary
    NOTE: ` makes a string "text" avoids keywords
*/

SELECT * FROM student;
/* SELECT = fetch = bring = list*/
/* * = what to bring (* = all, all columns) */
/* FROM, HARADAN, NERDEN */
/* student */


INSERT INTO `student`  
(`firstname`, `lastname`, `gender`) 
VALUES 
('Mahmizər', 'Həsənova', 'female'),
('Mədinə', 'Abdulsəmədova', 'female'),
('Adil', 'Rəhimov', 'male'),
('Rafiq', 'Rafiqzadə', 'male'),
('Anar','Əhmədov','male'),
('Minəxanım','Hacımuradova','female'),
('Riyad','Əhmədov','male'),
('Riyad','Əbdürəhimov','male'),
('Lalə','Məmmədli','female'),
('İlyas','Abbasov','male'),
('Yusif','Ağasalamlı','male'),
('Ləman','Rəhimli','female'),
('Həbibə','Məmmədli','female'),
('Lala','Taghiyeva','female'),
('Niyyət','Rzayev','female');


DELETE FROM `student`; /* deletes all rows !! */

/* WHERE = HARADA? NEREDE = OYLE KI | SUCH THAT */

/*
WORK BENCH
Error Code: 1175. 
You are using safe update mode and you tried to update a table without a 
WHERE that uses a KEY column.  
To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.
*/


DELETE FROM `student` 
WHERE id = 32;

/* Student tablosundan SIL, oyle ki (such that) id = 32 olsun
id = 32 olanlari sil */

SELECT * FROM `student`
WHERE gender = 'male';


SELECT * FROM `student`
WHERE firstname = 'Riyad';



SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE 
	(NOT cityid = 99)
    AND
    (maritialstatus = 'single')
    AND
    (militarystatus = 'completed')
LIMIT 10;




SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
LIMIT 15;

/* LIMIT 15;  === LIMIT 0, 15; */

SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
LIMIT 50, 25; /* 50 ile 75 inci record*/






SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE bloodtype = 'A'
LIMIT 0, 25; /* 50 ile 75 inci record*/

/*
python 
x[0:25]
*/


SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE bloodtype = 'A'
LIMIT 242, 10;


SELECT COUNT(*) FROM `Nefer` WHERE bloodtype = 'A';
/* Returns the number of rows with filter */


SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE bloodtype = 'A'
LIMIT 200, 50;




SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
LIMIT 200, 50;



SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE maritialstatus = 'single' OR maritialstatus = 'divorced'
LIMIT 10;

/* HER QUERY'YE MUTLAKA LIMIT KOYALIM */


/* Nefer tablosundan, id, FIN.... kolonlarini sec, oyle ki, maritial status 
single veya divorced olsun, sonuclari, birthdate e gore sirala, sadece 100 kayit goster
 */
SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE maritialstatus = 'single' OR maritialstatus = 'divorced'
ORDER BY birthdate
LIMIT 100;




SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE maritialstatus = 'single' OR maritialstatus = 'divorced'
ORDER BY birthdate, cityid
LIMIT 100;


/* sonuclari, birthdate e gore sirala, sonra city id'ye gore tersten sirala */
SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE maritialstatus = 'single' OR maritialstatus = 'divorced'
ORDER BY birthdate, cityid DESC
LIMIT 100;



SELECT firstname, lastname
FROM `Nefer`
LIMIT 1000;

/*
   tekil, yegane, unique, distinct
   l = ['Ahmet', 'Mehmet', 'Mehmet']
   l = list(set(l))
 */

SELECT DISTINCT firstname, lastname, bloodtype
FROM `Nefer`
LIMIT 1000;


SELECT DISTINCT cityid FROM `Nefer` LIMIT 1000;




SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE NOT cityid IN (43, 73, 84)
ORDER BY birthdate
LIMIT 100;



SELECT id, FIN, firstname, lastname, gender, birthdate, cityid, maritialstatus, militarystatus, bloodtype
FROM `Nefer`
WHERE MOD(cityid, 10) = 1 
ORDER BY birthdate
LIMIT 100;



SELECT * FROM `Nefer` 
WHERE cityid >= 50
LIMIT 100;



SELECT * FROM `Nefer` 
WHERE cityid BETWEEN 50 AND 60
LIMIT 100;


a = 50
a = "50"

SELECT CAST(cityid as CHAR(50)) FROM `Nefer` 
LIMIT 100;

/* SQL = Structure query language */




SELECT * 
FROM `Nefer` 
WHERE (cityid IS NULL) OR (cityid > 50) /* condition */
LIMIT 100;

/* cityid = NULL 
   cityid IS NULL
   ISNULL(cityid)
*/


SELECT * FROM `Nefer`
WHERE firstname LIKE 'R%' /* REGEX LIKE */
LIMIT 10;

/* LIKE TAN SONRA REGEX GIBI !! BIR IFADE YAZILIR
	'R%' ==> buradaki % isareti, regex deki "*" gibidir
    
 */

SELECT * FROM `Nefer`
WHERE firstname LIKE '%a' /* REGEX LIKE */
LIMIT 10;


SELECT * FROM `Nefer`
WHERE firstname LIKE 'R%a' /* REGEX LIKE */
LIMIT 10;


/*
	TRUNCATE
    RELATION
    NORMALIZATION
    RELATIONAL ALGEBRA
*/


/*
https://dev.mysql.com/doc/refman/8.0/en/comparison-operators.html
*/