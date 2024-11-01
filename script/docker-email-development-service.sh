#! /bin/bash

mkdir -p tmp
sudo docker run --rm -it -p 5000:80 -p 2525:25 -v "./tmp/mail:/smtp4dev" rnwood/smtp4dev

# open browser : http://localhost:5000