#!/bin/bash

for i in {1..101}
do
  echo "-------------------------------------"
  echo "Running curl request $i"
  curl -k -X 'GET' \
    'https://localhost:8443/api/microservices_user' \
    -H 'accept: application/json' 
  
done
