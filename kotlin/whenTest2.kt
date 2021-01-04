
fun test(){
	val a = 8
	when(a){
		8 -> print("apple")
		else -> print("banana")
	}
}

fun test2(){
	val a = 8
	when(a){
		in 0..4 -> print("apple")
		in 5..9 -> print("banana")
		else -> print("orange")
	}
}

