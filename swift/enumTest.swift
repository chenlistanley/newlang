
enum Gender{
    case M
    case F
}

func test(){
    let a = Gender.M
    print(a)
}

func test2(){
    let a = Gender.M
    switch a {
        case .M: print("male")
        case .F: print("female")
    }
}

test()