package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"os"
)

func main()  {
	test6()
}

func test()  {
	file,err := os.Open("README.md")
	if err != nil{
		panic(err)
	}
	defer func() {
		if err := file.Close(); err != nil{
			panic(err)
		}
	}()

	scanner := bufio.NewScanner(file)
	defer func(){
		if err := scanner.Err(); err != nil{
			panic(err)
		}
	}()

	for scanner.Scan(){
		println(scanner.Text())
	}
}

func test2()  {
	file,err := os.Open("README.md")
	if err != nil{
		panic(err)
	}
	defer func() {
		if err := file.Close(); err != nil{
			panic(err)
		}
	}()

	buf := make([]byte, 1024)
	for {
		n, err := file.Read(buf)
		if err != nil && err != io.EOF {
			panic(err)
		}
		if n == 0 {
			break
		}
		println(string(buf))
	}
}

func test3()  {
	buf,err := ioutil.ReadFile("README.md")
	if err != nil {
		panic(err)
	}
	println(string(buf))
}

func test4()  {
	file, err := os.Create("test.txt")
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := file.Close(); err != nil{
			panic(err)
		}
	}()

	file.WriteString("apple\nbanana\norange")
}

func test5()  {
	file, err := os.Create("test.txt")
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := file.Close(); err != nil{
			panic(err)
		}
	}()

	fmt.Fprintln(file, "apple")
	fmt.Fprintln(file, "banana")
	fmt.Fprintln(file, "orange")
}

func test6()  {
	text := []byte("apple\nbanana\norange")
	err := ioutil.WriteFile("test.txt", text, os.ModePerm)
	if err != nil {
		panic(err)
	}
}

