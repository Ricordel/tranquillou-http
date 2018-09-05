package main

import (
    "fmt"
    "net/http"
    "os"
    "time"
)

func tranquillou(w http.ResponseWriter, r *http.Request) {
    fmt.Printf("%s %s%s\n", time.Now().Format("2006-01-02T15:04:05Z"), r.Host, r.URL.Path)
    w.WriteHeader(http.StatusOK)
}

func main() {
    http.HandleFunc("/", tranquillou)

    var listenAddress string

    if len(os.Args) < 2 {
        listenAddress = "localhost:8080"
    } else {
        listenAddress = os.Args[1]
    }

    fmt.Println("Listening on " + listenAddress)

    if err := http.ListenAndServe(listenAddress, nil); err != nil {
        panic(err)
    }
}
