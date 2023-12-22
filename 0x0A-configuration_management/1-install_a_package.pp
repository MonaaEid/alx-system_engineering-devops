# Using Puppet, install flask from pip3
class { 'python':
  version => '3.8.10',
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
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}

exec { 'verify_python_version':
  command => '/usr/bin/python3 --version | grep -q "Python 3.8"',
  path    => '/usr/local/bin:/usr/bin:/bin',
}

package { 'python3-werkzeug':
  ensure => installed,
}

class python (
  String $version = '3.8.10',
) {
  package { 'python3':
    ensure => installed,
  }

  exec { 'set_python_alternative':
    command => "/usr/bin/update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${version} 1",
    unless  => "/usr/bin/python3 --version | grep -q 'Python ${version}'",
  }
}

class pip {
  package { 'python3-pip':
    ensure => installed,
  }
}

class werkzeug {
  package { 'python3-werkzeug':
    ensure => installed,
  }
}
