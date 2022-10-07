<?php
function test(){
	$a = array('A'=>"apple", 'B'=>"banana");
	foreach ($a as $k => $v) {
		echo "$k $v ";
	}
}

function test(){
	$a = ["A" => "apple", "B" => "banana"];
	foreach($a as $k => $v){
		echo "$k $v ";
	}
}

test()

?>