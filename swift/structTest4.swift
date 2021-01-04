struct Fruits{
    var fruits: [String]
    
    subscript(index: Int) -> String{
        get{
            if index < fruits.count{
                return fruits[index]
            }else {
                return ""
            }
        }
        set(value){
            if index < fruits.count {
                fruits[index]=value
            } else {
                fruits.append(value)
            }
        }
    }
}

func test(){
    var a = Fruits(fruits: [])
    a[0]="apple"
    a[1]="banana"
    print(a[0], a[1])
}

test()