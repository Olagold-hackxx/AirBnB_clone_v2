# Set server
exec {'Setup_server':
    provider => 'shell',
    command  => 'sudo apt-get -y update;
    sudo apt-get -y install nginx;
    sudo service nginx start;
    sudo mkdir -p /data/web_static/shared/;
    sudo mkdir -p /data/web_static/releases/test/;
    sudo echo "Hello World!" > /var/www/html/index.html;
    sudo sed -i \'/server_name _/a \\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-enabled/default;
    sudo sed -i \'/rewrite/a \\terror_page 404 /error404.html;\' /etc/nginx/sites-enabled/default;
    sudo sed -i \'/server_name _/a \\tadd_header X-Served-By $hostname;\' /etc/nginx/sites-enabled/default; sudo service nginx restart'
    echo \'Server configured\' > sudo /data/web_static/releases/test/index.html;
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
    sudo chown -R ubuntu:ubuntu /data/;
    sudo sed -i\
    \'/server_name _;/a \\\tlocation \hbnb_static {\n\t\talias /data/web_static/current/;\n\t\ttry_files $uri $uri/ =404;\n\t}\'\
    /etc/nginx/sites-enabled/default;
    sudo service nginx restart'
}