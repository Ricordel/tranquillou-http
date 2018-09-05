This is a stupid http server that's always happy and returns 200 OK. That looks useless, but it can in some cases be handy:

- to test service reachability
- as the most basic mock for a write-only http service (like monitoring)

Available at https://store.docker.com/community/images/yaude/tranquillou-http

If you want it Dockerized, run with

```
docker run yaude/tranquillou-http host:port`.
```

If you want just a binary:

```
make
./tranquillou-http host:port
```
