class Person<R, S>{
    let name:R
    let age:S
    
    init(name:R, age:S){
        self.name = name
        self.age = age
    }
    
    func say(){
        print(self.name, self.age)
    }
}

func test(){
    let a = Person(name:"Stanley", age:20)
    a.say()
}

test()