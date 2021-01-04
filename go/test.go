package main

import "fmt"
import "time"
import "errors"

func test1(){
	var a0 int = 10
	var a1 float32 = 10.99
	var a2 bool = true
	var a3 string = "apple"
	var a4 byte = 'C'
	fmt.Println(a0, a1, a2, a3, a4)
}

func test2(){
	var a = [2]string{"apple", "banana"}
	for _,v := range a{
		println(v)
	}
}

func test3(){
	var a = [...]string{"apple", "banana"}
	for _,v := range a{
		println(v)
	}
}

func test4(){
	var a = []string{"apple", "banana"}
	a = append(a, "orange")
	for _,v := range a{
		println(v)
	}
}

func test5(){
	var a = map[byte]string{'A':"apple", 'B':"banana"}
	a['O'] = "orange"
	for k,v := range a{
		println(k, v)
	}
}

func test6(){
	const a string = "apple"
	println(a)
}

func test7(){
	const (
		a0 = iota
		a1
		a2
	)
	println(a0, a1, a2)
}

type Person struct{
	name string
	age int
}
type Sayer interface{
	say()
}
func (a Person) say(){
	fmt.Println(a.name, a.age)
}
func test8(){
	a := Person{name:"Stanley", age:20}
	a.say()
}

func test9(){
	fa := func(a chan string, b string){
		a <- b
	}
	a := make(chan string, 10)
	go fa(a, "apple")
	go fa(a, "banana")
	go fa(a, "orange")
	time.Sleep(10)
	close(a)
	for k := range a{
		println(k)
	}
}

func test10(){
	defer println("apple")
	println("banana")
	panic("orange")
}

func test11(){
	fa := func() (a string, b error){
		b = errors.New("apple")
		return
	}
	a, b := fa()
	if b != nil{
		panic(b)
	}
	println(a)
}

type ne struct{
	code string
	message string
}
func (a ne) Error() string{
	return fmt.Sprintf("%s %s", a.code, a.message)
}
func test(){
	fa := func() (a string, b error){
		b = ne{code:"S999", message:"apple"}
		return
	}
	a, b := fa()
	if b != nil{
		panic(b)
	}
	println(a)
}


func main(){
	test()
}
