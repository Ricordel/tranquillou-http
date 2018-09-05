all:
	go build tranquillou-http.go

docker:
	docker build -t yaude/tranquillou-http .
	docker push yaude/tranquillou-http

docker-alpine:
	docker build -t yaude/tranquillou-http:alpine -f Dockerfile.alpine .
	docker push yaude/tranquillou-http:alpine
