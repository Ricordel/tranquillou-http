package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "time"
)

func tranquillou_body(w http.ResponseWriter, r *http.Request, ) {
    // Happy case only, because whatever
    body, _ := ioutil.ReadAll(r.Body)
    defer r.Body.Close()

    fmt.Printf("%s %s%s\n%s\n\n", time.Now().Format("2006-01-02T15:04:05Z"), r.Host, r.URL.Path, body)
    w.WriteHeader(http.StatusOK)
}

func tranquillou(w http.ResponseWriter, r *http.Request, ) {
    fmt.Printf("%s %s%s\n", time.Now().Format("2006-01-02T15:04:05Z"), r.Host, r.URL.Path)
    w.WriteHeader(http.StatusOK)
}

func help() {
    fmt.Printf("%s listen-address [--log-body]\n", os.Args[0])
}


func main() {
    var listenAddress string
    var logBody bool

    for _, option := range os.Args {
        if option == "--help" || option == "-h" || option == "help" || option == "-help" {
            help()
            return
        } else if option == "--log-body" {
            logBody = true
        } else {
            listenAddress = option
        }
    }

    /*
    if len(os.Args) < 2 {
        listenAddress = "localhost:8080"
    } else {
        listenAddress = os.Args[1]
    }
    */

    if logBody {
        fmt.Println("Logging host, path and body")
        http.HandleFunc("/", tranquillou_body)
    } else {
        fmt.Println("Logging only host and path")
        http.HandleFunc("/", tranquillou)
    }

    fmt.Println("Listening on " + listenAddress)

    if err := http.ListenAndServe(listenAddress, nil); err != nil {
        panic(err)
    }
}
