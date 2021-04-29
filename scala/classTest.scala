
class Person(var name:String, var age:Int){

	def say():Unit = {
		println(this.name, this.age)
	}

	def add():Unit = {
		age += 1
		println(age)
	}
}

object Test{
	def main(args: Array[String]):Unit = {
		val a = new Person("Stanley", 20)
		a.say()
		a.add()
	}
}