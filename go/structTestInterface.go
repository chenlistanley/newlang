package main

func main(){
	test3()
}

type Person struct{
	name string
	age int
}

type Sayer interface{
	say()
}

func (p Person) say() {
	println(p.name, p.age)
}

func test(){
	var p = Person{"Stanley", 30}
	p.say()
}