package main

import (
	"bufio"
	"os"
)

func  main()  {
	test2()
}

func test()  {
	scanner := bufio.NewScanner(os.Stdin)
	defer func(){
		if err := scanner.Err(); err != nil {
			panic(err)
		}
	}()

	if scanner.Scan(){
		var a = scanner.Text()
		println(a)
	}
}

func test2(){
	reader := bufio.NewReader(os.Stdin)
	a, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}
	println(a)
}


