package main

func main(){
	test()
}

func test(){
	defer println("apple")
	println("banana")
	panic("orange")
}