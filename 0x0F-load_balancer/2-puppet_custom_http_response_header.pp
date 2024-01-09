# comment
exec { 'command':
    sudo apt-get -y update;
    sudo apt-get -y install nginx;
    string="http {\n\tadd_header X-Served-By \"$HOSTNAME\";"
    sudo sed -i "s/http {/$string/" /etc/nginx/nginx.conf;
    sudo service nginx start;
}
