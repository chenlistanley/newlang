var fs = require('fs')
var zlib = require('zlib')

function test(){
	var text = ""
	var readStream = fs.createReadStream("test.txt")
	readStream.setEncoding("UTF8")
	readStream.on("data", function(chunk){
		text += chunk
	})
	readStream.on("end", function(){
		console.log(text)
	})
	readStream.on("error", function(err){
		console.log(err.stack)
	})
}

function test2(){
	var writeStream = fs.createWriteStream("test2.txt")
	writeStream.write("orange pear", "UTF8")
	writeStream.end()
	writeStream.on("finish", function(){
		console.log("apple")
	})
	writeStream.on("error", function(err){
		console.log(err.stack)
	})
}

function test3(){
	var readStream = fs.createReadStream("test.txt")
	var writeStream = fs.createWriteStream("test2.txt")
	readStream.pipe(writeStream)
}

function test4(){
	var readStream = fs.createReadStream("test.txt")
	var writeStream = fs.createWriteStream("test.txt.gz")
	readStream.pipe(zlib.createGzip()).pipe(writeStream)
}

function test5(){
	var readStream = fs.createReadStream("test.txt.gz")
	var writeStream = fs.createWriteStream("test.txt")
	readStream.pipe(zlib.createGunzip()).pipe(writeStream)
}

test5()

