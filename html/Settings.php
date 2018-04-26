<?php
session_start();
ob_start();
?>	
<!DOCTYPE html>
<html>
<body>

<h2>Settings</h2>


<?php
$jsonStringRaw = file_get_contents("http://127.0.0.1:1337/Settings");

$decodedJsonString = json_decode($jsonStringRaw);
?>

<form method="post">
    <input type="radio" name="cup" value="1" <?php if($decodedJsonString->kopper == 1) echo "checked"; ?>><label>1 Cup of coffee</label><br/>
    <input type="radio" name="cup" value="2" <?php if($decodedJsonString->kopper == 2) echo "checked"; ?>><label>2 Cup of coffee</label><br/>
    <input type="radio" name="cup" value="3" <?php if($decodedJsonString->kopper == 3) echo "checked"; ?>><label>3 Cup of coffee</label><br/>
    <input type="radio" name="cup" value="4" <?php if($decodedJsonString->kopper == 4) echo "checked"; ?>><label>4 Cup of coffee</label><br/>

    <input type="time" name="time" value=<?php echo $decodedJsonString->time; ?>>
    <input type="submit" name="submit" value="Submit"/>
</form>

<br/><br/>
<br/><br/>



<?php
if(isset($_POST['submit'])){
    if(!empty($_POST['cup'] && !empty($_POST['time']))) {

        $selected_cups = $_POST['cup'];
        $selected_time = $_POST['time'];
        echo "Du vil have {$selected_cups} kopper kaffe kl: {$selected_time} </br>";

        $PostData = array("kopper" => $selected_cups, "time" => $selected_time);
		$PostDataEncoded = json_encode($PostData);
		

		$ch = curl_init("127.0.0.1:1337/Settings");                                                                      
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
		curl_setopt($ch, CURLOPT_POSTFIELDS, $PostDataEncoded);    
		curl_setopt($ch, CURLOPT_POST, 1);                                                              
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
		curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
		    'Content-Type: application/json',                                                                                
		    'Content-Length: ' . strlen($PostDataEncoded))                                                                       
		);                                                                                                           
		$result = curl_exec($ch);

		if (curl_errno($ch)) {
		    echo 'Error:' . curl_error($ch);
		}
		else{
		    print_r($result);
		}
		curl_close ($ch);
		header("Refresh:3; url=index.php");

    }
    else{
        echo "<b>Please Select Atleast One Option.</b>";
    }
}
?>
