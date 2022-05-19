#!/bin/bash
 sudo docker run -it -p 80:80 --name mysite3-nginx \
 -v /home/s110810547/spdockercompose/Alzheimer_web/Alzheimer_web/static:/usr/share/nginx/html/static \
 -v /home/s110810547/spdockercompose/Alzheimer_web/Alzheimer_web/media:/usr/share/nginx/html/media \
 -v /home/s110810547/spdockercompose/Alzheimer_web/compose/nginx/log:/var/log/nginx \
 -d mark456tung/nginx:v1
