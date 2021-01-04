
pub fn test(){
	let a = "Hello";
	match a {
		"Hello" => println!("{}", a),
		_ => {}
	}

}

pub fn test2(){
	let a = "Hello";
	if let "Hello" = a {
		println!("{}", a);
	}
}