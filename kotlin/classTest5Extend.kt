
open class Person(var name:String, var age:Int)

fun Person.say(){
    println("$name $age")
}

class Student(name:String, age:Int, var grade:Int):Person(name, age)

fun Student.say(){
    println("$name $age $grade")
}

fun test(){
    var a = Student("Stanley", 20, 10)
    a.say()
}