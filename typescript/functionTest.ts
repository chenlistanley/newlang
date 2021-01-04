
function test() {
	var fa = function(a:string):string{
		return a + " banana"
	}
	let a = fa("apple")
	console.log(a)
}

function test2(){
	var fa = function(a:string, b:string = "orange"):string{
		return a + " " + b
	}
	console.log(fa("apple"))
	console.log(fa("apple", "banana"))
}

function test3(){
	var fa = function(a:string, b?:string):string{
		return a + " " + (b ? b:"orange")
	}
	console.log(fa("apple"))
	console.log(fa("apple", "banana"))
}

function test4() {
	var fa = function(a:string, ...b:string[]):string{
		return a + " " + b.join(" ")
	}
	console.log(fa("apple"))
	console.log(fa("apple", "banana"))
	console.log(fa("apple", "banana", "orange"))
}

function test5() {
	(function(a:string = "apple"){
		console.log(a)
	})()
}

function test6() {
	var fa = (a:string, b:String) => [a, b].join(" ") 
	console.log(fa("apple", "banana"))
}

function test7() {
	function fa(a:string | string[]){
		console.log(a)
	}
	fa("apple")
	fa(["apple", "banana"])
}

function test8(){
	let fa = function(f:() => any) : string{
		f()
		return "apple"
	}
	let fb = function(){
		console.log("orange")
	}
	let a = fa(fb)
	console.log(a)
}

test6()