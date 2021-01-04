use std::collections::HashMap;


pub fn test(){
	let mut map=HashMap::new();
	map.insert("a", "apple");
	map.insert("b", "banana");
	map.insert("c", "cane");
	println!("{}", map.get("a").unwrap());
}

pub fn test2(){
	let mut map=HashMap::new();
	map.insert("a", "apple");
	map.insert("b", "banana");
	map.insert("c", "cane");

	for e in map.iter(){
		println!("{:?}", e);
	}
}

pub fn test3(){
	let mut map=HashMap::new();
	map.insert("a", "apple");
	map.insert("b", "banana");
	map.insert("c", "cane");
	map.entry("c").or_insert("cane2");

	for e in map.iter(){
		println!("{:?}", e);
	}
}

pub fn test4(){
	let mut map=HashMap::new();
	map.insert("a", "apple");
	map.insert("b", "banana");
	map.insert("c", "cane");

	if let Some(x) = map.get_mut(&"c"){
		*x="coak";
	}

	for e in map.iter(){
		println!("{:?}", e);
	}
}