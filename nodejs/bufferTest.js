
function test(){
	let buf = Buffer.from("apple")
	console.log(buf.toString("base64"))
}

function test2(){
	let buf = Buffer.alloc(64)
	let a = buf.write("apple")
	console.log(buf.toString("base64", 0, a))
}

test2()