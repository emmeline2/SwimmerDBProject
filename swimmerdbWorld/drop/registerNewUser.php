<?
include "startSession.php";

$connection = mysqli_connect("localhost","droppUserLogin2","cruznashcosmo","droppUserLogin1");
/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}


    $EmailAddress = mysqli_real_escape_string($connection , $_POST['EmailAddress']);
    $Password1 = md5(mysqli_real_escape_string($connection , $_POST['Password1']));
    $FirstName = mysqli_real_escape_string($connection , $_POST['FirstName']);
    $LastName = mysqli_real_escape_string($connection , $_POST['LastName']);
    $PhoneNumber = mysqli_real_escape_string($connection , $_POST['PhoneNumber']);
     
    
    $checkEmailAddress = mysqli_query($connection , "SELECT * FROM UserDB WHERE EmailAddress = '".$EmailAddress."'");

    $numEmails = mysqli_num_rows($checkEmailAddress);
      
     if($numEmails>0)
     {
        echo "taken";
     }
     else
     {
        $registerquery = mysqli_query($connection , "INSERT INTO UserDB (Password, EmailAddress, FirstName, LastName, PhoneNumber) VALUES('".$Password1."', '".$EmailAddress."', '".$FirstName."', '".$LastName."', '".$PhoneNumber."')");
        if($registerquery)
        {
            echo "success";
        }
        else
        {
            echo "failure"; 
        }       
     }
    mysqli_close($connection);
    ?>