all:
	go build tranquillou-http.go

docker:
	docker build -t yaude/tranquillou-http .

docker-push:
	docker push yaude/tranquillou-http
