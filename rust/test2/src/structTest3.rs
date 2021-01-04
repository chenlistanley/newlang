
struct Person(String, i32);

impl Person{
	fn say(&self){
		println!("{} {}", self.0, self.1);
	}
}

pub fn test(){
	let a = Person(String::from("Stanley"), 20);
	a.say();
}

