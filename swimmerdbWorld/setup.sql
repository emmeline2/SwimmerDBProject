--create database and user

create database webdatabase; 
create user 'emmeline'@'localhost' identified by 'eecs341pass'; 
grant all on webdatabase.* to 'emmeline'@'localhost'; 
flush privileges; 


--create tables 

use webdatabase; 

CREATE TABLE entry(
	entry_id int(11) not null, 
	swimmer_id int(11) not null, 
	stroke varchar(50), 
	time decimal(2,5),
	int distance
); 

CREATE TABLE person(
  	id int(10) not null primary key,
  	name varchar(50) not null,
  	username varchar(50) not null,
  	password varchar(50) not null,
	has_role varchar(50) not null
);


--adding data in people database 
INSERT INTO person VALUES (1,'a','a','a', 'SWIMMER');
INSERT INTO person VALUES (122,'Emmeline Pearson','epearson','pass123', 'SWIMMER');
INSERT INTO person VALUES (3048,'Sean Mann','smann','pass1234', 'SWIMMER');
INSERT INTO person VALUES (2083,'Bhavya Kumaran','bkumaran','pass321', 'COACH');
INSERT INTO person VALUES (1835,'Helen Liu','hliu','pass3', 'COACH');

--insert into records/entries
INSERT INTO entry VALUES (122, 'freestyle', 41.11, 100 );
INSERT INTO entry VALUES (122, 'backstroke', 19.19, 50 );  
INSERT INTO entry VALUES (122, 'butterfly', 22.47, 50 );
INSERT INTO entry VALUES (3048, 'freestyle', 24.30, 50 );
INSERT INTO entry VALUES (3048, 'freestyle', 58.71, 100 );
INSERT INTO entry VALUES (2083, 'freestyle', 19.83, 50 );
INSERT INTO entry VALUES (2083, 'breaststroke', 21.98, 50);
INSERT INTO entry VALUES (1835, 'butterfly', 30.21, 50 );
INSERT INTO entry VALUES (1835, 'freestyle', 78.11, 200 );
INSERT INTO entry VALUES (1835, 'breaststroke', 24.98, 50);

