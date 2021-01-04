package main

func main(){
	test()
}

func test(){
	defer println("apple")
	panic("banana")
	
}