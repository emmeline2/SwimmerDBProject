--create database and user

create database swimmerdb_project; 
create user 'emmeline'@'localhost' identified by 'eecs341pass'; 
grant all on swimmerdb_project.* to 'emmeline'@'localhost'; 
flush privileges; 


--create tables 

use swimmerdb_project; 
create table entry(
	id int(11) not null, 
	name varchar(50) not null, 
	stroke varchar(50), 
	time decimal(2,5),
	int distance
); 

CREATE TABLE swimmers(
  	id int(11) DEFAULT NULL,
  	name varchar(50) DEFAULT NULL,
  	username varchar(50) DEFAULT NULL,
  	password varchar(50) DEFAULT NULL
);

CREATE TABLE coach(
  	id int(11) DEFAULT NULL,
  	name varchar(50) DEFAULT NULL,
  	username varchar(50) DEFAULT NULL,
  	password varchar(50) DEFAULT NULL
); 

INSERT INTO swimmers VALUES (122,'Emmeline Pearson','epearson','pass123'),
	(3048,'Sean Mann','smann','pass1234'),
	(2083,'Bhavya Kumaran','bkumaran','pass321'),
	(1835,'Helen Liu','hliu','pass3');