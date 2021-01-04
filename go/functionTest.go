package main

func main(){
	test5()
}

func test() {
	var f = func() {
		println("apple")
	}
	f()
}

func test2() {
	var f = func(a string) {
		println(a)
	}
	f("apple")
}

func test3() {
	var f = func(a string) string {
		return "apple " + a
	}
	println(f("banana"))
}

func test4() {
	var f = func (a...string) {
		for _,v := range a{
			println(v)
		}
	}
	f("apple", "banana", "orange")
}

func test5(){
	var f = func (f1 func() string){
		var a = f1()
		println(a)
	}
	var f2 = func() string{
		return "apple"
	}
	f(f2)
}
func test6(){
	var f = func (a...interface{}) {
		for _,v := range a{
			println(v)
		}
	}
	f("apple", "banana", "orange")
}
