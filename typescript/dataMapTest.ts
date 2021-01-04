
function test(){
	var a = new Map<String,String>()
	a.set("A", "apple")
	a.set("B", "banana")
	console.log(a.get("A"), a.get("B"))
}

function test2(){
	var a = new Map<String,String>()
	a.set("A", "apple")
	a.set("B", "banana")
	for(let [k, v] of a){
		console.log(k, v)
	}
	for(let k of a.keys()){
		console.log(k)
	}
	for(let k of a.values()){
		console.log(k)
	}
}

function test3(){
	var a = new Map<String,String>()
	a.set("A", "apple")
	a.set("B", "banana")
	console.log(a.size)
	a.delete("A")
	console.log(a.has("A"), a.get("A"))
}

test3()