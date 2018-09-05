This is a stupid http server that's always happy and returns 200 to all queries.
At first glance, it looks pretty useless. In truth, it mostly is, but can still be handy:

- to test service reachability, if you don't like netcat
- as the most basic mock for a write-only http service (like monitoring)
- to log request URIs (there are probably much better tools for that)

Available at https://store.docker.com/community/images/yaude/tranquillou-http

If you want it Dockerized, run with

```
docker run yaude/tranquillou-http host:port
```

If you want just a binary:

```
make
./tranquillou-http host:port
```

PR welcome, but if you want to do something interesting with it, maybe just consider using a proper http server?
