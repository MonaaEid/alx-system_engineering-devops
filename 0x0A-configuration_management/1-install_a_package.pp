# Using Puppet, install flask from pip3
package { 'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

package { ['libffi-dev', 'libssl-dev', 'python3-dev']:
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
}
