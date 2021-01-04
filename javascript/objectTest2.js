function test(){
	function Person(name, age){
		this.name=name
		this.age=age
		this.say=function(){
			print(this.name, this.age)
		}
	}
	var a = new Person("Stanley", 20)
	a.say()

	Person.prototype.say2=function(){
		print("apple")
	}
	a.say2()		
}