# Automates the task of creating a custom HTTP header response using Puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
} -> package { 'nginx':
  ensure => 'present',
} ~> service { 'nginx':
  ensure => 'running',
  enable => true,
} -> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
 line  => 'add_header X-Served-By $hostname;',
  match => 'http {',
  before => Exec['restart_nginx'],
} -> exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}
