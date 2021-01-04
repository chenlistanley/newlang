function test(){
	(function(){
		print("apple");
	})();
}

function test2(){
	var a = (function(){
		return "apple";
	})();
	print(a);
}

function test3(){
	var a = (function(){
		let x = 1;
		return function(){
			return x++;
		}
	})();
	for (var i = 0; i < 5; i++) {
		print(a());
	}
}