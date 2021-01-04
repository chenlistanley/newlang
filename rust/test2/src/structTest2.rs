
struct Person {
	name: String,
	age: i32
}

impl Person {
	fn new(name:String, age:i32) -> Person{
		Person{name, age}
	}
	fn say(&self){
		println!("{} {}", self.name, self.age);
	}
}

pub fn test(){
	let p =Person::new(String::from("Stanley"), 20);
	p.say();
}