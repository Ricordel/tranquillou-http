FROM alpine
LABEL maintainer="Yoann Ricordel"

COPY . /tranquillou
WORKDIR /
RUN apk add --no-cache python3 py3-pip gcc python3-dev libc-dev \
 && pip install --no-cache-dir -r /tranquillou/requirements.txt \
 && apk del gcc python3-dev libc-dev

ENTRYPOINT ["python3", "/tranquillou/tranquillou.py"]

