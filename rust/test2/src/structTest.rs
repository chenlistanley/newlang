
struct Person {
	name: String,
	age: i32
}

pub fn test(){
	let a = Person{name:String::from("Stanley"), age:20};
	println!("{} {}", a.name, a.age);
}