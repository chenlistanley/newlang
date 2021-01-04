
class Writer{
	lazy var connection: Connection
	func write(content: String){
		...
	}
}

class Connection{
	var address: String
	func connect(){
		...
	}
}