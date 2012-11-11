<?php
$data = $_POST['titletag'];
$timestamp = strftime("%r");
file_put_contents("titles.txt", $data." @ ".$timestamp."\n", FILE_APPEND);
?>
