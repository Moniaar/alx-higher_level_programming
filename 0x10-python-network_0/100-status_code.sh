#!/usr/bash
# a script that sends a request to a URL passed as an argument then shows the status code
curl -s -o /dev/null -w '%{http_code}' "$1"
