
struct Person{
	name: String,
	age: i32
}

trait Sayer {
	fn say(&self);
	fn say2(&self, words:String);
	fn say3(&self){
		println!("banana");
	}
}

impl Person {
	fn new(name: String, age: i32) -> Person{
		Person{name, age}
	}
}

impl Sayer for Person{
	fn say(&self){
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