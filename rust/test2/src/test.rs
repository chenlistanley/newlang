
pub fn test1(){
	let a0 = 10;
	let a1 = 10.99;
	let a2 = 10.999;
	let a3 = true;
	let a4 = 'C';
	let a5 = &"apple";
	println!("{} {} {} {} {} {}", a0, a1, a2, a3, a4, a5);
}

pub fn test2(){
	let a0:i32 = 10;
	let a1:f32 = 10.99;
	let a2:f64 = 10.999;
	let a3:bool = true;
	let a4:char = 'C';
	let a5:&str = &"apple";
	println!("{} {} {} {} {} {}", a0, a1, a2, a3, a4, a5);
}

pub fn test3(){
	let a = ["apple", "banana"];
	for k in &a {
		println!("{}", k);
	}
}

pub fn test4(){
	let a:[&str;2] = ["apple", "banana"];
	for k in a.iter() {
		println!("{}", k);
	}
}

pub fn test5(){
	let a = Some("apple");
	match a{
		Some(s) => println!("{}", s),
		None => println!("{}", "orange")
	}
}

pub fn test6(){
	let a:Option<&str> = None;
	match a{
		Some(s) => println!("{}", s),
		None => println!("{}", "orange")
	}
}

pub fn test7(){
	let a:Result<String,String> = Ok(String::from("apple"));
	match a {
		Ok(s) => println!("{}", s),
		Err(s) => panic!("{}", s)
	}
}

pub fn test8(){
	let a:Result<String,String> = Err(String::from("apple"));
	match a {
		Ok(s) => println!("{}", s),
		Err(s) => panic!("{}", s)
	}
}

pub fn test9(){
	struct Person{
		name:String,
		age:i32
	}
	impl Person{
		fn new(name:String, age:i32) -> Person{
			Person{name, age}
		}
	}
	let a = Person::new(String::from("Stanley"), 20);
	println!("{} {}", a.name, a.age);
}

pub fn test10(){
	struct Person{
		name:String,
		age:i32
	}
	trait Sayer{
		fn say(&self);
	}
	impl Person{
		fn new(name:String, age:i32) -> Person{
			Person{name, age}
		}
	}
	impl Sayer for Person{
		fn say(&self){
			println!("{} {}", self.name, self.age);
		}
	}
	let a = Person::new(String::from("Stanley"), 20);
	a.say();
}

pub fn test11(){
	struct Person<T, S>{
		name:T,
		age:S
	}
	trait Sayer<T, S>{
		fn say(&self) where T:std::fmt::Display, S:std::fmt::Display;
	}
	impl<T, S> Person<T, S>{
		fn new(name:T, age:S) -> Person<T, S>{
			Person{name, age}
		}
	}
	impl<T, S> Sayer<T, S> for Person<T, S>{
		fn say(&self) where T:std::fmt::Display, S:std::fmt::Display {
			println!("{} {}", self.name, self.age);
		}
	}
	let a = Person::new(String::from("Stanley"), 20);
	a.say();
}