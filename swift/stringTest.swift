
func test() {
	let a = "apple"
	print(a, a.count)
}

func test2() {
	let a = "apple"
	for c in a {
		print(c)
	}
}

func test3() {
	let a = "apple"
	for c in a.utf8 {
		print(c)
	}
}

