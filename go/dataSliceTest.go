package main

func main(){
	test4()
}

func test(){
	var a = []int{10, 20}
	for k, v := range a {
		println(k, v)
	}
}

func test2(){
	var a = make([]int, 10)
	// var a = make([]int, 10, 100)
	a = append(a, 10)
	a = append(a, 20)
	
	for k, v := range a {
		println(k, v)
	}
}

func test3(){
	var a = []int{10, 20}
	var b = make([]int, 10)
	copy(b, a)
	
	for k, v := range b {
		println(k, v)
	}
}

func test4(){
	var a = make([]int, 10, 100)
	println(len(a), cap(a))
}