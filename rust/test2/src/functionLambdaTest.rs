
pub fn test(){
	let f = ||{10};
	let a = f();
	println!("{}", a);
}

pub fn test2(){
	let f=|x, y|{x + y};
	let a = f(3, 5);
	println!("{}", a);
}