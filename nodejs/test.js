
function test1(){
	let a0 = "apple"
	let a1 = 10
	let a2 = 10.99
	let a3 = true
	console.log(a0, a1, a2, a3)
}

function test2(){
	let a = ["apple", "banana", "orange"]
	for(k in a){
		console.log(a[k])
	}
}

function test3(){
	let a = new Array()
	a[0] = "apple"
	a[1] = "banana"
	a[2] = 10
	for(k in a){
		console.log(a[k])
	}
}

function test4(){
	let Person = function(name, age){
		this.name = name
		this.age = age
		this.say = function(){
			console.log(this.name, this.age)
		}
	}
	let a = new Person("Stanley", 20)
	a.say()

	Person.prototype.speak = function(){
		console.log("apple")
	}
	a.speak()
}

function test5(){
	let a = new Object()
	a.name = "Stanley"
	a.age = 20
	a.say = function(){
		console.log(this.name, this.age)
	}
	a.say()
}

function test6(){
	let a = {}
	a.name = "Stanley"
	a.age = 20
	a.say = function(){
		console.log(this.name, this.age)
	}
	a.say()
}

function test(){

}

test()
