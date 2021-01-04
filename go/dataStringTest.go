package main

func main(){
	test2()
}

func test(){
	a := "apple"
	for k,v := range a{
		println(k, v)
	}
}

func test2(){
	a := "apple"
	b := a[0:3]
	println(a, b)
}