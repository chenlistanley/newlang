package main


func main(){
	test5()
}

type Person struct{
	name string
	age int
}

func (p Person) say(){
	println(p.name, p.age)
}

func test(){
	var p = Person{name:"Stanley", age:20}
	p.say()
}

func test2(){
	var p = Person{"Stanley", 20}
	p.say()
}

func test3(){
	var p = &Person{"Stanley", 20}
	p.say()
}

func test4(){
	var p = new(Person)
	p.name = "Stanley"
	p.age = 20
	p.say()
}

func test5(){
	var p Person
	p.name="Stanley"
	p.age = 20
	p.say()
}
