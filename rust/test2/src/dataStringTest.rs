
pub fn test(){
	let a = "apple";
	println!("{}", a);
	println!("{}", &a[..3]);
	println!("{}", &a[3..]);
	println!("{}", a.len());
}

pub fn test2(){
	let a = String::from("apple");
	println!("{}", a);
	println!("{}", &a[..3]);
	println!("{}", &a[3..]);
	println!("{}", a.len());
}

pub fn test3(){
	let mut a = String::from("apple");
	a.push(' ');
	a.push_str("banana");
	println!("{}", a);
}
