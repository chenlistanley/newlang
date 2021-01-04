var events = require('events')

function test(){
	var emitter = new events.EventEmitter()
	emitter.on("A", function(){
		console.log("apple")
	})
	emitter.emit("A")
}

function test2(){
	var emitter = new events.EventEmitter()
	emitter.on("A", function(){
		console.log("apple")
	})
	setTimeout(function(){
		emitter.emit("A")
	}, 1000)
}

function test3(){
	var emitter = new events.EventEmitter()
	emitter.once("A", function(){
		console.log("apple")
	})
	for(let k = 0; k < 2; k++){
		let a = emitter.listeners("A")
		console.log(a)
		emitter.emit("A")
	}
}

function test4(){
	var emitter = new events.EventEmitter()
	emitter.on("A", function(){
		console.log("apple")
	})
	emitter.addListener("A", function(){
		console.log("banana")
	})
	for(let k = 0; k < 2; k++){
		let a = emitter.listeners("A")
		console.log(a)
		emitter.emit("A")
		emitter.removeAllListeners(["A"])
	}
}

function test5(){
	var emitter = new events.EventEmitter()
	emitter.emit("error")
}

test5()