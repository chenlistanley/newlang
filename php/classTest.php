<?php

class Person{
	var $name;
	var $age;

	function __construct($name, $age){
		$this->name = $name;
		$this->age = $age;
	}

	function say(){
		echo "$this->name $this->age";
	}
}

function test(){
	$a = new Person("Stanley", 20);
	$a->say();
}

test()

?>