#test

package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}
exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/https://www.youtube.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}