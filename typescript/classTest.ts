
class Person{
	private name:string
	private age:number

	constructor(name:string, age:number){
		this.name=name
		this.age=age
	}

	say(){
		console.log(this.name, this.age)
	}
}

function test() {
	var a = new Person("Stanley", 20)
	a.say()
}

test()