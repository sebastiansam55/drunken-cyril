<?php
$filename = "urlList";
if(isset($_POST['delete'])){
	unlink($filename);
}else{
	$data = $_POST['taburl'];
	file_put_contents($filename, $data."\n", FILE_APPEND);
}
?>
