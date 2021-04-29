
class Person{
    let name:String
    let age:Int
    var fruits:[String]
    
    init(name:String, age:Int, fruits:[String]){
        self.name = name
        self.age = age
        self.fruits = fruits
    }
    
    func say(){
        print(self.name, self.age, self.fruits)
    }
    
    subscript(i:Int) -> String{
        get{
            if fruits.count > i {
                return fruits[i]
            }else{
                return ""
            }
        }
        set(value){
            if fruits.count > i {
                fruits[i] = value
            }else{
                fruits.append(value)
            }
        }
    }
}

func test(){
    let a = Person(name:"Stanley", age:20, fruits:["apple"])
    a[1] = "banana"
    a.say()
    print(a[0], a[1], a[2])
}