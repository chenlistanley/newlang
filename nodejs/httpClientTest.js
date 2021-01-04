var http = require("http")

function test(){
	let options = {
		host: 'localhost',
		port: 8080,
		path: '/'
	}
	let req = http.request(options, function(res){
		body = ''
		res.on('data', function(data){
			body += data
		})
		res.on('end', function(){
			console.log(body)
		})
	})
	req.end()
}

test()