
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

class Student extends Person{
	private grade:number

	constructor(name:string, age:number, grade:number){
		super(name, age)
		this.grade = grade
	}

	say(){
		super.say()
		console.log(this.grade)
	}
}

function test() {
	var a = new Student("Stanley", 20, 8)
	a.say()
}

test();