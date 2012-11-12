<?php
$separator = ":"; //change this based on the content we are getting
$file1 = "lnfile"; //file with newlines
$file2 = "unlnfile"; //"flat file"
$content = $_POST['<NAMEOFTHING>'];
file_put_contents($file1, $content."\n", FILE_APPEND);
file_put_contents($file2, $content.$seperator, FILE_APPEND);

?>