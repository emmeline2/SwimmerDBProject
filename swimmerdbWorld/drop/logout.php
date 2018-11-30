<?php include "startSession.php";
$_SESSION = array(); session_destroy(); 

echo "Logged Out";
?>