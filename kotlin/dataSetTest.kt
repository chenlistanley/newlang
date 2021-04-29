
fun test(){
	val a = setOf("apple", "banana")
	for(k in a){
		println(k)
	}
}

fun test(){
	var a = setOf("apple", "banana")
	a = a.plus("orange")
	for(k in a){
		println(k)
	}
}