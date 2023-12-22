# Using Puppet, install flask from pip3
package { 'python3':
  ensure   => '3.8.10',
  provider => 'pip3'
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { ['libffi-dev', 'libssl-dev', 'python3-dev']:
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}

