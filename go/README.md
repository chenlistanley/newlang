go test Caculator.go Caculator_test.go
go test Caculator.go Caculator_test.go -cover

go test -cover -coverprofile=c.out
go tool cover -html=c.out -o coverage.html 

curl -X GET http://localhost:8080