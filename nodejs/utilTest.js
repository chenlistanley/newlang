const util = require('util')

function test(){
	async function fa(){
		return "apple"
	}

	let callbackfa = util.callbackify(fa)

	callbackfa((err, ret) =>{
		if(err) throw err
		console.log(ret)
	})
}

test()

