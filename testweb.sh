#/bin/bash


sudo docker run -it --rm -p 80:8080 -v /home/s110810547/spdockercompose/newcompose/Alzheimer_web/Alzheimer_web/:/src/ --entrypoint /bin/bash alzheimer_web_web
