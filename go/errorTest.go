package main

import "errors"

func main(){
	test()
}

func test(){
	var fa = func()(res string, err error){
		err = errors.New("apple")
		return
	}
	if res, err := fa(); err == nil{
		println(res)
	} else {
		panic(err.Error())
	}	
}
