
interface Sayer{
    fun say()
    fun say(words:String){
        println(words)
    }
}

class Person(var name:String, var age:Int):Sayer{
    
    override fun say(){
        println("${this.name} ${this.age}")
    }
}


fun test(){
    var a = Person("Stanley", 20)
    a.say()
    a.say("apple")
}