#!/bin/bash
# Use curl to send a GET request and display the body of a 200 status code response
curl -sLf "$1" -X GET
