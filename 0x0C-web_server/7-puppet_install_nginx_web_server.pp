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
exec {'sudo sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/ permanent;' /etc/nginx/sites-available/default':
  provider => shell,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}