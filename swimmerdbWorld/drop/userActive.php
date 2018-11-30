<?php
include "startSession.php";

if(!empty($_SESSION['LoggedIn']) && !empty($_SESSION['EmailAddress']) && !empty($_SESSION['Password'])){
	$EmailAddress = $_SESSION["EmailAddress"];
    $FirstName = $_SESSION["FirstName"];
    $PhoneNumber = $_SESSION["PhoneNumber"];

	$data = array( 
		"EmailAddress" => $EmailAddress,
		"FirstName" => $FirstName,
		"PhoneNumber" => $PhoneNumber
	);
    
    echo json_encode($data);
}else{
	echo "false";
}
?>