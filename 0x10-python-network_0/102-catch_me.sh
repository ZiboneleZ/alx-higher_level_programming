#!/bin/bash

# Send a POST request with a custom header and body to cause the server to respond with "You got me!"
curl -sX POST -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
