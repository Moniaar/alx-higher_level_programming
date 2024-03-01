#!/bin/bash
# Use curl to send a GET request and display the body of a 200 status code response
curl -sI "$1" | grep -i Allow | cut -d " " -f 2-