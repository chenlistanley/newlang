class Person{
    let name:String
    let age:Int
    
    init(name:String, age:Int){
        self.name = name
        self.age = age
    }
    
    func say(){
        print(self.name, self.age)
    }
}

class Student:Person{
    let glade:Int
    
    init(name:String, age:Int, glade:Int){
        self.glade = glade
        super.init(name:name, age:age)
    }
    
    override func say(){
        print(self.name, self.age, self.glade)
    }
}

func test(){
    let a = Student(name:"Stanley", age:20, glade: 8)
    a.say()
}