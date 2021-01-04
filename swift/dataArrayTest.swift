
func test(){
	let a = ["apple", "banana"]
	for k in a {
		print(k)
	}
}

func test2(){
	let a:[String] = ["apple", "banana"]
	print(a)
}

func test3(){
	var a = [String]()
	a.append("apple")
	a.append("banana")
	print(a)
}

func test4(){
    var a = ["apple", "banana", "orange", "longan"]
    a.remove(at: 1)
    print(a)
}

func test5(){
	var a = ["apple", "banana"]
	let b = ["orange", "pear"]
	a += b
	print(a)
}

func test6(){
	let a = [String](repeating: "apple", count: 2)
	print(a, a.count, a.isEmpty)
    print(a)
}





