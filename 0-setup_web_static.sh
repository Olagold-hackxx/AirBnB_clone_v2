#!/usr/bin/env bash
#Set up for deployment

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo 'Server configured' > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\ttry_files $uri $uri/ =404;\n\t}' /etc/nginx/sites-enabled/default
sudo service nginx restart
