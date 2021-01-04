var http = require('http')

function test(){
	http.createServer(function(request, response){
		response.writeHead(200, {'Content-Type': 'text/plain'})
		data = "apple"
		response.end(data)
	}).listen(8080)
}

function test2(){
	http.createServer(function(request, response){
		response.writeHead(200, {'Content-Type': 'application/json'})
		data = {"Stanley":"apple", "Bill":"banana"}
		response.end(JSON.stringify(data))
	}).listen(8080)
}

test2()

