# Set server
exec {'Setup_server':
    provider => 'shell',
    command  => 'sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo service nginx start
    mkdir -p /data/web_static/shared/
    mkdir -p /data/web_static/releases/test/
    echo \'Server configured\' > /data/web_static/releases/test/index.html
    ln -s /data/web_static/releases/test/ /data/web_static/current
    chown -R ubuntu:ubuntu /data/
    sudo sed -i\
    \'/server_name _;/a \\\tlocation \hbnb_static {\n\t\talias /data/web_static/current/;\n\t\ttry_files $uri $uri/ =404;\n\t}\' /etc/nginx/sites-enabled/default
    sudo service nginx restart'
}