
pub fn test(){
	let a:Result<String,String> = Ok(String::from("apple"));
	match a {
		Ok(s)  => println!("{}", s),
		Err(s) => println!("{}", s)
	}
}

pub fn test2(){
	let a:Result<String,String> = Err(String::from("banana"));
	match a {
		Ok(s)  => println!("{}", s),
		Err(s) => println!("{}", s)
	}
}

pub fn test3(){
	fn f() -> Result<String,String>{
		return Ok(String::from("apple"));
	}
	let a = f();
	match a {
		Ok(s)  => println!("{}", s),
		Err(s) => println!("{}", s)
	}
}

pub fn test4(){
	fn f() -> Result<String,String>{
		return Err(String::from("banana"));
	}
	let a = f();
	match a {
		Ok(s)  => println!("{}", s),
		Err(s) => println!("{}", s)
	}
}