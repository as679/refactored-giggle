#!/usr/bin/env python

import argparse
import BaseHTTPServer


class echoHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Echo Server</title></head><body><pre>\n")
        s.wfile.write("Client: %s:%s\n" % (s.client_address[0], s.client_address[1]))
        s.wfile.write("Version: %s\n" % s.request_version)
        s.wfile.write("Path: %s\n" % s.path)
        s.wfile.write("Headers: %s" % s.headers)
        s.wfile.write("</pre></body></html>")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen", type=int, default=9000)
    parser.add_argument("--servername", type=str, default='')
    args = parser.parse_args()

    server = BaseHTTPServer.HTTPServer
    httpd  = server((args.servername, args.listen), echoHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()



if __name__ == '__main__':
    main()
