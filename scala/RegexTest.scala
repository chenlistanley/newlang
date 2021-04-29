import scala.util.matching.Regex

object Test{
	def main(args:Array[String]):Unit ={
		test()
	}
	def test():Unit ={
		val patten = "apple".r
		val a = "apple banana orange apple"
		println(patten findFirstIn a)
	}

	def test2():Unit ={
		val patten = "apple".r
		val a = "apple banana orange apple"
		println((patten findAllIn a).mkString(","))
	}

	def test3():Unit ={
		val patten = "apple".r
		val a = "apple banana orange apple"
		println((patten findAllIn a).mkString(","))
	}
}