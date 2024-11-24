#!/bin/bash

for i in {1..10}
do


  echo "-------------------------------------"
  echo "Running curl request $i"
  curl -k -X 'GET' \
    'https://localhost:8443/api/microservices_user/user/current-user' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6ImFkbWluIiwiYWdlIjoyMCwidXNlcm5hbWUiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AYWRtaW4uYWRtaW4iLCJpc19hZG1pbiI6dHJ1ZSwiaWF0IjoxNzMyNDM5OTU5LCJleHAiOjE3MzI0NDA1NTl9.pjvLf4yh86QPKtQkmByogNim0EeF8t8sUXIRFQJQ_Sg'
  
done

 