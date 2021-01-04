
fun main(args: Array<String>){
	test()
}

fun test(){
	println("apple")
}

fun test2(){
    fun f(s:String) :String{
        return "$s banana"
    }
    val a = f("apple")
    println(a)
}





