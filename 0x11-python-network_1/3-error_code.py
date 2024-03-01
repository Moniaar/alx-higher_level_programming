#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

def fetch_url_body(url):
    try:
        # Send a request and display the body of the response
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    # Check if URL parameter is provided
    if len(sys.argv) < 2:
        print("script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_body(url)

