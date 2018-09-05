package main

import (
    "fmt"
    "net/http"
    "os"
)

func tranquillou(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte(""))
}

func main() {
    http.HandleFunc("/", tranquillou)

    if len(os.Args) < 2 {
        fmt.Fprintf(os.Stderr, "Usage: %s listen-address\n", os.Args[0])
        os.Exit(1)
    }

    listenAddress := os.Args[1]

    if err := http.ListenAndServe(listenAddress, nil); err != nil {
        panic(err)
    }
}
