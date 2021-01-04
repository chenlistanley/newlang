
enum Sex{
	F(String),
	M{s:String},
	X
}

pub fn test(){
	let a = [
				Sex::F(String::from("female")), 
				Sex::M{s: String::from("male")}, 
				Sex::X
			];
	for k in a.iter(){
		match k {
			Sex::F(s) => println!("{}", s),
			Sex::M{s} => println!("{}", s),
			Sex::X => println!("{}", "orange")
		}
	}
}