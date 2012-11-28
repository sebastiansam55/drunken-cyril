<?php
$sep = ":"; //change this based on the content we are getting
$file1 = "lnfile"; //file with newlines
$file2 = "unlnfile"; //"flat file"
$fullprice = $_POST['price'].".".$_POST['decimalPrice'];
$UPC = $_POST['UPC'];
$shipWGT = $_POST['weight'];
$MFG_No = $_POST['MFG_No'];
$MFG = $_POST['MFG'];
//newlinefile
$handle1 = fopen($file1, "a");
fwrite($handle1, $fullprice."\n");
fwrite($handle1, $UPC."\n");
fwrite($handle1, $shipWGT."\n");
fwrite($handle1, $MFG_No."\n");
fwrite($handle1, $MFG."\n");
fwrite($handle1, "---------------\n");
fclose($handle1);


//flat file
$handle2 = fopen($file2, "a");
fwrite($handle2, $fullprice.$sep);
fwrite($handle2, $UPC.$sep);
fwrite($handle2, $shipWGT.$sep);
fwrite($handle2, $MFG_No.$sep);
fwrite($handle2, $MFG.$sep);
fclose($handle2);

?>