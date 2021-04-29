
object Test{
	def main(args:Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		val a0 = "apple"
		val a1 = 10
		val a2 = 10.99
		val a3 = true
		val a4 = 'C'
		println(a0, a1, a2, a3, a4)
	}

	def test2():Unit = {
		var a0:String = "apple"
		var a1:Int = 10
		var a2:Float = 10.99f
		var a3:Boolean = true
		var a4:Char = 'C'
		println(a0, a1, a2, a3, a4)
	}
}