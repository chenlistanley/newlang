
struct Person{
	var name: String
	var age: Int

	var say: (String, Int){
        return (self.name, self.age)
    }

    var say2: [String:String]{
        return ["name": self.name, "age": "\(self.age)"]
    }
}

func test(){
    let a = Person(name: "Stanely", age: 20)
    print(a.say)
    print(a.say2)
}
