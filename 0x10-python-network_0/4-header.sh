#!/bin/bash
# using delete to pass the url as a first argument
curl -s "$1" -X DELETE
