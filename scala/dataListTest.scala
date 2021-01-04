
object Test{
	def main(args:Array[String]) = {
		test()
	}

	def test() = {
		val a = List("apple", "banana", "orange")
		for(k <- a){
			println(k)
		}
	}
}