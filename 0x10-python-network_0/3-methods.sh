#!/bin/bash
# Use curl to send a GET request and display the body of a 200 status code response
curl -sI "$URL" | grep -i content-length | awk '{print $2}' | tr -d '\r'
