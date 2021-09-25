using System;

class Test{
	static void Main(string[] args){
		try{
			throw new Exception("apple");
		}catch(Exception e){
			Console.WriteLine("{0}", e);
		}finally{
			Console.WriteLine("orange");
		}
	}
}
