
pub fn test(){
	let a = Option::Some("apple");
	match a {
		Option::Some(s) => println!("{}", s),
		Option::None => println!("banana")
	}
}

pub fn test2(){
	let a = Some("apple");
	match a {
		Some(s) => println!("{}", s),
		None => println!("banana")
	}
}

pub fn test3(){
	let a:Option<&str> = None;
	match a {
		Some(s) => println!("{}", s),
		None => println!("banana")
	}
}



