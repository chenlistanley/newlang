
object Test{
	def main(args:Array[String]) = {
		test()
	}

	def test() = {
		var a = Array("apple", "banana", "orange")
		for(k <- a){
			println(k)
		}
	}

	def test2() = {
		var a = new Array[String](3)
		a(0) = "apple"
		a(1) = "banana"
		a(2) = "orange"
		for(k <- a){
			println(k)
		}
	}
}