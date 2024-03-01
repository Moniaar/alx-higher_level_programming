#!/usr/bin/python3
import requests
import sys

def fetch_x_request_id(url):
    try:
        # Send a request and display the value of the X-Request-Id variable
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"{x_request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    # Check if URL parameter is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
