
object Test{
	def main(args:Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		var a = Array("apple", "banana", "orange")
		for(k <- a){
			println(k)
		}
	}

	def test2():Unit = {
		var a = new Array[String](3)
		a(0) = "apple"
		a(1) = "banana"
		a(2) = "orange"
		for(k <- a){
			println(k)
		}
	}
}