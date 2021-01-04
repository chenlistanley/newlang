
struct Person<T, T2>{
	name: T,
	age: T2
}

trait Sayer<T, T2> {
	fn say(&self) where T:std::fmt::Display, T2:std::fmt::Display ;
	fn say2(&self, words:String);
	fn say3(&self){
		println!("banana");
	}
}

impl<T, T2> Person<T, T2> {
	fn new(name: T, age: T2) -> Person<T, T2>{
		Person{name, age}
	}
}

impl<T, T2> Sayer<T, T2> for Person<T, T2>{
	fn say(&self) where T:std::fmt::Display, T2:std::fmt::Display{
		println!("{} {}", self.name, self.age);
	}
	fn say2(&self, words: String){
		println!("{}", words);
	}
}

pub fn test(){
	let p = Person::new(String::from("Stanley"), 20);
	p.say();
	p.say2(String::from("apple"));
	p.say3();
}