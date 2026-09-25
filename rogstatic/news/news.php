<?php
//Include HTML display class :)
include('news.html.php');

class component {
	
	function index() {
	global $sql;	// Unfortunately due to a php limitation, 
					// every function must have this
	$template = new componenttemplate; 	//Declare our HTML class
	$sql->query("SELECT * FROM news");	// Run a select query.
	$template->index($sql->rowarray);	// Run the template for this function.
	}
}
?>
