package main

import (
	"log"
	"net/rpc"
)

func main(){
	client, err := rpc.DialHTTP("tcp", "localhost:666")
	if err != nil{
		log.Fatal("dialing error:", err)
	}
	var answer string
	err = client.Call("Person.Message", "apple", &answer)
	if err != nil {
		log.Fatal("Call error:", err)
	}
	println(answer)
}