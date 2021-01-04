package main

import "time"

func main(){
	test2()
	
}

func test(){
	var fa = func(a chan string){
		a <- "apple"
	}
	var a = make(chan string, 10)
	go fa(a)
	go fa(a)

	println(<-a)
	println(<-a)
	close(a)
}

func test2(){
	var fa = func(a chan string){
		a <- "apple"
		a <- "banana"
		a <- "orange"
		
	}
	var a = make(chan string, 10)
	go fa(a)
	go fa(a)

	time.Sleep(1000)
	close(a)

	for k := range a{
		println(k)
	}
}
