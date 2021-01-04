use std::thread;
use std::time::Duration;
use std::sync::mpsc;

pub fn test(){
	fn a(){
		for x in 0..5{
			println!("spawn thread: {}", x);
			thread::sleep(Duration::from_millis(1));
		}
	}
	thread::spawn(a);
	thread::sleep(Duration::from_millis(1000));
}

pub fn test2(){
	thread::spawn(||{
		for x in 0..5{
			println!("spawn thread: {}", x);
			thread::sleep(Duration::from_millis(1));
		}
	});
	thread::sleep(Duration::from_millis(1000));
}

pub fn test3(){
	let a= thread::spawn(||{
		for x in 0..5{
			println!("spawn thread: {}", x);
			thread::sleep(Duration::from_millis(1));
		}
	});
	a.join().unwrap();
}

pub fn test4(){
	let (tx, rx)=mpsc::channel();
	thread::spawn(move || {
		let val = String::from("Hi");
		tx.send(val).unwrap();
	});
	let val=rx.recv().unwrap();
	println!("{}", val);
}