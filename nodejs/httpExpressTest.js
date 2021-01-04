var express = require('express')
var app = express()

function test(){
	app.get("/list", function(req, res){
		data = {"Stanley":"apple", "Bill":"banana"}
		res.end(JSON.stringify(data))
	})
	app.listen(8080)
}

function test2(){
	app.get("/:fruit", function(req, res){
		data = {"Stanley":req.params.fruit}
		res.end(JSON.stringify(data))
	})
	app.listen(8080)
}

function test2(){
	app.post("/apple", function(req, res){
		console.log(req.body)
		data = {"result": "success"}
		res.end(JSON.stringify(data))
	})
	app.listen(8080)
}

test2()