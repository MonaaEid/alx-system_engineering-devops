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

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}