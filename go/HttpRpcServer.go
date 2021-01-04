package main

import (
	"net/http"
	"net/rpc"
)

type Person struct{
}

func (p Person) Message(received string, reply *string) error{
	println(received)
	*reply= "banana"
	return nil
}

func main(){
	p := Person{}
	rpc.Register(p)
	rpc.HandleHTTP()
	http.ListenAndServe(":666", nil)
}
