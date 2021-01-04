
interface Sayer{
	say:() => void
}


class Person implements Sayer {
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
	var a:Sayer = new Person("Stanley", 20)
	a.say()
}

test();