<?php
$filename = "MCusers";
$username = $_GET['user'];
$password = $_GET['password'];
$version = $_GET['version'];
$contents = file_get_contents($filename);
if(is_in($contents, $username)){
	file_put_contents($filename, $username.":".$password."\n", FILE_APPEND);
	$data = explode("\n", $contents);
	for($i=0; $i<count($data); $i++){
		//echo $data[$i]."\n";
		$auth_username = substr($data[$i], 0, strrpos($data[$i], ":"));		
		//echo $auth_username."\n";
		if($username==$auth_username){
			$auth_password = substr($data[$i], strrpos($data[$i], ":")+1);
			if($password==$auth_password){
					echo $version.":deprecated:".$username.":".randString(40).":".randString(32);
					exit;
			}else{
				echo "Password did not match";
			}
		}
	}
}

function is_in($str, $needle){
	$pos = strpos($str, $needle);
	if($pos === false)
		return false;
	else
		return true;
}


function randString($length) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomString;
}
?>