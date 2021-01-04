
pub fn test(){
	fn f(x:i32, y:i32) -> i32 {
		return x+y;
	}
	let a = f(3, 5);
	println!("{}", a);
}

pub fn test2(){
	fn f(x:i32, y:i32) -> i32 {
		x+y
	}
	let a = f(3, 5);
	println!("{}", a);
}
