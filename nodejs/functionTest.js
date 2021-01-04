
function test(){
	var fa = function(){
		let a = "apple"
		console.log(a)
	}
	fa()
}

function test2(){
	(function(){
		let a = "apple"
		console.log(a)
	})()
}

function test3(){
	var fa = function(){
		return "apple"
	}
	let a = fa()
	console.log(a)
}

function test4(){
	let fa = (function(){
		let a = "apple"
		return function(){
			return a += " banana"
		}
	})()
	let a = fa()
	console.log(a)
}

function test5(){
	let fa = (a, b) => a + " " + b
	let a = fa("apple", "banana")
	console.log(a)
}

function test6(){
	var fa = function(f){
		f()
	}
	fa(function(){
		let a = "apple"
		console.log(a)
	})
}

function test7(){
	var fa = function(){
		for(k in arguments){
			console.log(arguments[k])
		}
	}
	fa("apple", "banana")
}

test()