
function test(){
	let a = new Object()
	a.name = "Stanley"
	a.age = 20
	a.say = function(){
		console.log(this.name, this.age)
	}
	a.say()
}

function test2(){
	let a = {}
	a.name = "Stanley"
	a.age = 22
	a.say = function(){
		console.log(this.name, this.age)
	}
	a.say()
}

function test3(){
	let a = {
		name: "Stanley",
		age: 23,
		say: function(){
			console.log(this.name, this.age)
		}
	}
	
	a.say()
}

function test4(){
	let Person = function(name, age){
		this.name = name
		this.age = age
		this.say = function(){
			console.log(this.name, this. age)
		}
	}
	let a = new Person("Stanley", 24)
	a.say()
}

function test5(){
	let Person = function(name, age){
		this.name = name
		this.age = age
		this.say = function(){
			console.log(this.name, this. age)
		}
	}
	Person.prototype.say2=function(){
		this.say()
		console.log("apple")
	}
	let a = new Person("Stanley", 25)
	a.say2()
}

test5()