
open class Person(var name:String, var age:Int){

    open fun say(){
        println("$name $age")
    }
}
class Student(name:String, age:Int, var grade:Int):Person(name,age){

    override fun say(){
        super.say()
        println("$grade")
    }
}

fun test(){
    var a = Student("Stanley", 20, 8)
    a.say()
}