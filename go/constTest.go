package main

func main(){
	test2()
}

func test(){
	const a ="apple"
	println(a)
}

func test2(){
	const (
		a0 = iota
		a1
		a2 = "apple"
		a3
		a4 = iota
		a5
	)
	println(a0, a1, a2, a3, a4, a5)
}