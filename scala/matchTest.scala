
object Test{
	def main(args:Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		for(a <- List("apple", "banana", "orange")){
			a match{
				case "apple" => print("A")
				case "banana" => print("B")
				case _ => print("C")
			}
		}
	}
}
