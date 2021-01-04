
pub fn test(){
	let a=String::from("apple");
	let b=a;
	println!("{}", b);
}

pub fn test2(){
	let a=String::from("apple");
	let b=&a;
	println!("{} {}", a, b);
}

pub fn test3(){
	let a=String::from("apple");
	let b=&a;
	let c=b;
	println!("{} {} {}", a, b, c);
}

pub fn test4(){
	let a=String::from("apple");
	let b=&a;
	let c=a;
	println!("{}", c);
}

pub fn test5(){
	let mut a=String::from("apple");
	let b=&mut a;
	b.push_str(" banana");
	println!("{}", b);
}