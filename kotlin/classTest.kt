
class Person(var name:String, var age:Int){
    fun say(){
        println("$name $age")
    }
    fun say(words:String){
        println(words)
    }
}

fun test(){
    var a = Person("Stanley", 20)
    a.say()
    a.say("apple")
}