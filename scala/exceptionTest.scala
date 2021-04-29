
object Test{
	def main(args: Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		try{
			val a = 2/0
		}catch{
			case e:ArithmeticException => println(e)
			case e:Exception => println(e)
		}finally{
			println("apple")
		}
	}
}