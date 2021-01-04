
function test() {
	var a = 10
	var a0 = 10.99
	var a1 = true
	var a2 = "apple"
	console.log(a, a0, a1, a2)
}

function test2() {
	var a: number = 10
	var a0: number = 10.99
	var a1: boolean = true
	var a2: string = "apple"
	var a3: any = null
	var a4: any
	console.log(a, a0, a1, a2, a3, a4)
}

test2()