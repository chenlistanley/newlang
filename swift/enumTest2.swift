
enum Gender{
    case M(String)
    case F(String)
}

func test(){
    let a = Gender.M("male")
    print(a)
}

func test(){
    let a = Gender.M("male")
    switch a {
        case .M(let name): print(name)
        case .F(_): break
    }
}

test()