#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id variable found in the header of the response"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
