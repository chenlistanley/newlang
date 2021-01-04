package main


func main(){
	test()
}

func test(){
	var a [10]int
	a[0]=1
	a[1]=3
	
	for k, v := range a {
		println(k, v)
	}
}

func test2(){
	var a=[10]int{10, 20}

	for k, v := range a {
		println(k, v)
	}
}

func test3(){
	var a=[...]int{10, 20}
	
	for k, v := range a {
		println(k, v)
	}
}
