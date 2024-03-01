#!/usr/bin/python3
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    # Send a GET request and display the body of the response
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    # Display the content of the response
    print(response.text)
except requests.exceptions.HTTPError as e:
    print(f"Error code: {e.response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
