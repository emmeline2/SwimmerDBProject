<?php
session_start();
 
$dbhost = "localhost"; // this will ususally be 'localhost', but can sometimes differ
$dbname = "dbwebproject"; // the name of the database that you are going to use for this project
$dbuser = "new_user"; // the username that you created, or were given, to access your database
$dbpass = "db2018"; // the password that you created, or were given, to access your database
 
$connection = mysql_connect($dbhost, $dbuser, $dbpass) or die("mysqlii Error: " . mysql_error());
mysql_select_db($connection, $dbname) or die("mysql Error: " . mysql_error());


/* To go in server
CREATE TABLE `UserDB` (
`UserID` INT(25) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
`Password` VARCHAR(32) NOT NULL ,
`EmailAddress` VARCHAR(32) NOT NULL ,
`FirstName` VARCHAR(32) NOT NULL ,
`LastName` VARCHAR(32) NOT NULL , 
`PhoneNumber` INT(11) NOT NULL
);
*/
?>