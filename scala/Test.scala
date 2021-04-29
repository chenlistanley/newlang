object Test{
	def main(args:Array[String]):Unit = {
		test()
	}

	def test():Unit = {
		try{
			val a = 1 / 0
		} catch{
			case e:Exception => print(e)
		}finally{
			print("orange")
		}
	}

	
} 
