
pub fn test(){
	let a=vec![1, 2, 5, 9];

	println!("{:?}", a);
}

pub fn test2(){
	let mut a=vec![1, 2, 5, 9];
	a.push(20);
	println!("{:?}", a);
}

pub fn test3(){
	let a=vec![1, 2, 5, 9];

	println!("{}", a.get(0).unwrap());
}

pub fn test4(){
	let a=vec![1, 2, 5, 9];
	println!("{}", a[0]);
}

pub fn test5(){
	let a=vec![1, 2, 5, 9];
	let b=match a.get(10){
		Some(&v) => v,
		None => 0
	};
	println!("{}", b);
}

pub fn test6(){
	let a=vec![1, 2, 5, 9];
	for k in a.iter(){
		println!("{:?}", k);
	}
}

pub fn test7(){
	let a=vec![1, 2, 5, 9];
	for k in &a {
		println!("{:?}", k);
	}
}