package main

func main(){
	test3()
}

func test(){
	var a = 10;
	var b *int
	b=&a
	println(*b)
}

func test2(){
	var a *int
	if a != nil {
		println(*a)
	}
}

func test3(){
	var f = func(a *string){
		println(*a)
	}
	var a = "apple"
	var b *string
	b=&a
	f(b)
}