import {Sayer} from './moduleTesta' 


function test() {
	var a:Sayer = {
		name: "Stanley",
		age: 20,
		say: () => {console.log(a.name, a.age)}
	}
	a.say()
}

test()