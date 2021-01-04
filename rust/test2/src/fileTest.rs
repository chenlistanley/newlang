use std::fs;

const FILE_PATH = "D:/newlang/rust/test.txt";

pub fn test(){
	let a= fs::read_to_string(FILE_PATH).unwrap();
	println!("{}", a);
}

pub fn test2(){
	let a = fs::read(FILE_PATH).unwrap();
	for k in a{
		println!("{}", k);
	}
}

pub fn test3(){
	fs::write(FILE_PATH, "apple\nbanana\norange").unwrap();
}

