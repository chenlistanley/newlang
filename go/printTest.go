package main

import "fmt"

func main(){
	print()
	print("hi")
	print("hi", 2, 4, 6)
	println()
	println("hi")
	println("hi", 2, 4, 6)

	fmt.Print()
	fmt.Print("hello")
	fmt.Print("hello", 1, 3, 5)
	fmt.Println()
	fmt.Println("hello")
	fmt.Println("hello", 1, 3, 5)
}