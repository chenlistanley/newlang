
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

class Student<R, S, T>:Person<R, S>{
    let grade:T
    
    init(name:R, age:S, grade:T){
        self.grade = grade
        super.init(name:name, age:age)
    }
    
    override func say(){
        print(self.name, self.age, self.grade)
    }
}

func test(){
    let a = Student(name:"Stanley", age:20, grade:8)
    a.say()
}

test()