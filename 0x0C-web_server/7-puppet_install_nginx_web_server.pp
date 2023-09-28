# Redo the tasks using Puppet

# Ensure that the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Configure Nginx by adding a rewrite rule
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server',
  line   => 'rewrite ^/redirect_me https://google.com permanent;',
}

# Create an index.html file with content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => 'running',
  require => Package['nginx'],
}