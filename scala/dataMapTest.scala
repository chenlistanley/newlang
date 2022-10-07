
object Test{
	def main(args: Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		val a = Map("A" -> "apple", "B" -> "banana")
		for(k <- a){
			println(k)
		}
		println(a.isEmpty)
	}

	def test():Unit = {
		val a = Map("A" -> "apple", "B" -> "banana")
		a.keys.foreach{
			k => println(k, a(k))
		}
		a.values.foreach{
			k => println(k)
		}
	}

	def test():Unit = {
		val a = Map("A"-> "apple")
		a.get("B") match {
			case Some(s) => print(s)
			case None => print("none")
		}
	}
}