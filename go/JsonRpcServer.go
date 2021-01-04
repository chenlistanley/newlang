package main

import (
	"log"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

type Person struct{
}

func (p Person) Message(received string, reply *string) error{
	println(received)
	*reply = "banana"
	return nil
}


func main(){
	p := Person{}
	rpc.Register(p)
	tcpAddr, err := net.ResolveTCPAddr("tcp", ":666")
	if err != nil {
		log.Fatal("resolve error:", err)
	}
	listener, err := net.ListenTCP("tcp", tcpAddr)
	if err != nil {
		log.Fatal("listen error:", err)
	}
	for {
		conn, err := listener.Accept()
		if err != nil {
			continue
		}
		jsonrpc.ServeConn(conn)
	}
}
