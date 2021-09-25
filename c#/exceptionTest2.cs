using System;

class Ae:ApplicationException{
	private string code;

	public Ae(string code, string message):base(message){
		this.code = code;
	}

	public override string ToString(){
		return this.code + base.Message;
	}
}

class Test{
	static void Main(string[] args){
		try{
			throw new Ae("apple");
		}catch(Ae e){
			Console.WriteLine("{0}", e);
		}finally{
			Console.WriteLine("orange");
		}
	}
}
