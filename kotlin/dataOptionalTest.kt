
fun test(){
    var a:String? = "apple"
    val b = a?.capitalize()
    println(b)
}

fun test(){
    var a:String? = null
    val b = a?.capitalize()
    println(b)
}