def test(){
	a = ["A":"apple", "B":"banana"]
	a.put('C', "orange")
	for(k in a.keySet()){
		println("$k, ${a.get(k)}")
	}
	a.each((k, v) -> println("$k $v"))
}
