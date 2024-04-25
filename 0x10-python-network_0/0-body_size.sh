#!/bin/bash
# Script to fetch the size of the response body from a given URL.
curl -s "$1" -o response_body.txt -w '%{size_download}\n' && rm response_body.txt

