
interface Sayer{
	name:String
	age:Number
	say:() => void
}

function test() {
	var a:Sayer = {
		name: "Stanley",
		age: 20,
		say: () => {console.log(a.name, a.age)}
	}
	a.say()
}

test()