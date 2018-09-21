FROM alpine:latest
RUN apk add --no-cache python
ADD echoserver.py /usr/local/bin/echoserver.py
