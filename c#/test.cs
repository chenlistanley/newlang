using System;

class Test{

	public static void Main(string[] args){
		try{
			throw new ApplicationException("apple");
		}catch(ApplicationException e){
			Console.Write("{0}", e);
		}
	}
}

