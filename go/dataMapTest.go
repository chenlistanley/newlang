package main


func main(){
	test3()
}

func test(){
	a := map[string]string{"A":"apple", "B":"banana"}
	
	for k,v := range a{
		println(k,v)
	}
}

func test2(){
	var a = make(map[string]string)
	a["A"]="apple"
	a["B"]="banana"
	a["O"]="orange"
	delete(a, "O")

	for k,v := range a{
		println(k,v)
	}
}

func test3(){
	a := map[string]string{"A":"apple", "B":"banana"}
	
	if v, ok := a["A"]; ok {
		println(v)
	}else{
		println("orange")
	}
}