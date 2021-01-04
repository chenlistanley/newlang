
function test(){
	var a = new Object()
	a.name="Stanley"
	a.age=20
	a.say=function(){
		print(this.name, this.age)
	}
	a.say()
}

function test2(){
	function Person(name, age){
		this.name=name
		this.age=age
		this.say=function(){
			print(this.name, this.age)
		}
	}
	var a = new Person("Stanley", 20)
	a.say()		
}

function test3(){
	var a = {
		name: "Stanley",
		age: 20,
		say: function(){
			print(this.name, this.age)
		}
	}
	a.say()
}