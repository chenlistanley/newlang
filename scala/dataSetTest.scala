
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
}