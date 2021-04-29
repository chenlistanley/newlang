struct Person{
    let name:String
    let age:Int
    var fruits:[String]
    
    func say(){
        print(self.name, self.age, self.fruits)
    }
    
    mutating func have(fruit:String){
        fruits.append(fruit)
    }
    
    mutating func remove() -> String{
        return fruits.removeLast()
    }
}

func test(){
    var a = Person(name:"Stanley", age:20, fruits:["apple"])
    a.have(fruit:"banana")
    a.have(fruit:"orange")
    print(a.remove())
    a.say()
}