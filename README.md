# Echo Server

A *very* brain dead webserver written in Python used for testing. All it does is send
back to the client a few details around client address, path and headers etc.

Arguments are:
> ```
> --listen, default port 9000
> --servername, default name *blank*
> ```

Methods supported:
* HEAD
* GET

Usage:
* Create the image from the Dockerfile
> ```docker build -t "echoserver" .```
* Start the container
> ```docker run -p 9000:9000 -d echoserver /usr/local/bin/echoserver.py```

