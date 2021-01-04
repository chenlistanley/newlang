
class Person(var name:String, var age:Int)

fun Person.say(){
        println("$name $age")
    }

fun test(){
    var a = Person("Stanley", 20)
    a.say()
}