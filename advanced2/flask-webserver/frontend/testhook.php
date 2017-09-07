<?php 
	
	$handler = $_POST["handler"];
	if (preg_match('#^https?://#i', $handler) !== 1) {
		echo "Wrong scheme! You can only use http or https!";
		die();
	} else if(preg_match('#^https?://10.0.0.3#i', $handler) === 1) {
		echo "Restricted area!";
		die();
	}

	// create curl resource 
	$ch = curl_init(); 

	// set url 
	curl_setopt($ch, CURLOPT_URL, $_POST["handler"]); 

	//return the transfer as a string 
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 

	// $output contains the output string 
	$output = curl_exec($ch); 

	// close curl resource to free up system resources 
	curl_close($ch);

	echo $output;
?>