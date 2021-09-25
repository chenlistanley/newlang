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

class Student extends Person{
	var $grade;

	function __construct($name, $age, $grade){
		parent::__construct($name, $age);
		$this->grade = $grade;
	}

	function say(){
		parent::say();
		echo " $this->grade";
	}
}

function test(){
	$a = new Student("Stanley", 20, 8);
	$a->say();
}

test()

?>