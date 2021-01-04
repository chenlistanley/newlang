
namespace nsa{
	export function fa():string{
		return "apple";
	}
}

namespace nsb{
	export function fa():string{
		return "banana";
	}
}

function test(){
	console.log(nsa.fa())
	console.log(nsb.fa())
}

test()