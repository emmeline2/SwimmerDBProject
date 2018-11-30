<?php

include "startSession.php" ;

// Fetching Values From URL
$loginEmailAddress = $_POST["loginEmailAddress"];
$loginPassword = $_POST["loginPassword"];

$connection = mysqli_connect("localhost","droppUserLogin2","cruznashcosmo","droppUserLogin1");
//check connection
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}

$EmailAddress = mysqli_real_escape_string( $connection , $loginEmailAddress);
$Password = md5(mysqli_real_escape_string( $connection , $loginPassword));
 
$checklogin = mysqli_query( $connection ,"SELECT * FROM UserDB WHERE EmailAddress = '".$EmailAddress."' AND Password = '".$Password."'");


if(mysqli_num_rows($checklogin) > 0)
{

    $row = mysqli_fetch_array($checklogin); //obtain the DB row of the matched user
    
    
    //assign _SESSION variables to values obtained from DB row
    $EmailAddress = $row['EmailAddress'];
    $_SESSION['EmailAddress'] = $EmailAddress;
    
    $Password = $row['Password'];
    $_SESSION['Password'] = $Password;
    
    $firstName = $row['FirstName'];
    $_SESSION['FirstName'] = $firstName;
    
    $lastName = $row['LastName'];
    $_SESSION['LastName'] = $lastName; 

	$phoneNumber = $row['PhoneNumber'];
	$_SESSION['PhoneNumber'] = $phoneNumber;
	
    $_SESSION['LoggedIn'] = 1;

    echo "success";
}
?>