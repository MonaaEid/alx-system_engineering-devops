# Using Puppet, install flask from pip3.
package { 'flask':
  provider => 'pip3',
  ensure  => '2.1.0' 
}
#mod 'pbailey-flask_bootstrap', '0.1.0'
#exec {
#py -3 -m venv venv
#venv\Scripts\activate
#pip install Flask -v 2.1.0
