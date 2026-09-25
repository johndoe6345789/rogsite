<?php 

class componenttemplate {

	function index($rows) {
	    foreach ($rows as $row) {
	    ?>
	        <p><?php echo($row["CONTENT"]); ?></p>
	    <?php
	    }
	}
}
?>
