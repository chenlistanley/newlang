def test(){
	a = ["A":"apple", "B":"banana"]
	for(k in a.keySet()){
		println("$k, ${a.get(k)}")
	}
}
