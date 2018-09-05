FROM golang:alpine as build

COPY tranquillou-http.go /
WORKDIR /

RUN go build tranquillou-http.go


FROM golang:alpine

COPY --from=build /tranquillou-http /tranquillou-http

ENTRYPOINT ["/tranquillou-http"]
CMD []
