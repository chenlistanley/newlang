
function test(){
	function a(fruit){
		print(fruit)
	}
	a.call(a, "apple")
	a.apply(a, ["apple", "banana"])
}