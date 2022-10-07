

def test(){
	a = ["apple", "banana"]
	a.add("orange")
	for(k in a){
		println(k)
	}
	a.each(k -> println("$k"))
}

