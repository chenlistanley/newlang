
object Test{
	def main(args: Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		val a = Map("A" -> "apple", "B" -> "banana")
		println(a.isEmpty)
		a.keys.foreach{
			k => println(k, a(k))
		}
		a.values.foreach{
			k => println(k)
		}
	}
}