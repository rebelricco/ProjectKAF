<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title></title>

<link href="http://fonts.googleapis.com/css?family=Didact+Gothic" rel="stylesheet" />
<link href="default.css" rel="stylesheet" type="text/css" media="all" />
<link href="fonts.css" rel="stylesheet" type="text/css" media="all" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=0">


</head>
<body>
<div id="header-wrapper">
	<div id="header" class="container">
		<div id="logo">
			<h1><a href="#"></a></h1>
		</div>

	</div>
	<div id="banner" class="container">
		<div class="title">
			<h2>Automatic Coffee Machine™ </h2>
			<span class="byline">for whenever you're stressed in the morning or craving for the perfect cup of coffee</span>
		</div>


        <ul class="Input">

            <form method="post">

                <input type="submit" name="submit" value="Make coffee now"/>

            </form>



        </ul>
        </div>
</div>
<div id="wrapper">
	<div id="three-column" class="container">
		<div class="title">
			<h2>The Coffee</h2>
		</div>

		<div class="test">

			<div class="boxA tredjedel">
				<span class="fa fa-info-circle"></span>
				<a href="https://www.bki.dk/da-dk/om-bki/om-bki/bkis-historie" class="button button-alt">Info</a>
			</div>
			<div class="boxB tredjedel">
				<span class="fa fa-cogs"></span>
				<a href="Settings.php" class="button button-alt">Settings</a>
			</div>
			<div class="boxC tredjedel">
				<span class="fa fa-coffee"></span>
				<a href="http://www.esprezzo.dk/opskrifter" class="button button-alt">Coffee</a>
			</div>
			<div class="clearfix"></div>

		</div>

	</div>
</div>

<div id="copyright" class="container">
	<p>&copy;2018 Coffe Machine. All rights reserved by us. | Design by Fabian Wendell</a>.</p>
</div>

<?php
if(isset($_POST['submit'])){

		$ch = curl_init("127.0.0.1:1337/Kaffe");
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_HTTPHEADER, array(
		    'Content-Type: application/json')
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

?>
</body>
</html>
