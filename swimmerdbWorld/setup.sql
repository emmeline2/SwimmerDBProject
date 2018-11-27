--create database and user

create database swimmerdb_project; 
create user 'emmeline'@'localhost' identified by 'eecs341pass'; 
grant all on swimmerdb_project.* to 'emmeline'@'localhost'; 
flush privileges; 


--create tables 

use swimmerdb_project; 
CREATE TABLE entry_reccord(
	id int(11) not null, 
	name varchar(50) not null, 
	stroke varchar(50), 
	time decimal(2,5),
	int distance
); 

CREATE TABLE person(
  	id int not null auto_increment primary key,
  	name varchar(50) not null,
  	username varchar(50) not null,
  	password varchar(50) not null,
	has_role varchar(50) not null
);


--adding data in people database 
INSERT INTO person VALUES (122,'Emmeline Pearson','epearson','pass123', 'SWIMMER');
INSERT INTO person VALUES (3048,'Sean Mann','smann','pass1234', 'SWIMMER');
INSERT INTO person VALUES (2083,'Bhavya Kumaran','bkumaran','pass321', 'COACH');
INSERT INTO person VALUES (1835,'Helen Liu','hliu','pass3', 'COACH');

--insert into records/entries