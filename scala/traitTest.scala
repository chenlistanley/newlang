
trait Sayer{
	def say():Unit
}

class Person(var name:String, var age:Int) extends Sayer{
	def say():Unit = {
		print(name, age)
	}
}

object Test{
	def main(args: Array[String]):Unit = {
		val a = new Person("Stanley", 20)
		a.say()
	}
}