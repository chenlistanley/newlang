
fn test(){
	let a = 5;
	if a > 5 {
		println!("{}>5", a);
	}else {
		println!("{}<=5", a);
	}
}

pub fn test(){
	let a = 10;
	let b = if a >10 {5} else {0};
	println!("{}", b);
}