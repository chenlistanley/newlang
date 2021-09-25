using System;

namespace A{
	public class Sayer{
		public void say(){
			Console.WriteLine("apple");
		}
	}
}

namespace B{
	public class Sayer{
		public void say(){
			Console.WriteLine("banana");
		}
	}
}

namespace TestApplication{
	class Test{
		static void Main(string[] args){
			new A.Sayer().say();
			new B.Sayer().say();
		}
	}
}
