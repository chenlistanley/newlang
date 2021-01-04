
function test() {
	let a = ["apple", "banana"]
	for(let k of a){
		console.log(k)
	}
}

function test2() {
	let a: string[] = ["apple", "banana"]
	for(let k in a){
		console.log(a[k])
	}
}

function test3() {
	let a: string[] = new Array("apple", "banana")
	console.log(a)	
}

function test4() {
	let a = ["apple", "banana"]
	let b = a.join(", ")
	console.log(b)
}

function test5() {
	let a = ["apple", "banana"]
	let b = ["orange", "pear"]
	let c = a.concat(b)
	console.log(c)
}

function test6() {
	let a = ["apple", "banana"]
	let b = a.every((element, index, array) => element.match(/\S*a\S*/g))
	console.log(b)
}

function test7() {
	let a = ["apple", "banana"]
	let b = a.filter((element, index, array) => element.match(/\S*b\S*/g))
	console.log(b)
}

function test8() {
	let a = ["apple", "banana"]
	a.forEach(element => console.log(element))
}

function test9() {
	let a = ["apple", "banana"]
	console.log(a.indexOf("banana"), a.lastIndexOf("banana"))
}

function test10() {
	let a = ["apple", "banana"]
	let b = a.map((element, index, array) => element.substring(0, 3))
	console.log(b)
}

test10()