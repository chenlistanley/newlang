struct Fruits{
    var fruits: [String]
    
    mutating func push(fruit: String){
        fruits.append(fruit)
    }

    mutating func pop() -> String{
        return fruits.removeLast()
    }
}

func test(){
    var a = Fruits(fruits: [])
    a.push(fruit: "apple")
    a.push(fruit: "banana")
    print(a.pop())
}

test()