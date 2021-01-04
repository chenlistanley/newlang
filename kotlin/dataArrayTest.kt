
fun test(){
    var a = arrayOf("apple", "banana")
    for(k in a){
        println(k)
    }
}

fun test2(){
	val a=intArrayOf(1, 2, 3)
	for(k in a){
		println(k)
	}
}

fun test3(){
	val a=IntArray(3, {i -> i + 2})
	for(k in a){
		println(k)
	}
}