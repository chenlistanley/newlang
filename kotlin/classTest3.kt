class Person{
    var name:String
    var age:Int
    
    constructor(name:String, age:Int){
        this.name=name
        this.age=age
    }

    fun say(){
    	println("$name $age")
    }
}

fun test(){
    var a = Person("Stanley", 30)
    a.say()
}