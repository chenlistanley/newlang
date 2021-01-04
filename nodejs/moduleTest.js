var Person = require("./moduleA")

function test(){
	let a = new Person("Stanley", 30)
	a.say()
}

test()