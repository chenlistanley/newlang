
func test(){
	let a=["A": "apple", "B": "banana"]
	print(a, a.count, a.isEmpty)
	for (k, v) in a {
		print(k, v)
	}
}

func test2(){
	let a:[String:String]=["A": "apple", "B": "banana"]
	print(a)

}

func test3(){
	var a=[String:String]()
	a.updateValue("apple", forKey: "A")
	a.updateValue("banana", forKey: "B")
	print(a)
}

func test4(){
	var a=["A": "apple", "B": "banana"]
	a.removeValue(forKey: "A")
	print(a)
}

func test5(){
	var a=["A": "apple"]
	a["B"]="banana"
	print(a)
}

func test6(){
	var a=["A": "apple", "B": "banana"]
	a["A"]=nil
	print(a)
}

func test(){
    let a = ["B": "banana", "A": "apple"]
    print(a["B"]!)
}