
fun test(){
    var a = mapOf(Pair("A", "apple"), Pair("B", "banana"))
    a = a.plus(Pair("C", "orange"))

    for(k in a.keys){
        println("$k ${a.get(k)}")
    }
}