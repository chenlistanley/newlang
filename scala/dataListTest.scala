
object Test{
	def main(args:Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		val a = List("apple", "banana", "orange")
		for(k <- a){
			println(k)
		}
	}

	def test():Unit = {
		val a = List("apple", "banana")
		a.foreach{
			k => println(k)
		}
	}
}