
func test(){
	var a = "apple"
	var a0 = 10
	var a1 = 10.99
	var a2 = true
	println(a, a0, a1, a2)
}

func test2(){
	var a string = "apple"
	var a0 int = 10
	var a1 float64 = 10.99
	var a2 bool = true
	println(a, a0, a1, a2)
}

func test3(){
	var a0  int = 3264
	var a1  int8 = 8
	var a2  int16 = 16
	var a3  int32 = 32
	var a4  int64 = 64
	var a5  uint8 = 8
	var a6  uint16 = 16
	var a7  uint32 = 32
	var a8  uint64 = 64
	var a9  byte = 8
	var a10 rune = 32
	var a11 uint = 3264
	println(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11)
}

func test4(){
	var a0 float32 = 10.32
	var a1 float64 = 10.64
	println(a0, a1)
}

func test5(){
	var a0 complex64 = 32.32
	var a1 complex128 = 64.64
	println(a0, a1)
}

func test6(){
	var a = 10.99
	fmt.Println(reflect.TypeOf(a))
}