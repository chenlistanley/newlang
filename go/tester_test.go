package main

import "testing"

func Test_concat(t *testing.T){
	if a:=concat("apple", "banana"); a!="apple100"{
		t.Fail()
	}
}

