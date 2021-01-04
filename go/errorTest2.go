package main
import "fmt"

func main(){
	test()
}

type AppleError struct{
	code string
	message string
}

func (err AppleError) Error()(string){
	return fmt.Sprintf(`code: %s, message: %s`, err.code, err.message)
}

func test(){
	var fa = func()(res string, err error){
		err = AppleError{"2020", "apple"}
		return
	}
	res, err := fa()
	if err != nil{
		panic(err)
	}
	println(res)
}