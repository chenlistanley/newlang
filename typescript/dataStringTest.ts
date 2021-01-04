
function test(){
	let a = "apple"
	console.log(a, a.length)
}

function test2(){
	let a = new String("apple")
	console.log(a, a.valueOf())
}

function test3(){
	let a = "apple"
	console.log(a.charAt(1))
	console.log(a.charCodeAt(1))
}

function test4(){
	let a = "apple"
	console.log(a.indexOf("p"))
	console.log(a.lastIndexOf("p"))
}

function test5(){
	let a = "apple banana"
	let b = a.match(/\S*a\S*/g)
	console.log(b)
}

function test6(){
	let a = "apple banana"
	let b = a.search(/\S*a\S*/g)
	console.log(b)
}

function test7(){
	let a = "apple banana"
	let b = a.replace(/\S*a\S*/g, "orange")
	console.log(b)
}

function test8(){
	let a = "apple banana"
	let b = a.split(" ")
	console.log(b)
}

function test9(){
	let a = "apple"
	console.log(a.substr(1, 3))
	console.log(a.substring(1, 3))
}

function test10(){
	let a = "Apple"
	console.log(a.toLowerCase())
	console.log(a.toUpperCase())
}

test2()