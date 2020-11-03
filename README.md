This is a stupid http server that's always happy and returns 200 to all queries.
At first glance, it looks pretty useless. In truth, it mostly is, but can still be handy:

- to test service reachability, if you don't like netcat
- as the most basic mock for a write-only http service (like monitoring)
- to log request URIs (there are probably much better tools for that)

Available at https://store.docker.com/community/images/yaude/tranquillou-http

## Run locally

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./tranquillou.py --help
```


## Run dockerized

```
docker run yaude/tranquillou-http --help
```

and adapt the flags to your needs.
