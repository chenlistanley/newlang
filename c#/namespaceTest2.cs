using System;
using A;

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
			new Sayer().say();
			new B.Sayer().say();
		}
	}
}
