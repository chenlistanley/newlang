using System;
namespace TestApplication{
   class Test{
      static void Main(string[] args){
      	string a = "apple";
      	Console.WriteLine(a.Contains("a"));
      	Console.WriteLine(a.Substring(0, 3));
      	Console.WriteLine(a.Equals("apple"));
      	Console.WriteLine(a.StartsWith("app"));
      	Console.WriteLine(a.ToLower());
      	Console.WriteLine(a.ToUpper());
      	Console.WriteLine(a.Trim());
      }
   }
}