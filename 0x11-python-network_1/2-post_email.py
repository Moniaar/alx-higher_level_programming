#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

def send_post_request(url, email):
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Send a POST request and display the body of the response
        with urllib.request.urlopen(url, data=data) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if URL and email parameters are provided
    if len(sys.argv) < 3:
        print("script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
