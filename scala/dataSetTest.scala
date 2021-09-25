
object Test{
	def main(args: Array[String]) = {
		test()
	}
	def test() = {
		val a = Set("apple", "banana", "orange", "apple")
		for(k <- a){
			println(k)
		}
	}

	def test():Unit = {
		val a = Set("apple", "banana")
		a.foreach{
			k => println(k)
		}
	}
}