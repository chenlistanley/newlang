
func test() {
	let a: Optional<String> = "apple"
	if a != nil {
		print(a!)
	} else {
		print("banana")
	}
}

func test2() {
	let a: String? = "apple"
	if a != nil {
		print(a!)
	} else {
		print("banana")
	}
}

func test3() {
	let a: String? = "apple"
	if let b = a {
		print(b)
	} else {
		print("banana")
	}
}