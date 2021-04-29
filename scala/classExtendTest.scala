
class Person(val name:String, val age:Int){
	def say():Unit = {
		print(name, age)
	}
}
class Student(override val name:String, override val age:Int, val glade:Int) extends Person(name, age){
	override def say():Unit = {
		print(name, age, glade)
	}
}

object Test{
	def main(args: Array[String]):Unit = {
		val a = new Student("Stanley", 20, 8)
		a.say()
	}
}