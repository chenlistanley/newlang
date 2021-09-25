
fun test(){
	val a = listOf("apple", "banana", "orange")
	for(k in a){
		println(k)
	}
}

fun test2(){
	val a = listOf("apple", "banana", "orange")
	for(i in a.indices){
		println("$i ${a[i]}")
	}
}

fun test(){
	var a = listOf("apple", "banana")
	a = a.plus("orange")
	a = a.minus("apple")
	for(k in a){
		println(k)
	}
}