package main

func main(){
	test()
} 

func test(){
	const (
		a = "apple"
		b = iota
		c
	)
	println(a, b, c)

}

