
object Test{
	def main(args: Array[String]) = {
		test()
	}

	def test() = {
		val a = Map("A" -> "apple", "B" -> "banana")
		println(a.isEmpty)
		a.keys.foreach{
			k => println(k)
		}
		a.values.foreach{
			k => println(k)
		}
	}
}