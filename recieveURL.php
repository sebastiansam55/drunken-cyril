<?php
$filename = "price"; //filename that the data is written to (raw data from url)
#$URL = $_POST['URL'];
$URL = "http://tb.priceblink.com/products?rid=35&title=Samsung%20Galaxy%20S%20III%204G%20Android%20Phone%2C%20Blue%2016GB%20%28Sprint%29&price=&model=Galaxy%20S%20III&mpn=&brand=Samsung&upc=&sku=B00894K248&isbn=&ship=&rating=4.1&in_stock=&c1=39&c2=0&c3=&c4=&c5=&uid=c46fc3c0-1e3d-792e-1ba3-7656a22ae2c5&ver=3.4&browser=chrome";
$f = fopen($URL, 'r');
$contents = stream_get_contents($f); //raw JSON data
fclose($f); //close URL
file_put_contents($filename, $contents); //write JSON data to be retrived by python script
$result = exec('python recieve.py '.$filename); //execute command 'python recieve.py $filename'
echo $result; //never seen by user
unlink($filename);
?>



