
pub fn test(){
	let a:Result<String,&str>=Err("banana");
	match a {
		Ok(s) => println!("{}", s),
		Err(s) => panic!("{}", s)
	}
}

pub fn test2(){
	let a:Result<String,&str> = Err("banana");
	if let Err(s) = a {
		panic!("{}", s);
	}
}

pub fn test3(){
	let a:Result<String,&str> = Err("banana");
	a.unwrap();
}

pub fn test4(){
	let a:Result<String,&str> = Err("banana");
	a.expect("banana");
}