#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
# Check if URL parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Use curl to send a request and display the size of the response body
RESPONSE_SIZE=$(curl "$URL" -s -w '%{size_upload}')
echo "$RESPONSE_SIZE"


