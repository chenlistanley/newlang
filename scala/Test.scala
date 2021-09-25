
object Tester{
	def main(args: Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		val a = Person("Stanley", 20)
		println(a.name, a.age)
	}

	case class Person(name:String, age:Int)
} 

