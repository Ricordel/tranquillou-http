FROM golang:alpine as build

LABEL maintainer="Yoann Ricordel"

COPY tranquillou-http.go /
WORKDIR /

# Build a really static binary so that we can put it in scratch
ENV CGO_ENABLED=0
RUN go build tranquillou-http.go


FROM scratch

COPY --from=build /tranquillou-http /tranquillou-http

ENTRYPOINT ["/tranquillou-http"]
