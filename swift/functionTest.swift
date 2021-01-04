
func test(){
	func f(s: String) ->String{
	    return "apple " + s
	}
	let a=f(s: "banana")
	print(a)
}

func test2(){
    func f(fruit s: String) ->String{
	    return "apple " + s
	}
	let a=f(fruit: "banana")
	print(a)
}

func test3(){
    func f(_ s: String) ->String{
	    return "apple " + s
	}
	let a=f("banana")
	print(a)
}

func test4(){
    func f(_ s: inout String){
	    return s = "apple " + s
	}
	var a = "banana"
	f(&a)
	print(a)
}

func test5(){
    func f(_ array: String...){
	    for k in array {
	        print(k)
	    }
	}
	f("apple", "banana", "orange")
}

func test6(){
    func f(_ array: [String]){
	    for k in array {
	        print(k)
	    }
	}
	f(["apple", "banana", "orange"])
}

