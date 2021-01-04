
pub fn test(){
	let a=["apple", "banana", "orange"];
 	
 	println!("{:?}", a);
	println!("{:?}", &a[1..]);
	println!("{:?}", &a[..1]);
}

pub fn test2(){
	let a:[&str; 3] = ["apple", "banana", "orange"];
 
	println!("{}", a[0]);
	println!("{}", a[1]);
}

pub fn test3(){
	let a = ["apple", "banana", "orange"];
 
	for k in a.iter(){
		println!("{}", k);
	}
}

pub fn test4(){
	let a = ["apple", "banana", "orange"];
 
	for k in &a {
		println!("{}", k);
	}
}