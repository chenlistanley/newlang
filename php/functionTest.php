<?php
function say($s){
	echo "$s";
}

function speak(){
	return "banana";
}

function test(){
	say("apple");
	$a = speak();
	echo " $a";
}

test()

?>