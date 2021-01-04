package main

func main(){
	test()
}

type Person struct{
	name string
	age int

	say func()
}

func test(){
	var p = Person{name:"Stanley", age:18}
	p.say = func(){
		println("apple")
	}
	p.say()
}