
pub fn test(){
	let a=10;
	let b=10.99;
	let c=true;
	let d='A';
	println!("{}", a);
	println!("{}", b);
	println!("{}", c);
	println!("{}", d);
}


fn test1(){
	let a:i8 = 8;
	let b:i16 = 16;
	let c:i32 = 32;
	let d:i64 = 64;
	let e:i128 = 128;

	println!("{}", a);
	println!("{}", b);
	println!("{}", c);
	println!("{}", d);
	println!("{}", e);
}

fn test2(){
	let a:u8 = 8;
	let b:u16 = 16;
	let c:u32 = 32;
	let d:u64 = 64;
	let e:u128 = 128;

	println!("{}", a);
	println!("{}", b);
	println!("{}", c);
	println!("{}", d);
	println!("{}", e);
}

fn test3(){
	let a:f32 = 3.14;
	let b:f64 = 3.1415926;

	println!("{}", a);
	println!("{}", b);
}

fn test4(){
	let a:bool = false;

	println!("{}", a);
}

fn test5(){
	let a:char = 'H';

	println!("{}", a);
}
