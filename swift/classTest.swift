class Person{
    var name: String
    var age: Int
    
    init(name: String, age: Int){
        self.name=name
        self.age=age
    }
    
    func say(){
        print(self.name, self.age)
    }
}

func test(){
    let a=Person(name: "Stanley", age:20)
    a.say()
}