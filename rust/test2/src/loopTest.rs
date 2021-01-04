
fn test(){
	let mut a = 5;
	while a > 0 {
		println!("{}", a);
		a -= 1;
	}
}

fn test2(){
	let a = [1, 5, 7, 3];
	for v in a.iter() {
		println!("{}", v);
	}
}

fn test3(){
	for k in 1..3 {
		println!("{}", k);
	}
}

fn test4(){
	let mut a = 5;
	loop {
		println!("{}", a);
		a -= 1;
		if a == 0 {
			break;
		}
	}
}

fn test5(){
	let mut a = 5;
	let b = loop {
		a -= 1;
		if a == 0 {
			break a;
		}
	};
	println!("{}", b);
}