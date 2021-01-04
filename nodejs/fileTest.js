var fs = require('fs')
var FILE_PATH = "test.txt"

function test(){
	fs.readFile(FILE_PATH, function(error, data){
		if(error){
			console.error(error)
		}else{
			console.log(data.toString())
		}
	})
}

function test2(){
	var a = fs.readFileSync(FILE_PATH)
	console.log(a.toString())
}

test2()
