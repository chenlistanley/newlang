
fun test(){
    var a = mapOf(Pair("A", "apple"))
    a = a.plus(Pair("B", "banana"))

    for(k in a.keys){
        println("$k ${a.get(k)}")
    }
}