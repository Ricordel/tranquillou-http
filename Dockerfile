FROM alpine
LABEL maintainer="Yoann Ricordel"

COPY requirements.txt /tranquillou/requirements.txt
WORKDIR /
RUN apk add --no-cache python3 py3-pip gcc python3-dev libc-dev \
 && pip install --no-cache-dir -r /tranquillou/requirements.txt \
 && apk del gcc python3-dev libc-dev

# Copy code in two steps so that we don't rebuild the environment
# every time we change a line of application.
COPY . /tranquillou

ENTRYPOINT ["python3", "/tranquillou/tranquillou.py"]

