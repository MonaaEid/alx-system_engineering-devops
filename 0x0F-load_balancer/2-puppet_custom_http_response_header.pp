# comment
exec { 'command':
    command  => 'sudo apt-get -y update;
    sudo apt-get -y install nginx;
    sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
    sudo service nginx start',

}
