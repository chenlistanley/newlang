
fun test(){
	val a=true
	if(a){
		println("apple")
	}else{
		println("banana")
	}
}

fun test2(){
    var a = 5
    var b = 3
    var c = if(a > b) "apple" else "banana"
    println(c)
}

fun test3(){
	val a=3
	if(a in 1..9){
		println("apple")
	}
}
