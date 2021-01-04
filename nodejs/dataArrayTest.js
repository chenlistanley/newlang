
function test(){
	let a = ["apple", "banana"]
	console.log(a)
}

function test2(){
	let a = ["apple", "banana", 10]
	for(k in a){
		console.log(a[k])
	}
}

function test3(){
	let a = new Array()
	a[0] = "apple"
	a[1] = "banana"
	console.log(a)
}

function test4(){
	let a = []
	a[0] = "apple"
	a[1] = "banana"
	console.log(a)
}


test3()