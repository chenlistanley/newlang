
pub fn test(){
	let a:Result<String,String> = Err(String::from("apple"));
	match a{
		Ok(s) => println!("{}", s),
		Err(s) => panic!("{}", s)
	}
} 
