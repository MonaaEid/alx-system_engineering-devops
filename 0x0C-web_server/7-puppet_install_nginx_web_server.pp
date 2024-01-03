# Install the nginx module
puppet module install puppet-nginx

# Create the index file
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body><h1>Hello World!</h1></body></html>',
}

# Define the virtual host
nginx::resource::server { 'example.com':
  ensure        => present,
  listen_port   => 80,
  www_root      => '/var/www/html',
  rewrite_rules => [
    '^/redirect_me(.*)$ https://www.youtube.com permanent',
  ],
}
